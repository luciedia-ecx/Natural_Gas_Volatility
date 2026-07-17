import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_white'
st.set_page_config(page_title="Natural Gas Price Risk Dashboard", layout="wide")
st.title("Natural Gas Price Risk & Volatility Dashboard")
st.write("Analysis of U.S. state-level natural gas prices (Commercial & Industrial sectors, "
         "2001-present) benchmarked against the Henry Hub national wholesale price. States with "
         "no retail natural gas choice (fully regulated markets) are excluded.")

# LOAD & WRANGLE — SEDS

@st.cache_data
def load_seds():
    prices = pd.read_csv("pr_all.csv")
    prices.rename(columns={prices.columns[0]: 'data_status',
                            prices.columns[1]: 'state',
                            prices.columns[2]: 'msn'}, inplace=True)
    ng_codes = {'NGCCD': 'Commercial', 'NGICD': 'Industrial'}
    boolean_filter = prices['msn'].isin(ng_codes.keys())
    ng = prices.loc[boolean_filter, :].copy()
    ng['sector'] = ng['msn'].replace(ng_codes)

    us_states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA',
                 'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM',
                 'NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA',
                 'WV','WI','WY']
    boolean_filter = ng['state'].isin(us_states)
    ng = ng.loc[boolean_filter, :]

    year_cols = [c for c in ng.columns if c.isdigit()]
    tidy = pd.melt(ng, id_vars=['state', 'sector'], value_vars=year_cols,
                   var_name='year', value_name='price_per_mmbtu')
    tidy['year'] = tidy['year'].astype(int)
    tidy['price_per_mmbtu'] = pd.to_numeric(tidy['price_per_mmbtu'], errors='coerce')
    tidy.dropna(subset=['price_per_mmbtu'], inplace=True)

    boolean_filter = tidy['year'] >= 2001
    tidy = tidy.loc[boolean_filter, :]

    gas_fully_regulated = ['AL','AK','AR','HI','ID','KS','ME','MN','MS','NE','NH','NC','ND',
                            'OR','SC','SD','TN','UT','VT']
    boolean_filter = tidy['state'].isin(gas_fully_regulated)
    tidy = tidy.loc[~boolean_filter, :]

    region_map = {
        'CT':'Northeast','ME':'Northeast','MA':'Northeast','NH':'Northeast','RI':'Northeast','VT':'Northeast',
        'NJ':'Northeast','NY':'Northeast','PA':'Northeast',
        'IL':'Midwest','IN':'Midwest','MI':'Midwest','OH':'Midwest','WI':'Midwest','IA':'Midwest','KS':'Midwest',
        'MN':'Midwest','MO':'Midwest','NE':'Midwest','ND':'Midwest','SD':'Midwest',
        'DE':'South','DC':'South','FL':'South','GA':'South','MD':'South','NC':'South','SC':'South','VA':'South',
        'WV':'South','AL':'South','KY':'South','MS':'South','TN':'South','AR':'South','LA':'South','OK':'South','TX':'South',
        'AZ':'West','CO':'West','ID':'West','MT':'West','NV':'West','NM':'West','UT':'West','WY':'West',
        'AK':'West','CA':'West','HI':'West','OR':'West','WA':'West'
    }
    tidy['region'] = tidy['state'].replace(region_map)
    tidy.sort_values(['state', 'sector', 'year'], inplace=True)
    tidy['pct_change'] = tidy.groupby(['state', 'sector'])['price_per_mmbtu'].pct_change() * 100
    tidy['pct_change'] = tidy['pct_change'].round(2)
    return tidy

@st.cache_data
def load_henry_hub():
    hh = pd.read_csv("Henry_Hub_Natural_Gas_Spot_Price.csv", skiprows=4)
    hh.rename(columns={'Month': 'month_str',
                        'Henry Hub Natural Gas Spot Price Dollars per Million Btu': 'price'}, inplace=True)
    hh['date'] = pd.to_datetime(hh['month_str'], format='%b %Y')
    hh['year'] = hh['date'].dt.year
    hh['price'] = pd.to_numeric(hh['price'], errors='coerce')
    hh.dropna(subset=['price'], inplace=True)
    hh.sort_values('date', inplace=True)

    agg_dict = {'price': ['mean', 'std', 'min', 'max']}
    hh_annual = hh.groupby('year').agg(agg_dict)
    hh_annual.columns = ['hh_mean', 'hh_std', 'hh_min', 'hh_max']
    hh_annual.reset_index(inplace=True)
    return hh, hh_annual

tidy_gas = load_seds()
hh_tidy, hh_annual = load_henry_hub()
latest_year = tidy_gas['year'].max()

month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


# 1. Regional comparison

st.header(f"1. Average Gas Price by Region and Sector ({latest_year})")
st.caption("Question: In the latest year, how do Commercial and Industrial prices compare across "
           "U.S. regions — is one region consistently priciest regardless of sector?")

boolean_filter = tidy_gas['year'] == latest_year
data = tidy_gas.loc[boolean_filter, :].groupby(['region', 'sector'])[['price_per_mmbtu']].mean().round(2).reset_index()
fig = px.bar(data_frame=data, x='region', y='price_per_mmbtu', color='sector', barmode='group',
             title=f'Average Natural Gas Price by Region and Sector ({latest_year})',
             labels={'region': 'Region', 'price_per_mmbtu': 'Price ($/MMBtu)', 'sector': 'Sector'},
             category_orders={'region': ['Northeast', 'Midwest', 'South', 'West']},
             color_discrete_sequence=px.colors.qualitative.Prism, width=900, height=500)
st.plotly_chart(fig, use_container_width=True)


# 2. National price gap over time

st.header("2. National Price Gap by Sector Over Time")
st.caption("Question: Has the price gap between the highest- and lowest-cost state widened or "
           "narrowed since 2001 — is the market converging or fragmenting?")

agg_dict = {'price_per_mmbtu': ['min', 'max']}
data = tidy_gas.groupby(['year', 'sector']).agg(agg_dict)
data.columns = ['min_price', 'max_price']
data['price_gap'] = (data['max_price'] - data['min_price']).round(2)
data = data.reset_index()
fig = px.line(data_frame=data, x='year', y='price_gap', color='sector', markers=True,
              title='National Gas Price Gap (Highest minus Lowest-Cost State) by Sector',
              labels={'year': 'Year', 'price_gap': 'Price Gap ($/MMBtu)', 'sector': 'Sector'},
              color_discrete_sequence=px.colors.qualitative.Prism, width=900, height=500)
st.plotly_chart(fig, use_container_width=True)


# 3. Distribution by region and sector

st.header("3. Price Distribution by Region and Sector")
st.caption("Question: How does the full spread (not just the average) of Commercial and "
           "Industrial prices differ across regions?")

fig = px.box(data_frame=tidy_gas, x='region', y='price_per_mmbtu', color='sector',
             title='Distribution of Natural Gas Prices by Region and Sector (2001-Present)',
             labels={'region': 'Region', 'price_per_mmbtu': 'Price ($/MMBtu)', 'sector': 'Sector'},
             category_orders={'region': ['Northeast', 'Midwest', 'South', 'West']},
             color_discrete_sequence=px.colors.qualitative.Prism, width=1000, height=550)
st.plotly_chart(fig, use_container_width=True)


# 4. Commercial vs Industrial scatter

st.header(f"4. Commercial vs. Industrial Price by State ({latest_year})")
st.caption("Question: Do Commercial and Industrial prices move together within a state, or "
           "diverge? States above the trendline pay a relative commercial premium.")

boolean_filter = tidy_gas['year'] == latest_year
pivot_sector = pd.pivot_table(data=tidy_gas.loc[boolean_filter, :], index='state', columns='sector',
                               values='price_per_mmbtu', aggfunc='mean').reset_index()
fig = px.scatter(data_frame=pivot_sector, x='Industrial', y='Commercial', text='state', trendline='ols',
                  title=f'Commercial vs. Industrial Natural Gas Price by State ({latest_year})',
                  labels={'Industrial': 'Industrial Price ($/MMBtu)', 'Commercial': 'Commercial Price ($/MMBtu)'},
                  width=900, height=600)
fig.update_traces(textposition='top center')
st.plotly_chart(fig, use_container_width=True)


# 5 & 6. Industrial volatility — bar + choropleth

st.header("5. Industrial Price Volatility by State")
st.caption("Question: Which states have the least predictable Industrial gas prices historically? "
           "Volatility measured as coefficient of variation (std ÷ mean).")

boolean_filter = tidy_gas['sector'] == 'Industrial'
agg_dict = {'price_per_mmbtu': ['mean', 'std']}
vol_data = tidy_gas.loc[boolean_filter, :].groupby('state').agg(agg_dict)
vol_data.columns = ['mean_price', 'std_price']
vol_data['cv_pct'] = (vol_data['std_price'] / vol_data['mean_price'] * 100).round(2)
vol_data = vol_data.reset_index().sort_values('cv_pct', ascending=False)
fig = px.bar(data_frame=vol_data, x='state', y='cv_pct',
             title='Industrial Natural Gas Price Volatility by State (Coefficient of Variation)',
             labels={'state': 'State', 'cv_pct': 'Volatility (CV %)'},
             color='cv_pct', color_continuous_scale='OrRd', width=1100, height=500)
fig.update_xaxes(categoryorder='total descending')
st.plotly_chart(fig, use_container_width=True)

st.header("6. Industrial Price Volatility Map")
st.caption("Question: Where geographically is Industrial gas price risk concentrated?")

fig = px.choropleth(data_frame=vol_data, locations='state', locationmode='USA-states',
                     color='cv_pct', scope='usa', color_continuous_scale='OrRd',
                     title='Industrial Natural Gas Price Volatility by State (CV %)',
                     labels={'cv_pct': 'Volatility (CV %)'}, width=900, height=550)
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig, use_container_width=True)


# 7 & 8. Commercial volatility — bar + choropleth

st.header("7. Commercial Price Volatility by State")
st.caption("Question: Same volatility question, for Commercial customers — does the risk ranking "
           "differ from Industrial?")

boolean_filter = tidy_gas['sector'] == 'Commercial'
agg_dict = {'price_per_mmbtu': ['mean', 'std']}
vol_data_comm = tidy_gas.loc[boolean_filter, :].groupby('state').agg(agg_dict)
vol_data_comm.columns = ['mean_price', 'std_price']
vol_data_comm['cv_pct'] = (vol_data_comm['std_price'] / vol_data_comm['mean_price'] * 100).round(2)
vol_data_comm = vol_data_comm.reset_index().sort_values('cv_pct', ascending=False)
fig = px.bar(data_frame=vol_data_comm, x='state', y='cv_pct',
             title='Commercial Natural Gas Price Volatility by State (Coefficient of Variation)',
             labels={'state': 'State', 'cv_pct': 'Volatility (CV %)'},
             color='cv_pct', color_continuous_scale='PuBu', width=1100, height=500)
fig.update_xaxes(categoryorder='total descending')
st.plotly_chart(fig, use_container_width=True)

st.header("8. Commercial Price Volatility Map")
st.caption("Question: Where is Commercial gas price risk concentrated geographically?")

fig = px.choropleth(data_frame=vol_data_comm, locations='state', locationmode='USA-states',
                     color='cv_pct', scope='usa', color_continuous_scale='PuBu',
                     title='Commercial Natural Gas Price Volatility by State (CV %)',
                     labels={'cv_pct': 'Volatility (CV %)'}, width=900, height=550)
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig, use_container_width=True)


# 9 & 10. Volatility over time — heatmaps

st.header("9. Industrial Volatility Over Time by State")
st.caption("Question: When and where has Industrial price instability clustered historically? "
           "5-year rolling standard deviation.")

boolean_filter = tidy_gas['sector'] == 'Industrial'
data = tidy_gas.loc[boolean_filter, :].copy()
data.sort_values(['state', 'year'], inplace=True)
data['rolling_std'] = data.groupby('state')['price_per_mmbtu'].transform(lambda x: x.rolling(5, min_periods=3).std())
pivot_vol = pd.pivot_table(data=data, index='state', columns='year', values='rolling_std', aggfunc='mean').round(2)
fig = px.imshow(pivot_vol, color_continuous_scale='Reds', aspect='auto',
                 title='Industrial Gas Price Volatility by State Over Time (5-Year Rolling Std Dev)',
                 labels={'x': 'Year', 'y': 'State', 'color': 'Rolling Std ($/MMBtu)'},
                 width=1000, height=900)
st.plotly_chart(fig, use_container_width=True)

st.header("10. Commercial Volatility Over Time by State")
st.caption("Question: Same question for Commercial customers — do the volatile periods line up "
           "with Industrial, or differ?")

boolean_filter = tidy_gas['sector'] == 'Commercial'
data = tidy_gas.loc[boolean_filter, :].copy()
data.sort_values(['state', 'year'], inplace=True)
data['rolling_std'] = data.groupby('state')['price_per_mmbtu'].transform(lambda x: x.rolling(5, min_periods=3).std())
pivot_vol = pd.pivot_table(data=data, index='state', columns='year', values='rolling_std', aggfunc='mean').round(2)
fig = px.imshow(pivot_vol, color_continuous_scale='Reds', aspect='auto',
                 title='Commercial Gas Price Volatility by State Over Time (5-Year Rolling Std Dev)',
                 labels={'x': 'Year', 'y': 'State', 'color': 'Rolling Std ($/MMBtu)'},
                 width=1000, height=900)
st.plotly_chart(fig, use_container_width=True)


# 11. Most stable states (YoY)

st.header("11. Industrial Year-over-Year Price Stability by State")
st.caption("Question: Which states have the most predictable year-to-year Industrial pricing — "
           "candidates for longer-term fixed contracts?")

boolean_filter = tidy_gas['sector'] == 'Industrial'
stab = tidy_gas.loc[boolean_filter, :].groupby('state')[['pct_change']].std().round(2).reset_index()
stab.rename(columns={'pct_change': 'yoy_volatility'}, inplace=True)
fig = px.choropleth(data_frame=stab, locations='state', locationmode='USA-states',
                     color='yoy_volatility', scope='usa', color_continuous_scale='Greens',
                     title='Industrial Gas: Year-over-Year Price Volatility by State',
                     labels={'yoy_volatility': 'Std Dev of YoY % Change'}, width=900, height=550)
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig, use_container_width=True)


# 12 & 13. Treemap & Sunburst

boolean_filter = tidy_gas['year'] == latest_year
agg_dict = {'price_per_mmbtu': ['mean', 'std']}
tree_data = tidy_gas.groupby(['region', 'state', 'sector']).agg(agg_dict)
tree_data.columns = ['mean_price', 'std_price']
tree_data['cv_pct'] = (tree_data['std_price'] / tree_data['mean_price'] * 100).round(2)
tree_data = tree_data.reset_index()
tree_data['equal_weight'] = 1

st.header("12. Volatility Structure: Region → State → Sector")
st.caption("Question: How does price volatility break down hierarchically by region, state, and "
           "sector? Tile size is equal by design; color carries the volatility signal.")

fig = px.treemap(
    tree_data, path=['region', 'state', 'sector'], values='equal_weight',
    color='cv_pct', color_continuous_scale='OrRd',
    title='Natural Gas Price Volatility Structure: Region → State → Sector',
    custom_data=['mean_price', 'cv_pct']
)
fig.update_traces(hovertemplate=(
    "<b>%{label}</b><br>Avg Price: $%{customdata[0]:.2f}/MMBtu<br>"
    "Volatility (CV): %{customdata[1]:.1f}%<extra></extra>"
))
fig.update_layout(width=1000, height=700)
st.plotly_chart(fig, use_container_width=True)

st.header(f"13. Price Structure: Region → State → Sector ({latest_year})")
st.caption("Question: Same hierarchy, colored by average price level instead of volatility.")

fig = px.sunburst(
    tree_data, path=['region', 'state', 'sector'], values='equal_weight',
    color='mean_price', color_continuous_scale='Blues',
    title=f'Natural Gas Price by Region, State, and Sector ({latest_year})',
    custom_data=['mean_price', 'cv_pct']
)
fig.update_traces(hovertemplate=(
    "<b>%{label}</b><br>Avg Price: $%{customdata[0]:.2f}/MMBtu<br>"
    "Volatility (CV): %{customdata[1]:.1f}%<extra></extra>"
))
fig.update_layout(width=800, height=800)
st.plotly_chart(fig, use_container_width=True)


# 14. Henry Hub — last 12 months

st.header("14. Henry Hub Spot Price — Last 12 Months")
st.caption("Question: What is the current national wholesale price trend, as of the most recent "
           "data available?")

boolean_filter = hh_tidy['date'] >= (hh_tidy['date'].max() - pd.DateOffset(months=12))
recent = hh_tidy.loc[boolean_filter, :].copy()
latest_price = recent['price'].iloc[-1]
latest_date = recent['date'].iloc[-1]
fig = px.line(
    data_frame=recent, x='date', y='price', markers=True,
    title=f'Henry Hub Spot Price — Last 12 Months (Latest: ${latest_price:.2f}/MMBtu on {latest_date.strftime("%b %Y")})',
    labels={'date': 'Date', 'price': 'Price ($/MMBtu)'}, width=900, height=450
)
fig.add_scatter(x=[latest_date], y=[latest_price], mode='markers+text',
                 text=[f'${latest_price:.2f}'], textposition='top center',
                 marker=dict(size=12, color='red'), showlegend=False)
st.plotly_chart(fig, use_container_width=True)


# 15 & 16. Seasonality heatmaps

st.header("15. Henry Hub Seasonality — Full History")
st.caption("Question: Is there a predictable month-of-year pattern in Henry Hub pricing across "
           "the full available history?")

hh_tidy['month_name'] = hh_tidy['date'].dt.strftime('%b')
pivot_season = pd.pivot_table(data=hh_tidy, index='year', columns='month_name',
                               values='price', aggfunc='mean')
pivot_season = pivot_season[month_order]
fig = px.imshow(pivot_season, color_continuous_scale='Blues', aspect='auto',
                 title='Henry Hub Price by Month and Year',
                 labels={'x': 'Month', 'y': 'Year', 'color': 'Price ($/MMBtu)'},
                 width=1000, height=800)
st.plotly_chart(fig, use_container_width=True)

st.header("16. Henry Hub Seasonality — 2020-2024")
st.caption("Question: Does the seasonal pattern hold in the most recent five years specifically?")

boolean_filter = hh_tidy['year'].between(2020, 2024)
hh_recent = hh_tidy.loc[boolean_filter, :].copy()
pivot_season_recent = pd.pivot_table(data=hh_recent, index='year', columns='month_name',
                                      values='price', aggfunc='mean')
pivot_season_recent = pivot_season_recent[month_order]
fig = px.imshow(pivot_season_recent, color_continuous_scale='Blues', aspect='auto',
                 title='Henry Hub Price by Month and Year (2020-2024)',
                 labels={'x': 'Month', 'y': 'Year', 'color': 'Price ($/MMBtu)'},
                 width=1000, height=500)
st.plotly_chart(fig, use_container_width=True)


# 17. Sector vs Henry Hub over time

st.header("17. State Gas Price by Sector vs. Henry Hub Benchmark")
st.caption("Question: How closely do Commercial and Industrial state prices track the national "
           "Henry Hub wholesale benchmark over time?")

boolean_filter = tidy_gas['year'].between(2001, latest_year)
sector_mean = tidy_gas.loc[boolean_filter, :].groupby(['year', 'sector'])[['price_per_mmbtu']].mean().round(2).reset_index()
fig = px.line(data_frame=sector_mean, x='year', y='price_per_mmbtu', color='sector', markers=True,
              title='Average State Gas Price by Sector vs. Henry Hub Benchmark',
              labels={'year': 'Year', 'price_per_mmbtu': 'Price ($/MMBtu)', 'sector': 'Sector'},
              color_discrete_sequence=px.colors.qualitative.Prism, width=1000, height=550)
years_sorted = sorted(sector_mean['year'].unique())
hh_aligned = hh_annual.set_index('year').reindex(years_sorted)['hh_mean']
fig.add_trace(go.Scatter(x=years_sorted, y=hh_aligned, mode='lines+markers',
                          line=dict(color='black', width=2, dash='dash'), name='Henry Hub Benchmark'))
st.plotly_chart(fig, use_container_width=True)


# 18. Markup over Henry Hub by state and sector

st.header(f"18. Gas Price Markup Over Henry Hub by State and Sector ({latest_year})")
st.caption("Question: Which states pay the largest premium over the national wholesale benchmark "
           "right now — the biggest negotiating opportunities?")

boolean_filter = tidy_gas['year'] == latest_year
state_latest = tidy_gas.loc[boolean_filter, ['state', 'sector', 'price_per_mmbtu']].copy()
hh_row = hh_annual.loc[hh_annual['year'] == latest_year, 'hh_mean']
hh_baseline = hh_row.iloc[0] if len(hh_row) else hh_annual['hh_mean'].iloc[-1]
state_latest['markup'] = (state_latest['price_per_mmbtu'] - hh_baseline).round(2)
fig = px.bar(data_frame=state_latest, x='state', y='markup', color='sector', barmode='group',
             title=f'Gas Price Markup Over Henry Hub Baseline by State and Sector ({latest_year})',
             labels={'state': 'State', 'markup': 'Markup Over Henry Hub ($/MMBtu)', 'sector': 'Sector'},
             width=1200, height=550)
fig.add_hline(y=0, line_dash='dash', line_color='gray')
st.plotly_chart(fig, use_container_width=True)

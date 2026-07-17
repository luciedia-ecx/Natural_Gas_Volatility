import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.templates.default = 'plotly_white'
st.set_page_config(page_title="Natural Gas Price Risk Dashboard", layout="wide")
st.title("Natural Gas Price Risk & Volatility Dashboard")

@st.cache_data
def load_data():
    prices = pd.read_csv("pr_all.csv")
    prices.rename(columns={prices.columns[0]: 'data_status',
                            prices.columns[1]: 'state',
                            prices.columns[2]: 'msn'}, inplace=True)
    ng_codes = {'NGCCD': 'Commercial', 'NGICD': 'Industrial'}
    boolean_filter = prices['msn'].isin(ng_codes.keys())
    ng = prices.loc[boolean_filter, :].copy()
    ng['sector'] = ng['msn'].replace(ng_codes)
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
    return tidy

tidy_gas = load_data()

sector = st.sidebar.selectbox("Sector", sorted(tidy_gas['sector'].unique()))
year_range = st.sidebar.slider("Year range", int(tidy_gas['year'].min()), int(tidy_gas['year'].max()),
                                (2015, int(tidy_gas['year'].max())))
states = st.sidebar.multiselect("States (leave empty for all)", sorted(tidy_gas['state'].unique()))

boolean_filter = (tidy_gas['sector'] == sector) & (tidy_gas['year'].between(*year_range))
if states:
    boolean_filter &= tidy_gas['state'].isin(states)
filtered = tidy_gas.loc[boolean_filter, :]

st.header(f"{sector} Price Volatility Map")
vol = filtered.groupby('state')[['price_per_mmbtu']].agg(['mean', 'std'])
vol.columns = ['mean_price', 'std_price']
vol['cv_pct'] = (vol['std_price'] / vol['mean_price'] * 100).round(2)
vol = vol.reset_index()

fig_map = px.choropleth(vol, locations='state', locationmode='USA-states', color='cv_pct',
                         scope='usa', color_continuous_scale='OrRd',
                         labels={'cv_pct': 'Volatility (CV %)'}, width=900, height=500)
fig_map.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig_map, use_container_width=True)

st.header("Price Trend")
trend = filtered.groupby('year')[['price_per_mmbtu']].mean().reset_index()
fig_line = px.line(trend, x='year', y='price_per_mmbtu', markers=True,
                    labels={'price_per_mmbtu': 'Avg Price ($/MMBtu)'}, width=900, height=400)
st.plotly_chart(fig_line, use_container_width=True)

st.header("Top 15 Most Volatile States")
top_vol = vol.sort_values('cv_pct', ascending=False).head(15)
fig_bar = px.bar(top_vol, x='state', y='cv_pct',
                  labels={'cv_pct': 'Volatility (CV %)'}, width=900, height=400)
st.plotly_chart(fig_bar, use_container_width=True)

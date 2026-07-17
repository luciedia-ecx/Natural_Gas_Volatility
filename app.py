Last login: Thu Jul 16 05:11:59 on ttys000
cd ~/Desktop/my_first_streamlit_app
(base) lucie@Lucies-MacBook-Air ~ % cd ~/Desktop/my_first_streamlit_app
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % python3 -m pip install --upgrade pip
   pip3 install streamlit
Requirement already satisfied: pip in /opt/miniconda3/lib/python3.13/site-packages (26.0.1)
Collecting pip
  Downloading pip-26.1.2-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.1.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 11.3 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 26.0.1
    Uninstalling pip-26.0.1:
      Successfully uninstalled pip-26.0.1
Successfully installed pip-26.1.2
Requirement already satisfied: streamlit in /opt/miniconda3/lib/python3.13/site-packages (1.59.2)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (6.2.2)
Requirement already satisfied: blinker<2,>=1.5.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<8,>=5.5 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (7.1.4)
Requirement already satisfied: click<9,>=7.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (8.2.1)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (3.1.52)
Requirement already satisfied: numpy<3,>=1.23 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.5.1)
Requirement already satisfied: packaging>=20 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (26.0)
Requirement already satisfied: pandas<4,>=1.4.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (3.0.3)
Requirement already satisfied: pillow<13,>=7.1.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (12.3.0)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.9.3)
Requirement already satisfied: protobuf<8,>=3.20 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (7.35.1)
Requirement already satisfied: pyarrow<25,>=7.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (24.0.0)
Requirement already satisfied: requests<3,>=2.27 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.33.1)
Requirement already satisfied: tenacity<10,>=8.1.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (9.1.4)
Requirement already satisfied: toml<2,>=0.10.1 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.10.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: starlette>=0.40.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (1.3.1)
Requirement already satisfied: uvicorn>=0.30.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.51.0)
Requirement already satisfied: httptools>=0.6.3 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.8.0)
Requirement already satisfied: anyio>=4.0.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (4.12.1)
Requirement already satisfied: python-multipart>=0.0.10 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.0.32)
Requirement already satisfied: websockets>=12.0.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (16.1)
Requirement already satisfied: itsdangerous>=2.1.2 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.2.0)
Requirement already satisfied: jinja2 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)
Requirement already satisfied: narwhals>=2.4.0 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.24.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/miniconda3/lib/python3.13/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in /opt/miniconda3/lib/python3.13/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/miniconda3/lib/python3.13/site-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: charset_normalizer<4,>=2 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.26 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Requirement already satisfied: certifi>=2023.5.7 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (2026.4.22)
Requirement already satisfied: MarkupSafe>=2.0 in /opt/miniconda3/lib/python3.13/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2026.6.3)
Requirement already satisfied: six>=1.5 in /opt/miniconda3/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)
Requirement already satisfied: h11>=0.8 in /opt/miniconda3/lib/python3.13/site-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % streamlit run app.py
Usage: streamlit run [OPTIONS] [TARGET] [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: app.py
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % >....                                                          

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
zsh: parse error near `}'
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % streamlit
pandas
numpy
plotly
Usage: streamlit [OPTIONS] COMMAND [ARGS]...

  Try out a demo with:

      $ streamlit hello

  Or use the line below to run your own script:

      $ streamlit run your_script.py

Options:
  --log_level [error|warning|info|debug]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

Commands:
  activate  Activate Streamlit by entering your email.
  cache     Manage the Streamlit cache.
  config    Manage Streamlit's config settings.
  docs      Look up a Streamlit command, or open the docs in your browser.
  hello     Runs the Hello World script.
  help      Print this help message.
  init      Initialize a new Streamlit project.
  run       Run a Python script, piping stderr to Streamlit.
  skills    Install Streamlit AI-agent skills.
  version   Print Streamlit's version number.
zsh: command not found: pandas
zsh: command not found: numpy
zsh: command not found: plotly
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % cd ~/Desktop/my_streamlit_app
pip3 install streamlit
streamlit run app.py
cd: no such file or directory: /Users/lucie/Desktop/my_streamlit_app
Requirement already satisfied: streamlit in /opt/miniconda3/lib/python3.13/site-packages (1.59.2)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (6.2.2)
Requirement already satisfied: blinker<2,>=1.5.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<8,>=5.5 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (7.1.4)
Requirement already satisfied: click<9,>=7.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (8.2.1)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (3.1.52)
Requirement already satisfied: numpy<3,>=1.23 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.5.1)
Requirement already satisfied: packaging>=20 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (26.0)
Requirement already satisfied: pandas<4,>=1.4.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (3.0.3)
Requirement already satisfied: pillow<13,>=7.1.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (12.3.0)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.9.3)
Requirement already satisfied: protobuf<8,>=3.20 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (7.35.1)
Requirement already satisfied: pyarrow<25,>=7.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (24.0.0)
Requirement already satisfied: requests<3,>=2.27 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.33.1)
Requirement already satisfied: tenacity<10,>=8.1.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (9.1.4)
Requirement already satisfied: toml<2,>=0.10.1 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.10.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: starlette>=0.40.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (1.3.1)
Requirement already satisfied: uvicorn>=0.30.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.51.0)
Requirement already satisfied: httptools>=0.6.3 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.8.0)
Requirement already satisfied: anyio>=4.0.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (4.12.1)
Requirement already satisfied: python-multipart>=0.0.10 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (0.0.32)
Requirement already satisfied: websockets>=12.0.0 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (16.1)
Requirement already satisfied: itsdangerous>=2.1.2 in /opt/miniconda3/lib/python3.13/site-packages (from streamlit) (2.2.0)
Requirement already satisfied: jinja2 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)
Requirement already satisfied: narwhals>=2.4.0 in /opt/miniconda3/lib/python3.13/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.24.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/miniconda3/lib/python3.13/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in /opt/miniconda3/lib/python3.13/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/miniconda3/lib/python3.13/site-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: charset_normalizer<4,>=2 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.26 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Requirement already satisfied: certifi>=2023.5.7 in /opt/miniconda3/lib/python3.13/site-packages (from requests<3,>=2.27->streamlit) (2026.4.22)
Requirement already satisfied: MarkupSafe>=2.0 in /opt/miniconda3/lib/python3.13/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in /opt/miniconda3/lib/python3.13/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2026.6.3)
Requirement already satisfied: six>=1.5 in /opt/miniconda3/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)
Requirement already satisfied: h11>=0.8 in /opt/miniconda3/lib/python3.13/site-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)
Usage: streamlit run [OPTIONS] [TARGET] [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: app.py
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % cd ~/Desktop/my_first_streamlit_app
(base) lucie@Lucies-MacBook-Air my_first_streamlit_app % >....                                                          

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

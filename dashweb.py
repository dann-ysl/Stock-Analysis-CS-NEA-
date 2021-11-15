import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries

key = '###'
ts = TimeSeries(key, output_format='pandas')
ttm_data, ttm_meta_data = ts.get_intraday(symbol='TSLA',interval='1min', outputsize='compact')
df = ttm_data.copy()
df=df.transpose()
df.rename(index={"1. open":"open", "2. high":"high", "3. low":"low",
                  "4. close":"close","5. volume":"volume"},inplace=True)
df=df.reset_index().rename(columns={'index': 'indicator'})
df = pd.melt(df,id_vars=['indicator'],var_name='date',value_name='rate')
df = df[df['indicator']!='volume']

print(df.head(10))

df.to_csv("data2.csv", index=False)
exit()

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
#import seaborn as sns
#import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

external_stylesheets = [
   {
       'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
       'rel': 'stylesheet',
       'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
       'crossorigin': 'anonymous'
   }
]
data=pd.read_csv('facccc.csv')

options=[{'label':'confirmed','value':'confirmed'},
          {'label':'deaths','value':'deaths'}
          ]
options2=[{'label':'0-2000','value':'0-2000'},
          {'label':'2001-3000','value':'2001-3000'},
          {'label':'3001-80000','value':'3001-80000'},
          {'label':'80000+','value':'80000+'}

          ]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

app.layout=html.Div([
    html.H1("Corona Virus Pandemic",style={'color':'#fff','text-align':'center'}),
    html.Div([
        html.Div([
            dcc.Dropdown(id='picker1', options=options2, value='0-2000'),
            dcc.Graph(id='heatmap')
        ],className='col-md-12')
    ],className='row'),
    html.Div([],className='row'),
    html.Div([],className='row'),
    html.Div([],className='row')
],className='container')
@app.callback(Output('heatmap','figure'),[Input('picker1','value')])
def update_graph(type1):
    bins = [0, 2000, 3000, 80000, 400000]
    data3 = data.copy()
    data3['confirmed'] = pd.cut(data3['confirmed'], bins, labels=['0-2000', '2001-3000', '3001-80000', '80000+'])
    new=data3[data3['confirmed']==type1]
    trace1=go.Box(x=new['HMT.current'],name='')
    return {'data':[trace1],'layout':go.Layout(title="Confirmed cases Vs Lead Exposure")}

if __name__=="__main__":
   app.run_server(debug=True)
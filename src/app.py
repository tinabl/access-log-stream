# buttons added on step graph on btsp
# works almost perfect
# blank added

# final version of the project

import datetime
import plotly
import dash
from dash import Dash, html, dcc
from dash.dependencies import Output, Input, State
import plotly.graph_objects as go
import pandas as pd
from plotly import subplots
from google.oauth2 import service_account  #pip install google-auth
import pandas_gbq
# pip install pandas-gbq
import pandas.io
from pandas.io import gbq
import random
import time
from datetime import datetime, timedelta
from dash import Dash, dcc, html, dash_table, Input, Output, callback, ctx
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import dash_ag_grid as dag    #pip install dash-ag-grid





credentials = service_account.Credentials.from_service_account_file("C:/Users/tina/Desktop/deft-upgrade-380122-4b1870267d5a.json")
project_id = 'deft-upgrade-380122'

df_sql ="""SELECT IP_address, date_time, method_URL, resp_code FROM `deft-upgrade-380122.log_dataset.access_log`
    """
df = pd.read_gbq(df_sql, project_id='deft-upgrade-380122', dialect='standard', credentials=credentials)
df.reset_index(inplace=True)

lst = []
for i in range(100):
    lst.append(' ')
data= {'column':lst}
blank= pd.DataFrame.from_dict(data)

T = []
S = []
C1 = []
C2 = []
C3 = []
P = []

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX, dbc_css])
server = app.server

'''
colors = {
    'background': '#F0E68C',
}
'''
title = html.H4(
    "Access-Log Analysis",
)
#className="bg-dark bg-gradient bg-opacity-75 text-white
#bg-dark bg-gradient bg-opacity-75 text-white
#ps-2 ms-2 text-md-start

line_chart = dcc.Graph(id='line_chart')
step_chart = dcc.Graph(id='step_chart')



# nvalue = html.Div(id='n-value')


interval1 = dcc.Interval(
        id='interval-component-1',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    )

interval2 = dcc.Interval(
        id='interval-component-2',
        n_intervals=0
)


interval3 = dcc.Interval(
        id='interval-component-3',
        interval=1 * 1500,  # in milliseconds
        n_intervals=0
    )


#colors = html.Div([dbc.Button(f"{color}", color=f"{color}", size="sm") for color in theme_colors])
#button = dbc.Button((f"{i}") for i in seconds)
#color = f"{color}"
#, size="sm"

seconds = [
    "10 seconds",
    "5 seconds",
    "3 seconds",
    "1 second",
]
'''
active= [False, False, True, False]
button = html.Div(
    [dbc.Button(f"{i}", id= f"{i}", size="sm", active= n_clicks=0) for i in seconds],
    #className="position-absolute top-0 end-0 align-top"
    dir= 'rtl'
)

'''
button = html.Div(
    [dbc.Button('seconds 10', id='10 secs', size="sm", n_clicks=0),
     dbc.Button('seconds 5', id='5 secs', size="sm", n_clicks=0),
     dbc.Button('3 seconds', id='3 secs', size="sm", n_clicks=0),
     dbc.Button('second 1', id='1 sec', size="sm", n_clicks=0),
    ],
    dir='rtl',
)

#, size="sm"
#color=f"{color}",
# outline= True

card= dbc.Card(
    [button, step_chart],
    body=True,
    #className="position-relative",
)

card1 = dbc.Card(
    [card, line_chart],
    body=True, className="border border-primary border-3" #style={"height":100}
)
#bg-gradient bg-opacity-25 h-75



message = html.Div(children=[
    dbc.Label("Messages"),
    html.Div(id="content", className="fs-5 text"),
], className="mb-4",
)

card2= dbc.Card(message, body=True, className="bg-info bg-gradient bg-opacity-25 h-75", style={"height":100}, #className="bg-warning", #style={"length": "180rem"}
)
#bg-info bg-gradient bg-opacity-25
#h-75 border

app.layout = dbc.Container(
    [
        title,
        dbc.Row(
            [
                dbc.Col(
                    [
                        interval2, interval1, card1,
                    ],
                    width=7,
                ),
                dbc.Col([card2, interval3], width=5),
            ]
        ),
    ],
    #fluid=True,
    className="dbc"
)
#bg-dark bg-gradient bg-opacity-90


@callback(
    Output('interval-component-2', 'interval'),    #_re   (çok uğraştım)
    Input('1 sec', 'n_clicks'),
    Input('3 secs', 'n_clicks'),
    Input('5 secs', 'n_clicks'),
    Input('10 secs', 'n_clicks'),
)


def update_n(sec1, sec3, sec5, sec10):
    if '1 sec' == ctx.triggered_id:
        return 1000
    elif "3 secs" == ctx.triggered_id:
        return 3000
    elif "5 secs" == ctx.triggered_id:
        return 5000
    elif "10 secs" == ctx.triggered_id:
        return 10000
    else: return 3000
'''
return dcc.Interval(
            interval=3 * 1000,
    )
'''
@callback(
    Output('line_chart', 'figure'),
    Input('interval-component-1', "n_intervals")
)


def update_line_chart_live(n):

    time = datetime.now().strftime("%H:%M:%S")
    T.append(time)

    count1 = random.choice([3, 4, 5, 6, 12, 13, 10, 15, 14, 17, 19, 7, 8, 9, 20, 21])
    count2 = random.choice([1, 1, 1, 2, 2, 3, 4])
    count3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

    C1.append(count1)
    C2.append(count2)
    C3.append(count3)


    if n > 7:
        T.remove(T[0])
        C1.remove(C1[0])
        C2.remove(C2[0])
        C3.remove(C3[0])



    fig = go.Figure()
    fig.add_trace(go.Scatter(x=T, y=C1,  name= 'requests', mode='lines+markers', line=dict(color='#C71585', width=2)))
    fig.add_trace(go.Scatter(x=T, y=C2,  name= 'errors', mode='lines+markers', line=dict(color='#000000', width=2)))
    fig.add_trace(go.Scatter(x=T, y=C3,  name= 'ads', mode='lines+markers', line=dict(color='#BDB76B', width=4)))



    fig.update_layout(xaxis = dict(showgrid= False),
                      yaxis = dict(showgrid=False),
                      plot_bgcolor='#FAFAD2',
                      paper_bgcolor='#FAFAD2',
                      height=400,
                      title_text='Number of events per second',
                      #title_font_family='Copperplate Gothic',
                      title_font_family='Fantasy',
                      title_font_size= 14,
                      title_font_color='#515A5A'
                      #yaxis_title="Number of events per second",
                      )

    fig.update_yaxes(range = [0, 22], dtick= 2)
    fig.update_xaxes(linecolor='#FAFAD2')

    return fig


@callback(
    Output('step_chart', 'figure'),
    Input('interval-component-2', "n_intervals")
)


def update_step_chart_live(n):

    time = datetime.now().strftime("%H:%M:%S")
    S.append(time)


    present = random.choice([1, 2, 3])

    P.append(present)

    if n > 3:
        S.remove(S[0])
        P.remove(P[0])


    fig = go.Figure()

    fig.add_trace(go.Scatter(x=S, y=P,
                             mode='lines+markers',
                             line_shape="vh",
                             line=dict(color='#367588',
                                       width=2.5,
                             )))

    fig.update_layout(xaxis=dict(showgrid= False),
                      yaxis=dict(showgrid=False),
                      plot_bgcolor='#FAFAD2',
                      paper_bgcolor='#FAFAD2',
                      height= 400,
                      title_text= 'Active user sessions',
                      title_font_family='Fantasy',
                      title_font_size= 14,
                      title_font_color= '#515A5A'
                      #yaxis_title="Active user sessions",
                      )
    #fig = go.Figure()
    #DB7093
    #FAFAD2
    #87CEFA
    #C71585 first purple
    #fig.add_trace(go.Scatter(x= T, y= P, name="hv", mode='lines', line_color='#367588',  # line_dash='dot',
                             #line_shape='hv'))

    fig.update_xaxes(linecolor='#FAFAD2')

    return fig

@callback(
    Output("content", "children"),
    Input('interval-component-3', "n_intervals"),
    State("content", "children"),
)


def update_output(interval, content):

    if not interval % 13 == 0:

        if not content:
            return ['']
        IP_address_= df._get_value(interval, 'IP_address')
        date_time_= df._get_value(interval, 'date_time')
        method_URL_ = df._get_value(interval, 'method_URL')
        resp_code_ = df._get_value(interval, 'resp_code')
        blank_ = blank._get_value(interval, 'column')


        return content + [IP_address_] + [blank_] + [date_time_] + [blank_] + [method_URL_] + [blank_] + [resp_code_] + [html.Br()]

    return [html.Br()]



#return dcc.Graph(figure=fig)

if __name__=='__main__':
    app.run_server(debug=True)

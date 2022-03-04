#!/usr/bin/env python
import snowflake.connector as c
import pandas as pd
import matplotlib.pyplot as plt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pdrese
import plotly.graph_objs as go

# Gets the version
# ctx = c.connect(user='DEEPIKA',password='Life@123',account='go75189.us-east-2.aws')

# sql = "SELECT * FROM BENCHPREP_DATASET.PUBLIC.TABLE3"

# df = pd.read_sql(sql, ctx)

# app_name = 'dash-snowflakeedataplot'
 
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.title = 'Snowflake + Dash'

# if __name__ == '__main__':
#     app.run_server(debug=True)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
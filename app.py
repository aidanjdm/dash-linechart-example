import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

heading = "Graph Viewer"
title = "Enter parameters above to view the expression's graph below:"
x_values = list(range(-10,11))
color = '#1a237e'
name = 'f(x)'
tabtitle = 'Graph Viewer'
githublink = 'https://github.com/aidanjdm/midcourse-project'

# Create traces
trace = go.Scatter(
    x = x_values,
    y = [(1*x**2 + 0) for x in x_values],
    mode = 'lines',
    marker = {'color': color},
    name = name
)

# assign traces to data
data = trace
layout = go.Layout(
    title = title,
    width=600,
    height=600
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(heading),
    html.Div('coefficient:'),
    dcc.Input(id='input-1', value=1, type='number'),
    html.Div('power:'),
    dcc.Input(id='input-2', value=2, type='number'),
    html.Div('y-intercept:'),
    dcc.Input(id='input-3', value=0, type='number'),
    html.Div('expression:'),
    html.Div(id = 'expression'),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    ]
)

########## Define Callback
@app.callback(
    [Output(component_id='figure-1', component_property='figure'),
    Output(component_id='expression', component_property='children')],
    [Input(component_id='input-1', component_property='value'),
    Input(component_id='input-2', component_property='value'),
    Input(component_id='input-3', component_property='value')]
)
def update_graph(input_value1, input_value2, input_value3):
    trace = go.Scatter(
        x = x_values,
        y = [(input_value1*x**input_value2 + input_value3) for x in x_values],
        mode = 'lines',
        marker = {'color': color},
        name = name
    )

    # assign traces to data
    data = trace
    layout = go.Layout(
        title = title,
        width=600,
        height=600
    )

    # Generate the figure dictionary
    fig = go.Figure(data=data,layout=layout)
    expression = f'{input_value1}x^{input_value2} + {input_value3}'
    return fig, expression

############ Deploy
if __name__ == '__main__':
    app.run_server()

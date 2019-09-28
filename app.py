import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

heading = "Graph Viewer"
title = "Enter an expression to view its graph"
x_values = list(range(-10,11))
y_values = [x**2 for x in x_values]
color = '#1a237e'
name = 'f(x)'
tabtitle = 'Graph Viewer'
githublink = 'https://github.com/aidanjdm/midcourse-project'

########### Set up the chart

# create trace
trace = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines',
    marker = {'color': color},
    name = name
)

# assign traces to data
data = trace
layout = go.Layout(
    title = title
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
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()

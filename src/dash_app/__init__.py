"""import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label('Select a value from the dropdown:'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'opt1'},
            {'label': 'Option 2', 'value': 'opt2'},
            {'label': 'Option 3', 'value': 'opt3'}
        ],
        value='opt1'  # default selected value
    ),
    dcc.Textarea(
        id='textarea',
        placeholder='Enter text...',
        value='',
        readOnly=True,
        style={'width': '50%', 'height': '100px'}
    ),
    dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    ),
    dcc.RadioItems(['Active wheelchair', 'No limitations', 'E-wheelchair' ,'Stroller', 'Scewo BRO'],'No limitations')
])

@app.callback(
    dash.dependencies.Output('textarea', 'value'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_textarea(selected_value):
    return f'You selected: {selected_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
"""
import dash
from dash import dcc
from dash import html
import os


app = dash.Dash(__name__)

app.layout = html.Div([
    # Company description on the left
    html.Div([
        html.H1("Your Company Name"),
        html.P("Welcome to our company. We specialize in... (add your description here)"),
    ], style={'width': '30%', 'float': 'left'}),

    # Logo at the top right
    html.Div([
        html.Img(src=r'C:\git\OpenDataHackSG\src\dash_app\your_logo.png',alt='logo', style={'width': '100px', 'float': 'right'}),
    ], style={'width': '70%', 'float': 'right'}),

    # Dropdown menu and text input on the second line
    html.Div([
        html.Label('Select a value from the dropdown:'),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Option 1', 'value': 'opt1'},
                {'label': 'Option 2', 'value': 'opt2'},
                {'label': 'Option 3', 'value': 'opt3'}
            ],
            value='opt1'  # default selected value
        ),
        dcc.Input(
            id='text-input',
            type='text',
            value='',  # Initial value is empty
            placeholder='Enter text...',
            style={'width': '50%'}
        ),
    ], style={'clear': 'both'}),  # Clear the float to start a new line

    # Text output on the third line
    html.Div([
        html.Label('Output:'),
        dcc.Textarea(
            id='output-textarea',
            value='',
            readOnly=True,
            style={'width': '100%', 'height': '100px'}
        ),
    ]),
])

@app.callback(
    dash.dependencies.Output('output-textarea', 'value'),
    [dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('text-input', 'value')]
)
def update_output(selected_dropdown_value, text_input_value):
    return f'You selected: {selected_dropdown_value}\nText input: {text_input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)

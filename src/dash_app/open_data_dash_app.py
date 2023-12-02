import dash
from dash import dcc, State
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import os

# Get the directory where the current Python file is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Load the .env file from the current directory
imagepath = os.path.join(current_directory, 'your_logo.png')
encoded_image = base64.b64encode(open(imagepath, 'rb').read())

class OpenDataDashApp:
    def __init__(self, places):
        dash_places = places
        self._observers = []
        self.limitations_value = ""
        self.text_input_value = ""
        self.selected_dropdown_value = ""
        self.answer = ""



        self.app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

        self.setup_layout(dash_places)
        self.setup_callbacks()

    def setup_layout(self,places):

        sidebar = html.Div(
            [
                dbc.Row(
                    [
                    html.H1("Sitios"),
                    html.P("Willkomen zum Projekt der Gruppe MEGATRON ON ICE zur Challange: Umfassende Informationen - einfach erklärt."),
                    ], style={"height": "5vh"}

                )
            ]

        )
        content = html.Div(
            [
                html.Div(id='output', style={'display': 'none'}),
                dcc.Interval(id='interval-component', interval=2000, n_intervals=0),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                               html.H1("MEGATRON ON ICE"),
                                ]),
                        dbc.Col(
                            [
                                html.Img(src=f"data:image/jpg;base64,{encoded_image.decode()}", alt="Your Image Description")    
                                ])
                    ],
                    style={"height":"10vh"}),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Input(
                                        id='text-input',
                                        type='text',
                                        value='',  # Initial value is empty
                                        placeholder='Enter text...'
                                    ),
                                    html.Button('Submit', id='submit-val', n_clicks=0),
                                    html.Div(id='container-button-basic',
                                    children='Enter a value and press submit')
                            ]),
                            dbc.Col(
                            [
                                html.Label('Select a value from the dropdown:'),
                                dcc.Dropdown(places, id='pandas-dropdown-1',value='opt1'),  # default selected value),
                                html.Div(id='pandas-output-container-1')
                                            ])
                        ],
                        style={"height": "20vh"}),
                dbc.Row(
                    [
                        dcc.RadioItems(['Active wheelchair', 'No limitations', 'E-wheelchair' ,'Stroller', 'Scewo BRO'],'No limitations',inline=True,id='limitations')
                    ],
                    style={"height": "50vh"}),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label('Output:'),
                                dcc.Textarea(
                                    id='output-textarea',
                                    value='',
                                    readOnly=True,
                                    style={'width': '100%', 'height': '100px'}
                                )
                            ])
                    ],
                    style={"height": "50vh"})    
           
                
            ]
        )
            
        self.app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
                ]
            ),
        ],
    fluid=True
    )

   
    def setup_callbacks(self):
        @self.app.callback(
            Output('output', 'children'),
    
            [Input('pandas-dropdown-1', 'value'),
             Input('text-input', 'value'),
             Input('limitations', 'value')],
            State('text-input', 'value'),
            prevent_initial_call=True
        )
        def update_output(selected_dropdown_value, text_input_value,limitations_value, value):
            self.limitations_value = limitations_value
            self.text_input_value = text_input_value
            self.selected_dropdown_value = selected_dropdown_value
            self.notify((self.selected_dropdown_value, self.limitations_value, self.text_input_value))
            return f'You selected: {selected_dropdown_value}\nText input: {text_input_value}\nText input: {limitations_value}'
        
        @self.app.callback(
            Output('container-button-basic', 'children'),
            Input('submit-val', 'n_clicks'),
            prevent_initial_call=True
        )
        def update_output2(n_clicks):
            if n_clicks==1:
                self.notify((self.selected_dropdown_value, self.limitations_value, self.text_input_value))

        @self.app.callback(
            Output('output-textarea', 'value'), 
            [Input('interval-component', 'n_intervals')]
            )
        def update_value(n):
            return str(self.answer)

    def run_server(self, debug=True):
        self.app.run_server(debug=debug)

    def set_answer(self, answer):
        self.answer = answer

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, query):
        for observer in self._observers:
            observer.update(query)   

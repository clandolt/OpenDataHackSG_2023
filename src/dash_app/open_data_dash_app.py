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
imagepath = os.path.join(current_directory, 'Sitios_logotype_color_PNG.png')
encoded_image = base64.b64encode(open(imagepath, 'rb').read())

imagepath2 = os.path.join(current_directory, 'LinkedIn.png')
encoded_image2 = base64.b64encode(open(imagepath2, 'rb').read())

class OpenDataDashApp:
    def __init__(self, places):
        dash_places = []
        self.limitations_value = ""
        self.text_input_value = ""
        self.selected_dropdown_value = ""
        for id, place in places:        
            dash_places.append(place)



        self.app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

        self.setup_layout(dash_places)
        self.setup_callbacks()

    def setup_layout(self,places):

        sidebar = html.Div(
            [
                dbc.Row(
                    [
                         html.A( href="https://www.sitios.info/",
                                children=[html.Img(src=f"data:image/jpg;base64,{encoded_image.decode()}", alt="Your Image Description",style={"align": "right",'width': '60%'})]
                            )], style={"height": "10vh"}

                ),
                dbc.Row(
                    [
                    html.P("Willkomen zum Projekt der Gruppe MEGATRON ON ICE zur Challange: Umfassende Informationen - einfach erklärt."),
                    
                    ], style={"height": "15vh"}

                ),
                dbc.Row(
                    [
                    html.P("Challenge Owner:"),
                    ], style={"height": "5vh"}

                ),
                dbc.Row(
                    [
                    
                    html.P("Christoph Inhelder"),
                    html.A( href="https://www.linkedin.com/in/christoph-inhelder/",
                                children=[html.Img(src=f"data:image/jpg;base64,{encoded_image2.decode()}", alt="Your Image Description",style={"align": "right",'width': '10%'})]
                            ),
                    ], style={"height": "10vh"}

                ),
                dbc.Row(
                    [
                    html.P(""),
                    ], style={"height": "5vh"}

                ),
                dbc.Row(
                    [
                    html.P("Creater:"),
                    ], style={"height": "5vh"}

                ),
                dbc.Row(
                    [
                    
                    html.P("Christoph Landolt"),
                    html.A( href="https://www.linkedin.com/in/christoph-landolt-072068b1/",
                                children=[html.Img(src=f"data:image/jpg;base64,{encoded_image2.decode()}", alt="Your Image Description",style={"align": "right",'width': '10%'})]
                            ),
                    ], style={"height": "10vh"}

                ),
                dbc.Row(
                    [
                    html.P("Ruwen Frick"),                    
                    html.A( href="https://www.linkedin.com/in/ruwen-frick-5527b6197/",
                                children=[html.Img(src=f"data:image/jpg;base64,{encoded_image2.decode()}", alt="Your Image Description",style={"align": "right",'width': '10%'})]
                            ),
                    ], style={"height": "10vh"}

                ),
                dbc.Row(
                    [
                    html.P("Noah Lüchinger"),
                    html.A( href="https://www.linkedin.com/in/noah-l%C3%BCchinger-8495b5236/",
                                children=[html.Img(src=f"data:image/jpg;base64,{encoded_image2.decode()}", alt="Your Image Description",style={"align": "right",'width': '10%'})]
                            ),
                    ], style={"height": "10vh"}

                )
            ]

        )
        content = html.Div(
            [
                dbc.Row(
                    [
                         html.H1("MEGATRON ON ICE",style={'width': '80vh'})
                        
                    ],
                    style={"height":"10vh"}),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label('Stell eine Frage und drücke Enter:'),
                                dcc.Input(
                                        id='text-input',
                                        type='text',
                                        value='',  # Initial value is empty
                                        placeholder='Enter text...',
                                        style={'width': '80vh','height':'40px'},
                                    )
                            ]),
                            dbc.Col(
                            [
                                html.Label('Wähle einen Ort:'),
                                dcc.Dropdown(places, id='pandas-dropdown-1',value='opt1',style={'height':'40px'}),  # default selected value),
                                html.Div(id='pandas-output-container-1')
                                            ])
                        ],
                        style={"height": "10vh"}),
                dbc.Row(
                    [
                        html.Button('Enter', id='submit-val', n_clicks=0,style={'height':'40px','width': '80px', 'margin-left': '10px'}),
                        html.Div(id='container-button-basic',
                        children='Enter a value and press submit')
                    ],
                    style={"height": "8vh"}),
                dbc.Row(
                    [
                        dcc.RadioItems(['Active wheelchair', 'No limitations', 'E-wheelchair' ,'Stroller', 'Scewo BRO'],'No limitations',inline=True,id='limitations')
                    ],
                    style={"height": "5vh"}),
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
            Output('output-textarea', 'value'),
    
            [Input('pandas-dropdown-1', 'value'),
             Input('text-input', 'value'),
             Input('limitations', 'value')],
            State('text-input', 'value'),
            prevent_initial_call=True
        )
        def update_output(selected_dropdown_value, text_input_value,limitations_value, value):
            print(limitations_value,selected_dropdown_value, value)
            self.limitations_value = limitations_value
            self.text_input_value = text_input_value
            self.selected_dropdown_value = selected_dropdown_value
            return f'You selected: {selected_dropdown_value}\nText input: {text_input_value}\nText input: {limitations_value}'
        
        @self.app.callback(
            Output('container-button-basic', 'children'),
            Input('submit-val', 'n_clicks')
        )
        def update_output2(n_clicks):
            if n_clicks==1:
                print("Button clicked", n_clicks)
                print(self.selected_dropdown_value)

    def run_server(self, debug=True):
        self.app.run_server(debug=debug)

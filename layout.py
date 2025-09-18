from dash import  dcc, html
import dash_bootstrap_components as dbc # type: ignore

class HtmlLayout:
    def __init__(self):
        pass

    def button(self, id, name,flex="1", margin="7px" ):
        button = html.Button(
            children=name,
            id=id,
            style={

                "flex": flex,
                "margin": margin
            }
        )
        return button
    
    def dropdown(self, id, options, placeholder, flex="1", margin="5px"):
        dropdown = dcc.Dropdown(
            id=id,
            options=options,
            placeholder=placeholder,
            style={
                "flex": flex,
                "margin": margin
            }
        )
        return dropdown
    def card(self,phrase,value,color="#2ecc71",margin= "5px"):
        card = dbc.Card(
        dbc.CardBody([
            html.H2(
                     f"{phrase}: {value:,.0f}",
                     style={
                         "color":color,
                           "margin": margin
                           }
                    )
                    ]))
        return card

    def graf(self,id,figure,width = "50%", height = "500px"):
        graf = dcc.Graph(
            id=id,
            figure=figure,
            style={
                "width":width,
                "height":height
            },
            config={"displayModeBar": False}
        )
        return graf


# dcc.Graph(id="line_chart",
#                    figure=line_chart_sales,
#                      style={"width": "50%", "height": "500px"}),



# dbc.Card(
#         dbc.CardBody([
#             html.H2(f" تعداد فروش"+":"+f"{Count_sales:,.0f}"+f"    |", className="card-text", style={"color": "#2ecc71","margin": "5px"})])),

# # 3. app layout
# app = Dash(__name__, title="Amirhosein daria")
# app.layout = html.Div([
#     html.Div([
#         html.Button("Reset Filters",
#                      id="reset_btn",
#                        n_clicks=0,
#                          style={"flex": "1", "margin": "5px"}
#                          ),
#         dcc.Dropdown(
#                     id='year_filter',
#                     options=df_clean["Year"].dropna().unique(),
#                     placeholder="Select Year",
#                     style={"flex": "2", "margin": "5px"}
                    
#         ),
#         dcc.Dropdown(
#                     id='main_category_filter',
#                     options=df_clean["main_category"].dropna().unique(),
#                     placeholder="Select main_category",
#                     style={"flex": "3", "margin": "5px"}     
#         ),        
#         dcc.Dropdown(
#                     id='sub_category_filter',
#                     options=df_clean["sub_category"].dropna().unique(),
#                     placeholder="Select sub_category",
#                     style={"flex": "4", "margin": "5px"}     
#         ),
#         dbc.Card(
#         dbc.CardBody([
#             html.H2(f" تعداد فروش"+":"+f"{Count_sales:,.0f}"+f"    |", className="card-text", style={"color": "#2ecc71","margin": "5px"})])),
#         dbc.Card(
#         dbc.CardBody([
#             html.H2(f" جمع فروش"+":"+f"{total_sales:,.0f}", className="card-text", style={"color": "#3498db","margin": "5px"})])),
#     ], style={"display": "flex", "alignItems": "center", "justifyContent": "center", "width": "100%"}),
#     html.Div([
#         dcc.Graph(id="line_chart",
#                    figure=line_chart_sales,
#                      style={"width": "50%", "height": "500px"}),
#         dcc.Graph(id="pie_chart",
#                    figure=pie_chart_sales,
#                      style={"width": "50%", "height": "500px"})
#     ], style={"display": "flex", "alignItems": "center", "justifyContent": "center", "width": "100%"}),
#     html.Div([
#         dcc.Graph(id="hist_chart",
#                    figure=histogram_chart,
#                      style={"width": "50%", "height": "500px"}),
#         dcc.Graph(id="Boxplot_chart",
#                    figure=Boxplot_chart,
#                      style={"width": "50%", "height": "500px"})
#     ], style={"display": "flex", "alignItems": "center", "justifyContent": "center", "width": "100%"})
# ])

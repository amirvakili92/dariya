from src.charts import drow_chart
from src.cleaner import cleaner
from src.reader import DataLoad
from dash import Dash, dcc, html, Output, Input, callback_context
import dash_bootstrap_components as dbc    
from src.layout import HtmlLayout



# 1. load data
loader = DataLoad(r"E:\D\AmirHosein\py\daria\data\amazon_products.csv")
df = loader.read_file()

cleaner_obj = cleaner(df)
df_clean = cleaner_obj.to_float_number('actual_price','actual_price')
df_clean = cleaner_obj.to_float_number('discount_price','discount_price')
df_clean = cleaner_obj.to_float_number('ratings','ratings')
df_clean = cleaner_obj.to_float_number('no_of_ratings','no_of_ratings')
df_clean = cleaner_obj.to_miladi('date','date2')
df_clean['date_Month'] = df_clean['date2'].apply(lambda x: str(x)[0:7])
df_clean['Year'] = df_clean['date2'].apply(lambda x: str(x)[0:4])
print(df_clean.head())
df_clean = cleaner_obj.season_from_date('date2','season')

total_sales = df_clean['discount_price'].sum()
Count_sales = df_clean['discount_price'].count()
date_Month_sales = df_clean.groupby(['date_Month'], as_index=False)['discount_price'].sum()

fig1 = drow_chart(date_Month_sales)
line_chart = fig1.line_chart(x='date_Month',y='discount_price',title='Monthly Sales')


# line_chart.show()
fig2 = drow_chart(df_clean)
pie_chart = fig2.pie_chart(names='season', 
                        values='discount_price',
                        title="Sales by Season",
                        color='season',
                        color_discrete_map={
                        "Spring": "#2ecc71", 
                        "Summer": "#f39c12",   
                        "Fall"  : "#e74c3c",    
                        "Winter": "#3498db"    })

fig3 = drow_chart(df_clean)
hist_chart = fig3.histogram_chart(
                               x='ratings',
                               y='discount_price',
                               title='count of Discount by Ratings',
                               histfunc='count',
                               color_discrete_sequence = ['indianred'],
                               nbins=10
                            )

fig4 = drow_chart(df_clean)
box_chart = fig4.Box_cahrt(x = 'sub_category',
                           y = 'actual_price')




# 3. app layout
app = Dash(__name__, title="Amirhosein daria")
layout = HtmlLayout()
btn = layout.button(id = "reset_btn", name= "reset filter")
dd_season = layout.dropdown(id="season",options=df_clean['season'].unique(), placeholder="Select... Season")
dd_sub_category = layout.dropdown(id="sub_category",options=df_clean['sub_category'].unique(), placeholder="Select... Sub")
dd_main_category = layout.dropdown(id="main_category",options=df_clean['main_category'].unique(), placeholder="Select... Main")
card_total_sales = layout.card('Total Sales',total_sales,color="#2e8dcc")
card_count_sales = layout.card('Count Sales',Count_sales,color="#2ec7cc")
line_chart_graf = layout.graf(id="line_chart",figure=line_chart)
pie_chart_graf = layout.graf(id="pie_chart",figure = pie_chart)
box_chart_graf = layout.graf (id="box_chart",figure=box_chart)
hist_chart_graf = layout.graf (id="hist_chart",figure=hist_chart)
dd_main_category2 = layout.dropdown(id="main_category2",options=df_clean['main_category'].unique(), placeholder="Select... Main")

#4 html design

app.layout = html.Div([
html.Div([btn, dd_season, dd_main_category, dd_sub_category,card_total_sales,card_count_sales],
          style={"display": "flex","gap": "10px", "flexWrap": "wrap","alignItems": "center"}),
html.Div([line_chart_graf,pie_chart_graf],
          style={"display": "flex"}),
html.Div([hist_chart_graf,box_chart_graf],
         style={"display": "flex"}),
])


# 4. callback: Pie click or Reset -> update Line
@app.callback(
            Output("line_chart", "figure"),
            Output("pie_chart", "figure"),
            Output("hist_chart", "figure"),
            Input("season", "value"),
            Input("sub_category","value"),
            Input("pie_chart", "clickData"),
            Input("reset_btn","n_clicks")
        )

def update_charts(selected_season,selected_sub,selected_pie,reset_clicks):
    dff = df_clean.copy()
    
    ctx = callback_context
    if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("reset_btn"):
        selected_season = None
        selected_sub = None
        selected_pie = None


    if selected_season :
        dff = dff[dff["season"] == selected_season]

    if selected_sub :
        dff  = dff[dff["sub_category"] == selected_sub]

        
    if selected_pie and "points" in selected_pie:
        pie_season = selected_pie["points"][0]["label"]
        dff = dff[dff["season"] == pie_season]


    date_Month_sales = dff.groupby(['date_Month'], as_index=False)['discount_price'].sum()
    line_fig = drow_chart(date_Month_sales)
    line_fig = line_fig.line_chart( x='date_Month', y='discount_price', title="Monthly Sales")

    # Pie chart
    pie_fig = drow_chart(dff)
    pie_fig = pie_fig.pie_chart(names='season', values='discount_price',
                        color='season',
                        color_discrete_map={
                            "Spring": "#2ecc71", 
                            "Summer": "#f39c12",   
                            "Fall"  : "#e74c3c",    
                            "Winter": "#3498db"
                        },
                        title="Sales by Season")
    
    #histochart
    hist_fig = drow_chart(dff)
    hist_fig = hist_fig.histogram_chart(
                               x='ratings',
                               y='discount_price',
                               title='count of Discount by Ratings',
                               histfunc='count',
                                color_discrete_sequence = ['indianred'],
                               nbins=10)


    return line_fig, pie_fig , hist_fig


# 5. run app
if __name__ == "__main__":
    app.run(debug=True)
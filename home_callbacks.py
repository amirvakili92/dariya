from dash import Input, Output
import plotly.express as px
import pandas as pd


@app.callback(
    Output("line_chart", "figure"),
    Output("pie_chart", "figure"),
    Output("hist_chart", "figure"),
    Input("season", "value"),
    Input("sub_category", "value"),
    Input("pie_chart", "clickData")  # <-- اینجا clickData
)
def update_charts(selected_season, selected_sub, pie_click):
    dff = df_clean.copy()
    
    # فیلتر بر اساس اسلایسر فصل
    if selected_season:
        dff = dff[dff["season"] == selected_season]

    # فیلتر بر اساس زیرشاخه
    if selected_sub:
        dff = dff[dff["sub_category"] == selected_sub]

    # فیلتر بر اساس کلیک روی Pie
    if pie_click:
        season_clicked = pie_click['points'][0]['label']
        dff = dff[dff["season"] == season_clicked]

    # تولید نمودارها
    line_fig = drow_chart(dff).line_chart(x='date_Month', y='discount_price', title="Monthly Sales")
    pie_fig = drow_chart(dff).pie_chart(
        names='season', values='discount_price',
        color_discrete_map={
            "Spring": "#2ecc71",
            "Summer": "#f39c12",
            "Fall": "#e74c3c",
            "Winter": "#3498db"
        },
        title="Sales by Season"
    )
    hist_fig = drow_chart(dff).histogram_chart(
        x='ratings', y='discount_price',
        title='Count of Discount by Ratings',
        histfunc='count',
        color_discrete_sequence=["#2ecc71"],
        nbins=10
    )

    return line_fig, pie_fig, hist_fig

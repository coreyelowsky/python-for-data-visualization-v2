from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

stocks = pd.read_csv("./stock-prices.csv")
stocks["Volume"] = round(stocks["Volume"] / 1_000_000, 1)
stocks = stocks.nlargest(5, "Volume")
print(stocks)

app = Dash()

pie_figure = px.pie(
    stocks,
    values='Volume',
    names='Company',
    title='Top 5 Stocks by Volume',
)

bar_figure = px.bar(
    stocks,
    x='Company',
    y='Volume',
    title='Top 5 Stocks by Volume, as a Bar Chart',
)

horizontal_bar_figure = px.bar(
    stocks,
    x='Volume',
    y='Company',
    orientation='h',
    title='Top 5 Stocks by Volume, as a Horizontal Bar Chart',
)

scatter_plot_figure = px.scatter(
    stocks,
    x='Volume',
    y='Close',
    title='Volume vs. Closing Price, as a Scatter Plot',
)

app.layout = html.Div([
    html.H1("Visualizing Stock Prices"),
    html.P("by Colin Jaffe"),
    dcc.Graph(figure=pie_figure),
    dcc.Graph(figure=bar_figure),
    dcc.Graph(figure=horizontal_bar_figure),
    dcc.Graph(figure=scatter_plot_figure),
])

app.run(debug=True)

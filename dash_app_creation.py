import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load and prepare data
data = pd.read_csv("finalFile.csv")
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by="Date")

# Initialize Dash app
dash_app = Dash(__name__)

# Define app layout
dash_app.layout = html.Div(
    style={'font-family': 'Arial', 'text-align': 'center', 'background-color': '#f9f9f9', 'padding': '20px'},
    children=[
        # Header
        html.H1(
            "Pink Morsel Sales Visualizer",
            style={'color': '#ff5a5f', 'margin-bottom': '40px'}
        ),

        # Radio buttons for region selection
        html.Div([
            html.Label("Select Region:", style={'font-weight': 'bold', 'margin-right': '10px'}),
            dcc.RadioItems(
                id='region_selector',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',
                inline=True,
                inputStyle={"margin-right": "5px", "margin-left": "20px"}
            )
        ], style={'margin-bottom': '30px'}),

        # Line chart
        dcc.Graph(id='sales_chart')
    ]
)


# Callback to update line chart based on selected region
@dash_app.callback(
    Output('sales_chart', 'figure'),
    Input('region_selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all': filtered_data = data
    else: filtered_data = data[data['Region'].str.lower() == selected_region]

    fig = px.line(
        filtered_data,
        x='Date',
        y='Sales',
        title=f"Pink Morsel Sales ({selected_region.capitalize()})",
        labels={'Sales': 'Sales', 'Date': 'Date'},
        template='plotly_white'
    )
    return fig

# Run the app
if __name__ == '__main__': dash_app.run(debug=True)
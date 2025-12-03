# Import packages
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('finalFile.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Define price increase date
price_increase_date = pd.Timestamp('2021-01-15')

# Filter 12 months before and after (make a copy)
start_date = price_increase_date - pd.DateOffset(months=12)
end_date = price_increase_date + pd.DateOffset(months=12)
df_window = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)].copy()

# Create month column
df_window['Month'] = df_window['Date'].dt.to_period('M').apply(lambda r: r.start_time)

# Create a complete list of months in the range
all_months = pd.date_range(start=start_date, end=end_date, freq='MS')

# Aggregate sales monthly
monthly_sales = df_window.groupby('Month')['Sales'].sum().reindex(all_months, fill_value=0).reset_index()
monthly_sales.rename(columns={'index': 'Month'}, inplace=True)

# Add a column for period coloring
monthly_sales['Period'] = ['Before' if m < price_increase_date else 'After' for m in monthly_sales['Month']]

# Create bar chart with space between bars
fig = px.bar(
    monthly_sales,
    x='Month',
    y='Sales',
    color='Period',
    title='Monthly Sales: 12 Months Before and After Price Increase',
    text='Sales',
    color_discrete_map={'Before': 'skyblue', 'After': 'orange'}
)

# Add space between bars
fig.update_layout(bargap=0.4)

# Initialize Dash app
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
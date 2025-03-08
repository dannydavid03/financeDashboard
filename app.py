import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import numpy as np
import os
import kagglehub


# Function to convert values like '41.05B', '127.00M' to numeric
def convert_to_numeric(value):
    if isinstance(value, str):
        value = value.replace(",", "")  # Remove commas
        if "B" in value:
            return float(value.replace("B", "")) * 1e9
        elif "M" in value:
            return float(value.replace("M", "")) * 1e6
        elif "K" in value:
            return float(value.replace("K", "")) * 1e3
        elif "%" in value:
            return float(value.replace("%", ""))
        else:
            try:
                return float(value)
            except ValueError:
                return np.nan
    return value


# Step 1: Load the dataset
path = kagglehub.dataset_download(
    "ilyaryabov/financial-performance-of-companies-from-sp500"
)
csv_file = os.path.join(path, "snp500_companies_description.csv")
df = pd.read_csv(csv_file)

# Check data loading

# Step 2: Data Preprocessing
# Convert relevant columns to numeric
df["Market capitalization"] = df["Market capitalization"].apply(convert_to_numeric)
df["Revenue (ttm)"] = df["Revenue (ttm)"].apply(convert_to_numeric)
df["Income (ttm)"] = df["Income (ttm)"].apply(convert_to_numeric)
df["Price-to-Earnings (ttm)"] = df["Price-to-Earnings (ttm)"].apply(convert_to_numeric)
df["Dividend yield (annual)"] = df["Dividend yield (annual)"].apply(convert_to_numeric)
df["EPS growth this year"] = df["EPS growth this year"].apply(convert_to_numeric)
df["EPS growth next year"] = df["EPS growth next year"].apply(convert_to_numeric)
df["Return on Assets (ttm)"] = df["Return on Assets (ttm)"].apply(convert_to_numeric)
df["Return on Equity (ttm)"] = df["Return on Equity (ttm)"].apply(convert_to_numeric)
df["Insider ownership"] = df["Insider ownership"].apply(convert_to_numeric)
df["Institutional ownership"] = df["Institutional ownership"].apply(convert_to_numeric)

# Convert columns that might have '-' or other non-numeric entries into NaN
df["Market capitalization"] = pd.to_numeric(
    df["Market capitalization"], errors="coerce"
)
df["Revenue (ttm)"] = pd.to_numeric(df["Revenue (ttm)"], errors="coerce")
df["Income (ttm)"] = pd.to_numeric(df["Income (ttm)"], errors="coerce")
df["Price-to-Earnings (ttm)"] = pd.to_numeric(
    df["Price-to-Earnings (ttm)"], errors="coerce"
)
df["Dividend yield (annual)"] = pd.to_numeric(
    df["Dividend yield (annual)"], errors="coerce"
)
df["EPS growth this year"] = pd.to_numeric(df["EPS growth this year"], errors="coerce")
df["EPS growth next year"] = pd.to_numeric(df["EPS growth next year"], errors="coerce")
df["Return on Assets (ttm)"] = pd.to_numeric(
    df["Return on Assets (ttm)"], errors="coerce"
)
df["Return on Equity (ttm)"] = pd.to_numeric(
    df["Return on Equity (ttm)"], errors="coerce"
)
df["Insider ownership"] = pd.to_numeric(df["Insider ownership"], errors="coerce")
df["Institutional ownership"] = pd.to_numeric(
    df["Institutional ownership"], errors="coerce"
)

# Drop rows with missing values in key columns (if necessary)
df = df.dropna(subset=["Market capitalization", "Revenue (ttm)", "Income (ttm)"])

# Step 3: Create plots
fig1 = px.scatter(
    df,
    x="Market capitalization",
    y="Revenue (ttm)",
    color="Company",
    title="Market Cap vs Revenue",
)

# Price-to-Earnings vs Market Cap
fig2 = px.scatter(
    df,
    x="Market capitalization",
    y="Price-to-Earnings (ttm)",
    color="Company",
    title="Market Cap vs P/E Ratio",
)

# Revenue vs Dividend Yield
fig3 = px.scatter(
    df,
    x="Revenue (ttm)",
    y="Dividend yield (annual)",
    color="Company",
    title="Revenue vs Dividend Yield",
)

# EPS Growth vs Price-to-Earnings Ratio
fig4 = px.scatter(
    df,
    x="Price-to-Earnings (ttm)",
    y="EPS growth this year",
    color="Company",
    title="EPS Growth vs P/E Ratio",
)

# Performance over Time (e.g., Performance (Quarter))
fig5 = px.scatter(
    df,
    x="Performance (Quarter)",
    y="Performance (Year)",
    color="Company",
    title="Performance (Quarter) vs Performance (Year)",
)

# Return on Assets vs Return on Equity
fig6 = px.scatter(
    df,
    x="Return on Assets (ttm)",
    y="Return on Equity (ttm)",
    color="Company",
    title="Return on Assets vs Return on Equity",
)

# Insider Ownership vs Institutional Ownership
fig7 = px.scatter(
    df,
    x="Insider ownership",
    y="Institutional ownership",
    color="Company",
    title="Insider Ownership vs Institutional Ownership",
)

fig8 = px.scatter(
    df,
    x="Book value per share (mrq)",
    y="Market capitalization",
    color="Company",
    title="Book Value per Share vs Market Capitalization",
)

fig9 = px.scatter(
    df,
    x="Price-to-Sales (ttm)",
    y="Price-to-Earnings (ttm)",
    color="Company",
    title="Price-to-Sales vs Price-to-Earnings Ratio",
)

fig10 = px.scatter(
    df,
    x="Operating Margin (ttm)",
    y="Net Profit Margin (ttm)",
    color="Company",
    title="Operating Margin vs Net Profit Margin",
)

fig11 = px.scatter(
    df,
    x="Total Debt to Equity (mrq)",
    y="Return on Equity (ttm)",
    color="Company",
    title="Debt-to-Equity Ratio vs Return on Equity",
)

fig12 = px.scatter(
    df,
    x="Dividend yield (annual)",
    y="EPS growth next year",
    color="Company",
    title="Dividend Yield vs EPS Growth (Next Year)",
)

fig13 = px.scatter(
    df,
    x="Quarterly revenue growth (YoY)",
    y="Quarterly earnings growth (YoY)",
    color="Company",
    title="Quarterly Revenue Growth vs Quarterly Earnings Growth",
)

fig14 = px.scatter(
    df,
    x="Price-to-Book (mrq)",
    y="Price to cash per share (mrq)",
    color="Company",
    title="Price-to-Book vs Price-to-Cash Ratio",
)

fig15 = px.scatter(
    df,
    x="Performance (Year To Date)",
    y="Performance (Quarter)",
    color="Company",
    title="Performance (Year to Date) vs Performance (Quarter)",
)

fig16 = px.scatter(
    df,
    x="Institutional ownership",
    y="Institutional transactions (3-Month change in Institutional Ownership)",
    color="Company",
    title="Institutional Ownership vs Insider Transactions",
)

fig17 = px.scatter(
    df,
    x="EPS estimate for next year",
    y="Analysts' mean recommendation (1=Buy 5=Sell)",
    color="Company",
    title="Earnings Estimate vs Analysts' Mean Recommendation",
)

fig18 = px.scatter(
    df,
    x="Market capitalization",
    y="Book value per share (mrq)",
    color="Company",
    title="Market Capitalization vs Book Value per Share",
)

fig19 = px.scatter(
    df,
    x="Cash per share (mrq)",
    y="Current stock price",
    color="Company",
    title="Cash per Share vs Current Stock Price",
)

fig20 = px.scatter(
    df,
    x="Dividend yield (annual)",
    y="Dividend (annual)",
    color="Company",
    title="Dividend Yield vs Dividend (Annual)",
)

fig21 = px.scatter(
    df,
    x="Performance (Year)",
    y="Beta",
    color="Company",
    title="Performance (Year) vs Beta",
)

fig22 = px.scatter(
    df,
    x="Full time employees",
    y="Market capitalization",
    color="Company",
    title="Full-Time Employees vs Market Capitalization",
)

fig23 = px.scatter(
    df,
    x="Volatility (Week, Month)",
    y="Performance (Year)",
    color="Company",
    title="Volatility (Week, Month) vs Performance (Year)",
)

fig24 = px.scatter(
    df,
    x="Previous close",
    y="Current stock price",
    color="Company",
    title="Previous Close vs Current Stock Price",
)

fig25 = px.scatter(
    df,
    x="Performance (Quarter)",
    y="Performance (Half Year)",
    color="Company",
    title="Performance (Quarter) vs Performance (Half Year)",
)

fig26 = px.scatter(
    df,
    x="Performance (today)",
    y="Performance (Year To Date)",
    color="Company",
    title="Performance (Today) vs Performance (Year to Date)",
)

fig27 = px.scatter(
    df,
    x="Analysts' mean recommendation (1=Buy 5=Sell)",
    y="Analysts' mean target price",
    color="Company",
    title="Analysts' Mean Recommendation vs Mean Target Price",
)


# Step 4: Create Dash App
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Financial Dashboard"),
        # Dropdown for selecting which chart to display
        dcc.Dropdown(
            id="chart-dropdown",
            options=[
                {"label": "Market Cap vs Revenue", "value": "fig1"},
                {"label": "Market Cap vs P/E Ratio", "value": "fig2"},
                {"label": "Revenue vs Dividend Yield", "value": "fig3"},
                {"label": "EPS Growth vs P/E Ratio", "value": "fig4"},
                {
                    "label": "Performance (Quarter) vs Performance (Year)",
                    "value": "fig5",
                },
                {"label": "Return on Assets vs Return on Equity", "value": "fig6"},
                {
                    "label": "Insider Ownership vs Institutional Ownership",
                    "value": "fig7",
                },
                {
                    "label": "Book Value per Share vs Market Capitalization",
                    "value": "fig8",
                },
                {"label": "Price-to-Sales vs P/E Ratio", "value": "fig9"},
                {"label": "Operating Margin vs Net Profit Margin", "value": "fig10"},
                {"label": "Debt-to-Equity vs Return on Equity", "value": "fig11"},
                {"label": "Dividend Yield vs EPS Growth (Next Year)", "value": "fig12"},
                {
                    "label": "Quarterly Revenue Growth vs Quarterly Earnings Growth",
                    "value": "fig13",
                },
                {"label": "Price-to-Book vs Price-to-Cash", "value": "fig14"},
                {
                    "label": "Performance (Year to Date) vs Performance (Quarter)",
                    "value": "fig15",
                },
                {
                    "label": "Institutional Ownership vs Insider Transactions",
                    "value": "fig16",
                },
                {
                    "label": "Earnings Estimate vs Analysts' Mean Recommendation",
                    "value": "fig17",
                },
                {"label": "Market Cap vs Book Value per Share", "value": "fig18"},
                {"label": "Cash per Share vs Current Stock Price", "value": "fig19"},
                {"label": "Dividend Yield vs Dividend (Annual)", "value": "fig20"},
                {"label": "Performance (Year) vs Beta", "value": "fig21"},
                {
                    "label": "Full-Time Employees vs Market Capitalization",
                    "value": "fig22",
                },
                {
                    "label": "Volatility (Week, Month) vs Performance (Year)",
                    "value": "fig23",
                },
                {"label": "Previous Close vs Current Stock Price", "value": "fig24"},
                {
                    "label": "Performance (Quarter) vs Performance (Half Year)",
                    "value": "fig25",
                },
                {
                    "label": "Performance (Today) vs Performance (Year to Date)",
                    "value": "fig26",
                },
                {
                    "label": "Analysts' Mean Recommendation vs Analysts' Mean Target Price",
                    "value": "fig27",
                },
            ],
            value="fig1",  # default value
            style={"width": "50%"},
        ),
        # Graph to display selected chart
        dcc.Graph(id="graph"),
    ]
)


# Step 5: Callback to update the graph based on dropdown selection
@app.callback(
    dash.dependencies.Output("graph", "figure"),
    [dash.dependencies.Input("chart-dropdown", "value")],
)
def update_graph(selected_chart):
    if selected_chart == "fig1":
        return fig1
    elif selected_chart == "fig2":
        return fig2
    elif selected_chart == "fig3":
        return fig3
    elif selected_chart == "fig4":
        return fig4
    elif selected_chart == "fig5":
        return fig5
    elif selected_chart == "fig6":
        return fig6
    elif selected_chart == "fig7":
        return fig7
    elif selected_chart == "fig8":
        return fig8
    elif selected_chart == "fig9":
        return fig9
    elif selected_chart == "fig10":
        return fig10
    elif selected_chart == "fig11":
        return fig11
    elif selected_chart == "fig12":
        return fig12
    elif selected_chart == "fig13":
        return fig13
    elif selected_chart == "fig14":
        return fig14
    elif selected_chart == "fig15":
        return fig15
    elif selected_chart == "fig16":
        return fig16
    elif selected_chart == "fig17":
        return fig17
    elif selected_chart == "fig18":
        return fig18
    elif selected_chart == "fig19":
        return fig19
    elif selected_chart == "fig20":
        return fig20
    elif selected_chart == "fig21":
        return fig21
    elif selected_chart == "fig22":
        return fig22
    elif selected_chart == "fig23":
        return fig23
    elif selected_chart == "fig24":
        return fig24
    elif selected_chart == "fig25":
        return fig25
    elif selected_chart == "fig26":
        return fig26
    elif selected_chart == "fig27":
        return fig27
    else:
        return fig1  # Default chart


if __name__ == "__main__":
    app.run_server(debug=True)

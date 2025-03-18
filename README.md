# Financial Dashboard

This project is a financial dashboard application built with **Dash**, **Plotly**, and **Pandas**. It provides visualizations and interactive plots that allow users to explore various financial metrics for different companies.

The data includes key financial information such as market capitalization, income, revenue, earnings per share (EPS), and various ratios, along with stock performance over time. The app allows users to view these financial metrics through interactive visualizations and compare them across multiple companies.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

---

## Features

- **Data Visualization:** 
  - Scatter plots comparing financial metrics such as market capitalization vs revenue, P/E ratio, dividend yield, and EPS growth.
  - Visualizations for stock performance over different periods (week, month, quarter, year).
  
- **Interactive Dashboard:**
  - Dropdown menu to choose different visualizations dynamically.
  - Color-coded scatter plots for each company in the dataset.

- **Custom Data Preprocessing:**
  - Conversion of financial values (e.g., ‘41.05B’, ‘127.00M’) to numeric values.
  - Handling missing data and outliers.

---

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/financial-dashboard.git
```

### 2. Navigate to the project directory and install the necessary Python libraries:
```bash
pip install -r requirements.txt
```

---

## Usage

To start the dashboard, run the following command in your terminal:
```bash
python app.py
```

Once the server is running, open your browser and go to http://127.0.0.1:8050/ to access the dashboard.

### How to interact with the dashboard:

1. Use the dropdown menu to select the financial metrics or company you want to visualize.
2. Explore different plots by selecting various timeframes for stock performance (week, month, quarter, year).
3. Hover over the data points in the visualizations to see more details about each company.

### Future Improvements

1. Deploy the finance dashboard online for easy visibility
2. Use the insights from the dashboard to develop machine learning models.



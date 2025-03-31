import pandas as pd
from alpha_vantage.fundamentaldata import FundamentalData

API_KEY = "UTM62HDCH8O84Z0X"  # Get it from https://www.alphavantage.co/support/#api-key
symbol = "GOOG"  # Replace with your ticker

fd = FundamentalData(API_KEY)

# Fetch data
income = fd.get_income_statement_annual(symbol)[0]
balance = fd.get_balance_sheet_annual(symbol)[0]
cashflow = fd.get_cash_flow_annual(symbol)[0]

# Save to CSV
income.to_csv(f"{symbol}_income_statement_10y.csv")
balance.to_csv(f"{symbol}_balance_sheet_10y.csv")
cashflow.to_csv(f"{symbol}_cash_flow_10y.csv")

print(f"Data saved for {symbol}!")

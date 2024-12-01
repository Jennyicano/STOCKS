#! /usr/bin/env python

# Financial data.
import yfinance as yf

# Dates and times.
import datetime as dt

# Get data for Microsoft, Apple and Google
tickets = ['MSFT', 'AAPL', 'GOOG']
df = yf.download(['MSFT', 'AAPL', 'GOOG'], period='1d', interval="1m")

# Get the current date and time.
filename = dt.datetime.now()
# Create a string in the format YYYYMMDD_HHMMSS.
filename = filename.strftime("%Y%m%d_%H%M%S")
# Prepend data folder, append file extension. 
filename = 'data/' + filename + ".csv"

# Show the filename.
filename

# Save the data to a CSV file.
df['Close'].to_csv(filename)

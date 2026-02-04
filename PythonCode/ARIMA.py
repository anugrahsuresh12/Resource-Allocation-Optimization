import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Load your data
df = pd.read_excel('cleaned_data.xlsx')

# Convert 'EntryTimeandDate' to datetime if it's not already
df['EntryTimeandDate'] = pd.to_datetime(df['EntryTimeandDate'])

# Ensure the data is sorted by EntryTimeandDate
df = df.sort_values('EntryTimeandDate')

# Remove duplicates by aggregating values (e.g., taking the mean of duplicates)
df = df.groupby('EntryTimeandDate').agg({'Consultation Revenue': 'mean'}).reset_index()

# Set EntryTimeandDate as the index
df.set_index('EntryTimeandDate', inplace=True)

# Set frequency (daily, hourly, etc.)
df = df.asfreq('h', method='pad')  # Using 'pad' to propagate the last value forward for missing timestamps

# Select the column you want to forecast (e.g., 'Consultation Revenue')
series = df['Consultation Revenue']

# Perform ADF test to check stationarity
result = adfuller(series.dropna())
print(f"ADF Statistic: {result[0]}")
print(f"p-value: {result[1]}")
if result[1] <= 0.05:
    print("The series is stationary.")
else:
    print("The series is not stationary.")

# Fit ARIMA model (adjust p, d, q values based on your data)
model = ARIMA(series, order=(1, 1, 1))  # ARIMA(p, d, q)
model_fit = model.fit()

# Summary of the ARIMA model
print(model_fit.summary())

# Make predictions
forecast_steps = 720 # Number of steps ahead to predict (e.g., next 24 hours/days)
forecast = model_fit.forecast(steps=forecast_steps)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(series, label='Actual')
plt.plot(pd.date_range(series.index[-1], periods=forecast_steps+1, freq='h')[1:], forecast, label='Forecast', color='red')
plt.title('ARIMA Forecast of Consultation Revenue')
plt.xlabel('Date')
plt.ylabel('Consultation Revenue')
plt.legend()
plt.show()

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Step 1: Download data
tickers = ['QQEW', 'EFA', 'TLT', 'UUP', 'IEI']  # in real trading use QQQE instead of QQEW
data = yf.download(tickers, start="2011-01-01", end=datetime.today().strftime('%Y-%m-%d'))['Adj Close']

# Step 2: Calculate the rates of change (ROC)
roc10 = data.pct_change(10)
roc21 = data.pct_change(21)
roc63 = data.pct_change(63)
roc126 = data.pct_change(126)

# Step 3: Calculate momentum for qqew and efa
momentum_qqew = (roc21['QQEW'] + roc63['QQEW'] + roc126['QQEW']) / 3
momentum_efa = (roc21['EFA'] + roc63['EFA'] + roc126['EFA']) / 3
momentum_iei = (roc21['IEI'] + roc63['IEI'] + roc126['IEI']) / 3

# Calculate ROC21 for TLT and UUP
roc21_tlt = roc21['TLT'] + roc63['TLT']
roc21_uup = roc21['UUP'] + roc63['UUP']

### WEEKLY DECISIONS ###
# Step 4: Define weekly decision dates (last trading day of each week)
weekly_dates = data.resample('W-FRI').last().index

# Step 5: Initialize variables for equity and position tracking
initial_balance = 10000  # Starting with $10,000
equity = np.full(len(data), initial_balance)  # Start with initial balance for each day
positions = np.zeros(len(data), dtype=int)  # Track position (1 for qqew, 2 for efa, 3 for TLT, 4 for UUP)

## Step 6: Iterate over each weekly date to apply the trading logic and update positions
current_position = None  # Track current position
min_date = data.index[126]  # First date with enough data for all momentum calculations

for date in weekly_dates:
    if date in data.index and date >= min_date:
        idx = data.index.get_loc(date)

        # Get momentum values on the last trading day of the week
        qqew_mom = momentum_qqew.iloc[idx]
        efa_mom = momentum_efa.iloc[idx]
        iei_mom = momentum_iei.iloc[idx]
        
        tlt_mom = roc21_tlt.iloc[idx]
        uup_mom = roc21_uup.iloc[idx]
        

        # Determine the position based on momentum values
        if qqew_mom > efa_mom and qqew_mom > iei_mom and qqew_mom > 0:
            current_position = 1  # Long qqew
        elif efa_mom > qqew_mom and efa_mom > iei_mom and efa_mom > 0:
            current_position = 2  # Long efa
        # if not long equities
        else:
            current_position = 3 if tlt_mom > uup_mom else 4
        # Fill the positions array continuously with the selected position until the next decision point
        positions[idx:] = current_position

# plt.plot(data.index, positions)
# plt.show()

# print(positions[:600])

# Step 7: Calculate the daily equity line based on the selected positions
returns = data.pct_change().fillna(0)
for i in range(1, len(data)):
    # Carry forward the last position if not on a decision date
    if positions[i] == 0:
        positions[i] = positions[i-1]
    
    # Update equity based on the returns of the selected asset
    if positions[i-1] == 1:
        equity[i] = equity[i-1] * (1 + returns['QQEW'].iloc[i])
    elif positions[i-1] == 2:
        equity[i] = equity[i-1] * (1 + returns['EFA'].iloc[i])
    elif positions[i-1] == 3:
        equity[i] = equity[i-1] * (1 + returns['TLT'].iloc[i])
    elif positions[i-1] == 4:
        equity[i] = equity[i-1] * (1 + returns['UUP'].iloc[i])
    else:
        equity[i] = equity[i-1]  # No position change

print(f"momentum system equity = {equity[-1]}")

plt.plot(data.index, equity, label='Total Equity Line with VOO System')
plt.xlabel('Date')
plt.ylabel('Equity ($)')
plt.title('Combined Equity Line of Trading Systems (Continuous Mark-to-Market)')
plt.legend()
plt.show()

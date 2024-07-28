import pandas as pd
import matplotlib.pyplot as plt

# Loading and preprocessing the data
df = pd.read_csv('test_logs.csv', sep=';', header=0)
df['currentTime'] = pd.to_datetime(df['currentTime'], unit='ns')
trades = df[df['action'] == 'filled'].copy()

trades['tradePx'] = pd.to_numeric(trades['tradePx'], errors='coerce')
trades['tradeAmt'] = pd.to_numeric(trades['tradeAmt'], errors='coerce')

# Calculateing PnL
trades['PnL'] = trades.apply(lambda row: row['tradeAmt'] * row['tradePx'] * (-1 if row['orderSide'] == 'buy' else 1), axis=1)

# Calculating total gross PnL
total_gross_pnl = trades['PnL'].sum()

# Calculate total gross PnL over each security ID
pnl_by_security = trades.groupby('orderProduct')['PnL'].sum()

# Plotting Graph
trades = trades.sort_values('currentTime')
trades['Cumulative_PnL'] = trades['PnL'].cumsum()

plt.figure(figsize=(12, 6))
plt.plot(trades['currentTime'], trades['Cumulative_PnL'])
plt.title('Cumulative Gross PnL')
plt.xlabel('Time')
plt.ylabel('Cumulative PnL')
plt.grid(True)
plt.tight_layout()
plt.savefig('cumulative_gross_pnl.png')

# Print results
print(f"Total Gross PnL: {total_gross_pnl:.2f}")
print("\nGross PnL by Security ID:")
print(pnl_by_security)
print("\nCumulative Gross PnL chart has been saved as 'cumulative_gross_pnl.png'")
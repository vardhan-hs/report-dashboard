import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the data
df = pd.read_csv('test_logs.csv', sep=';', header=0)
df['currentTime'] = pd.to_datetime(df['currentTime'], unit='ns')
trades = df[df['action'] == 'filled'].copy()

print(df)
# Convert tradePx and tradeAmt to numeric, handling potential empty strings
trades['tradePx'] = pd.to_numeric(trades['tradePx'], errors='coerce')
trades['tradeAmt'] = pd.to_numeric(trades['tradeAmt'], errors='coerce')

# Calculate PnL for each trade
trades['PnL'] = trades.apply(lambda row: row['tradeAmt'] * row['tradePx'] * (-1 if row['orderSide'] == 'buy' else 1), axis=1)

# Step 2: Calculate total gross PnL
total_gross_pnl = trades['PnL'].sum()

# Step 3: Calculate total gross PnL over each security ID
pnl_by_security = trades.groupby('orderProduct')['PnL'].sum()

# Step 4: Draw cumulative gross PnL
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
import pandas as pd
import os

def load_and_process_data(file_path):
    file_path = os.path.join('..', 'resources', file_path)
    
    df = pd.read_csv(file_path, sep=';', header=0)
    df['currentTime'] = pd.to_datetime(df['currentTime'], unit='ns')
    trades = df[df['action'] == 'filled'].copy()

    trades['tradePx'] = pd.to_numeric(trades['tradePx'], errors='coerce')
    trades['tradeAmt'] = pd.to_numeric(trades['tradeAmt'], errors='coerce')

    trades['PnL'] = trades.apply(lambda row: row['tradeAmt'] * row['tradePx'] * (-1 if row['orderSide'] == 'buy' else 1), axis=1)
    
    trades = trades.sort_values('currentTime') # can be removed to improve performance if data is guaranteed to be in sorted order
    trades['Cumulative_PnL'] = trades['PnL'].cumsum()

    return trades

def calculate_total_pnl(trades):
    return trades['PnL'].sum()

def calculate_pnl_by_security(trades):
    return trades.groupby('orderProduct')['PnL'].sum()

def calculate_cumulative_pnl_by_security(trades):
    securities = trades['orderProduct'].unique()
    return {security: trades[trades['orderProduct'] == security]['PnL'].cumsum() for security in securities}
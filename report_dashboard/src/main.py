from dash import Dash
from data_processing import load_and_process_data, calculate_total_pnl, calculate_pnl_by_security, calculate_cumulative_pnl_by_security
from layouts import create_layout
from callbacks import register_callbacks

# Load and process data
trades = load_and_process_data('test_logs.csv')
total_gross_pnl = calculate_total_pnl(trades)
pnl_by_security = calculate_pnl_by_security(trades)
cumulative_pnl_by_security = calculate_cumulative_pnl_by_security(trades)

# Create Dash app
app = Dash(__name__)

# Set up the layout
app.layout = create_layout(total_gross_pnl, pnl_by_security, trades['orderProduct'].unique())

# Register callbacks
register_callbacks(app, trades, cumulative_pnl_by_security)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
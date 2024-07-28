from dash import html, dcc
from styles import STYLES, COLORS

def create_layout(total_gross_pnl, pnl_by_security, securities,file_name):
    return html.Div([
        html.H1("Report Analysis Dashboard", style=STYLES['header']),
        
        html.Div([
            html.Div([
            html.H2(f"PnL Report: {file_name}", style=STYLES['report_name']),
            html.H4(f"Total Gross PnL: {total_gross_pnl:.2f}", style=STYLES['key_details_1']),
            
            html.H3("Gross PnL by Security ID:", style=STYLES['subheader']),
            html.Pre(pnl_by_security.to_string(index=True, header=False), style=STYLES['key_details_2'])
            ]),

            dcc.Graph(id='cumulative-pnl-chart', style=STYLES['graph']),

            html.Div([
            dcc.Checklist(
                id='security-checklist',
                options=[{'label': security, 'value': security} for security in securities] + [{'label': 'Total', 'value': 'Total'}],
                value=['Total'],
                inline=True,
                style=STYLES['checklist'],
                inputStyle=STYLES['checklist_item'],
                labelStyle=STYLES['checklist_item']
            )
            ])
        ], style =STYLES['report_container'])
    ], style=STYLES['main_container'])
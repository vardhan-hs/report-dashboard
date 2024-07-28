from dash import html, dcc
from styles import STYLES, COLORS

def create_layout(total_gross_pnl, pnl_by_security, securities):
    return html.Div([
        html.H1("Trading Analysis Dashboard", style=STYLES['header']),
        
        html.Div([
            html.Div([
            html.H3(f"Total Gross PnL: {total_gross_pnl:.2f}", style=STYLES['subheader']),
            
            html.H3("Gross PnL by Security ID:", style=STYLES['subheader']),
            html.Pre(pnl_by_security.to_string(), style=STYLES['paragraph'])
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
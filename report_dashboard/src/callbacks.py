from dash.dependencies import Input, Output
import plotly.graph_objs as go
from styles import GRAPH_COLORS, COLORS

def register_callbacks(app, trades, cumulative_pnl_by_security):
    @app.callback(
        Output('cumulative-pnl-chart', 'figure'),
        Input('security-checklist', 'value')
    )
    def update_graph(selected_securities):
        traces = []
        
        if 'Total' in selected_securities:
            traces.append(go.Scatter(
                x=trades['currentTime'],
                y=trades['Cumulative_PnL'],
                mode='lines',
                name='Total',
                line=dict(color=GRAPH_COLORS[0])
            ))
        
        for i, security in enumerate(trades['orderProduct'].unique()):
            if security in selected_securities:
                traces.append(go.Scatter(
                    x=trades[trades['orderProduct'] == security]['currentTime'],
                    y=cumulative_pnl_by_security[security],
                    mode='lines',
                    name=security,
                    line=dict(color=GRAPH_COLORS[(i + 1) % len(GRAPH_COLORS)])
                ))
        
        layout = go.Layout(
            title='Cumulative Gross PnL',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Cumulative PnL'},
            plot_bgcolor=COLORS['background'],
            paper_bgcolor=COLORS['background'],
            font=dict(color=COLORS['text'])
        )
        
        return {'data': traces, 'layout': layout}
COLORS = {
    'background': '#181818',
    'text': '#FFFFFF',
    'primary': '#FF6600',
    'secondary_background': '#1F1F1F',
    'border': '#333333',
    'grid_color':"#202020"
}

FONTS = {
    'main': 'Arial, sans-serif',
    'headers': 'Helvetica, sans-serif'
}

STYLES = {
    'main_container': {
        'backgroundColor': COLORS['background'],
        'padding': '20px 100px',
        'fontFamily': FONTS['main'],
        'textAlign': 'center', 
    },
    'report_container': {
        'backgroundColor': COLORS['secondary_background'],
        'padding': '20px 100px 50px 100px',
        'fontFamily': FONTS['main'],
        'textAlign': 'left', 
    },
    'header': {
        'color': COLORS['primary'],
        'fontFamily': FONTS['headers'],
        'fontSize': '28px',
        'marginBottom': '40px'
    },
    'key_details_1': {
        'color': COLORS['primary'],
        'fontFamily': FONTS['headers'],
        'fontSize': '20px',
        'marginTop': '15px',
        'marginBottom': '10px'
    },
    'key_details_2': {
        'color': COLORS['primary'],
        'fontFamily': FONTS['headers'],
        'fontSize': '14px',
        'lineHeight': '2'
    },
    'subheader': {
        'color': COLORS['text'],
        'fontFamily': FONTS['headers'],
        'fontSize': '14px',
        'marginTop': '16px',
    },
    'report_name': {
        'color': COLORS['text'],
        'fontFamily': FONTS['headers'],
        'fontSize': '24px',
        'marginBottom': '15px',
        'borderBottom': f'2px solid {COLORS["border"]}',
        'paddingBottom': '5px'
    },
    'graph': {
        'backgroundColor': 'white',
        'border': f'1px solid {COLORS['border']}',
        'borderRadius': '5px',
        'padding': '10px'
    },
    'checklist': {
        'marginTop': '15px',
        'marginBottom': '15px',
        'textAlign': 'center'
    },
    'checklist_item': {
        'color': COLORS['text'],
        'fontSize': '14px',
        'marginRight': '20px'
    }
}

GRAPH_COLORS = [
    COLORS['primary'],
    '#00FFFF',
    '#39FF14',
    '#FF1493',
    '#FF6B6B',
    '#4ECDC4',
    '#45B7D1'
]
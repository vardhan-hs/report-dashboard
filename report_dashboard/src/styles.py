# styles.py

# Color scheme
COLORS = {
    'background': '#000000',
    'text': '#FFFFFF',
    'primary': '#007BFF',
    'secondary': '#6C757D',
    'secondary_background': '#161A1D',
    #'danger': '#DC3545',
    #'warning': '#FFC107',
    #'info': '#17A2B8'
}

# Font styles
FONTS = {
    'main': 'Arial, sans-serif',
    'headers': 'Helvetica, sans-serif'
}

# Styles for specific components
STYLES = {
    'main_container': {
        'backgroundColor': COLORS['background'],
        'padding': '50px 100px',
        'fontFamily': FONTS['main'],
        'textAlign': 'center', 
    },
    'report_container': {
        'backgroundColor': COLORS['secondary_background'],
        'padding': '100px',
        'fontFamily': FONTS['main'],
        'textAlign': 'center', 
    },
    'header': {
        'color': COLORS['primary'],
        'fontFamily': FONTS['headers'],
        'fontSize': '28px',
        'marginBottom': '20px'
    },
    'subheader': {
        'color': COLORS['secondary'],
        'fontFamily': FONTS['headers'],
        'fontSize': '20px',
        'marginTop': '15px',
        'marginBottom': '10px'
    },
    'paragraph': {
        'color': COLORS['text'],
        'fontSize': '14px',
        'lineHeight': '1.5'
    },
    'graph': {
        'backgroundColor': 'white',
        'border': f'1px solid {COLORS["secondary"]}',
        'borderRadius': '5px',
        'padding': '10px'
    },
    'checklist': {
        'marginTop': '15px',
        'marginBottom': '15px'
    },
    'checklist_item': {
        'color': COLORS['text'],
        'fontSize': '14px',
        'marginRight': '10px'
    }
}

# Graph color scheme
GRAPH_COLORS = [
    COLORS['primary'],
    # COLORS['success'],
    # COLORS['danger'],
    # COLORS['warning'],
    # COLORS['info'],
    '#FF6B6B',  # Additional colors for more data series
    '#4ECDC4',
    '#45B7D1',
    '#F9D56E',
    '#FF8C42'
]
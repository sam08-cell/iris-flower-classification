def get_custom_css(dark_mode: bool = False) -> str:
    """Return sleek, modern, enterprise SaaS typography and responsive layout styling."""
    if dark_mode:
        bg_primary = "#0b0f19"
        bg_card = "#111827"
        border_card = "#1f2937"
        text_primary = "#f9fafb"
        text_secondary = "#9ca3af"
        accent_color = "#6366f1"
        card_shadow = "0 4px 20px -2px rgba(0, 0, 0, 0.5)"
        sidebar_bg = "#0f172a"
        stat_bg = "#1f2937"
        hero_gradient = "linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%)"
    else:
        bg_primary = "#f8fafc"
        bg_card = "#ffffff"
        border_card = "#e2e8f0"
        text_primary = "#0f172a"
        text_secondary = "#475569"
        accent_color = "#4f46e5"
        card_shadow = "0 4px 16px -2px rgba(15, 23, 42, 0.06), 0 2px 6px -2px rgba(15, 23, 42, 0.04)"
        sidebar_bg = "#ffffff"
        stat_bg = "#f1f5f9"
        hero_gradient = "linear-gradient(135deg, #1e1b4b 0%, #3730a3 50%, #4f46e5 100%)"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    
    code, pre {{
        font-family: 'JetBrains Mono', monospace !important;
    }}
    
    .stApp {{
        background: {bg_primary};
        color: {text_primary};
    }}
    
    /* Clean, Professional SaaS Card (no fixed heights, no overflow) */
    .saas-card {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 12px;
        padding: 24px;
        box-shadow: {card_shadow};
        margin-bottom: 20px;
        height: auto;
        overflow: visible;
        box-sizing: border-box;
    }}
    
    .saas-card h3, .saas-card h4, .saas-card h5 {{
        color: {text_primary};
        margin-top: 0;
        font-weight: 700;
        letter-spacing: -0.01em;
    }}
    
    .saas-card p, .saas-card span, .saas-card li {{
        color: {text_secondary};
        line-height: 1.6;
        word-wrap: break-word;
    }}
    
    /* Premium Executive Hero Banner */
    .saas-hero {{
        background: {hero_gradient};
        border-radius: 16px;
        padding: 36px 32px;
        color: #ffffff;
        box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.35);
        margin-bottom: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .saas-hero h1 {{
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 12px 0;
        color: #ffffff;
        letter-spacing: -0.02em;
    }}
    
    .saas-hero p {{
        font-size: 1.05rem;
        color: #e0e7ff;
        margin: 0;
        line-height: 1.6;
        max-width: 800px;
    }}
    
    /* Executive Metric Badge */
    .saas-stat-badge {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 12px;
        padding: 18px 20px;
        box-shadow: {card_shadow};
        margin-bottom: 12px;
    }}
    
    .saas-stat-badge .stat-num {{
        font-size: 1.85rem;
        font-weight: 800;
        color: {accent_color};
        line-height: 1.2;
    }}
    
    .saas-stat-badge .stat-lbl {{
        font-size: 0.8rem;
        font-weight: 600;
        color: {text_secondary};
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-top: 4px;
    }}
    
    /* Clean Species Diagnostic Badge */
    .species-tag {{
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }}
    
    .species-tag-setosa {{
        background: rgba(59, 130, 246, 0.12);
        color: #2563eb;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }}
    
    .species-tag-versicolor {{
        background: rgba(139, 92, 246, 0.12);
        color: #7c3aed;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }}
    
    .species-tag-virginica {{
        background: rgba(236, 72, 153, 0.12);
        color: #db2777;
        border: 1px solid rgba(236, 72, 153, 0.3);
    }}
    
    /* Streamlit Components Enhancement */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg};
        border-right: 1px solid {border_card};
    }}
    
    .stButton>button {{
        border-radius: 8px;
        font-weight: 600;
        padding: 8px 18px;
    }}
    
    /* Ensure clean tables */
    [data-testid="stDataFrame"] {{
        border-radius: 8px;
        overflow: hidden;
    }}
    </style>
    """

def get_custom_css(dark_mode: bool = False) -> str:
    """Return sleek, modern, enterprise SaaS typography and high-contrast light/dark mode."""
    if dark_mode:
        bg_primary = "#090d16"
        bg_card = "#121826"
        border_card = "#1f293d"
        text_primary = "#ffffff"
        text_secondary = "#94a3b8"
        accent_color = "#818cf8"
        card_shadow = "0 4px 20px -2px rgba(0, 0, 0, 0.6)"
        sidebar_bg = "#0c111d"
        stat_bg = "#1e293b"
        hero_gradient = "linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%)"
        input_bg = "#1e293b"
        input_text = "#ffffff"
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
        input_bg = "#ffffff"
        input_text = "#0f172a"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: {bg_primary} !important;
        color: {text_primary} !important;
    }}
    
    /* Main Streamlit App Wrapper */
    .stApp {{
        background-color: {bg_primary} !important;
        color: {text_primary} !important;
    }}
    
    /* Sidebar Background & Elements */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        border-right: 1px solid {border_card} !important;
    }}
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] span {{
        color: {text_primary} !important;
    }}
    
    /* Ensure Header & Nav are styled */
    header[data-testid="stHeader"] {{
        background-color: transparent !important;
    }}
    
    /* Clean, Professional SaaS Card (no fixed heights, no overflow) */
    .saas-card {{
        background-color: {bg_card} !important;
        border: 1px solid {border_card} !important;
        border-radius: 12px;
        padding: 24px;
        box-shadow: {card_shadow};
        margin-bottom: 20px;
        height: auto;
        overflow: visible;
        box-sizing: border-box;
    }}
    
    .saas-card h2, .saas-card h3, .saas-card h4, .saas-card h5 {{
        color: {text_primary} !important;
        margin-top: 0;
        font-weight: 700;
        letter-spacing: -0.01em;
    }}
    
    .saas-card p, .saas-card span, .saas-card li {{
        color: {text_secondary} !important;
        line-height: 1.6;
        word-wrap: break-word;
    }}
    
    /* Premium Executive Hero Banner */
    .saas-hero {{
        background: {hero_gradient} !important;
        border-radius: 16px;
        padding: 36px 32px;
        color: #ffffff !important;
        box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.35);
        margin-bottom: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .saas-hero h1 {{
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 12px 0;
        color: #ffffff !important;
        letter-spacing: -0.02em;
    }}
    
    .saas-hero p {{
        font-size: 1.05rem;
        color: #e0e7ff !important;
        margin: 0;
        line-height: 1.6;
        max-width: 800px;
    }}
    
    /* Species Diagnostic Badges */
    .species-tag {{
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.8rem;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }}
    
    .species-tag-setosa {{
        background: rgba(59, 130, 246, 0.18) !important;
        color: #3b82f6 !important;
        border: 1px solid rgba(59, 130, 246, 0.4);
    }}
    
    .species-tag-versicolor {{
        background: rgba(139, 92, 246, 0.18) !important;
        color: #a855f7 !important;
        border: 1px solid rgba(139, 92, 246, 0.4);
    }}
    
    .species-tag-virginica {{
        background: rgba(236, 72, 153, 0.18) !important;
        color: #ec4899 !important;
        border: 1px solid rgba(236, 72, 153, 0.4);
    }}
    
    /* Buttons */
    .stButton>button {{
        border-radius: 8px;
        font-weight: 600;
        padding: 8px 18px;
    }}
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {text_primary} !important;
    }}
    </style>
    """

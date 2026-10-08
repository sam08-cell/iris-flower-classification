def get_custom_css(dark_mode: bool = False) -> str:
    """Return polished custom CSS styling for light or dark glassmorphic SaaS theme."""
    if dark_mode:
        bg_primary = "#0a0e1a"
        bg_card = "rgba(23, 31, 51, 0.75)"
        border_card = "rgba(99, 102, 241, 0.25)"
        text_primary = "#f8fafc"
        text_secondary = "#94a3b8"
        accent_gradient = "linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%)"
        card_shadow = "0 8px 32px 0 rgba(0, 0, 0, 0.37)"
        sidebar_bg = "#0f172a"
        stat_bg = "rgba(30, 41, 59, 0.8)"
    else:
        bg_primary = "#f8fafc"
        bg_card = "rgba(255, 255, 255, 0.85)"
        border_card = "rgba(226, 232, 240, 0.8)"
        text_primary = "#0f172a"
        text_secondary = "#475569"
        accent_gradient = "linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%)"
        card_shadow = "0 10px 25px -5px rgba(99, 102, 241, 0.1), 0 8px 10px -6px rgba(99, 102, 241, 0.05)"
        sidebar_bg = "#ffffff"
        stat_bg = "rgba(241, 245, 249, 0.85)"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    
    /* Main application background */
    .stApp {{
        background: {bg_primary};
        color: {text_primary};
    }}
    
    /* Glassmorphism Cards */
    .glass-card {{
        background: {bg_card};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {border_card};
        border-radius: 16px;
        padding: 24px;
        box-shadow: {card_shadow};
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        margin-bottom: 20px;
    }}
    
    .glass-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 14px 35px -5px rgba(99, 102, 241, 0.18);
    }}
    
    /* Hero Section Banner */
    .hero-banner {{
        background: {accent_gradient};
        border-radius: 20px;
        padding: 40px 32px;
        color: #ffffff;
        text-align: center;
        box-shadow: 0 20px 35px -10px rgba(99, 102, 241, 0.4);
        margin-bottom: 28px;
        animation: fadeIn 0.8s ease-in-out;
    }}
    
    .hero-title {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }}
    
    .hero-subtitle {{
        font-size: 1.15rem;
        font-weight: 400;
        opacity: 0.95;
        max-width: 680px;
        margin: 0 auto 20px auto;
        line-height: 1.5;
    }}
    
    /* Stat Metric Box */
    .metric-badge {{
        background: {stat_bg};
        border: 1px solid {border_card};
        border-radius: 14px;
        padding: 16px 20px;
        text-align: center;
        transition: all 0.2s ease;
    }}
    
    .metric-value {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        background: {accent_gradient};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }}
    
    .metric-label {{
        font-size: 0.85rem;
        font-weight: 600;
        color: {text_secondary};
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }}
    
    /* Species Prediction Card */
    .prediction-card-setosa {{
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.12) 0%, rgba(99, 102, 241, 0.2) 100%);
        border: 2px solid #3b82f6;
        border-radius: 18px;
        padding: 24px;
        text-align: center;
    }}
    
    .prediction-card-versicolor {{
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.12) 0%, rgba(168, 85, 247, 0.2) 100%);
        border: 2px solid #8b5cf6;
        border-radius: 18px;
        padding: 24px;
        text-align: center;
    }}
    
    .prediction-card-virginica {{
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.12) 0%, rgba(244, 63, 94, 0.2) 100%);
        border: 2px solid #ec4899;
        border-radius: 18px;
        padding: 24px;
        text-align: center;
    }}
    
    /* Best Model Tag */
    .best-badge {{
        display: inline-block;
        background: #10b981;
        color: white;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg};
        border-right: 1px solid {border_card};
    }}
    
    /* Primary buttons */
    .stButton>button {{
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    
    /* Form inputs */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{
        border-radius: 10px;
    }}
    
    /* Keyframe Animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    """

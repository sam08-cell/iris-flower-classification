def get_custom_css(dark_mode: bool = False) -> str:
    """
    Official shadcn/ui Design System Implementation for Streamlit.
    Faithfully reproduces shadcn/ui zinc theme design tokens, borders, radix-style typography,
    subtle micro-interactions, clean cards, badges, and tab styling.
    """
    if dark_mode:
        # shadcn/ui dark (zinc) design tokens
        background = "#09090b"         # bg-zinc-950
        card = "#09090b"               # bg-zinc-950
        card_foreground = "#fafafa"    # text-zinc-50
        popover = "#09090b"
        popover_foreground = "#fafafa"
        primary = "#fafafa"            # text-zinc-50 / bg-zinc-50
        primary_foreground = "#18181b" # text-zinc-900
        secondary = "#27272a"          # bg-zinc-800
        secondary_foreground = "#fafafa"
        muted = "#27272a"              # bg-zinc-800
        muted_foreground = "#a1a1aa"   # text-zinc-400
        accent = "#27272a"
        accent_foreground = "#fafafa"
        destructive = "#7f1d1d"
        destructive_foreground = "#fafafa"
        border = "#27272a"             # border-zinc-800
        input_border = "#27272a"
        ring = "#d4d4d8"
        sidebar_bg = "#09090b"
        shadow_sm = "0 1px 2px 0 rgba(0, 0, 0, 0.4)"
        shadow_card = "0 1px 3px 0 rgba(0, 0, 0, 0.4), 0 1px 2px -1px rgba(0, 0, 0, 0.4)"
    else:
        # shadcn/ui light (zinc) design tokens
        background = "#ffffff"         # bg-white
        card = "#ffffff"               # bg-white
        card_foreground = "#09090b"    # text-zinc-950
        popover = "#ffffff"
        popover_foreground = "#09090b"
        primary = "#18181b"            # bg-zinc-900
        primary_foreground = "#fafafa" # text-zinc-50
        secondary = "#f4f4f5"          # bg-zinc-100
        secondary_foreground = "#18181b"
        muted = "#f4f4f5"              # bg-zinc-100
        muted_foreground = "#71717a"   # text-zinc-500
        accent = "#f4f4f5"
        accent_foreground = "#18181b"
        destructive = "#ef4444"
        destructive_foreground = "#fafafa"
        border = "#e4e4e7"             # border-zinc-200
        input_border = "#e4e4e7"
        ring = "#18181b"
        sidebar_bg = "#fafafa"         # bg-zinc-50
        shadow_sm = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
        shadow_card = "0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.03)"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap');
    
    :root {{
        --background: {background};
        --foreground: {card_foreground};
        --card: {card};
        --card-foreground: {card_foreground};
        --muted: {muted};
        --muted-foreground: {muted_foreground};
        --border: {border};
        --primary: {primary};
        --primary-foreground: {primary_foreground};
        --secondary: {secondary};
        --secondary-foreground: {secondary_foreground};
        --radius: 0.5rem;
    }}
    
    /* Global Typography in Geist font (Official Vercel/shadcn font) */
    html, body, [class*="css"], [data-testid="stAppViewContainer"], .stApp {{
        font-family: 'Geist', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        background-color: {background} !important;
        color: {card_foreground} !important;
        letter-spacing: -0.011em;
    }}
    
    code, pre, .font-mono {{
        font-family: 'Geist Mono', monospace !important;
    }}
    
    /* shadcn/ui Header bar */
    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}
    
    /* shadcn/ui Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        border-right: 1px solid {border} !important;
        padding-top: 1.5rem !important;
    }}
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] span {{
        color: {card_foreground} !important;
        font-size: 0.875rem;
    }}
    
    /* shadcn/ui Card Component */
    .shadcn-card {{
        background-color: {card} !important;
        color: {card_foreground} !important;
        border: 1px solid {border} !important;
        border-radius: 0.75rem !important;
        box-shadow: {shadow_card} !important;
        padding: 1.5rem !important;
        margin-bottom: 1.25rem !important;
        box-sizing: border-box;
        transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }}
    
    .shadcn-card:hover {{
        border-color: {muted_foreground}40 !important;
    }}
    
    .shadcn-card-header {{
        display: flex;
        flex-direction: column;
        space-y: 0.375rem;
        margin-bottom: 0.75rem;
    }}
    
    .shadcn-card-title {{
        font-size: 1.125rem !important;
        font-weight: 600 !important;
        line-height: 1.25 !important;
        color: {card_foreground} !important;
        letter-spacing: -0.02em !important;
        margin: 0 !important;
    }}
    
    .shadcn-card-description {{
        font-size: 0.875rem !important;
        color: {muted_foreground} !important;
        margin: 0.25rem 0 0 0 !important;
        line-height: 1.5 !important;
    }}
    
    .shadcn-card-content {{
        color: {card_foreground} !important;
        font-size: 0.875rem;
        line-height: 1.6;
    }}
    
    /* shadcn/ui Hero Banner */
    .shadcn-hero {{
        background-color: {card} !important;
        border: 1px solid {border} !important;
        border-radius: 0.75rem !important;
        padding: 2.25rem 2rem !important;
        margin-bottom: 1.5rem !important;
        position: relative;
        overflow: hidden;
    }}
    
    .shadcn-hero h1 {{
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: {card_foreground} !important;
        letter-spacing: -0.03em !important;
        margin: 0.5rem 0 0.75rem 0 !important;
        line-height: 1.2 !important;
    }}
    
    .shadcn-hero p {{
        font-size: 1rem !important;
        color: {muted_foreground} !important;
        max-width: 720px !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }}
    
    /* shadcn/ui Badge Component */
    .shadcn-badge {{
        display: inline-flex;
        align-items: center;
        border-radius: 9999px;
        border: 1px solid {border};
        padding: 0.125rem 0.625rem;
        font-size: 0.75rem;
        font-weight: 600;
        line-height: 1rem;
        transition: background-color 0.15s ease-in-out;
        letter-spacing: 0.01em;
    }}
    
    .shadcn-badge-default {{
        background-color: {primary} !important;
        color: {primary_foreground} !important;
        border-color: transparent !important;
    }}
    
    .shadcn-badge-secondary {{
        background-color: {secondary} !important;
        color: {secondary_foreground} !important;
        border-color: transparent !important;
    }}
    
    .shadcn-badge-outline {{
        background-color: transparent !important;
        color: {card_foreground} !important;
        border: 1px solid {border} !important;
    }}
    
    .shadcn-badge-success {{
        background-color: rgba(16, 185, 129, 0.1) !important;
        color: #10b981 !important;
        border: 1px solid rgba(16, 185, 129, 0.25) !important;
    }}
    
    /* shadcn/ui Metric Stat Card */
    .shadcn-stat {{
        background-color: {card} !important;
        border: 1px solid {border} !important;
        border-radius: 0.75rem !important;
        padding: 1.25rem 1.5rem !important;
    }}
    
    .shadcn-stat .stat-label {{
        font-size: 0.8125rem !important;
        font-weight: 500 !important;
        color: {muted_foreground} !important;
        letter-spacing: -0.01em !important;
        margin-bottom: 0.25rem !important;
    }}
    
    .shadcn-stat .stat-value {{
        font-size: 1.75rem !important;
        font-weight: 700 !important;
        color: {card_foreground} !important;
        letter-spacing: -0.03em !important;
        line-height: 1.2 !important;
    }}
    
    /* shadcn/ui Button styling */
    .stButton>button {{
        border-radius: 0.5rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 1px solid {border} !important;
        background-color: {secondary} !important;
        color: {secondary_foreground} !important;
        box-shadow: {shadow_sm} !important;
    }}
    
    .stButton>button:hover {{
        background-color: {muted_foreground}20 !important;
        border-color: {muted_foreground}50 !important;
    }}
    
    .stButton>button[kind="primary"], .stButton>button[data-testid="stBaseButton-primary"] {{
        background-color: {primary} !important;
        color: {primary_foreground} !important;
        border: 1px solid {primary} !important;
    }}
    
    .stButton>button[kind="primary"]:hover, .stButton>button[data-testid="stBaseButton-primary"]:hover {{
        opacity: 0.9 !important;
    }}
    
    /* shadcn/ui Tabs styling */
    [data-baseweb="tab-list"] {{
        background-color: {muted} !important;
        border-radius: 0.5rem !important;
        padding: 0.25rem !important;
        gap: 0.25rem !important;
        border: 1px solid {border} !important;
    }}
    
    [data-baseweb="tab"] {{
        border-radius: 0.375rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        color: {muted_foreground} !important;
        padding: 0.375rem 0.875rem !important;
        border: none !important;
        background: transparent !important;
    }}
    
    [aria-selected="true"][data-baseweb="tab"] {{
        background-color: {card} !important;
        color: {card_foreground} !important;
        box-shadow: {shadow_sm} !important;
    }}
    
    /* Form Inputs */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{
        border-radius: 0.5rem !important;
        border: 1px solid {input_border} !important;
        background-color: {card} !important;
        color: {card_foreground} !important;
        font-size: 0.875rem !important;
    }}
    
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {{
        border-color: {ring} !important;
        box-shadow: 0 0 0 1px {ring} !important;
    }}
    
    /* Clean Divider */
    hr {{
        border-color: {border} !important;
        opacity: 0.8;
    }}
    
    /* Dataframes */
    [data-testid="stDataFrame"] {{
        border: 1px solid {border} !important;
        border-radius: 0.5rem !important;
        overflow: hidden;
    }}
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {card_foreground} !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
    }}
    </style>
    """

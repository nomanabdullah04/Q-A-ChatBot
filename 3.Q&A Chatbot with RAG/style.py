import streamlit as st

def apply_custom_theme():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #f8fafc !important; }
        .stApp { background-color: #0b0f19; }
        header[data-testid="stHeader"] { background: rgba(11, 15, 25, 0.8); }
        section[data-testid="stSidebar"] { background-color: #111827; border-right: 1px solid #1f2937; }
        [data-testid="stBottom"], [data-testid="stBottom"] > div { background-color: #0b0f19 !important; padding-bottom: 40px !important; }
        [data-testid="stChatInput"] { background-color: #111827 !important; border: 1px solid #374151 !important; border-radius: 12px !important; }
        [data-testid="stChatMessage"] { background-color: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 14px 18px; }
        .hero-title { font-size: 2rem; font-weight: 700; background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-subtitle { color: #9ca3af; font-size: 0.9rem; margin-bottom: 1.2rem; }
        .nexus-footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #080b12; border-top: 1px solid #1f2937; color: #9ca3af; text-align: center; padding: 8px 0; font-size: 12px; z-index: 99999; }
        .nexus-footer a { color: #38bdf8; text-decoration: none; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown('<div class="nexus-footer">POWERED BY <a href="https://nabdullah.vercel.app/" target="_blank">Nexus Lab</a></div>', unsafe_allow_html=True)

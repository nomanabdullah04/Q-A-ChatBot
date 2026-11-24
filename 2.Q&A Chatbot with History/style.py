import streamlit as st

def apply_custom_theme():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #f8fafc !important;
        }

        /* Clean dark slate background */
        .stApp {
            background-color: #0b0f19;
        }

        /* Hide default top bar decoration */
        header[data-testid="stHeader"] {
            background: rgba(11, 15, 25, 0.8);
            backdrop-filter: blur(8px);
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #111827;
            border-right: 1px solid #1f2937;
        }
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {
            color: #e5e7eb !important;
            font-weight: 500;
        }

        /* Fix bottom chat input bar container so there is NO white box */
        [data-testid="stBottom"] {
            background-color: #0b0f19 !important;
            border-top: 1px solid #1f2937;
            padding-bottom: 42px !important; /* Space for fixed footer */
        }
        [data-testid="stBottom"] > div {
            background-color: #0b0f19 !important;
        }
        [data-testid="stChatInput"] {
            background-color: #111827 !important;
            border: 1px solid #374151 !important;
            border-radius: 12px !important;
        }
        [data-testid="stChatInput"] textarea {
            color: #f8fafc !important;
        }

        /* Chat message bubbles */
        [data-testid="stChatMessage"] {
            background-color: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 16px 20px;
            margin-bottom: 12px;
        }
        [data-testid="stChatMessage"] p,
        [data-testid="stChatMessage"] li,
        [data-testid="stChatMessage"] span {
            color: #f1f5f9 !important;
            font-size: 15px;
            line-height: 1.6;
        }

        /* Clean gradient header */
        .hero-title {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        .hero-subtitle {
            color: #9ca3af;
            font-size: 0.92rem;
            margin-bottom: 1.5rem;
        }

        /* Sleek fixed footer */
        .nexus-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #080b12;
            border-top: 1px solid #1f2937;
            color: #9ca3af;
            text-align: center;
            padding: 8px 0;
            font-size: 12px;
            letter-spacing: 0.5px;
            z-index: 99999;
        }
        .nexus-footer a {
            color: #38bdf8;
            text-decoration: none;
            font-weight: 600;
        }
        .nexus-footer a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

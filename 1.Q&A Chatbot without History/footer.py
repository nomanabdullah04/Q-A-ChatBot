import streamlit as st

def render_footer():
    footer_html = """
    <style>
        .nexus-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            color: #cbd5e1;
            text-align: center;
            padding: 12px 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 13px;
            letter-spacing: 0.6px;
            z-index: 9999;
        }
        .nexus-footer a {
            color: #38bdf8;
            font-weight: 700;
            text-decoration: none;
            transition: color 0.2s ease, text-shadow 0.2s ease;
        }
        .nexus-footer a:hover {
            color: #7dd3fc;
            text-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
        }
        /* Adds spacing at the bottom so content isn't hidden behind the fixed footer */
        .block-container {
            padding-bottom: 70px;
        }
    </style>

    <div class="nexus-footer">
        POWERED BY <a href="https://nabdullah.vercel.app/" target="_blank">Nexus Lab</a>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

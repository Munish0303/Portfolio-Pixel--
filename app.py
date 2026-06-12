"""
MUNISH-OS — Pixel Portfolio (Streamlit deployable)
Run locally:  streamlit run app.py
Deploy:       push this folder to GitHub -> share.streamlit.io -> point to app.py
"""
import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

st.set_page_config(page_title="Munish Patwa — Pixel Portfolio",
                   page_icon="🕹️", layout="wide",
                   initial_sidebar_state="collapsed")

# strip default Streamlit chrome / padding so the OS fills the viewport
st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden;}
.stApp{background:#f6b8c6;}
.block-container{padding:0!important;max-width:100%!important;}
[data-testid="stAppViewBlockContainer"]{padding:0!important;}
[data-testid="stMain"]{overflow:hidden!important;}
iframe{border:none!important;height:100vh!important;min-height:100vh!important;width:100%!important;}
</style>
""", unsafe_allow_html=True)


def b64(path: Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def build_html() -> str:
    html = (ROOT / "portfolio.html").read_text(encoding="utf-8")
    avatar = b64(ASSETS / "avatar.png", "image/png")
    resume = ROOT / "Munish_Patwa_Resume.pdf"
    resume_uri = b64(resume, "application/pdf") if resume.exists() else "#"
    return (html
            .replace("{{AVATAR}}", avatar)
            .replace("{{RESUME}}", resume_uri))


components.html(build_html(), height=900, scrolling=False)

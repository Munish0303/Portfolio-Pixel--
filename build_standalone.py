"""Build a single self-contained index.html (assets + resume inlined as base64).
Open it directly in any browser, host on GitHub Pages, or anywhere static."""
import base64
from pathlib import Path

ROOT = Path(__file__).parent


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


html = (ROOT / "portfolio.html").read_text(encoding="utf-8")
html = html.replace("{{AVATAR}}", b64(ROOT / "assets/avatar.png", "image/png"))
resume = ROOT / "Munish_Patwa_Resume.pdf"
html = html.replace("{{RESUME}}", b64(resume, "application/pdf") if resume.exists() else "#")

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print("wrote", out, len(html), "chars")

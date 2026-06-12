# MUNISH-OS — Pixel Portfolio 🕹️

An interactive, retro pixel-desktop portfolio for **Munish Patwa** (M.Sc. Data Science, TU Dortmund).
A fake operating system with draggable windows, a working terminal, a mini-game, and an idle avatar.

## Features
- 🖥️ Boot screen → pixel desktop with icons & taskbar (live clock + START menu)
- 🪟 **Draggable windows** (desktop) / full-screen panels (mobile): About, Projects, Experience, Skills, Education, Contact
- ⌨️ **Interactive Terminal** — try `help`, `projects`, `skills`, `neofetch`, `contact`, `clear`
- 🎮 **Mini Game** "Data Catch" — catch 📊💻☕🤖🐍, dodge the bugs 🐛 (keyboard, mouse or touch)
- 🧍 **Idle avatar** of you walking along the desktop (click it for quips)
- 📄 Resume download baked in (button in About & Contact)
- 📱 Fully **mobile-friendly** (responsive layout, touch controls)

## Files
| File | Purpose |
|------|---------|
| `app.py` | Streamlit entry point (inlines assets + resume, serves the page) |
| `portfolio.html` | The whole portfolio (HTML/CSS/JS). Uses `{{AVATAR}}`, `{{AVATAR_PIXEL}}`, `{{RESUME}}` placeholders |
| `build_standalone.py` | Builds `index.html` — a single self-contained file (no Streamlit needed) |
| `assets/` | `avatar.png` (headshot) + `avatar_pixel.png` (pixelated sprite) |
| `Munish_Patwa_Resume.pdf` | Resume used for the download button |

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud (free)
1. Push this folder to a GitHub repo.
2. Go to <https://share.streamlit.io> → **New app** → pick the repo, set **Main file** = `app.py`.
3. Deploy. Done — you get a public `*.streamlit.app` URL.

## No-Streamlit option (GitHub Pages / any static host)
```bash
python build_standalone.py   # creates index.html with everything inlined
```
Then host `index.html` anywhere static (GitHub Pages, Netlify, Vercel) — or just double-click it to open locally.

## Editing your info
All content lives in **`portfolio.html`**. Update the window sections (search for `win-about`, `win-projects`, etc.).
After editing, re-run `streamlit run app.py` (it rebuilds automatically) or `python build_standalone.py` for the static file.

> Tip: the LinkedIn link in `win-contact` points to `linkedin.com/in/munish-patwa` — change it if your handle differs.

# Yes/No Button Page

This repository contains a small static page (`index.html`) and a minimal Flask app (`website14.py` + `templates/index.html`). The static `index.html` is ready to be deployed to static hosts (Netlify, GitHub Pages, etc.).

How to run locally (static):
- Open `index.html` in a browser or serve with a static server.

How to run locally (Flask):
- Install dependencies: `pip install -r requirements.txt`
- Run: `python website14.py`
- Open: `http://127.0.0.1:5000`

Deploying to GitHub Pages:
1. Create a repo on GitHub and push this folder.
2. Set GitHub Pages to use `main` branch / `root` in repository settings.

Deploying to Netlify Drop:
- Upload the `index.html` file or a ZIP of the site.

Useful git commands:
```bash
git init
git add .
git commit -m "Initial commit: add static index + Flask app"
# create a repo on GitHub, then add remote and push:
# git remote add origin git@github.com:<your-username>/<repo>.git
# git push -u origin main
```

If you want, I can create the repo locally and make the initial commit for you.
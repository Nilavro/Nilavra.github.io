# Nilavra Pathak Academic Website

This is a Jekyll-based GitHub Pages starter site for Nilavra Pathak.

## Upload instructions

1. Unzip this folder.
2. Create or open your GitHub repository.
3. Upload all files and folders to the root of the repository.
4. Go to `Settings → Pages`.
5. Choose:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`
6. Save.

## Important files to edit first

- `_config.yml`: replace `your-github-username` and `your.email@example.com`.
- `assets/`: add your real `profile.jpg` and `cv.pdf`.
- `publications.md`: add correct publication titles, links, and venues.

## Add a new research page

Create a file like `_research/new-project-name.md`.

## Add a new update

Create a file like `_posts/2026-05-01-update-title.md`.

## Optional automated research news

The site includes `.github/workflows/update-research-news.yml`, `scripts/update_research_news.py`, and `data/research_news.json`.
The workflow can refresh the external research-news feed daily using public RSS feeds.

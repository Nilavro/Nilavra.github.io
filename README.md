# Academic GitHub Pages Starter

A minimal static website for GitHub Pages.

## Files

```text
.
├── index.html
├── style.css
├── README.md
├── CNAME.example
└── assets/
    ├── .gitkeep
    ├── profile.jpg   # add your photo here
    └── cv.pdf        # add your CV here
```

## How to publish

1. Create a repository named either:
   - `yourusername.github.io` for a personal homepage, or
   - any repo name, such as `academic-site`, for a project-style page.

2. Upload these files to the repository root.

3. Go to:
   `Settings` → `Pages`

4. Under **Build and deployment**, choose:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`

5. Save. GitHub will publish the site after the Pages build finishes.

## What to edit first

- `index.html`
  - Replace `Your Name`
  - Replace email and profile links
  - Replace project/publication text
  - Update Google Scholar and GitHub URLs

- `assets/profile.jpg`
  - Add your profile photo with this exact filename

- `assets/cv.pdf`
  - Add your CV with this exact filename

- `style.css`
  - Change colors, spacing, or typography if needed

## Optional custom domain

If you buy a domain, rename `CNAME.example` to `CNAME` and put only the domain name inside it, for example:

```text
www.yourdomain.com
```

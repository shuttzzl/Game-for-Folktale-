# Who Stole the Stairs?

A goblin stole the dungeon stairs. Type commands to track him down in a keyboard-only Python adventure.

## Run locally

Open `public/index.html` in a browser and press Enter. If you edit the game in `public/game.py`, run `python3 public/game.py` from the repository root to rebuild the page and play.

## Deploy on Vercel

1. Extract the ZIP and upload `public/`, `README.md`, and `vercel.json` to the root of your GitHub repository.
2. In Vercel, choose **Add New → Project** and import that repository.
3. Leave **Root Directory** at `./` and choose **Deploy**.

Vercel reads `vercel.json` and rebuilds the page from the Python source on each deployment. All six audio clips, the ending image, and the Brython runtime are included.

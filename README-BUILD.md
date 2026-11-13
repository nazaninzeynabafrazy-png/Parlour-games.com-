# The Parlour — how to build

Everything needed is in this folder. No other files are required.

- `ads.html`        the ONE source of the whole game hub (edit this)
- `new.html`        page shell used for the web version
- `head_lines.txt`  the first lines (doctype / head) shared by the builds
- `webpkg/`         the website folder (icons, fonts, privacy, credits, sw.js, manifest)
- `build.py`        run:  `mkdir -p out && python3 build.py`

Result:
- `out/parlour-online.html`       online build, ads off
- `out/parlour-online-gems.html`  online build, ads + gems on
- `out/parlour-offline*.html`     single-file offline builds
- `webpkg/index.html`             the file Cloudflare serves (upload `webpkg/` to GitHub)

Before each release change the cache name in `webpkg/sw.js` (e.g. parlour-v75 -> parlour-v76).

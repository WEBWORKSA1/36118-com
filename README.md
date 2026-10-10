# 36118.com

Free number intelligence: decode any number, look up ZIP and postal codes, read lucky-number meanings and score numeric domains. Static HTML/CSS/JS, hosted free on GitHub Pages.

- `RESEARCH.md`: what 36118 means and why this concept
- `PROMPTS.md`: phase-wise prompts used to build and extend the site
- `_build/`: the generator. Edit `_build/guides.py` or `_build/build.py`, then run `python3 _build/build.py` from the repo root and commit the regenerated HTML.

## One-time setup checklist

1. **GitHub Pages**: Settings → Pages → Build and deployment → *Deploy from a branch* → `main` / `(root)`. Site goes live at `https://webworksa1.github.io/36118-com/`.
2. **Custom domain**: in Settings → Pages enter `36118.com` (this creates a `CNAME` file). At the registrar set apex A records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and `www` CNAME to `webworksa1.github.io`. Tick *Enforce HTTPS* once the certificate is issued.
3. **Forms**: submit any form once (e.g. the newsletter box). FormSubmit sends a one-time activation email to the site inbox; click *Activate*. All forms then deliver.
4. **AdSense**: add the site `36118.com` in AdSense, keep `ads.txt` at the root, turn on Auto ads, and enable the Google consent message for EEA/UK under Privacy & messaging. After approval, paste display-unit slot IDs into `CONFIG.adSlots` in `assets/js/site.js` to fill the reserved positions.
5. **Payments (optional)**: put PayPal.me / Stripe Payment Link / Buy Me a Coffee URLs in `CONFIG.payLinks` in `assets/js/site.js`; the Support page shows the buttons automatically.
6. **Search Console**: verify the domain and submit `https://36118.com/sitemap.xml`.

© 36118.com, a Webworks property. "36118" is used descriptively as a number and ZIP code; no trademark is claimed in it. See `disclaimer.html`.

# Digivexora Solution website

Static HTML/CSS/JS website with a small PHP + MySQL enquiry form.

## Pages (14, all in sitemap.xml)
index, about, services, contact, privacy-policy, plus one landing page per service:
search-engine-optimization, local-seo-google-business-profile, social-media-management,
meta-ads, google-ads-ppc, website-design-development, graphic-poster-design,
reels-video-editing, youtube-channel-management.
`404.html` is a custom error page (noindex, not in the sitemap).

## BEFORE YOU UPLOAD - set your real domain and email
The sitemap, canonical tags, Open Graph tags and robots.txt currently use the placeholder
domain `https://www.digivexora.in` and email `hello@digivexora.in`.
1. Open `tools/build.py` and edit `DOMAIN` and `EMAIL` at the top.
2. Run `python3 tools/build.py`. All 14 pages, sitemap.xml and robots.txt are regenerated together.
3. Do not upload the `tools/` folder.

## Run locally (XAMPP/WAMP)
1. Copy this folder to `htdocs`.
2. Start Apache and MySQL, import `database.sql` in phpMyAdmin.
3. Copy `config.example.php` to `config.php` and enter your MySQL details.
4. Open the folder in your browser and send a test enquiry. A row should appear in `enquiries`.
Requires PHP 8.1 or newer.

## After going live
- Install HTTPS, then enable the HTTPS redirect lines in `.htaccess`.
- Submit `https://YOUR-DOMAIN/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- Replace the placeholder email, add phone, address and social links where you want them.
- Have the privacy policy reviewed for your business and location.
- Add real client work, reviews and numbers only when they are true and you can prove them.
- Keep `config.php` private. `.htaccess` blocks it from download on Apache.

## Logo files (assets/)
`logo.png` (full size, transparent), `logo-600.png` (used in header/footer), `logo-mark.png` (DV symbol),
`favicon.ico`, `favicon-48.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `og-image.jpg` (1200x630 share image).

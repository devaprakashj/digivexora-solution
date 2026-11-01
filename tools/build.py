#!/usr/bin/env python3
"""
Digivexora Solution - static site generator.

Generates every HTML page, sitemap.xml and robots.txt from one list of pages,
so the sitemap can never drift out of sync with the real pages.

Usage:   python3 tools/build.py
Change DOMAIN / EMAIL below, run again, and every canonical URL, Open Graph tag,
JSON-LD block, sitemap entry and robots.txt line is updated together.

Do NOT upload the tools/ folder to your web server.
"""
import html
import json
import os
from datetime import date

# ------------------------------------------------------------------ settings
DOMAIN = "https://digivexora.in"          # <- no trailing slash. Change to your real domain.
EMAIL = "digivexorasolution@gmail.com"             # <- change to your real business email.
BRAND = "Digivexora Solution"
YEAR = date.today().year
LASTMOD = date.today().isoformat()
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

e = html.escape


# ------------------------------------------------------------------ services
SERVICES = [
    dict(
        slug="search-engine-optimization", name="Search Engine Optimization", form="Search Engine Optimization (SEO)",
        group="found", short="Technical, on-page and content SEO so the right people find you.",
        title="SEO Services | Digivexora Solution",
        meta="SEO services covering site audit, keyword research, on-page fixes, content and reporting, so more of the right people find your business on Google.",
        h1="SEO that puts your business in front of people already searching",
        lead="We fix what holds your site back, build pages around what customers actually search for, and report on the results in plain language.",
        fit=["Your website exists but rarely brings in enquiries", "Competitors appear above you for the searches that matter", "You are launching a new site and want it found from day one"],
        included=[
            ("Site audit", "Checks for speed, crawling, indexing, mobile usability and broken pages."),
            ("Keyword research", "The terms your customers really use, grouped by intent and matched to pages."),
            ("On-page optimization", "Titles, headings, meta descriptions, internal links and structured data."),
            ("Content plan", "Pages and articles that answer real questions and support your services."),
            ("Technical fixes", "Sitemap, robots.txt, canonical tags, redirects and page-speed problems."),
            ("Monthly reporting", "Rankings, traffic and enquiries explained without jargon."),
        ],
        steps=[("Audit", "We review your site, your competitors and how people search for you."),
               ("Prioritise", "We agree which fixes and keywords will matter most first."),
               ("Optimise", "We update pages, fix technical issues and publish new content."),
               ("Track", "We measure results monthly and adjust the plan.")],
        faqs=[("How long does SEO take to show results?", "SEO is gradual. Small technical fixes can help within weeks, but competitive searches usually take several months of steady work. After the audit we will tell you what is realistic for your market."),
              ("Do you guarantee first-page rankings?", "No. Search engines decide rankings, and anyone who guarantees a position is overpromising. We commit to the work, clear reporting and improvements you can measure."),
              ("Do I need a new website for SEO?", "Not always. We start with your current site and recommend a rebuild only if it is blocking progress."),
              ("What do you need from me to start?", "Access to your website, plus Google Search Console and Analytics if you have them, and a conversation about your services and customers.")],
        related=["local-seo-google-business-profile", "website-design-development", "google-ads-ppc"],
    ),
    dict(
        slug="local-seo-google-business-profile", name="Local SEO & Google Business Profile", form="Local SEO & Google Business Profile",
        group="found", short="Show up when nearby customers search, with a profile that works.",
        title="Local SEO & Google Business Profile | Digivexora",
        meta="Local SEO and Google Business Profile setup and optimization: accurate listings, review strategy and local pages that help nearby customers find you.",
        h1="Get found by customers searching near you",
        lead="When someone searches for your service nearby, your Google Business Profile is often the first thing they see. We set it up, tidy it and keep it working.",
        fit=["You serve customers in a specific town, city or region", "You want more calls, direction requests and walk-ins", "Your Google listing is missing, unverified or out of date"],
        included=[
            ("Profile setup and verification", "We create or claim your listing and guide you through Google's verification."),
            ("Profile optimization", "Categories, services, description, opening hours, photos and posts."),
            ("Listing consistency", "Your name, address and phone number kept consistent across key directories."),
            ("Review strategy", "Simple ways to ask happy customers for reviews, and replies to the ones you receive."),
            ("Local landing pages", "Pages for the areas and services you cover, so search engines understand where you work."),
            ("Local reporting", "Calls, direction requests and profile views from Google's own insights."),
        ],
        steps=[("Check", "We review your current listing, reviews and local competitors."),
               ("Fix", "We complete and correct your profile and directory details."),
               ("Build", "We grow reviews, photos and local pages over time."),
               ("Monitor", "We watch performance and keep the profile up to date.")],
        faqs=[("Do I need a physical shop?", "Google Business Profile suits businesses that meet customers in person or travel to them. Rules differ for service-area businesses, so we check your situation against Google's guidelines first."),
              ("Can you remove a bad review?", "Only reviews that break Google's policies can be reported, and Google makes the decision. We help you reply professionally and build up genuine reviews."),
              ("Will you buy or post fake reviews?", "No. Fake or incentivised reviews break Google's rules and can get a profile suspended."),
              ("How long until I see a difference?", "Profile improvements can show quickly. Stronger local visibility builds over weeks and months.")],
        related=["search-engine-optimization", "google-ads-ppc", "website-design-development"],
    ),
    dict(
        slug="social-media-management", name="Social Media Management", form="Social Media Management",
        group="visible", short="Content planning, design, publishing and community replies.",
        title="Social Media Management | Digivexora Solution",
        meta="Social media management: content calendar, post design, captions, scheduling and engagement for Instagram, Facebook and LinkedIn, handled for you.",
        h1="Social media that stays active, on brand and worth following",
        lead="We plan, design, schedule and publish your content, then reply and engage so your pages feel alive between sales.",
        fit=["You know you should post but do not have the time", "Your pages look different from one post to the next", "You want social to support enquiries, not just likes"],
        included=[
            ("Content calendar", "A monthly plan built around your offers, seasons and audience."),
            ("Post and carousel design", "Branded graphics and carousels that look consistent."),
            ("Captions and hashtags", "Clear copy written for each platform."),
            ("Scheduling and publishing", "Posts go live on the days and times we agree."),
            ("Community engagement", "Replies to comments and messages, as agreed with you."),
            ("Monthly review", "What worked, what did not, and what we will change next month."),
        ],
        steps=[("Learn", "We learn your brand, customers and goals."),
               ("Plan", "We map out the month's content and themes."),
               ("Create", "We design and write posts for your approval."),
               ("Publish", "We schedule, engage and review the results.")],
        faqs=[("Which platforms do you manage?", "We recommend platforms based on where your customers spend time. That is commonly Instagram and Facebook, with LinkedIn for business-to-business brands."),
              ("Do I get to approve posts?", "Yes. You see the calendar and designs before anything goes live, unless you ask us to publish directly."),
              ("How many posts will you publish?", "It depends on your package and goals. We agree a realistic schedule instead of posting for the sake of it."),
              ("Do you also run paid ads?", "Paid campaigns are a separate service, and the two work well together. See our Meta Ads service.")],
        related=["meta-ads", "graphic-poster-design", "reels-video-editing"],
    ),
    dict(
        slug="meta-ads", name="Meta Ads (Facebook & Instagram)", form="Meta Ads - Facebook & Instagram",
        group="visible", short="Planned Facebook and Instagram campaigns, tested and improved.",
        title="Meta Ads: Facebook & Instagram Ads | Digivexora",
        meta="Meta Ads management for Facebook and Instagram: campaign setup, audiences, ad creative, tracking and optimization focused on enquiries, not just reach.",
        h1="Facebook and Instagram ads built to bring in enquiries",
        lead="We set up your campaigns, test creatives and audiences, and adjust based on real results so your budget is not spent on guesswork.",
        fit=["You want leads, calls or messages, not just reach", "You have boosted posts before without clear results", "You have an offer and need the right people to see it"],
        included=[
            ("Goal and offer review", "We agree what a good result looks like before spending anything."),
            ("Audience setup", "Targeting based on location, interests and people who already know you."),
            ("Ad creative", "Images, carousels and short videos made for the feed and Stories."),
            ("Lead and tracking setup", "Meta Pixel, conversion events, lead forms or message destinations."),
            ("Testing and optimization", "We compare creatives and audiences and shift budget to what works."),
            ("Clear reports", "Spend, cost per result and what we are changing next."),
        ],
        steps=[("Define", "We agree the goal, offer and budget."),
               ("Build", "We create audiences, ads and tracking."),
               ("Launch", "We start with controlled tests."),
               ("Improve", "We review results and scale what works.")],
        faqs=[("How much ad budget do I need?", "It depends on your market and goal. We suggest a starting budget and scale only when results justify it. Ad spend is paid directly to Meta and is separate from our service fee."),
              ("Can you promise a number of leads?", "No. Results depend on your offer, market and budget. We promise careful setup, structured testing and honest reporting."),
              ("Do I need a website?", "A landing page or lead form helps. We can use Meta's built-in lead forms or build a dedicated landing page."),
              ("Who owns the ad account?", "You do. We work inside your account so you keep access to everything.")],
        related=["social-media-management", "google-ads-ppc", "graphic-poster-design"],
    ),
    dict(
        slug="google-ads-ppc", name="Google Ads (PPC)", form="Google Ads (PPC)",
        group="found", short="Reach people actively searching, with tracked conversions.",
        title="Google Ads (PPC) Management | Digivexora Solution",
        meta="Google Ads (PPC) management: keyword research, search campaigns, ad copy, conversion tracking and landing pages that turn searches into enquiries.",
        h1="Google Ads that reach people ready to enquire",
        lead="Appear when people search for what you sell. We build focused campaigns, send visitors to pages made to convert, and track every enquiry.",
        fit=["You need enquiries now while SEO builds up", "You are launching a new service or location", "You have run ads before and costs felt out of control"],
        included=[
            ("Campaign structure", "Accounts organised by service so budget goes where it should."),
            ("Keyword research", "Search terms to target, plus negative keywords to block wasted clicks."),
            ("Ad copy and extensions", "Clear, relevant ads with sitelinks, calls and other extensions."),
            ("Landing page review", "Feedback on your page, or a new one through our web design service."),
            ("Conversion tracking", "Calls, form submissions and message clicks measured properly."),
            ("Budget and bid management", "Regular adjustments and search-term reviews, with reports."),
        ],
        steps=[("Research", "We study how your customers search and what competitors do."),
               ("Set up", "We build campaigns, ads and tracking."),
               ("Launch", "We go live with a controlled budget."),
               ("Optimise", "We review search terms and costs, then refine.")],
        faqs=[("What is the difference between Google Ads and SEO?", "Ads start working once approved and stop when the budget stops. SEO takes longer but builds lasting visibility. Many businesses use both."),
              ("Who pays Google?", "You pay Google directly for ad spend. Our fee is separate."),
              ("Will I pay for clicks from uninterested people?", "Some, which is why we add negative keywords and review search terms regularly."),
              ("How soon will I see results?", "Traffic can start within days of launch, but the first weeks are for learning and tuning.")],
        related=["search-engine-optimization", "website-design-development", "meta-ads"],
    ),
    dict(
        slug="website-design-development", name="Website Design & Development", form="Website Design & Development",
        group="build", short="Responsive, search-friendly websites that make the next step clear.",
        title="Website Design & Development | Digivexora Solution",
        meta="Website design and development: responsive, fast, search-friendly business websites with clear enquiry forms, built around your brand and customers.",
        h1="Websites that look sharp and make the next step obvious",
        lead="Responsive, fast, search-friendly websites designed around your customers, and built so visitors know exactly how to contact you.",
        fit=["You do not have a website yet", "Your current site is slow, dated or hard to use on a phone", "Your site gets visitors but few enquiries"],
        included=[
            ("Design in your brand", "Layouts based on your logo, colours and content."),
            ("Responsive build", "Works properly on phones, tablets and desktops."),
            ("Speed and performance", "Lightweight pages that load quickly."),
            ("SEO foundations", "Clean structure, meta tags, sitemap.xml, robots.txt and structured data."),
            ("Enquiry tools", "Contact forms plus call and WhatsApp buttons where useful."),
            ("Handover", "Training on updating your site, and help with hosting and domain."),
        ],
        steps=[("Brief", "We agree your goals, pages and structure."),
               ("Design", "You review the look before we build."),
               ("Build", "We develop, test and refine the site."),
               ("Launch", "We publish, check everything and support you after.")],
        faqs=[("How long does a website take?", "A focused business website often takes a few weeks. It depends on the number of pages and how quickly content and feedback arrive."),
              ("Do you write the content?", "We can help structure and edit your content, and write copy as an add-on if you need it."),
              ("Will I own the website?", "Yes. You own your domain and your content."),
              ("Can you improve my existing site instead of rebuilding?", "Yes. We review what works first, then improve or rebuild only what is needed.")],
        related=["search-engine-optimization", "graphic-poster-design", "google-ads-ppc"],
    ),
    dict(
        slug="graphic-poster-design", name="Graphic & Poster Design", form="Graphic Design & Poster Design",
        group="build", short="Brand graphics, campaign creatives and promotional posters.",
        title="Graphic & Poster Design | Digivexora Solution",
        meta="Graphic and poster design: social media creatives, posters, flyers, brochures and brand graphics, delivered as print-ready and web-ready files.",
        h1="Graphics and posters that carry your message at a glance",
        lead="Posters, social creatives, brochures and brand graphics designed to look consistent and get read.",
        fit=["You have an offer, event or launch to promote", "Your posts look different every time", "You need print-ready files for a printer"],
        included=[
            ("Social media creatives", "Posts, stories and covers sized for each platform."),
            ("Posters and flyers", "Designs for print and for sharing online."),
            ("Brand kit", "Logo usage, colours, fonts and reusable templates."),
            ("Brochures and catalogues", "Multi-page layouts that present products and services clearly."),
            ("Ad creatives", "Graphics prepared for Meta and Google campaigns."),
            ("Final files", "Print-ready PDFs and web-ready PNG or JPG exports."),
        ],
        steps=[("Brief", "You share your message, audience and brand assets."),
               ("Draft", "We design first concepts."),
               ("Revise", "We refine with your feedback."),
               ("Deliver", "You receive final files in the formats you need.")],
        faqs=[("What file formats do I receive?", "Print-ready PDFs, and PNG or JPG for web and social. Editable source files can be shared when we agree it in advance."),
              ("How many revisions are included?", "We agree the number of revision rounds up front so timelines stay clear."),
              ("Can you work from my existing logo?", "Yes. Send your logo and brand colours. If you do not have them yet, ask us about a brand kit."),
              ("Do you handle the printing?", "We design the artwork and can advise on print specifications, then send files to your printer.")],
        related=["social-media-management", "reels-video-editing", "website-design-development"],
    ),
    dict(
        slug="reels-video-editing", name="Reels & Video Editing", form="Reels & Video Editing",
        group="build", short="Short-form reels, promo edits and branded video stories.",
        title="Reels & Video Editing | Digivexora Solution",
        meta="Reels and video editing: short-form reels, promo videos and ad cuts with captions, branding and the right format for each platform.",
        h1="Short videos edited to hold attention",
        lead="Send us your footage and we will cut it into reels, ads and promo videos with pacing, captions and branding that suit each platform.",
        fit=["You film clips but do not have time to edit them", "You want regular reels for Instagram and Facebook", "You need a promo video to use in ads"],
        included=[
            ("Reel editing", "Cuts, pacing, transitions and music that fit the platform."),
            ("Captions and subtitles", "On-screen text so videos work with the sound off."),
            ("Branded intros and outros", "Consistent opening and closing frames."),
            ("Ad versions", "Alternate cuts for different placements and audiences."),
            ("Cover images", "Thumbnails and covers that match your grid."),
            ("Format exports", "Vertical, square and landscape versions as needed."),
        ],
        steps=[("Share", "You send footage and tell us the goal."),
               ("Cut", "We edit a first version."),
               ("Refine", "We adjust based on your feedback."),
               ("Export", "You receive final files in the right formats.")],
        faqs=[("Do you shoot the videos?", "Our service is editing and post-production. If you need filming too, tell us what you have in mind and we will say what we can arrange."),
              ("How long does editing take?", "It depends on the length and number of videos. We confirm a turnaround before starting."),
              ("Can you add captions in my language?", "Tell us the language and share the script if you have one, and we will confirm what we can do."),
              ("What about music?", "We use music that is licensed for social platforms where possible. Trending audio usually has to be added inside the app when you publish.")],
        related=["social-media-management", "youtube-channel-management", "graphic-poster-design"],
    ),
    dict(
        slug="youtube-channel-management", name="YouTube Channel Management", form="YouTube Channel Management",
        group="visible", short="Planning, thumbnails, publishing and a consistent channel identity.",
        title="YouTube Channel Management | Digivexora Solution",
        meta="YouTube channel management: channel branding, content planning, thumbnails, titles, descriptions and upload scheduling for steady, professional growth.",
        h1="A YouTube channel that publishes consistently and looks professional",
        lead="We handle the planning, thumbnails, titles and uploads so your channel grows steadily without becoming a second job.",
        fit=["You have a channel but upload irregularly", "Your thumbnails and titles are not getting clicks", "You are starting a channel for your business or brand"],
        included=[
            ("Channel setup and branding", "Banner, profile image, about section and playlists."),
            ("Content planning", "Video ideas based on what your audience searches for and watches."),
            ("Thumbnail design", "Clear, consistent thumbnails that match your brand."),
            ("Titles, descriptions and tags", "Written to help people and search find each video."),
            ("Upload and scheduling", "Videos published on a rhythm you can sustain."),
            ("Performance review", "Watch time, click-through rate and retention, explained simply."),
        ],
        steps=[("Audit", "We review your channel, audience and goals."),
               ("Plan", "We build a content and publishing schedule."),
               ("Publish", "We prepare thumbnails, metadata and uploads."),
               ("Review", "We study analytics and refine the plan.")],
        faqs=[("Do you make the videos too?", "We manage the channel. Editing is available through our Reels & Video Editing service."),
              ("Can you guarantee subscribers or monetisation?", "No. Growth and monetisation depend on your content, your audience and YouTube's policies. We focus on what we can control."),
              ("Who owns the channel?", "You do. We are added as managers, and you can remove access at any time."),
              ("How often should we upload?", "We agree a schedule you can keep up. Consistency matters more than volume.")],
        related=["reels-video-editing", "social-media-management", "graphic-poster-design"],
    ),
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

GROUPS = [
    ("found", "Get found", "For people who are searching right now.", ["search-engine-optimization", "local-seo-google-business-profile", "google-ads-ppc"]),
    ("visible", "Stay visible", "For staying in front of your audience.", ["social-media-management", "meta-ads", "youtube-channel-management"]),
    ("build", "Build and create", "For the website, graphics and video.", ["website-design-development", "graphic-poster-design", "reels-video-editing"]),
]

PAGES = []  # (filename, in_sitemap)


# ------------------------------------------------------------------ helpers
def url(fn):
    return f"{DOMAIN}/" if fn == "index.html" else f"{DOMAIN}/{fn}"


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


ORG = {
    "@type": "Organization", "@id": f"{DOMAIN}/#org", "name": BRAND, "url": f"{DOMAIN}/",
    "logo": f"{DOMAIN}/assets/logo.png", "email": EMAIL,
}


def breadcrumb_ld(items):
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]})


def head(title, desc, fn, ld="", noindex=False, pre=""):
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    canon = "" if noindex else f'<link rel="canonical" href="{url(fn)}">'
    og = "" if noindex else f'''
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(BRAND)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(fn)}">
<meta property="og:image" content="{DOMAIN}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{DOMAIN}/assets/og-image.jpg">'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
{canon}
<meta name="theme-color" content="#081b66">
<link rel="icon" href="{pre}assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="{pre}assets/favicon-48.png">
<link rel="apple-touch-icon" href="{pre}assets/apple-touch-icon.png">{og}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Unbounded:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}style.css">
{ld}
</head>
'''


def header(current="", pre=""):
    def a(fn, label):
        cur = ' aria-current="page"' if current == fn else ""
        return f'<a href="{pre}{fn}"{cur}>{label}</a>'
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap header__inner">
<a class="brand" href="{pre}index.html" aria-label="{e(BRAND)} home"><img src="{pre}assets/logo-600.png" width="600" height="122" alt="{e(BRAND)} logo"></a>
<button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav class="nav" id="nav" aria-label="Main">
{a("index.html", "Home")}
{a("about.html", "About")}
{a("services.html", "Services")}
{a("contact.html", "Contact")}
<a class="btn btn--primary" href="{pre}contact.html">Get a free consultation</a>
</nav>
</div>
</header>
'''


def footer(pre=""):
    svc = "\n".join(f'<li><a href="{pre}{s["slug"]}.html">{e(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer">
<div class="wrap footer__grid">
<div class="footer__brand">
<a href="{pre}index.html" aria-label="{e(BRAND)} home"><img src="{pre}assets/logo-600.png" width="600" height="122" alt="{e(BRAND)} logo" loading="lazy"></a>
<p>Websites, search, ads, social media and creative work for businesses that want to grow online.</p>
</div>
<div>
<h4>Company</h4>
<ul>
<li><a href="{pre}index.html">Home</a></li>
<li><a href="{pre}about.html">About us</a></li>
<li><a href="{pre}services.html">All services</a></li>
<li><a href="{pre}contact.html">Contact</a></li>
<li><a href="{pre}privacy-policy.html">Privacy policy</a></li>
</ul>
</div>
<div>
<h4>Services</h4>
<ul>
{svc}
</ul>
</div>
<div>
<h4>Get in touch</h4>
<ul>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><a href="{pre}contact.html">Request a consultation</a></li>
</ul>
</div>
</div>
<div class="wrap footer__bottom"><span>&copy; {YEAR} {e(BRAND)}. All rights reserved.</span><a href="{pre}privacy-policy.html">Privacy policy</a></div>
</footer>
<script src="{pre}script.js" defer></script>
</body>
</html>
'''


def crumbs(trail):
    lis = []
    for i, (label, href) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li aria-current="page">{e(label)}</li>')
        else:
            lis.append(f'<li><a href="{href}">{e(label)}</a></li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(lis) + "</ol></nav>"


def options(selected=None):
    opts = ['<option value="">Choose a service</option>']
    for s in SERVICES:
        sel = " selected" if s["form"] == selected else ""
        opts.append(f'<option value="{e(s["form"])}"{sel}>{e(s["form"])}</option>')
    multi = "Multiple services / Not sure yet"
    sel = " selected" if selected == multi else ""
    opts.append(f'<option value="{e(multi)}"{sel}>{e(multi)}</option>')
    return "".join(opts)


def form(source, selected=None, heading="Request a free consultation"):
    return f'''<form class="form" action="submit_enquiry.php" method="POST" data-enquiry novalidate>
<h3>{e(heading)}</h3>
<p class="req">Fields marked * are required.</p>
<input type="hidden" name="source_page" value="{e(source)}">
<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website_url" tabindex="-1" autocomplete="off"></label></div>
<div class="row2">
<label>Full name *<input type="text" name="name" required minlength="2" maxlength="120" autocomplete="name" placeholder="Your name"></label>
<label>Phone number *<input type="tel" name="phone" required pattern="[0-9+\\(\\) .\\-]{{8,25}}" autocomplete="tel" placeholder="+91 98765 43210"></label>
</div>
<div class="row2">
<label>Business name<input type="text" name="business" maxlength="160" autocomplete="organization" placeholder="Your company"></label>
<label>Email address<input type="email" name="email" maxlength="190" autocomplete="email" placeholder="you@example.com"></label>
</div>
<label>Service you are interested in *<select name="service" required>{options(selected)}</select></label>
<label>Tell us about your project<textarea name="message" maxlength="5000" placeholder="Your goals, timeline or anything else we should know"></textarea></label>
<label class="consent"><input type="checkbox" name="consent" value="1" required><span>I agree to be contacted about this enquiry. *</span></label>
<button class="btn btn--primary" type="submit">Send enquiry</button>
<p class="status" role="status" aria-live="polite"></p>
<p class="fine">We only use your details to reply to your enquiry. <a href="privacy-policy.html">Privacy policy</a></p>
</form>'''


def cta_band(title="Ready to talk about your business?", text="Tell us what you are building and what you want to achieve. We will reply with clear next steps."):
    return f'''<section class="band band--navy cta">
<div class="wrap">
<div><h2>{e(title)}</h2><p>{e(text)}</p></div>
<a class="btn btn--light" href="contact.html">Get a free consultation</a>
</div>
</section>
'''


def write(fn, content, in_sitemap=True):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(content)
    if in_sitemap:
        PAGES.append(fn)


def svc_rows(slugs):
    return "\n".join(
        f'<a class="svc-row" href="{s}.html"><strong>{e(BY_SLUG[s]["name"])}</strong><span>{e(BY_SLUG[s]["short"])}</span></a>' for s in slugs)


# ------------------------------------------------------------------ hero art
HERO_ART = '''<svg viewBox="0 0 560 420" role="img" aria-label="Illustration: four channels (search, social, ads and websites) feeding one chip that powers a rising bar chart">
<g>
<path class="art-trace t1" pathLength="1" d="M120 60H170L215 105V180H232"/>
<path class="art-trace t2" pathLength="1" d="M120 150H165L190 175H232"/>
<path class="art-trace t3" pathLength="1" d="M120 250H165L190 225H232"/>
<path class="art-trace t4" pathLength="1" d="M120 340H170L215 295V250H232"/>
<circle class="art-node" cx="120" cy="60" r="7"/><circle class="art-node" cx="120" cy="150" r="7"/>
<circle class="art-node" cx="120" cy="250" r="7"/><circle class="art-node" cx="120" cy="340" r="7"/>
<text class="art-label" x="0" y="66">Search</text><text class="art-label" x="0" y="156">Social</text>
<text class="art-label" x="0" y="256">Ads</text><text class="art-label" x="0" y="346">Websites</text>
</g>
<g>
<rect class="art-chip" x="232" y="150" width="100" height="100" rx="10"/>
<rect class="art-chip-core" x="258" y="176" width="48" height="48" rx="5"/>
<path class="art-pin" d="M254 150v-14M282 150v-14M310 150v-14M254 250v14M282 250v14M310 250v14"/>
</g>
<path class="art-trace out" pathLength="1" d="M332 200H372V318"/>
<rect class="art-bar b1" x="390" y="268" width="44" height="86" rx="3"/>
<rect class="art-bar b2" x="446" y="226" width="44" height="128" rx="3"/>
<rect class="art-bar b3" x="502" y="168" width="44" height="186" rx="3"/>
<path class="art-arrow" pathLength="1" d="M384 236C420 214 458 176 508 118"/>
<path class="art-arrowhead" d="M524 100l-44 6 30 32z"/>
</svg>'''


# ------------------------------------------------------------------ pages
def build_home():
    title = "Digivexora Solution | SEO, Ads, Websites & Social Media"
    desc = "Digivexora Solution helps businesses grow online with SEO, local SEO, Google and Meta ads, website development, social media, design and video."
    ld = jsonld({"@context": "https://schema.org", "@graph": [
        {**ORG, "description": desc},
        {"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": f"{DOMAIN}/", "name": BRAND, "publisher": {"@id": f"{DOMAIN}/#org"}},
    ]})
    groups = ""
    for _, gtitle, note, slugs in GROUPS:
        groups += f'<div class="group"><h3>{e(gtitle)}</h3><p class="group__note">{e(note)}</p><div class="bus">{svc_rows(slugs)}</div></div>\n'
    steps = "".join(f'<li class="step"><h3>{e(t)}</h3><p>{e(p)}</p></li>' for t, p in [
        ("Discover", "We learn about your business, audience, challenges and goals."),
        ("Plan", "We shape a practical strategy, clear priorities and a creative direction."),
        ("Create and launch", "We build, publish and launch the work with care."),
        ("Review and improve", "We look at performance and refine the approach as we learn."),
    ])
    body = f'''<main id="main">
<section class="hero">
<div class="wrap hero__grid">
<div class="hero__copy">
<h1>Websites, search and ads that bring in enquiries</h1>
<p class="lead">Digivexora Solution is a digital marketing partner for businesses that want to be found, trusted and chosen online. Strategy, design and campaigns, handled together.</p>
<div class="actions">
<a class="btn btn--primary" href="contact.html">Get a free consultation</a>
<a class="btn btn--ghost" href="services.html">See our services</a>
</div>
</div>
<div class="hero__art">{HERO_ART}</div>
</div>
</section>

<section class="band" id="services">
<div class="wrap">
<div class="sec-head"><h2>Nine services, one connected plan</h2><p>Choose one service or combine several. Each has its own page with what is included and how we work.</p></div>
<div class="groups">
{groups}</div>
</div>
</section>

<section class="band band--paper">
<div class="wrap split">
<div>
<h2>Big ideas deserve a bigger digital stage</h2>
<p class="lead" style="margin-top:20px">We help brands connect with the right people through clear strategy, engaging creative and campaigns tied to real business goals.</p>
<div class="actions"><a class="btn btn--ghost" href="about.html">More about us</a></div>
</div>
<ul class="principles">
<li><h3>One plan across channels</h3><p>Your website, search, ads and social content are planned together, so each one supports the others.</p></li>
<li><h3>Plain-language reporting</h3><p>You see what was done, what it cost and what happened, without jargon.</p></li>
<li><h3>Honest expectations</h3><p>We do not promise rankings, followers or lead numbers. We promise careful work and clear measurement.</p></li>
</ul>
</div>
</section>

<section class="band">
<div class="wrap">
<div class="sec-head"><h2>How we work</h2><p>A simple, collaborative process that keeps you informed at every stage.</p></div>
<ol class="steps">{steps}</ol>
</div>
</section>

{cta_band()}
</main>
'''
    write("index.html", head(title, desc, "index.html", ld) + header("index.html") + body + footer())


def build_about():
    fn = "about.html"
    title = "About Digivexora Solution | Digital Marketing Agency"
    desc = "Learn how Digivexora Solution works: strategy, creative and performance marketing joined up, with clear scope, honest reporting and you in control."
    ld = jsonld({"@context": "https://schema.org", "@type": "AboutPage", "name": title, "url": url(fn), "about": {"@id": f"{DOMAIN}/#org"}}) + \
        breadcrumb_ld([("Home", url("index.html")), ("About", url(fn))])
    body = f'''<main id="main">
<section class="page-hero">
<div class="wrap">
{crumbs([("Home", "index.html"), ("About", fn)])}
<h1>A digital partner built around your goals</h1>
<p class="lead">Digivexora Solution brings strategy, design and performance marketing together, so your business is easier to find and easier to choose.</p>
</div>
</section>
<section class="band">
<div class="wrap split">
<div class="prose">
<h2 style="margin-top:0">What we do</h2>
<p>We help businesses build a stronger digital presence: a website that works, search visibility that lasts, ads that reach the right people, and social content that keeps your brand active.</p>
<p>Whether you are starting from scratch or ready to scale, we help you bring each part of your digital marketing together in one plan.</p>
<div class="actions"><a class="btn btn--primary" href="services.html">Explore services</a></div>
</div>
<ul class="principles">
<li><h3>Strategy first</h3><p>We start with your business goals and customers, then choose the channels that fit.</p></li>
<li><h3>Creative that has a job</h3><p>Every design, video and post is made to help someone take the next step.</p></li>
<li><h3>Measured and improved</h3><p>We track the right numbers and use them to decide what to do next.</p></li>
<li><h3>You stay in control</h3><p>You approve the plan, see the reports and keep access to your own accounts.</p></li>
</ul>
</div>
</section>
{cta_band("Have a project in mind?", "Tell us about your business and we will suggest where to start.")}
</main>
'''
    write(fn, head(title, desc, fn, ld) + header(fn) + body + footer())


def build_services():
    fn = "services.html"
    title = "Digital Marketing Services | Digivexora Solution"
    desc = "Explore all Digivexora Solution services: SEO, local SEO, Google Ads, Meta Ads, social media, websites, graphic design, video editing and YouTube."
    items = [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": url(s["slug"] + ".html")} for i, s in enumerate(SERVICES)]
    ld = jsonld({"@context": "https://schema.org", "@type": "ItemList", "name": "Digivexora Solution services", "itemListElement": items}) + \
        breadcrumb_ld([("Home", url("index.html")), ("Services", url(fn))])
    groups = ""
    for _, gtitle, note, slugs in GROUPS:
        groups += f'<div class="group"><h3>{e(gtitle)}</h3><p class="group__note">{e(note)}</p><div class="bus">{svc_rows(slugs)}</div></div>\n'
    body = f'''<main id="main">
<section class="page-hero">
<div class="wrap">
{crumbs([("Home", "index.html"), ("Services", fn)])}
<h1>Everything your brand needs to move up</h1>
<p class="lead">One connected team for visibility, engagement and growth, from the first impression to the next customer.</p>
</div>
</section>
<section class="band">
<div class="wrap"><div class="groups">
{groups}</div></div>
</section>
{cta_band("Not sure which service you need?", "Tell us about your business and we will recommend where to start.")}
</main>
'''
    write(fn, head(title, desc, fn, ld) + header(fn) + body + footer())


def build_contact():
    fn = "contact.html"
    title = "Contact Digivexora Solution | Free Consultation"
    desc = "Contact Digivexora Solution to discuss SEO, ads, websites, social media or design. Tell us about your project and request a free consultation."
    ld = jsonld({"@context": "https://schema.org", "@type": "ContactPage", "name": title, "url": url(fn), "about": {"@id": f"{DOMAIN}/#org"}}) + \
        breadcrumb_ld([("Home", url("index.html")), ("Contact", url(fn))])
    body = f'''<main id="main">
<section class="page-hero">
<div class="wrap">
{crumbs([("Home", "index.html"), ("Contact", fn)])}
<h1>Tell us what you are building</h1>
<p class="lead">Share a little about your business and what you want to achieve. We will get back to you to talk through next steps.</p>
</div>
</section>
<section class="band">
<div class="wrap enquiry">
<div class="enquiry__copy">
<h2>Request a free consultation</h2>
<p>Fill in the form and tell us which service interests you. If you are not sure yet, choose &ldquo;Multiple services / Not sure yet&rdquo; and describe your goal.</p>
<div class="direct">Prefer email?<br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
{form("contact.html")}
</div>
</section>
</main>
'''
    write(fn, head(title, desc, fn, ld) + header(fn) + body + footer())


def build_privacy():
    fn = "privacy-policy.html"
    title = "Privacy Policy | Digivexora Solution"
    desc = "How Digivexora Solution collects, uses and protects the details you share through our website enquiry form."
    ld = breadcrumb_ld([("Home", url("index.html")), ("Privacy policy", url(fn))])
    body = f'''<main id="main">
<section class="page-hero">
<div class="wrap">
{crumbs([("Home", "index.html"), ("Privacy policy", fn)])}
<h1>Privacy policy</h1>
<p class="lead">Last updated {date.today().strftime("%d %B %Y")}.</p>
</div>
</section>
<section class="band">
<div class="wrap prose">
<p>This page explains what information {e(BRAND)} collects through this website and how we use it.</p>
<h2>Information we collect</h2>
<p>When you submit the enquiry form we collect the details you enter: your name, phone number, business name (optional), email address (optional), the service you are interested in and your message. We also record which page you submitted the form from.</p>
<h2>How we use it</h2>
<p>We use these details only to respond to your enquiry and to discuss our services with you. We do not sell your information.</p>
<h2>Where it is stored</h2>
<p>Enquiries are stored in a database on our web hosting. Access is limited to people who need it to respond to you. We keep enquiries only for as long as needed to follow up and manage our business relationship.</p>
<h2>Third-party services</h2>
<p>This website loads fonts from Google Fonts, which means your browser connects to Google's servers when a page loads. This website does not set advertising cookies.</p>
<h2>Your choices</h2>
<p>You can ask us to show, correct or delete the information you sent us by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2>
<p>We may update this policy from time to time. The date at the top shows when it was last changed.</p>
</div>
</section>
</main>
'''
    write(fn, head(title, desc, fn, ld) + header() + body + footer())


def build_service(s):
    fn = s["slug"] + ".html"
    ld = jsonld({"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
                 "description": s["meta"], "url": url(fn), "provider": {"@id": f"{DOMAIN}/#org"}}) + \
        breadcrumb_ld([("Home", url("index.html")), ("Services", url("services.html")), (s["name"], url(fn))]) + \
        jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]})
    fit = "".join(f"<li>{e(x)}</li>" for x in s["fit"])
    inc = "".join(f'<div class="inc"><h3>{e(t)}</h3><p>{e(p)}</p></div>' for t, p in s["included"])
    steps = "".join(f'<li class="step"><h3>{e(t)}</h3><p>{e(p)}</p></li>' for t, p in s["steps"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in s["faqs"])
    rel = svc_rows(s["related"])
    body = f'''<main id="main">
<section class="page-hero">
<div class="wrap">
{crumbs([("Home", "index.html"), ("Services", "services.html"), (s["name"], fn)])}
<div class="page-hero__grid">
<div>
<h1>{e(s["h1"])}</h1>
<p class="lead">{e(s["lead"])}</p>
<div class="actions">
<a class="btn btn--primary" href="#enquire">Get a free consultation</a>
<a class="btn btn--ghost" href="services.html">All services</a>
</div>
</div>
<aside class="fit"><h2>This is a good fit if</h2><ul>{fit}</ul></aside>
</div>
</div>
</section>

<section class="band">
<div class="wrap">
<div class="sec-head"><h2>What is included</h2></div>
<div class="included">{inc}</div>
</div>
</section>

<section class="band band--navy">
<div class="wrap">
<div class="sec-head"><h2>How it works</h2></div>
<ol class="steps">{steps}</ol>
</div>
</section>

<section class="band">
<div class="wrap">
<div class="sec-head"><h2>Common questions</h2></div>
<div class="faq">{faqs}</div>
</div>
</section>

<section class="band band--paper" id="enquire">
<div class="wrap enquiry">
<div class="enquiry__copy">
<h2>Talk to us about {e(s["name"])}</h2>
<p>Tell us about your business and what you want to achieve. We will reply with clear next steps and an honest view of what to expect.</p>
<div class="direct">Prefer email?<br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
{form(fn, s["form"])}
</div>
</section>

<section class="band">
<div class="wrap">
<div class="sec-head"><h2>Related services</h2></div>
<div class="related">{rel}</div>
</div>
</section>
</main>
'''
    write(fn, head(s["title"], s["meta"], fn, ld) + header("services.html") + body + footer())


def build_404():
    pre = "/"
    body = f'''<main id="main">
<section class="band"><div class="wrap notice">
<h1>That page could not be found</h1>
<p class="lead">The link may be broken or the page may have moved. Try one of these instead.</p>
<div class="actions"><a class="btn btn--primary" href="/index.html">Go to the home page</a><a class="btn btn--ghost" href="/services.html">See our services</a></div>
</div></section>
</main>
'''
    write("404.html", head("Page not found | " + BRAND, "Page not found.", "404.html", noindex=True, pre=pre)
          + header(pre=pre) + body + footer(pre=pre), in_sitemap=False)


def build_sitemap_and_robots():
    urls = []
    for fn in PAGES:
        urls.append(f"  <url>\n    <loc>{url(fn)}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n  </url>")
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sm)
    robots = f"""# robots.txt for {DOMAIN}
User-agent: *
Allow: /
Disallow: /submit_enquiry.php
Disallow: /tools/

Sitemap: {DOMAIN}/sitemap.xml
"""
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)


if __name__ == "__main__":
    build_home()
    build_about()
    build_services()
    for s in SERVICES:
        build_service(s)
    build_contact()
    build_privacy()
    build_404()
    build_sitemap_and_robots()
    # sanity warnings for search snippets
    for s in SERVICES:
        if len(s["title"]) > 60:
            print("WARN title >60:", s["slug"], len(s["title"]))
        if len(s["meta"]) > 160:
            print("WARN meta >160:", s["slug"], len(s["meta"]))
    print(f"Built {len(PAGES)} indexable pages + 404.html, sitemap.xml and robots.txt in {OUT}")

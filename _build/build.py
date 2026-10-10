#!/usr/bin/env python3
"""Static site generator for 36118.com.
Run:  python3 _build/build.py   (from the repo root)
Writes plain HTML into the repo root so GitHub Pages can serve it with no build step.
"""
import json, os, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from guides import GUIDES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://36118.com"
NAME = "36118"
TODAY = datetime.date.today().isoformat()
ADSENSE = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271"
     crossorigin="anonymous"></script>'''
INTEREST_URL = "https://web.works/contact"
PAGES = []  # for sitemap

def esc(s): return html.escape(s, quote=True)

def rel(depth): return "../" * depth if depth else "./"

def head(title, desc, path, depth, schema, noindex=False):
    r = rel(depth)
    url = SITE + "/" + ("" if path == "index.html" else path)
    ld = "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False) for s in schema)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<meta property="og:type" content="website">
<meta property="og:site_name" content="36118.com">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13233F">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/site.css">
{ADSENSE}
{ld}
</head>'''

NAV = [("tools/index.html", "Tools", "tools"), ("guides/index.html", "Guides", "guides"), ("videos.html", "Videos", "videos"),
       ("the-number-36118.html", "About 36118", "36118"), ("support.html", "Support us", "support")]

def header(depth, active):
    r = rel(depth)
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{r}{h}"{cur if k == active else ""}>{t}</a>' for h, t, k in NAV)
    return f'''<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="interest" role="note"><a href="{INTEREST_URL}" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-head">
 <div class="wrap">
  <a class="brand" href="{r}index.html" aria-label="36118.com home"><span class="brand-mark" aria-hidden="true"><i>3</i><i>6</i><i>1</i><i>1</i><i>8</i></span><span>.com</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="cta" href="{r}services.html">Buy, sell or appraise</a>
   <button class="theme-btn" data-theme-toggle aria-label="Switch light or dark theme" title="Light / dark"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3a9 9 0 0 0 0 18z" fill="currentColor"/></svg></button></nav>
 </div>
</header>
'''

def footer(depth):
    r = rel(depth)
    return f'''<footer class="site-foot">
 <div class="wrap">
  <div class="foot-grid">
   <div><a class="brand" style="color:#fff" href="{r}index.html"><span class="brand-mark" aria-hidden="true"><i>3</i><i>6</i><i>1</i><i>1</i><i>8</i></span><span>.com</span></a>
    <p style="margin-top:12px">Free number intelligence: decode any number, look up postal codes, score domains and learn what digits mean in business, AI and everyday life.</p>
    <p><a href="#" data-mail="Inquiry from 36118.com">Email us</a></p></div>
   <div><h4>Tools</h4><ul>
    <li><a href="{r}tools/number-decoder.html">Number decoder</a></li><li><a href="{r}tools/zip-explorer.html">ZIP &amp; postal explorer</a></li>
    <li><a href="{r}tools/lucky-number.html">Lucky-number reader</a></li><li><a href="{r}tools/domain-valuator.html">Domain scorecard</a></li></ul></div>
   <div><h4>Work with us</h4><ul>
    <li><a href="{r}services.html">Buy, sell or appraise</a></li><li><a href="{r}advertise.html">Advertise &amp; sponsor</a></li>
    <li><a href="{r}contests.html">Contests</a></li><li><a href="{r}careers.html">Careers</a></li><li><a href="{r}support.html">Support us</a></li></ul></div>
   <div><h4>Site</h4><ul>
    <li><a href="{r}about.html">About</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}privacy.html">Privacy policy</a></li>
    <li><a href="{r}terms.html">Terms of use</a></li><li><a href="{r}disclaimer.html">Disclaimer &amp; trademarks</a></li></ul></div>
  </div>
  <div class="ad-slot" data-slot="footer"></div>
  <p class="legal-line">© <span data-year>{datetime.date.today().year}</span> 36118.com, a Webworks property. Site content and code are original works. "36118" is used as a number and U.S. ZIP code in a descriptive sense; no trademark is claimed in the number, and no affiliation with the U.S. Postal Service, the U.S. Air Force or any other organisation is implied. Third-party names belong to their owners. See <a href="{r}disclaimer.html">Disclaimer &amp; trademarks</a>.</p>
 </div>
</footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice">
 <p style="margin:0">We use cookies for basic preferences and, through Google AdSense, to show and measure ads. Read the <a href="{r}privacy.html">privacy policy</a>.</p>
 <div class="btns"><button class="btn btn-dark" data-cookie-ok>OK</button><a class="btn btn-ghost" href="https://adssettings.google.com" rel="noopener">Ad settings</a></div>
</div>
<script src="{r}assets/js/numbers.js" defer></script>
<script src="{r}assets/js/site.js" defer></script>
<script src="{r}assets/js/tools.js" defer></script>
</body>
</html>'''

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "36118.com", "url": SITE, "logo": SITE + "/assets/img/apple-touch-icon.png"}

def crumbs(depth, trail):
    r = rel(depth)
    items = [("Home", "index.html")] + trail
    htmlc = " / ".join(f'<a href="{r}{p}">{esc(t)}</a>' if p else esc(t) for t, p in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + "/" + (p if p and p != "index.html" else "")} for i, (t, p) in enumerate(items)]}
    return f'<nav class="crumbs" aria-label="Breadcrumb">{htmlc}</nav>', ld

def write(path, title, desc, body, active=None, schema=None, noindex=False, priority="0.6"):
    depth = path.count("/")
    out = head(title, desc, path, depth, [ORG] + (schema or []), noindex) + header(depth, active) + f'<main id="main">{body}</main>' + footer(depth)
    out = out.replace("{r}", rel(depth))
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(out)
    if not noindex: PAGES.append((path, priority))

def faq_html(faqs):
    return '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs) + "</section>"

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def yt(vid, cap):
    return f'<button class="yt" data-yt="{vid}" aria-label="Play video: {esc(cap)}"><span class="play"></span><span class="cap">{esc(cap)}</span></button>'

VIDEOS = [
    ("EK32jo7i5LQ", "Why do prime numbers make these spirals?", "3Blue1Brown", "Primes plotted in polar coordinates form spirals and rays. The video explains why, using Dirichlet's theorem and approximations of pi."),
    ("aircAruvnKk", "But what is a neural network?", "3Blue1Brown", "A visual introduction to the numbers inside AI models: weights, biases and layers, built up from a digit-recognition example."),
    ("LPZh9BOjkQs", "Large language models explained briefly", "3Blue1Brown", "How chatbots turn text into tokens and numbers, and predict what comes next."),
]

def side_cta(depth):
    r = rel(depth)
    return f'''<aside class="aside"><div class="panel">
<h3>Own a number worth money?</h3>
<p class="small">Numeric domains, phone numbers and short names trade in an active market. Get a free human review of yours.</p>
<a class="btn btn-primary" href="{r}services.html?intent=Appraise">Request a free review</a>
<div class="ad-slot" data-slot="sidebar"></div>
</div></aside>'''

# -------------------------------------------------------------------------------------------- HOME
def home():
    gl = "".join(f'<li><a href="guides/{g["slug"]}.html"><strong>{esc(g["title"])}</strong><span class="m">{g["topic"]}, {g["minutes"]} min</span></a></li>' for g in GUIDES[:7])
    vids = "".join(f'<div>{yt(v, t)}<p class="small muted" style="margin-top:8px">{esc(d)} Video by {ch}.</p></div>' for v, t, ch, d in VIDEOS)
    faqs = [
        ("What is 36118.com?", "A free number-intelligence site. Type any number to see its mathematical properties, its meaning as a postal code, its cultural associations and how it scores as a domain name."),
        ("Is 36118 a real ZIP code?", "Yes. 36118 is a unique ZIP code in Montgomery, Alabama, assigned to an institution rather than to households, which is why it has no residential population."),
        ("Are the tools free?", "Yes. Every tool runs in your browser, needs no account and is supported by advertising and voluntary donations."),
        ("Can you help me buy or sell a numeric domain?", "Yes. Use the Buy, sell or appraise form and we reply within two business days."),
    ]
    body = f'''
<section class="hero">
 <div class="wrap hero-grid">
  <div>
   <h1>Type any number. See everything it means.</h1>
   <p class="lede">Maths, postal geography, culture and market value, decoded in one place. We start with 36118.</p>
   <label class="flap" for="heroNum"><span class="visually-hidden">Number to decode</span>
    <input id="heroNum" inputmode="numeric" autocomplete="off" maxlength="15" value="36118" aria-describedby="heroHint">
    <span class="tiles" id="heroTiles" aria-hidden="true"></span></label>
   <p class="hint" id="heroHint">Click the tiles and type up to 15 digits. Press Enter for the full decode.</p>
  </div>
  <div>
   <div class="readout" id="heroOut" aria-live="polite"></div>
   <div class="btns">
    <a class="btn btn-primary" id="heroDecode" href="tools/number-decoder.html?n=36118">Full decode</a>
    <a class="btn btn-ghost" id="heroZip" href="tools/zip-explorer.html?zip=36118" style="color:#fff">Look up as ZIP</a>
    <a class="btn btn-ghost" id="heroLucky" href="tools/lucky-number.html?n=36118" style="color:#fff">Lucky reading</a>
    <a class="btn btn-ghost" id="heroDomain" href="tools/domain-valuator.html?d=36118.com" style="color:#fff">Score as .com</a>
   </div>
  </div>
 </div>
</section>
<div class="wrap"><div class="ad-slot" data-slot="top"></div></div>

<section class="section">
 <div class="wrap">
  <div class="section-head"><h2>Tools</h2><p class="muted">Free, instant and private. Calculations run in your browser.</p></div>
  <div class="directory">
   <a class="dir-row" href="tools/number-decoder.html"><strong>Number decoder</strong><span>Primes, factors, divisors, bases, words, Roman numerals and 25 more properties of any number.</span><span class="eg">36118 = 2 × 18059</span></a>
   <a class="dir-row" href="tools/zip-explorer.html"><strong>ZIP &amp; postal explorer</strong><span>Place names, coordinates and a map for U.S. ZIP codes and postal codes in dozens of countries, plus distance between two codes.</span><span class="eg">36117, 226001, M5V</span></a>
   <a class="dir-row" href="tools/lucky-number.html"><strong>Lucky-number reader</strong><span>Cultural associations and memorability for prices, phone numbers, plates and addresses.</span><span class="eg">168, 518, 888</span></a>
   <a class="dir-row" href="tools/domain-valuator.html"><strong>Domain scorecard</strong><span>A transparent 0–10 liquidity score for numeric and word domains, factor by factor.</span><span class="eg">36118.com: 7.7 / 10</span></a>
  </div>
 </div>
</section>

<section class="section alt">
 <div class="wrap grid-2">
  <div>
   <h2>Why 36118?</h2>
   <p>It is a real U.S. ZIP code with no residents, an even semiprime (2 × 18,059), 8D16 in hexadecimal, and a five-digit "chip" that ends in the luckiest digit in Chinese culture. One number, four different stories, which is exactly what this site is built to uncover.</p>
   <a class="btn btn-dark" href="the-number-36118.html">Read the full profile</a>
  </div>
  <div class="panel">
   <h3>Number of the day</h3>
   <p id="nod" class="muted">Loading…</p>
   <p class="small muted">A new number every day, the same for every visitor. Subscribe for the weekly pick and one useful guide.</p>
   <form class="inline-form" data-form="Newsletter signup" data-ok="You're on the list. Look out for the weekly number.">
    <label class="visually-hidden" for="nl-email">Email address</label>
    <input id="nl-email" type="email" name="email" placeholder="you@example.com" required>
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="btn btn-primary" type="submit">Subscribe</button>
   </form>
  </div>
 </div>
</section>

<section class="section">
 <div class="wrap">
  <div class="funnel">
   <div class="grid-2">
    <div>
     <h2>Buying, selling or naming with numbers?</h2>
     <p>Numeric domains, memorable phone numbers and short brand names are bought and sold every day. Tell us what you have or what you need and get a straight answer from a person, not a bot.</p>
     <ul>
      <li>Free appraisal of a numeric or short domain</li>
      <li>Help finding and negotiating the number you want</li>
      <li>Sponsorship and partnership on 36118.com</li>
     </ul>
     <div class="trust"><span>Reply within 2 business days</span><span>No account needed</span><span>Your details are never sold</span></div>
    </div>
    <form data-form="Quick lead" data-ok="Thanks. We'll reply within two business days with next steps.">
     <div class="field"><label class="lbl" for="q-intent">I want to</label>
      <select id="q-intent" name="intent" required><option value="">Choose one</option><option>Buy a numeric domain</option><option>Sell or appraise my domain</option><option>Acquire 36118.com</option><option>Sponsor or partner</option><option>Something else</option></select></div>
     <div class="field"><label class="lbl" for="q-domain">Domain or number (optional)</label><input id="q-domain" type="text" name="domain" placeholder="e.g. 88168.com"></div>
     <div class="field"><label class="lbl" for="q-email">Email</label><input id="q-email" type="email" name="email" required autocomplete="email"></div>
     <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
     <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request.</label>
     <p style="margin-top:14px"><button class="btn btn-primary" type="submit">Get my free answer</button> <a href="services.html">or use the detailed form</a></p>
    </form>
   </div>
  </div>
 </div>
</section>
<div class="wrap"><div class="ad-slot" data-slot="inContent"></div></div>

<section class="section alt">
 <div class="wrap">
  <div class="section-head"><h2>Guides</h2><a href="guides/index.html">All guides</a></div>
  <ul class="guide-list">{gl}</ul>
 </div>
</section>

<section class="section">
 <div class="wrap">
  <div class="section-head"><h2>Watch: numbers explained</h2><a href="videos.html">More videos</a></div>
  <div class="grid-3">{vids}</div>
 </div>
</section>

<section class="section alt">
 <div class="wrap grid-3">
  <div><h3>Keep the tools free</h3><p>Donations pay for hosting, new tools, promotion, contributor fees and contest prizes. Choose where your support goes.</p><a class="btn btn-dark" href="support.html">Support 36118.com</a></div>
  <div><h3>Number Hunt contest</h3><p>Find the most surprising true fact about a number. Winners are featured on the site and receive sponsor-funded prizes.</p><a class="btn btn-dark" href="contests.html">Enter the contest</a></div>
  <div><h3>Write or build with us</h3><p>We hire freelance writers, data researchers, video creators and front-end developers who love numbers.</p><a class="btn btn-dark" href="careers.html">See open roles</a></div>
 </div>
</section>

<section class="section"><div class="wrap"><div class="prose">{faq_html(faqs)}</div></div></section>
'''
    schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": "36118.com", "url": SITE,
               "potentialAction": {"@type": "SearchAction", "target": SITE + "/tools/number-decoder.html?n={search_term_string}", "query-input": "required name=search_term_string"}},
              faq_ld(faqs)]
    write("index.html", "36118.com: decode any number, ZIP code or numeric domain",
          "Free number intelligence. Decode any number's maths, look up ZIP and postal codes, read lucky-number meanings and score numeric domains. Starting with 36118.",
          body, active=None, schema=schema, priority="1.0")

# -------------------------------------------------------------------------------------------- TOOLS
def tool_page(path, title, desc, h1, intro, form, out_id, explain, faqs, crumb):
    c, cl = crumbs(1, [("Tools", "tools/index.html"), (crumb, None)])
    body = f'''<div class="wrap">{c}
<div class="layout"><div>
<h1>{h1}</h1><p class="muted prose">{intro}</p>
<div class="panel">{form}<div id="{out_id}" aria-live="polite" style="margin-top:18px"></div></div>
<div class="ad-slot" data-slot="inContent"></div>
<div class="prose" style="margin-top:32px">{explain}{faq_html(faqs)}</div>
</div>{side_cta(1)}</div></div>'''
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": h1, "url": SITE + "/" + path,
           "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    write(path, title, desc, body, active="tools", schema=[app, cl, faq_ld(faqs)], priority="0.9")

def tools():
    c, cl = crumbs(1, [("Tools", None)])
    write("tools/index.html", "Free number tools: decoder, ZIP explorer, lucky numbers, domain scorecard | 36118.com",
          "Four free tools for numbers: decode mathematical properties, look up postal codes, read cultural number meanings and score domain names.",
          f'''<div class="wrap">{c}<h1>Number tools</h1><p class="prose muted">Each tool runs in your browser. Nothing you type is stored.</p>
<div class="directory">
<a class="dir-row" href="number-decoder.html"><strong>Number decoder</strong><span>Prime factorisation, divisors, σ, φ, bases 2–36, words, Roman numerals, square and Fibonacci checks, neighbours.</span><span class="eg">Up to 15 digits</span></a>
<a class="dir-row" href="zip-explorer.html"><strong>ZIP &amp; postal explorer</strong><span>Place, region and coordinates with a map; straight-line distance between two codes.</span><span class="eg">US, CA, GB, IN, DE…</span></a>
<a class="dir-row" href="lucky-number.html"><strong>Lucky-number reader</strong><span>Cultural luck score, memorability score, digit-by-digit associations.</span><span class="eg">Phones, plates, prices</span></a>
<a class="dir-row" href="domain-valuator.html"><strong>Domain scorecard</strong><span>Liquidity score and tier for numeric and word domains with every factor shown.</span><span class="eg">36118.com</span></a>
</div><div class="ad-slot" data-slot="inContent"></div></div>''', active="tools", schema=[cl], priority="0.9")

    tool_page("tools/number-decoder.html", "Number decoder: prime factors, divisors, binary, hex and more | 36118.com",
        "Decode any whole number up to 15 digits: prime factorisation, divisors, totient, square and Fibonacci checks, binary, hex, base 36, words and Roman numerals.",
        "Number decoder", "Enter any whole number up to 15 digits. You get more than 25 exact properties, computed in your browser.",
        '''<form id="decodeForm" class="inline-form" role="search"><label class="visually-hidden" for="decodeInput">Number</label>
<input id="decodeInput" type="text" inputmode="numeric" autocomplete="off" placeholder="e.g. 36118" required><button class="btn btn-primary" type="submit">Decode</button></form>''',
        "decodeOut",
        '''<h2>What the properties mean</h2>
<p><strong>Prime factorisation</strong> writes the number as a product of primes; every whole number above 1 has exactly one. <strong>σ(n)</strong> is the sum of all divisors, and comparing σ(n) − n with n tells you whether a number is perfect (equal), abundant (greater) or deficient (less). <strong>φ(n)</strong>, Euler's totient, counts the numbers below n that share no factor with it and is central to RSA encryption.</p>
<p>A <strong>Harshad number</strong> is divisible by the sum of its digits. The <strong>digital root</strong> is what you get by summing digits until one remains; it equals the remainder after dividing by 9. Base conversions show the same quantity written in binary, octal, hexadecimal and base 36.</p>
<p>Read more in <a href="../guides/prime-numbers-and-encryption.html">primes and encryption</a> and <a href="../guides/binary-hex-and-number-bases.html">number bases</a>.</p>''',
        [("How large a number can I decode?", "Up to 15 digits. That keeps every result exact in standard browser arithmetic."),
         ("Is my number stored?", "No. All calculations happen in your browser."),
         ("What is a semiprime?", "A number that is the product of exactly two primes, such as 36118 = 2 × 18,059.")], "Number decoder")

    tool_page("tools/zip-explorer.html", "ZIP code and postal code lookup with map and distance | 36118.com",
        "Look up any U.S. ZIP code or postal codes in dozens of countries: place names, region, coordinates and map. Measure the distance between two codes.",
        "ZIP &amp; postal code explorer", "Look up place names, coordinates and a map for a postal code, then measure the distance between two codes.",
        '''<form id="zipForm" class="inline-form"><label class="visually-hidden" for="zipCountry">Country</label>
<select id="zipCountry" style="flex:0 0 170px"><option value="us">United States</option><option value="ca">Canada (first 3)</option><option value="gb">United Kingdom (outward)</option><option value="in">India (PIN)</option><option value="de">Germany</option><option value="fr">France</option><option value="es">Spain</option><option value="it">Italy</option><option value="au">Australia</option><option value="jp">Japan</option><option value="mx">Mexico</option><option value="br">Brazil</option><option value="nl">Netherlands</option><option value="lk">Sri Lanka</option></select>
<label class="visually-hidden" for="zipInput">Postal code</label><input id="zipInput" type="text" autocomplete="postal-code" placeholder="e.g. 36117" required><button class="btn btn-primary" type="submit">Look up</button></form>''',
        "zipOut",
        '''<h2>Distance between two codes</h2>
<form id="distForm" class="inline-form"><label class="visually-hidden" for="distC">Country</label><select id="distC" style="flex:0 0 140px"><option value="us">United States</option><option value="ca">Canada</option><option value="gb">United Kingdom</option><option value="in">India</option><option value="de">Germany</option><option value="au">Australia</option></select>
<label class="visually-hidden" for="distA">From</label><input id="distA" type="text" placeholder="From, e.g. 36117" required><label class="visually-hidden" for="distB">To</label><input id="distB" type="text" placeholder="To, e.g. 35203" required><button class="btn btn-dark" type="submit">Measure</button></form>
<p id="distOut" aria-live="polite" style="margin-top:12px"></p>
<h2>About ZIP 36118</h2>
<p>36118 is a <a href="../guides/what-is-a-unique-zip-code.html">unique ZIP code</a> in Montgomery, Alabama, tied to a single institution rather than to homes. Open postal datasets often leave unique codes out, so try a neighbouring standard code such as 36117 for area data. Learn how the digits work in <a href="../guides/how-us-zip-codes-work.html">how ZIP codes work</a>.</p>''',
        [("Where does the data come from?", "Place names and coordinates come from the open Zippopotam.us API, which compiles GeoNames postal data. Maps are from OpenStreetMap."),
         ("Why is my code not found?", "Unique and PO Box ZIP codes are often missing from open datasets. Check the format, or try a nearby standard code."),
         ("Is the distance the driving distance?", "No, it is the straight-line (great-circle) distance. Road distance is usually 20–40% longer.")], "ZIP explorer")

    tool_page("tools/lucky-number.html", "Lucky number meaning checker for phone numbers, prices and plates | 36118.com",
        "Score any number for Chinese cultural luck and memorability: digit-by-digit meanings for 8, 6, 9 and 4, lucky combinations like 168 and 518, and memorability patterns.",
        "Lucky-number reader", "Paste a phone number, price, license plate or address. You get a cultural luck score, a memorability score and the meaning of every digit.",
        '''<form id="luckyForm" class="inline-form"><label class="visually-hidden" for="luckyInput">Number</label>
<input id="luckyInput" type="text" inputmode="numeric" autocomplete="off" placeholder="e.g. 888-5168" required><button class="btn btn-primary" type="submit">Read number</button></form>''',
        "luckyOut",
        '''<h2>How the scores work</h2>
<p>The <strong>cultural luck score</strong> starts at 50. Each digit adds or subtracts according to widely shared Mandarin and Cantonese homophones: 8 for prosperity, 6 for smoothness, 9 for longevity, 4 for death. Known combinations such as 168 and 518 add points, numbers ending in 8 earn a bonus, and avoiding 4 entirely earns another.</p>
<p>The <strong>memorability score</strong> rewards short length, few distinct digits, repeats, palindromes and sequences, the patterns people recall most easily.</p>
<p>Read the background in <a href="../guides/chinese-lucky-numbers-in-business.html">Chinese lucky numbers in business</a> and <a href="../guides/choosing-a-business-phone-number.html">choosing a business phone number</a>.</p>''',
        [("Is this fortune telling?", "No. It reports cultural preferences that affect buyer choices. It does not predict outcomes."),
         ("Why does 4 lower the score?", "In Mandarin and Cantonese, 4 sounds like the word for death, so many buyers avoid it."),
         ("What makes a number memorable?", "Short length, repeated digits, simple patterns and meaningful chunks.")], "Lucky-number reader")

    tool_page("tools/domain-valuator.html", "Domain name scorecard: numeric 4N/5N and word domains | 36118.com",
        "Score any domain from 0 to 10 for liquidity. Numeric names are rated on length, chip status, lucky digits and patterns; word names on length, pronounceability and extension.",
        "Domain scorecard", "A transparent liquidity score for any domain. Every factor is shown, so you can see exactly why a name ranks where it does.",
        '''<form id="valueForm" class="inline-form"><label class="visually-hidden" for="valueInput">Domain</label>
<input id="valueInput" type="text" autocomplete="off" placeholder="e.g. 36118.com" required><button class="btn btn-primary" type="submit">Score domain</button></form>''',
        "valueOut",
        '''<h2>What the score measures</h2>
<p>The score estimates <strong>liquidity</strong>: how many buyers are likely to want a name and how quickly it could sell. For numeric domains the biggest factor is length, because each extra digit multiplies supply by ten. Chip status (no 0 or 4), a final 8, repeating patterns and the extension adjust the score. For word domains, length, hyphens, digits and pronounceability matter most.</p>
<p>It is deliberately not a price. Prices depend on recent comparable sales and on whether a specific end user needs the name. For that, request a human appraisal.</p>
<p>Background: <a href="../guides/numeric-domain-names-explained.html">numeric domains explained</a> and <a href="../guides/how-to-value-a-numeric-domain.html">how to value a domain</a>.</p>''',
        [("Why no dollar value?", "Automated dollar figures are often wrong by an order of magnitude. A transparent score plus real comparables is more useful."),
         ("What tier is 36118.com?", "On this model 36118.com scores 7.7 out of 10, tier A: a 5N .com chip ending in 8."),
         ("Can you sell my domain?", "We can review it and connect you with buyers. Use the Buy, sell or appraise form.")], "Domain scorecard")

# -------------------------------------------------------------------------------------------- 36118 PROFILE
def profile():
    c, cl = crumbs(0, [("About 36118", None)])
    faqs = [("What does 36118 mean?", "36118 is a unique U.S. ZIP code in Montgomery, Alabama; mathematically it is 2 × 18,059; in Chinese number culture its digits read as life, smoothness, want-want and prosperity."),
            ("Is 36118 prime?", "No. It is even and equals 2 × 18,059, which makes it a semiprime."),
            ("Is 36118.com for sale?", "Use the link at the top of every page to contact the owner about the domain, sponsorship or partnership.")]
    body = f'''<div class="wrap">{c}<div class="layout"><div class="prose">
<h1>36118: one number, four stories</h1>
<p>Most numbers are only quantities. 36118 has a postal identity, a clean mathematical signature, a cultural reading and a place in a traded asset class. Here is each in turn.</p>
<h2>1. A ZIP code with no residents</h2>
<p>36118 is a U.S. ZIP code in Montgomery, Alabama, wholly inside Montgomery County and served by area code 334. It is classified as a <strong>unique</strong> ZIP code, meaning it routes mail to a single organisation rather than to homes. Directories associate it with the Gunter Annex area of Maxwell-Gunter Air Force Base. That explains why demographic sites show zero population for it. <a href="guides/what-is-a-unique-zip-code.html">How unique ZIP codes work</a>.</p>
<h2>2. The mathematics</h2>
<table class="facts"><tbody>
<tr><th scope="row">Prime factorisation</th><td>2 × 18,059 (semiprime)</td></tr>
<tr><th scope="row">Divisors</th><td>1, 2, 18,059, 36,118 (four in total)</td></tr>
<tr><th scope="row">Sum of divisors σ(n)</th><td>54,180 (deficient)</td></tr>
<tr><th scope="row">Euler's totient φ(n)</th><td>18,058</td></tr>
<tr><th scope="row">Neighbouring primes</th><td>36,109 and 36,131</td></tr>
<tr><th scope="row">Binary / octal / hex / base 36</th><td>1000110100010110 / 106426 / 8D16 / RVA</td></tr>
<tr><th scope="row">Digit sum / digital root</th><td>19 / 1</td></tr>
<tr><th scope="row">In words</th><td>thirty-six thousand one hundred eighteen</td></tr>
</tbody></table>
<p><a href="tools/number-decoder.html?n=36118">Open the live decode</a>.</p>
<h2>3. The cultural reading</h2>
<p>Read through Chinese homophones, 3 suggests life (in Cantonese), 6 smoothness, the paired 1s "want, want" and the final 8 prosperity. The number contains no 4, the most avoided digit. On our lucky-number model it scores 80 out of 100. These are cultural associations, not predictions, but they shape how buyers in large markets feel about a number. <a href="tools/lucky-number.html?n=36118">See the digit-by-digit reading</a>.</p>
<h2>4. An asset class</h2>
<p>As a domain, 36118.com is a five-digit numeric .com, a class with exactly 100,000 members. It is a "chip" (no 0 or 4), one of 32,768 such 5N names, and it ends in 8. Our scorecard rates it 7.7 out of 10 for liquidity. <a href="tools/domain-valuator.html?d=36118.com">See the scorecard</a>.</p>
<h2>In AI and the economy</h2>
<p>To a language model, 36118 is a short run of tokens rather than a quantity, which is why AI assistants use calculators for exact arithmetic (<a href="guides/how-ai-reads-numbers.html">how AI reads numbers</a>). In economic data, a figure like 36,118 only gains meaning with units and context: dollars or people, nominal or real, total or per person (<a href="guides/reading-economic-numbers.html">reading economic numbers</a>).</p>
<div class="callout">"36118" is used here descriptively. No trademark is claimed in the number, and this site is not affiliated with the U.S. Postal Service, the U.S. Air Force or any organisation that uses 36118 as a code, model or part number.</div>
{faq_html(faqs)}
</div>{side_cta(0)}</div></div>'''
    art = {"@context": "https://schema.org", "@type": "Article", "headline": "36118: one number, four stories", "dateModified": TODAY,
           "author": {"@type": "Organization", "name": "36118.com"}, "publisher": ORG, "mainEntityOfPage": SITE + "/the-number-36118.html"}
    write("the-number-36118.html", "36118 meaning: ZIP code, prime factors, lucky reading and domain value | 36118.com",
          "Everything about the number 36118: a unique ZIP code in Montgomery, Alabama; 2 × 18,059; 8D16 in hex; its Chinese lucky-number reading and its value as a 5N.com.",
          body, active="36118", schema=[art, cl, faq_ld(faqs)], priority="0.9")

# -------------------------------------------------------------------------------------------- GUIDES
def guides():
    c, cl = crumbs(1, [("Guides", None)])
    topics = []
    for g in GUIDES:
        if g["topic"] not in topics: topics.append(g["topic"])
    blocks = ""
    for t in topics:
        items = "".join(f'<li><a href="{g["slug"]}.html"><strong>{esc(g["title"])}</strong><span class="m">{g["minutes"]} min</span></a></li>' for g in GUIDES if g["topic"] == t)
        blocks += f'<h2 style="margin-top:32px">{esc(t)}</h2><ul class="guide-list">{items}</ul>'
    write("guides/index.html", "Guides to numbers in business, AI, ZIP codes and domains | 36118.com",
          "Plain-English guides on ZIP codes, Chinese lucky numbers, numeric domains, Benford's law, prime numbers, AI and economic figures.",
          f'<div class="wrap">{c}<h1>Guides</h1><p class="prose muted">Clear, sourced explanations of what numbers mean and how they are used. Updated {TODAY}.</p>{blocks}<div class="ad-slot" data-slot="inContent"></div></div>',
          active="guides", schema=[cl], priority="0.8")
    for i, g in enumerate(GUIDES):
        c, cl = crumbs(1, [("Guides", "guides/index.html"), (g["title"], None)])
        vid = ""
        if g.get("video"):
            vid = f'<div style="margin:24px 0">{yt(*g["video"])}</div>'
        body_html = g["body"]
        # place the in-content ad slot after the second H2 so ads never sit between a heading and its first paragraph
        parts = body_html.split("<h2>", 3)
        if len(parts) == 4:
            body_html = parts[0] + "<h2>" + parts[1] + "<h2>" + parts[2] + '<div class="ad-slot" data-slot="inContent"></div><h2>' + parts[3]
        related = [x for x in GUIDES if x["slug"] != g["slug"] and x["topic"] == g["topic"]][:2] + [GUIDES[(i + 1) % len(GUIDES)]]
        rel_html = "".join(f'<li><a href="{x["slug"]}.html"><strong>{esc(x["title"])}</strong><span class="m">{x["minutes"]} min</span></a></li>' for x in {x["slug"]: x for x in related}.values())
        body = f'''<div class="wrap">{c}<div class="layout"><article class="prose">
<h1>{esc(g["title"])}</h1>
<p class="muted small">{esc(g["topic"])}. {g["minutes"]}-minute read. Updated {TODAY}.</p>
{body_html}{vid}
{faq_html(g["faqs"])}
<h2>Keep reading</h2><ul class="guide-list">{rel_html}</ul>
</article>{side_cta(1)}</div></div>'''
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "dateModified": TODAY,
               "author": {"@type": "Organization", "name": "36118.com"}, "publisher": ORG, "mainEntityOfPage": SITE + "/guides/" + g["slug"] + ".html", "image": SITE + "/assets/img/og.png"}
        write(f'guides/{g["slug"]}.html', g["title"] + " | 36118.com", g["desc"], body, active="guides", schema=[art, cl, faq_ld(g["faqs"])], priority="0.8")

# -------------------------------------------------------------------------------------------- VIDEOS
def videos():
    c, cl = crumbs(0, [("Videos", None)])
    items = "".join(f'<div>{yt(v, t)}<h3 style="margin-top:12px">{esc(t)}</h3><p class="small muted">{esc(d)} Video by {ch}, embedded from YouTube.</p></div>' for v, t, ch, d in VIDEOS)
    vo = [{"@context": "https://schema.org", "@type": "VideoObject", "name": t, "description": d, "thumbnailUrl": f"https://i.ytimg.com/vi/{v}/hqdefault.jpg",
           "embedUrl": f"https://www.youtube-nocookie.com/embed/{v}", "uploadDate": "2017-10-05" if v == "aircAruvnKk" else ("2019-10-08" if v == "EK32jo7i5LQ" else "2024-11-20")} for v, t, ch, d in VIDEOS]
    body = f'''<div class="wrap">{c}<h1>Videos: numbers explained</h1>
<p class="prose muted">Hand-picked explainers on primes, AI and the numbers inside language models. Videos load only when you press play.</p>
<div class="grid-3">{items}</div>
<div class="ad-slot" data-slot="inContent"></div>
<div class="panel" style="margin-top:32px"><h2>Make a video with us</h2><p>We commission short explainers about numbers in business, culture and AI. Pitch an idea or apply as a creator.</p>
<div class="btns"><a class="btn btn-dark" href="careers.html">Apply as a creator</a><a class="btn btn-ghost" href="advertise.html">Sponsor a video</a><a class="btn btn-ghost" data-yt-channel hidden href="#">Our YouTube channel</a></div></div>
</div>'''
    write("videos.html", "Videos about numbers, primes and AI | 36118.com", "Watch curated explainers on prime number spirals, neural networks and how large language models handle numbers.",
          body, active="videos", schema=[cl] + vo, priority="0.7")

# -------------------------------------------------------------------------------------------- LEAD GEN
def services():
    c, cl = crumbs(0, [("Buy, sell or appraise", None)])
    intents = [("Buy", "Buy a numeric domain", "Find and negotiate a 3N, 4N, 5N or short name."),
               ("Appraise", "Sell or appraise my domain", "Free human review with comparable sales."),
               ("Acquire", "Acquire 36118.com", "Make an offer on this domain or website."),
               ("Strategy", "Number &amp; naming strategy", "Phone, plate, price or brand numbers that convert."),
               ("Sponsor", "Sponsor or partner", "Reach readers who care about numbers and names."),
               ("Data", "Data, API or custom tool", "Number, postal or domain data built for your product.")]
    cards = "".join(f'<label class="intent"><input type="radio" name="intent" value="{v}" required{" checked" if i == 0 else ""}><strong>{t}</strong><span class="small muted">{d}</span></label>' for i, (v, t, d) in enumerate(intents))
    faqs = [("Is the appraisal really free?", "Yes. A human reviews your name and replies with a liquidity view and comparable sales. Brokerage, if you want it, is quoted separately."),
            ("How fast will you reply?", "Within two business days, usually sooner."),
            ("Do you sell my details?", "No. Your details are used only to answer your request. See the privacy policy.")]
    body = f'''<div class="wrap">{c}<div class="grid-2" style="align-items:start">
<div class="prose">
<h1>Buy, sell or appraise a number</h1>
<p>Numeric domains, memorable phone numbers and short names change hands every day, and the gap between a good price and a bad one is often large. Tell us what you have or what you are looking for. A person reads every request.</p>
<h2>What you get</h2>
<ul>
<li><strong>Buyers:</strong> a shortlist that fits your budget, outreach to current owners and negotiation support.</li>
<li><strong>Sellers:</strong> an honest liquidity view, comparable sales and, if you want it, introductions to qualified buyers.</li>
<li><strong>Brands:</strong> a number strategy across domain, phone and pricing, including cultural fit for Chinese-speaking markets.</li>
<li><strong>Sponsors and partners:</strong> placements on tools, guides, contests and the newsletter.</li>
</ul>
<h2>How it works</h2>
<ol><li>Send the form. It takes about a minute.</li><li>We reply within two business days with an initial view.</li><li>If it makes sense, we agree scope and fees in writing before any work starts.</li></ol>
<p class="small muted">Transactions should always close through a licensed escrow service. We never ask you to send funds to an individual.</p>
{faq_html(faqs)}
</div>
<div class="funnel" id="lead">
<ol class="steps" id="leadSteps"><li>Goal</li><li>Details</li><li>Contact</li></ol>
<form id="leadForm" data-form="Lead" data-ok="Request received. Expect a reply within two business days.">
<div class="fstep"><h2 style="font-size:1.4rem">What do you want to do?</h2><div class="intent-grid">{cards}</div>
<p style="margin-top:16px"><button class="btn btn-primary" type="button" data-next>Continue</button></p></div>
<div class="fstep" hidden><h2 style="font-size:1.4rem">A few details</h2>
<div class="field"><label class="lbl" for="l-domain">Domain, number or name</label><input id="l-domain" type="text" name="domain" data-prefill="domain" placeholder="e.g. 36118.com, 888-5168, or 'a 4N .com'"></div>
<div class="field"><label class="lbl" for="l-budget">Budget or asking price (USD)</label><select id="l-budget" name="budget"><option>Not sure yet</option><option>Under $2,500</option><option>$2,500–$10,000</option><option>$10,000–$25,000</option><option>$25,000–$50,000</option><option>$50,000–$100,000</option><option>$100,000+</option></select></div>
<div class="field"><label class="lbl" for="l-time">Timeline</label><select id="l-time" name="timeline"><option>Now</option><option>Within 30 days</option><option>1–3 months</option><option>Just exploring</option></select></div>
<div class="field"><label class="lbl" for="l-msg">Anything we should know?</label><textarea id="l-msg" name="message" placeholder="Goals, deadlines, names you like or dislike"></textarea></div>
<p class="btns"><button class="btn btn-ghost" type="button" data-back>Back</button><button class="btn btn-primary" type="button" data-next>Continue</button></p></div>
<div class="fstep" hidden><h2 style="font-size:1.4rem">Where should we reply?</h2>
<div class="field"><label class="lbl" for="l-name">Name</label><input id="l-name" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label class="lbl" for="l-email">Email</label><input id="l-email" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label class="lbl" for="l-phone">Phone or WhatsApp (optional)</label><input id="l-phone" type="tel" name="phone" autocomplete="tel"></div>
<div class="field"><label class="lbl" for="l-co">Company (optional)</label><input id="l-co" type="text" name="company" autocomplete="organization"></div>
<div class="field"><label class="lbl" for="l-country">Country</label><input id="l-country" type="text" name="country" autocomplete="country-name"></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request and accept the <a href="privacy.html">privacy policy</a>.</label>
<p class="btns" style="margin-top:14px"><button class="btn btn-ghost" type="button" data-back>Back</button><button class="btn btn-primary" type="submit">Send my request</button></p></div>
</form>
<div class="trust"><span>Human reply in 2 business days</span><span>No spam, no data resale</span><span>Escrow-only transactions</span></div>
</div></div></div>'''
    svc = {"@context": "https://schema.org", "@type": "Service", "name": "Numeric domain appraisal and acquisition", "provider": ORG, "areaServed": "Worldwide"}
    write("services.html", "Buy, sell or appraise numeric domains and memorable numbers | 36118.com",
          "Free human appraisal of numeric and short domains, help buying the number you want, number strategy for brands, and sponsorship on 36118.com.",
          body, active=None, schema=[svc, cl, faq_ld(faqs)], priority="0.9")

def advertise():
    c, cl = crumbs(0, [("Advertise & sponsor", None)])
    body = f'''<div class="wrap">{c}<div class="grid-2" style="align-items:start"><div class="prose">
<h1>Advertise and sponsor on 36118.com</h1>
<p>Our readers are founders, domain investors, marketers, developers and students who look up numbers with a purpose. Sponsorships are clearly labelled and never placed inside tool results.</p>
<h2>Placements</h2>
<table class="rate"><thead><tr><th scope="col">Placement</th><th scope="col">What you get</th></tr></thead><tbody>
<tr><td><strong>Tool sponsor</strong></td><td>"Presented by" credit and a short message on one tool page for a month.</td></tr>
<tr><td><strong>Guide sponsor</strong></td><td>Sponsor credit on a guide in your field, plus a link in the sidebar.</td></tr>
<tr><td><strong>Contest prize partner</strong></td><td>Your prize, logo and link on the Number Hunt page and winners' post.</td></tr>
<tr><td><strong>Video sponsor</strong></td><td>A credit in a commissioned explainer and on the Videos page.</td></tr>
<tr><td><strong>Newsletter mention</strong></td><td>A short, labelled message in the weekly number email.</td></tr>
<tr><td><strong>Domain &amp; partnership</strong></td><td>Acquire, co-brand or partner on 36118.com itself.</td></tr>
</tbody></table>
<p>Pricing is quoted per placement based on current traffic. Ask for the media kit.</p>
<h2>Standards</h2>
<ul><li>All sponsored content is labelled.</li><li>No gambling, adult, weapons, deceptive financial or get-rich-quick offers.</li><li>We keep editorial independence: sponsors never change tool results or guide conclusions.</li></ul>
</div>
<div class="funnel"><h2 style="font-size:1.4rem">Request the media kit</h2>
<form data-form="Advertising inquiry" data-ok="Thanks. The media kit and rates are on their way.">
<input type="hidden" name="intent" value="Sponsor">
<div class="field"><label class="lbl" for="a-name">Name</label><input id="a-name" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label class="lbl" for="a-email">Work email</label><input id="a-email" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label class="lbl" for="a-co">Company and website</label><input id="a-co" type="text" name="company" required></div>
<div class="field"><label class="lbl" for="a-p">Interested in</label><select id="a-p" name="placement"><option>Tool sponsor</option><option>Guide sponsor</option><option>Contest prize partner</option><option>Video sponsor</option><option>Newsletter mention</option><option>Domain &amp; partnership</option><option>Not sure</option></select></div>
<div class="field"><label class="lbl" for="a-b">Monthly budget (USD)</label><select id="a-b" name="budget"><option>Not sure yet</option><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
<div class="field"><label class="lbl" for="a-m">Goals</label><textarea id="a-m" name="message"></textarea></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about advertising.</label>
<p style="margin-top:14px"><button class="btn btn-primary" type="submit">Send me the media kit</button></p>
</form></div></div></div>'''
    write("advertise.html", "Advertise and sponsor | 36118.com", "Sponsor a tool, guide, video, contest or newsletter on 36118.com, or partner on the domain itself.", body, schema=[cl], priority="0.6")

def support():
    c, cl = crumbs(0, [("Support us", None)])
    body = f'''<div class="wrap">{c}<div class="grid-2" style="align-items:start"><div class="prose">
<h1>Keep the tools free</h1>
<p>36118.com has no paywall and no sign-up. Advertising covers part of the cost; supporters cover the rest and let us move faster. You choose where your contribution goes.</p>
<h2>Where support goes</h2>
<ul>
<li><strong>Operations:</strong> hosting, data sources, security and maintenance.</li>
<li><strong>New tools and content:</strong> fees for writers, researchers and developers.</li>
<li><strong>Promotion and marketing:</strong> reaching students, founders and investors who need these tools.</li>
<li><strong>Contests and prizes:</strong> funding the Number Hunt prize pool.</li>
</ul>
<h2>Other ways to help</h2>
<ul><li>Share a tool with someone who would use it.</li><li>Link to a guide from your site or course.</li><li>Report an error or suggest a tool on the <a href="contact.html">contact page</a>.</li></ul>
<p class="small muted">Contributions are voluntary support for an independent website and are not tax-deductible charitable donations. Supporters who opt in are thanked on the site.</p>
</div>
<div class="funnel"><h2 style="font-size:1.4rem">Pledge your support</h2>
<div class="btns" style="margin-bottom:14px"><a class="btn btn-primary" data-pay="paypal" hidden href="#">Give with PayPal</a><a class="btn btn-primary" data-pay="stripe" hidden href="#">Give by card</a><a class="btn btn-primary" data-pay="coffee" hidden href="#">Buy us a coffee</a></div>
<form id="allocForm" data-form="Support pledge" data-ok="Thank you. We'll email a secure payment link within one business day.">
<fieldset style="border:0;padding:0;margin:0"><legend class="lbl">Amount (USD)</legend>
<div class="amounts"><label><input type="radio" name="amount" value="$5" required>$5</label><label><input type="radio" name="amount" value="$25" checked>$25</label><label><input type="radio" name="amount" value="$100">$100</label><label><input type="radio" name="amount" value="$500">$500</label><label><input type="radio" name="amount" value="Custom">Other</label></div></fieldset>
<div class="field" hidden><label class="lbl" for="customAmount">Your amount</label><input id="customAmount" type="number" name="custom_amount" min="1" step="1"></div>
<div class="field"><label class="lbl">Frequency</label><select name="frequency" aria-label="Frequency"><option>One time</option><option>Monthly</option></select></div>
<p class="lbl" style="margin-bottom:4px">Direct my support</p>
<div class="alloc"><label for="al1">Operations</label><input type="range" id="al1" data-label="Operations" min="0" max="10" value="4"><output id="al1Out"></output></div>
<div class="alloc"><label for="al2">Tools &amp; talent</label><input type="range" id="al2" data-label="Tools & talent" min="0" max="10" value="3"><output id="al2Out"></output></div>
<div class="alloc"><label for="al3">Promotion</label><input type="range" id="al3" data-label="Promotion" min="0" max="10" value="2"><output id="al3Out"></output></div>
<div class="alloc"><label for="al4">Contest prizes</label><input type="range" id="al4" data-label="Contest prizes" min="0" max="10" value="1"><output id="al4Out"></output></div>
<input type="hidden" id="allocSummary" name="allocation">
<div class="field" style="margin-top:12px"><label class="lbl" for="s-name">Name</label><input id="s-name" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label class="lbl" for="s-email">Email</label><input id="s-email" type="email" name="email" required autocomplete="email"></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters list.</label>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<p style="margin-top:14px"><button class="btn btn-primary" type="submit">Pledge support</button></p>
<p class="small muted">We reply with a secure payment link. We never ask for card details by email.</p>
</form></div></div></div>'''
    write("support.html", "Support 36118.com: keep the number tools free", "Support free number tools. Direct your contribution to operations, new tools and talent, promotion or contest prizes.", body, active="support", schema=[cl], priority="0.6")

def contests():
    c, cl = crumbs(0, [("Contests", None)])
    body = f'''<div class="wrap">{c}<div class="grid-2" style="align-items:start"><div class="prose">
<h1>Number Hunt</h1>
<p>Find the most surprising <em>true</em> fact about a number, and show how to check it. Each round has a theme, and the best entries are published with credit.</p>
<h2>How a round works</h2>
<ol><li>Read the current theme below.</li><li>Submit your number, your fact and a way to verify it (a calculation, source or tool link).</li><li>Judges score entries on accuracy (40%), surprise (30%), clarity (20%) and usefulness (10%).</li><li>Winners are announced on this page and contacted by email.</li></ol>
<div class="callout"><strong>Current theme: numbers that are also places.</strong> ZIP codes, PIN codes, area codes or postcodes with a story, like 36118. Entries close at the end of the month.</div>
<h2>Prizes</h2>
<p>Winners are featured on 36118.com with a link of their choice. Additional prizes for each round are funded by sponsors and supporters, and are listed here when the round opens. <a href="advertise.html">Become a prize partner</a> or <a href="support.html">fund the prize pool</a>.</p>
<h2>Official rules (summary)</h2>
<ul><li>No purchase or payment necessary. Void where prohibited.</li><li>Open to individuals who have reached the age of majority where they live.</li><li>One entry per person per round. Entries must be your own original work.</li><li>By entering you allow 36118.com to publish your entry with credit. You keep your copyright.</li><li>Judges' decisions are final. Prizes are not transferable, and winners are responsible for any taxes.</li><li>Personal data is used only to run the contest, as described in the <a href="privacy.html">privacy policy</a>.</li></ul>
</div>
<div class="funnel"><h2 style="font-size:1.4rem">Enter this round</h2>
<form data-form="Contest entry" data-ok="Entry received. Good luck — winners are announced on this page.">
<div class="field"><label class="lbl" for="c-n">Your number</label><input id="c-n" type="text" name="number" required></div>
<div class="field"><label class="lbl" for="c-f">The fact</label><textarea id="c-f" name="fact" required></textarea></div>
<div class="field"><label class="lbl" for="c-v">How to verify it</label><input id="c-v" type="text" name="verification" required placeholder="Source link or calculation"></div>
<div class="field"><label class="lbl" for="c-name">Name or handle to credit</label><input id="c-name" type="text" name="name" required></div>
<div class="field"><label class="lbl" for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I have read and accept the official rules.</label>
<p style="margin-top:14px"><button class="btn btn-primary" type="submit">Submit my entry</button></p>
</form></div></div></div>'''
    write("contests.html", "Number Hunt contest: find a surprising number fact | 36118.com", "Enter Number Hunt: submit the most surprising verifiable fact about a number. Winners are featured with sponsor-funded prizes.", body, schema=[cl], priority="0.6")

def careers():
    c, cl = crumbs(0, [("Careers", None)])
    roles = [("Contributing writer", "Explain numbers in business, culture, AI or geography in clear, sourced English. Paid per article."),
             ("Data researcher", "Verify facts, build datasets on postal codes and number markets, and keep tools accurate."),
             ("Front-end developer", "Build fast, accessible tools in plain HTML, CSS and JavaScript."),
             ("Video creator", "Script and produce short explainers for YouTube and social."),
             ("Community and contest moderator", "Run Number Hunt rounds, judge entries and answer readers.")]
    rl = "".join(f"<li><strong>{t}.</strong> {d}</li>" for t, d in roles)
    opts = "".join(f"<option>{t}</option>" for t, _ in roles)
    body = f'''<div class="wrap">{c}<div class="grid-2" style="align-items:start"><div class="prose">
<h1>Work with 36118.com</h1>
<p>We are a small, remote team building the clearest place on the web to understand numbers. Work is freelance and paid per project, with ongoing work for people who do it well.</p>
<h2>Open roles</h2><ul>{rl}</ul>
<h2>What we look for</h2><ul><li>Accuracy first, and the habit of showing your sources.</li><li>Plain writing and clean code.</li><li>Reliability on deadlines.</li></ul>
</div>
<div class="funnel"><h2 style="font-size:1.4rem">Apply</h2>
<form data-form="Job application" data-ok="Application received. We reply to every applicant within a week.">
<div class="field"><label class="lbl" for="j-r">Role</label><select id="j-r" name="role" required>{opts}</select></div>
<div class="field"><label class="lbl" for="j-n">Name</label><input id="j-n" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label class="lbl" for="j-e">Email</label><input id="j-e" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label class="lbl" for="j-p">Portfolio, GitHub or samples (link)</label><input id="j-p" type="url" name="portfolio" required placeholder="https://"></div>
<div class="field"><label class="lbl" for="j-m">Why you, in a few lines</label><textarea id="j-m" name="message" required></textarea></div>
<div class="field"><label class="lbl" for="j-rate">Expected rate (optional)</label><input id="j-rate" type="text" name="rate"></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that my application data may be stored to assess it.</label>
<p style="margin-top:14px"><button class="btn btn-primary" type="submit">Send application</button></p>
</form></div></div></div>'''
    write("careers.html", "Careers: writers, developers, researchers and creators | 36118.com", "Freelance roles at 36118.com for writers, data researchers, front-end developers, video creators and moderators.", body, schema=[cl], priority="0.5")

# -------------------------------------------------------------------------------------------- STATIC / LEGAL
def simple(path, title, desc, h1, inner, crumb, priority="0.4", noindex=False):
    c, cl = crumbs(0, [(crumb, None)])
    write(path, title, desc, f'<div class="wrap">{c}<div class="prose"><h1>{h1}</h1>{inner}</div></div>', schema=[cl], priority=priority, noindex=noindex)

def static_pages():
    simple("about.html", "About 36118.com", "Who runs 36118.com, what we build and how we keep tools accurate and free.", "About 36118.com", f'''
<p>36118.com is a free number-intelligence site. We build tools and guides that explain what a number is, mathematically, geographically, culturally and commercially, in plain language.</p>
<h2>Why a number?</h2><p>36118 is a real U.S. ZIP code, an even semiprime and a five-digit "chip" domain. That one number touches postal systems, mathematics, Chinese number culture and a traded asset class. The site extends that curiosity to any number you type.</p>
<h2>How we work</h2><ul><li><strong>Exact where possible.</strong> Mathematical properties are computed, not estimated.</li><li><strong>Labelled where cultural.</strong> Lucky-number readings are presented as cultural associations, never predictions.</li><li><strong>Sourced where factual.</strong> Guides draw on public records and reputable references, and we correct errors quickly.</li><li><strong>Private by default.</strong> Tools run in your browser; we do not store what you type.</li></ul>
<h2>Who we are</h2><p>36118.com is published by Webworks, an independent publisher of websites and online tools. Contributors are credited on their work.</p>
<h2>Corrections</h2><p>Spotted an error? <a href="contact.html">Tell us</a> and we will fix it.</p>''', "About", "0.5")
    simple("contact.html", "Contact 36118.com", "Contact 36118.com about tools, corrections, partnerships, advertising or the domain.", "Contact us", f'''
<p>Use the form for questions, corrections and ideas. For buying, selling or appraisal requests, the <a href="services.html">detailed form</a> gets you a faster answer. For interest in this website or domain, sponsorship, advertising or partnership, you can also use the <a href="{INTEREST_URL}" rel="noopener">Webworks contact page</a>.</p>
<form class="panel" data-form="Contact" data-ok="Message received. We reply within two business days.">
<div class="field"><label class="lbl" for="ct-topic">Topic</label><select id="ct-topic" name="intent"><option>General question</option><option>Correction</option><option>Tool idea</option><option>Partnership</option><option>Advertising</option><option>Domain inquiry</option><option>Privacy request</option></select></div>
<div class="field"><label class="lbl" for="ct-n">Name</label><input id="ct-n" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label class="lbl" for="ct-e">Email</label><input id="ct-e" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label class="lbl" for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my message.</label>
<p style="margin-top:14px"><button class="btn btn-primary" type="submit">Send message</button></p>
</form>
<p>Prefer email? <a href="#" data-mail="Message from 36118.com">Email us</a>.</p>''', "Contact", "0.5")

    simple("privacy.html", "Privacy policy | 36118.com", "How 36118.com collects, uses and protects information, including cookies and Google AdSense.", "Privacy policy", f'''
<p>Last updated {TODAY}. This policy explains what information 36118.com ("we") collects and how it is used.</p>
<h2>Information you give us</h2><p>When you submit a form (contact, lead, newsletter, contest, job application or support pledge) we receive what you enter, such as your name, email, phone and message. Forms are delivered to our private inbox through FormSubmit, a form-processing service. We use this information only to respond to you, run the activity you signed up for, and keep basic records. We do not sell personal information.</p>
<h2>Information our tools handle</h2><p>The number decoder, lucky-number reader and domain scorecard run entirely in your browser; what you type is not sent to us. The postal code explorer sends the code you enter to the Zippopotam.us API to retrieve place data, and the map loads tiles from OpenStreetMap.</p>
<h2>Cookies and advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the internet.</p>
<p>You may opt out of personalised advertising by visiting <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="noopener">aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">how Google uses information from sites that use its services</a>.</p>
<p>Visitors in the European Economic Area, the United Kingdom and Switzerland are shown a consent message, and personalised ads are served only with consent.</p>
<p>We also store small preferences in your browser (theme choice and cookie-notice dismissal). Embedded YouTube videos use the privacy-enhanced youtube-nocookie.com domain and load only when you press play.</p>
<h2>Retention and security</h2><p>We keep form messages only as long as needed for the purpose you sent them, and for up to 24 months for business records unless you ask us to delete them sooner. The site is served over HTTPS.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under GDPR, UK GDPR, CCPA/CPRA or PIPEDA) you may request access to, correction of or deletion of your personal information, or object to its use. Use the <a href="contact.html">contact form</a> and choose "Privacy request".</p>
<h2>Children</h2><p>The site is intended for a general audience and is not directed to children under 13. We do not knowingly collect their personal information.</p>
<h2>Changes</h2><p>We will post any changes here with a new date.</p>''', "Privacy policy", "0.3")

    simple("terms.html", "Terms of use | 36118.com", "The terms that apply when you use 36118.com and its tools.", "Terms of use", f'''
<p>Last updated {TODAY}. By using 36118.com you agree to these terms.</p>
<h2>Use of the site</h2><p>You may use the tools and read the guides for personal and commercial purposes. You may not scrape the site at a rate that degrades service, attempt to break its security, or use it for unlawful purposes.</p>
<h2>No professional advice</h2><p>Tool outputs and guides are for information only. Domain scores are not appraisals or offers. Cultural number readings are for interest and entertainment. Nothing on the site is financial, legal, tax or investment advice; consult a qualified professional before acting.</p>
<h2>Accuracy</h2><p>We work to keep information accurate, but postal data, market conditions and third-party data change. Information is provided "as is" without warranties of any kind.</p>
<h2>Intellectual property</h2><p>Site text, design and code are owned by 36118.com's publisher unless stated otherwise. You may quote short passages with a link back. Embedded videos and third-party data remain the property of their owners.</p>
<h2>User submissions</h2><p>When you submit a contest entry or other content, you confirm it is your own and grant us a non-exclusive licence to publish it with credit.</p>
<h2>Services and transactions</h2><p>Any appraisal, brokerage or sponsorship work is governed by a separate written agreement. Domain transactions must close through a licensed escrow service.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, we are not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Links</h2><p>We link to third-party sites for convenience and are not responsible for their content.</p>
<h2>Changes</h2><p>We may update these terms and will post the new date here.</p>''', "Terms of use", "0.3")

    simple("disclaimer.html", "Disclaimer, trademark and copyright notice | 36118.com", "Trademark, copyright, affiliation and accuracy disclosures for 36118.com.", "Disclaimer, trademark and copyright notice", f'''
<h2>Trademark disclosure</h2>
<p>"36118" is a number and a U.S. ZIP code. On this site it is used in its ordinary, descriptive sense. 36118.com does not claim trademark rights in the number 36118 and does not intend to suggest any connection with a third party that uses the same number as a postal code, model number, part number, product code or brand element.</p>
<p>36118.com is <strong>not affiliated with, endorsed by or sponsored by</strong> the United States Postal Service, the United States Air Force, Maxwell-Gunter Air Force Base, the City of Montgomery, the State of Alabama, or any manufacturer or business that uses "36118" in its products or names. ZIP Code is a trademark of the United States Postal Service and is used descriptively.</p>
<p>All other trademarks, service marks and trade names mentioned, including Google, AdSense, YouTube, PayPal, OpenStreetMap and 3Blue1Brown, belong to their respective owners and are used only to identify those products or services.</p>
<h2>Copyright notice</h2>
<p>The text, page designs, illustrations, interface and source code of 36118.com are original works © {datetime.date.today().year} 36118.com (a Webworks property). All rights reserved except where stated. Short quotations with attribution and a link are welcome.</p>
<p>Embedded videos are displayed through YouTube's official embed player and remain the property of their creators. Map tiles are © OpenStreetMap contributors. Postal place data is provided by Zippopotam.us from GeoNames sources.</p>
<p>If you believe content on this site infringes your rights, <a href="contact.html">contact us</a> with details and we will review it promptly.</p>
<h2>Estimates and cultural content</h2>
<p>Domain liquidity scores are model outputs, not appraisals, offers or guarantees of value. Lucky-number readings describe cultural associations for interest and entertainment and do not predict any outcome.</p>
<h2>Advertising and sponsorship</h2>
<p>This site displays ads served by Google AdSense and may include clearly labelled sponsorships. Advertisers do not influence tool results or editorial conclusions.</p>''', "Disclaimer", "0.3")

    # 404 (noindex)
    depth = 0
    out = head("Page not found | 36118.com", "That page does not exist.", "404.html", 0, [ORG], noindex=True) + header(0, None) + '''<main id="main"><div class="wrap prose" style="padding:60px 16px">
<h1>That page doesn't exist</h1><p>The link may be old or mistyped. Try a tool or the guides instead.</p>
<div class="btns"><a class="btn btn-primary" href="index.html">Go to the homepage</a></div>
<p class="small muted" style="margin-top:20px">Looking for a number? Type it into the <a href="tools/number-decoder.html">number decoder</a>.</p></div></main>''' + footer(0)
    # 404 can be served from any depth on Pages, so use absolute paths based on the site root at runtime
    out = out.replace("<head>", "<head>\n<script>document.write('<base href=\"' + (location.pathname.indexOf('/36118-com/') === 0 ? '/36118-com/' : '/') + '\">');</script>", 1)
    with open(os.path.join(ROOT, "404.html"), "w") as f: f.write(out)

def meta_files():
    urls = "".join(f"<url><loc>{SITE}/{'' if p == 'index.html' else p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>" for p, pr in PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, "ads.txt"), "w").write("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    open(os.path.join(ROOT, "site.webmanifest"), "w").write(json.dumps({"name": "36118.com", "short_name": "36118", "start_url": "./index.html",
        "display": "standalone", "background_color": "#F6F7F9", "theme_color": "#13233F",
        "icons": [{"src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "assets/img/favicon.svg", "type": "image/svg+xml", "sizes": "any"}]}, indent=1))

if __name__ == "__main__":
    home(); tools(); profile(); guides(); videos(); services(); advertise(); support(); contests(); careers(); static_pages(); meta_files()
    print("Built", len(PAGES), "indexable pages")

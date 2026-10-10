# Guide content for 36118.com. Each guide: slug, title, description, minutes, topic, body (HTML), faqs, optional video.
# Add a new dict to GUIDES and re-run `python3 _build/build.py` to publish another article.

GUIDES = [
{
"slug": "what-is-a-unique-zip-code",
"title": "What is a unique ZIP code? The story behind 36118",
"desc": "Unique ZIP codes belong to a single organisation, not a neighbourhood. Here is how they work, why 36118 has no residents, and what that means for data you find online.",
"minutes": 6, "topic": "ZIP codes",
"body": """
<p>Most people think of a ZIP code as an area on a map. That is true for the codes printed on household mail, but the U.S. Postal Service also assigns codes that have no neighbourhood at all. They are called <strong>unique ZIP codes</strong>, and 36118 is one of them.</p>
<h2>Four kinds of ZIP code</h2>
<p>The Postal Service sorts ZIP codes into four types:</p>
<ul>
<li><strong>Standard</strong> codes cover streets and delivery routes. These are the codes with population figures, home values and school districts.</li>
<li><strong>PO Box</strong> codes cover only post-office boxes inside a single facility.</li>
<li><strong>Unique</strong> codes are given to one high-volume address: a government agency, a university, a military installation, or a company that receives enough mail to justify its own sorting code.</li>
<li><strong>Military</strong> codes route mail to APO, FPO and DPO addresses overseas.</li>
</ul>
<h2>Where 36118 fits</h2>
<p>ZIP 36118 sits in Montgomery, Alabama, inside Montgomery County, and is classified as a unique code. Public ZIP directories associate it with the Gunter Annex area of Maxwell-Gunter Air Force Base, and some list former place names connected with the old Gunter Air Force Station. Because the code serves an institution rather than homes, demographic sites report its population, income and home value as zero. That is not missing data; there are simply no households on the code.</p>
<div class="callout">If you see a ZIP page full of zeros, check its type before drawing conclusions. A zero-population code is usually a unique or PO Box code, not an empty town.</div>
<h2>Why organisations get their own code</h2>
<p>A single address that receives tens of thousands of letters a day would overwhelm a normal carrier route. Giving it a dedicated code lets the mail be sorted straight to that organisation's own mailroom. State revenue departments, large universities, utility billing centres and bases are common examples. Montgomery alone has several unique codes because it is Alabama's capital and hosts state agencies and military facilities.</p>
<h2>What this means for data and marketing</h2>
<ul>
<li><strong>Demographic lookups fail.</strong> Census-style tables are built from residential geography, so unique codes return blanks. Tools that show them as poor or empty areas are misreading the data.</li>
<li><strong>Geocoding is approximate.</strong> Coordinates for a unique code usually point to the organisation's mail facility or the centre of the parent city.</li>
<li><strong>Lead lists need cleaning.</strong> If a CRM groups customers by ZIP, unique codes can make one employer look like a whole town. Tag them separately.</li>
<li><strong>Open datasets skip them.</strong> Free postal APIs often omit unique and PO Box codes, which is why our <a href="../tools/zip-explorer.html">ZIP explorer</a> suggests trying a neighbouring code such as 36117 when a unique code is not found.</li>
</ul>
<h2>The number itself</h2>
<p>Outside the mail system, 36118 is an even number equal to 2 × 18,059, where 18,059 is prime, so 36118 is a semiprime. In hexadecimal it is 8D16, and it contains neither a 0 nor a 4, which numeric-domain buyers call a "chip". The <a href="../the-number-36118.html">full profile of 36118</a> pulls these threads together.</p>
""",
"faqs": [
("Does anyone live in ZIP code 36118?", "Public directories report no residential population for 36118 because it is a unique code assigned to an institution rather than to households."),
("Can I use 36118 on a package?", "Only if the recipient's official mailing address uses it. Unique codes route to a specific organisation's mail facility."),
("How many ZIP codes are there?", "Directories count a little over 41,000 active U.S. ZIP codes, including standard, PO Box, unique and military types.")
]},

{
"slug": "how-us-zip-codes-work",
"title": "How U.S. ZIP codes work, digit by digit",
"desc": "What each digit in a ZIP code means, how ZIP+4 narrows delivery to a building face, and how businesses use postal geography for pricing, tax and marketing.",
"minutes": 7, "topic": "ZIP codes",
"body": """
<p>ZIP stands for Zone Improvement Plan. The five-digit system went live nationally in 1963, replacing a patchwork of two-digit city zones. Six decades later it underpins sales tax, insurance pricing, delivery promises and a good share of the world's marketing data.</p>
<h2>Reading the five digits</h2>
<ol>
<li><strong>First digit: the national area.</strong> The country is split into ten groups numbered 0 to 9, running roughly from the Northeast (0) to the West Coast, Alaska and Hawaii (9). Alabama falls in group 3, along with much of the Southeast.</li>
<li><strong>First three digits: the sectional centre.</strong> Together the first three digits identify a sectional centre facility, a large processing plant that serves a region. Codes beginning 361 are processed for the Montgomery area.</li>
<li><strong>Last two digits: the delivery area.</strong> These point to a specific post office or delivery zone inside that region.</li>
</ol>
<p>So 36118 reads as: Southeast group (3), Montgomery sectional centre (361), delivery code 18.</p>
<h2>ZIP+4</h2>
<p>Introduced in 1983, the four extra digits after the hyphen narrow delivery to a segment such as one side of a city block, a floor of an office building, or a large single recipient. Bulk mailers that pre-sort to ZIP+4 earn postage discounts because the machines have less work to do.</p>
<h2>Why ZIP codes are not boundaries</h2>
<p>A ZIP code is a set of delivery routes, not a polygon. Routes change when new subdivisions open, and a single code can cross city or even county lines. The Census Bureau publishes ZIP Code Tabulation Areas (ZCTAs) to approximate ZIP areas for statistics, but they are not identical to the postal codes. Anyone pricing insurance, setting delivery fees or drawing sales territories should know which of the two they are using.</p>
<h2>How businesses put ZIP codes to work</h2>
<ul>
<li><strong>Sales tax:</strong> local rates often vary within a ZIP, so tax engines use the full address, with ZIP as a first filter.</li>
<li><strong>Delivery promises:</strong> retailers estimate shipping times from origin and destination ZIP pairs.</li>
<li><strong>Territories:</strong> franchise agreements and sales teams split markets by ZIP lists because they are easy to administer.</li>
<li><strong>Audience targeting:</strong> ad platforms allow ZIP-level location targeting, and direct-mail campaigns are priced per ZIP route.</li>
</ul>
<h2>Try it</h2>
<p>Our <a href="../tools/zip-explorer.html">ZIP and postal code explorer</a> looks up place names and coordinates for U.S. codes and dozens of other countries, and measures the straight-line distance between any two codes.</p>
""",
"faqs": [
("What does the first digit of a ZIP code mean?", "It identifies one of ten national areas, numbered 0 in the Northeast through 9 on the West Coast and Pacific."),
("Is a ZIP code the same as a ZCTA?", "No. ZIP codes are mail delivery routes; ZCTAs are Census Bureau areas built to approximate them for statistics."),
("When were ZIP codes introduced?", "The national five-digit system started in 1963. ZIP+4 followed in 1983.")
]},

{
"slug": "chinese-lucky-numbers-in-business",
"title": "Chinese lucky numbers in business: 8, 6, 9 and the trouble with 4",
"desc": "Why digits carry commercial weight across Chinese-speaking markets, how it shows up in prices, phone numbers and plates, and how to read a number like 36118.",
"minutes": 7, "topic": "Numbers and culture",
"body": """
<p>In Mandarin and Cantonese many number words sound like other words. Over centuries those sound-alikes became associations, and in modern commerce they show up in prices, addresses, phone numbers, license plates and domain names. Ignoring them can quietly cost a business customers; using them well can make a brand easier to remember.</p>
<h2>The digits that matter most</h2>
<ul>
<li><strong>8 (bā)</strong> sounds close to <em>fā</em>, as in 发财, to prosper. It is the most sought-after digit. The Beijing Olympic Games opened on 8 August 2008 at 8:08 in the evening.</li>
<li><strong>6 (liù)</strong> suggests flowing smoothly. 66 and 666 are wished for in business, unlike the Western reading of 666.</li>
<li><strong>9 (jiǔ)</strong> sounds like 久, long-lasting, and is popular for weddings and partnerships.</li>
<li><strong>4 (sì)</strong> sounds like 死, death. Some buildings skip fourth floors, and many buyers avoid 4 in phone numbers or plates.</li>
<li><strong>3</strong> in Cantonese is close to the word for life or birth, so it reads positively in Hong Kong and southern China.</li>
</ul>
<h2>Combinations people look for</h2>
<p>Readers also pair digits. 168 can be read as "prosperity all the way", 518 as "I will prosper", and repeated 1s before an 8 (118) as "want, want, prosper". Combinations containing 14 or 514 are avoided because they can be read as wishing death. These readings vary by dialect and region, so treat them as tendencies rather than rules.</p>
<h2>Where it changes money</h2>
<ul>
<li><strong>Pricing:</strong> retailers in Chinese-speaking markets often end prices in 8 rather than 9.</li>
<li><strong>Phone numbers and plates:</strong> government auctions of vanity plates and carrier auctions of mobile numbers have produced headline prices for strings of 8s.</li>
<li><strong>Domain names:</strong> numeric .com names are popular in China because digits are easier to type and remember than romanised words. Names without 0 or 4, known as "chips", trade at a premium.</li>
<li><strong>Addresses:</strong> some developers renumber floors or units to avoid 4.</li>
</ul>
<h2>Reading 36118</h2>
<p>3 (life), 6 (smooth), 1-1 (want, want) and a final 8 (prosper), with no 4 or 0. On our model it scores 80 out of 100. You can score any number, from a price to a phone number, with the <a href="../tools/lucky-number.html">lucky-number reader</a>.</p>
<div class="callout">Cultural associations influence buyer preference, which is a market fact. They do not influence outcomes, which is why our tools report them as preferences, not predictions.</div>
""",
"faqs": [
("Why is 8 lucky in Chinese culture?", "Because bā sounds like fā, the word for prosperity, as in the New Year greeting 恭喜发财."),
("Should I avoid 4 in prices or phone numbers?", "If your customers include Chinese-speaking buyers, avoiding 4 removes a small but real friction. Elsewhere it makes little difference."),
("What is a chip number?", "A number with no 0 and no 4. In the numeric domain market, chip names are preferred by many Chinese end users.")
]},

{
"slug": "numeric-domain-names-explained",
"title": "Numeric domain names explained: 3N, 4N, 5N and chips",
"desc": "How the numeric domain market is organised, how scarce each length is, why Chinese demand shapes prices, and where a 5N.com like 36118.com sits.",
"minutes": 8, "topic": "Domains",
"body": """
<p>Numeric domains are names made only of digits, such as 888.com or 36118.com. Investors describe them by length: 2N for two digits, 3N for three, and so on. The class is simple to define, which makes it unusually easy to measure scarcity.</p>
<h2>Scarcity by length</h2>
<table class="facts"><thead><tr><th scope="col">Class</th><th scope="col">Possible .com names</th><th scope="col">Chips (no 0 or 4)</th></tr></thead><tbody>
<tr><th scope="row">2N</th><td>100</td><td>64</td></tr>
<tr><th scope="row">3N</th><td>1,000</td><td>512</td></tr>
<tr><th scope="row">4N</th><td>10,000</td><td>4,096</td></tr>
<tr><th scope="row">5N</th><td>100,000</td><td>32,768</td></tr>
<tr><th scope="row">6N</th><td>1,000,000</td><td>262,144</td></tr>
</tbody></table>
<p>Every extra digit multiplies supply by ten, while demand does not grow nearly as fast. That is why short numerics are among the most liquid domain assets: buyers can value them without debating meaning or branding.</p>
<h2>Why Chinese demand sets the tone</h2>
<p>Numbers are easier for many Chinese users to type and remember than romanised brand names, and several well-known Chinese internet companies have used numeric domains. As a result, Chinese preferences decide which numbers trade best. Names without 4 are preferred, names without 0 are cleaner, and 8 or 6 add appeal. The term "chip" (no 0, no 4) comes from that market.</p>
<h2>Patterns that add value</h2>
<ul>
<li>Repeated digits (88888) and repeated blocks (1818).</li>
<li>Palindromes (12321) and straight sequences (12345).</li>
<li>Meaningful combinations: lucky phrases, years, area codes or famous numbers.</li>
<li>No leading zero, which is easy to drop when typing.</li>
</ul>
<h2>Where 36118.com sits</h2>
<p>36118.com is a 5N chip ending in 8, with no 0 and no 4 and a doubled 1. It is not a repeating pattern, so it sits in the upper middle of the 5N class rather than at the top. Its second asset is meaning: it is a real U.S. ZIP code, which gives it a use case outside the domain market. Run any name through the <a href="../tools/domain-valuator.html">domain scorecard</a> to see the factor-by-factor breakdown.</p>
<h2>Buying and selling safely</h2>
<ul>
<li>Use an escrow service for any transfer; never send funds directly to a stranger.</li>
<li>Check the registrar lock status and the registration history before agreeing a price.</li>
<li>Expect most serious numeric buyers to ask for comparable sales. Have them ready.</li>
</ul>
<p>Thinking about buying or selling? <a href="../services.html?intent=Buy">Tell us what you need</a>.</p>
""",
"faqs": [
("How many 5-digit .com domains exist?", "100,000, from 00000.com to 99999.com. Of those, 32,768 contain no 0 and no 4."),
("Are numeric domains good investments?", "They are among the most liquid domain classes, but prices are cyclical and track Chinese market conditions. Treat them as a speculative asset."),
("Why do buyers avoid domains with 4?", "Because 4 sounds like the word for death in Mandarin and Cantonese, and many end users will not use it.")
]},

{
"slug": "how-to-value-a-numeric-domain",
"title": "How to value a domain name without fooling yourself",
"desc": "A practical framework for valuing numeric and keyword domains: liquidity versus end-user value, comparable sales, and the traps in automated appraisals.",
"minutes": 7, "topic": "Domains",
"body": """
<p>Every domain has two prices. The <strong>wholesale price</strong> is what another investor will pay quickly. The <strong>end-user price</strong> is what a business that needs the name will pay, which can be ten or more times higher but may take years to find. Most bad valuations come from mixing up the two.</p>
<h2>Step 1: place the name in its class</h2>
<p>For numerics, length and composition do most of the work: 3N above 4N above 5N, chips above names with 4, no leading zero, bonus for patterns. For word domains, the questions are length, extension, how common the words are, and whether businesses already spend money on them in advertising.</p>
<h2>Step 2: find comparable sales</h2>
<p>Look for public sales of names in the same class and extension within the last two or three years. One sale is an anecdote; five are a range. Prefer reported sales from marketplaces and industry sales charts over asking prices, which say nothing about what buyers actually paid.</p>
<h2>Step 3: adjust for liquidity</h2>
<p>How many buyers could plausibly want this name this year? A 3N.com has a deep pool of investor buyers. A two-word .net may have five potential end users in the world. The thinner the pool, the bigger the discount you should apply to any comparable.</p>
<h2>Step 4: check for legal and technical risk</h2>
<ul>
<li>Does the name match a registered trademark? If so, its resale value may be close to nothing, and holding it can create legal exposure.</li>
<li>Is the name on spam blocklists from previous use?</li>
<li>Is the registration history clean, with no disputes?</li>
</ul>
<h2>Why automated appraisals mislead</h2>
<p>Automated tools are useful for ranking names, but they often anchor to search volume and ignore liquidity. That is why our <a href="../tools/domain-valuator.html">domain scorecard</a> gives a liquidity score and shows every factor rather than producing a dollar figure. For a number you can act on, combine the score with real comparables, or <a href="../services.html?intent=Appraise">request a human appraisal</a>.</p>
<div class="callout">A useful test: if you would not accept your own estimate as an offer today, it is an end-user dream, not a valuation.</div>
""",
"faqs": [
("What is the difference between wholesale and retail domain value?", "Wholesale is what investors pay quickly; retail or end-user value is what a business that needs the name pays, usually after a longer search."),
("Are automated domain appraisals accurate?", "They are fine for ranking but unreliable as prices. Use comparable sales for anything you plan to act on."),
("How long does it take to sell a premium domain?", "It varies widely. Liquid classes like short numerics can sell within weeks at wholesale; end-user sales can take years.")
]},

{
"slug": "benfords-law-for-business",
"title": "Benford's law: the first-digit pattern that catches fraud",
"desc": "Why 1 is the leading digit about 30% of the time in real-world data, how auditors use it, and how to test your own numbers.",
"minutes": 6, "topic": "Numbers in business",
"body": """
<p>Take any large set of naturally occurring numbers, such as invoice totals, city populations or river lengths, and count how often each digit appears first. You might expect each of 1 through 9 to show up about 11% of the time. In practice, 1 leads about 30% of the time and 9 leads less than 5% of the time. This is Benford's law.</p>
<h2>The formula</h2>
<p>The expected share for leading digit <em>d</em> is log<sub>10</sub>(1 + 1/<em>d</em>).</p>
<table class="facts"><thead><tr><th scope="col">First digit</th><th scope="col">Expected share</th></tr></thead><tbody>
<tr><th scope="row">1</th><td>30.1%</td></tr><tr><th scope="row">2</th><td>17.6%</td></tr><tr><th scope="row">3</th><td>12.5%</td></tr>
<tr><th scope="row">4</th><td>9.7%</td></tr><tr><th scope="row">5</th><td>7.9%</td></tr><tr><th scope="row">6</th><td>6.7%</td></tr>
<tr><th scope="row">7</th><td>5.8%</td></tr><tr><th scope="row">8</th><td>5.1%</td></tr><tr><th scope="row">9</th><td>4.6%</td></tr>
</tbody></table>
<h2>Why it happens</h2>
<p>Quantities that grow multiplicatively, like prices, populations and revenues, spend longer with a leading 1 than with a leading 9. To go from 100 to 200 a value must double; to go from 900 to 1,000 it needs to grow only about 11%. Data that spans several orders of magnitude inherits this pattern.</p>
<h2>How auditors use it</h2>
<p>People who invent numbers tend to spread first digits evenly or favour mid-range digits. Forensic accountants compare a ledger's first-digit distribution with Benford's expectation; large deviations flag accounts for closer review. Tax authorities and election analysts have used the same idea. It is a screening test, not proof: some legitimate data, such as prices set just under a threshold or numbers with a fixed range, does not follow the law.</p>
<h2>When not to use it</h2>
<ul>
<li>Assigned numbers: phone numbers, ZIP codes, invoice IDs.</li>
<li>Data with a hard minimum or maximum, such as adult heights.</li>
<li>Small samples. Aim for at least several hundred values.</li>
</ul>
<p>Every result in the <a href="../tools/number-decoder.html">number decoder</a> notes the leading digit, a quick way to sanity-check individual figures.</p>
""",
"faqs": [
("What is Benford's law?", "The observation that in many real-world data sets the leading digit is 1 about 30% of the time, falling to under 5% for 9."),
("Can Benford's law prove fraud?", "No. It flags unusual distributions for review. Many legitimate data sets do not follow it."),
("Does Benford's law apply to ZIP codes?", "No. ZIP codes are assigned identifiers, not measured quantities.")
]},

{
"slug": "how-ai-reads-numbers",
"title": "How AI models read numbers, and why they sometimes get maths wrong",
"desc": "Tokenisation, pattern-matching and tool use: a plain-English look at how large language models handle digits, and how to get reliable numeric answers from them.",
"minutes": 7, "topic": "AI and numbers",
"body": """
<p>Large language models can explain calculus, yet occasionally fumble a long multiplication. The reason lies in how they see numbers in the first place.</p>
<h2>Numbers become tokens</h2>
<p>Before a model reads text, a tokenizer splits it into pieces called tokens. Common words are often single tokens; numbers are usually split into chunks of one to a few digits, depending on the tokenizer. The model never sees 36118 as a quantity. It sees a short sequence of symbols, much as it sees the letters of an unfamiliar word.</p>
<h2>Pattern-matching versus calculation</h2>
<p>A language model predicts the next token from patterns learned in training. For familiar facts and small sums those patterns are reliable. For long arithmetic, each digit depends on carries from other digits, and one wrong step propagates. Newer models are far better at this than early ones, but exact arithmetic is still a place where a calculator is the right tool.</p>
<h2>Why tool use fixes it</h2>
<p>Modern AI assistants can call tools: a code interpreter, a calculator, a database. When a model writes a short program to compute an answer and reads back the result, the arithmetic is done by ordinary software. That is the same principle behind our tools, which compute every property of a number exactly in your browser rather than estimating it.</p>
<h2>Numbers inside the model</h2>
<p>A neural network is itself made of numbers: weights, often counted in billions, that are multiplied and added in layer after layer. The videos below explain the mechanics clearly, without heavy maths.</p>
<h2>Getting reliable numbers from AI</h2>
<ul>
<li>Ask the assistant to compute with code or a calculator when exactness matters.</li>
<li>Ask for intermediate steps; errors are easier to spot.</li>
<li>Check headline figures against a primary source, especially statistics and prices that change over time.</li>
<li>Be explicit about units, currencies and dates.</li>
</ul>
""",
"faqs": [
("Why do AI chatbots make arithmetic mistakes?", "Language models predict text from patterns and see numbers as token sequences, so long exact calculations can go wrong unless the model uses a calculator or code tool."),
("What is a token?", "A chunk of text, such as a word, part of a word or a few digits, that a language model processes as one unit."),
("How can I get accurate maths from an AI assistant?", "Ask it to use a code or calculator tool and to show its steps, then verify key results.")
],
"video": ("aircAruvnKk", "But what is a neural network? (3Blue1Brown)")
},

{
"slug": "reading-economic-numbers",
"title": "Reading economic numbers: percent, basis points, real versus nominal",
"desc": "A field guide to the numbers in business news: percentage points, basis points, inflation-adjusted figures, annualised rates and the rule of 72.",
"minutes": 7, "topic": "Numbers in business",
"body": """
<p>Economic headlines compress a lot of maths into a few words. Misreading one term can flip the meaning of a story. Here are the ones that trip people up most.</p>
<h2>Percent versus percentage points</h2>
<p>If an interest rate rises from 4% to 5%, it has risen by one <strong>percentage point</strong>, which is a 25% <strong>increase</strong> in the rate. Both statements are true; they answer different questions. Good reporting says which one it means.</p>
<h2>Basis points</h2>
<p>A basis point is one hundredth of a percentage point, or 0.01%. A central bank that raises rates by 25 basis points has added a quarter of a percentage point. Bond traders use basis points because small moves matter on large sums.</p>
<h2>Nominal versus real</h2>
<p>Nominal figures are in today's money. Real figures are adjusted for inflation. If wages rose 4% while prices rose 3%, real wages rose roughly 1%. When comparing values across years, always ask which one you are looking at.</p>
<h2>Annualised rates</h2>
<p>Quarterly growth figures are often reported at an annualised rate, meaning what the year would look like if the quarter's pace continued. A 0.5% quarterly rise annualises to roughly 2%. Some countries report quarter-on-quarter figures without annualising, which makes international comparisons tricky.</p>
<h2>The rule of 72</h2>
<p>Divide 72 by an annual growth rate to estimate how many years it takes to double. At 6% a year, money doubles in about 12 years; at 9%, about 8. The rule works because 72 has many divisors and approximates 100 × ln 2 with a small correction.</p>
<h2>Big numbers</h2>
<p>A million seconds is about 11.6 days; a billion seconds is about 31.7 years. When a story jumps from millions to billions, it is jumping a thousandfold. Converting to per-person figures (divide by population) often makes large totals easier to judge.</p>
<p>Want to see a figure written out in words or scientific notation? Paste it into the <a href="../tools/number-decoder.html">number decoder</a>.</p>
""",
"faqs": [
("What is a basis point?", "One hundredth of one percentage point, or 0.01%. 100 basis points equal 1 percentage point."),
("What is the rule of 72?", "A shortcut for doubling time: divide 72 by the annual growth rate in percent to estimate the number of years."),
("What is the difference between real and nominal?", "Nominal values are in current money; real values remove the effect of inflation.")
]},

{
"slug": "prime-numbers-and-encryption",
"title": "Prime numbers and encryption: why 36118 = 2 × 18,059 matters",
"desc": "How multiplying two primes is easy but splitting the product is hard, and how that asymmetry protects online payments and messages.",
"minutes": 6, "topic": "Number science",
"body": """
<p>A prime number has exactly two divisors: 1 and itself. Every whole number above 1 can be written as a product of primes in exactly one way. That simple fact, called the fundamental theorem of arithmetic, sits underneath much of the internet's security.</p>
<h2>A small example</h2>
<p>36118 factors as 2 × 18,059, and 18,059 is prime. A number with exactly two prime factors is called a <strong>semiprime</strong>. Finding those factors is quick here because one of them is 2. Now imagine both factors were primes hundreds of digits long.</p>
<h2>The asymmetry</h2>
<p>Multiplying two large primes takes a computer a fraction of a second. Recovering them from the product, with no other information, is believed to take classical computers an impractically long time once the numbers are large enough. RSA encryption, introduced in 1977, is built on that gap: the public key contains the product, and only the holder of the private key knows the factors.</p>
<h2>How big is big enough?</h2>
<p>RSA keys of 2048 bits, numbers with about 617 decimal digits, are a common baseline today. Many systems now prefer elliptic-curve cryptography, which offers similar security with shorter keys. Researchers are also standardising post-quantum algorithms, because a large enough quantum computer could factor semiprimes efficiently.</p>
<h2>Primes are everywhere else too</h2>
<ul>
<li>Hash tables often use prime sizes to spread data evenly.</li>
<li>Cicadas in parts of North America emerge in 13- and 17-year cycles.</li>
<li>Primes thin out slowly: among numbers near 36,000, roughly one in ten is prime.</li>
</ul>
<p>The video below shows a beautiful pattern that appears when primes are plotted in polar coordinates. To factor your own number, use the <a href="../tools/number-decoder.html">number decoder</a>.</p>
""",
"faqs": [
("Is 36118 a prime number?", "No. 36118 = 2 × 18,059. Because 18,059 is prime, 36118 is a semiprime."),
("Why are primes important for encryption?", "Multiplying two large primes is easy, but factoring their product is very hard, which lets public-key systems like RSA keep private keys secret."),
("What is the next prime after 36118?", "36131. The previous prime is 36109.")
],
"video": ("EK32jo7i5LQ", "Why do prime numbers make these spirals? (3Blue1Brown)")
},

{
"slug": "binary-hex-and-number-bases",
"title": "Binary, hex and other bases: one number, many spellings",
"desc": "How positional number systems work, why computers use binary and hexadecimal, and how to convert 36118 to base 2, 8, 16 and 36 by hand.",
"minutes": 6, "topic": "Number science",
"body": """
<p>36118 is a quantity. "36118" is one way to write it, using base 10. Change the base and the same quantity gets a different spelling.</p>
<h2>How a base works</h2>
<p>In base 10 each position is worth ten times the one to its right: 36118 means 3×10,000 + 6×1,000 + 1×100 + 1×10 + 8×1. In base 2 each position is worth twice the one to its right; in base 16, sixteen times.</p>
<h2>36118 in other bases</h2>
<table class="facts"><tbody>
<tr><th scope="row">Base 2 (binary)</th><td>1000110100010110</td></tr>
<tr><th scope="row">Base 8 (octal)</th><td>106426</td></tr>
<tr><th scope="row">Base 16 (hexadecimal)</th><td>8D16</td></tr>
<tr><th scope="row">Base 36</th><td>RVA</td></tr>
</tbody></table>
<h2>Converting by hand</h2>
<p>Divide by the base, write down the remainder, and repeat with the quotient until it reaches zero. Reading the remainders from last to first gives the answer. For hexadecimal: 36118 ÷ 16 = 2257 remainder 6; 2257 ÷ 16 = 141 remainder 1; 141 ÷ 16 = 8 remainder 13 (D); 8 ÷ 16 = 0 remainder 8. Reading upward: 8D16.</p>
<h2>Why computers love binary and hex</h2>
<p>Electronic circuits are reliable at telling two states apart, so binary is natural for hardware. Hexadecimal is a compact shorthand: each hex digit stands for exactly four binary digits, so 8D16 maps to 1000 1101 0001 0110. That is why colours (#13233F), memory addresses and file signatures are written in hex.</p>
<h2>Base 36 and short links</h2>
<p>Base 36 uses 0–9 and A–Z. It packs numbers into short, case-insensitive strings, which is why it turns up in URL shorteners and order codes.</p>
<p>The <a href="../tools/number-decoder.html">number decoder</a> converts any number up to 15 digits into all four bases instantly.</p>
""",
"faqs": [
("What is 36118 in binary?", "1000110100010110."),
("What is 36118 in hexadecimal?", "8D16."),
("Why do programmers use hexadecimal?", "Each hex digit maps to exactly four bits, so long binary values become short and readable.")
]},

{
"slug": "choosing-a-business-phone-number",
"title": "Choosing a business phone number people remember",
"desc": "Local versus toll-free, vanity numbers, memorable digit patterns and cultural preferences: how to pick a number that gets dialled.",
"minutes": 6, "topic": "Numbers in business",
"body": """
<p>A phone number is one of the few brand assets people have to memorise exactly. A good one raises call-back rates from ads, radio and vehicle signage; a forgettable one leaks leads you paid for.</p>
<h2>Local or toll-free?</h2>
<ul>
<li><strong>Local numbers</strong> signal a real presence in a community and tend to suit trades, clinics and shops.</li>
<li><strong>Toll-free numbers</strong> in North America use prefixes 800, 833, 844, 855, 866, 877 and 888. They suit national brands and support lines. 800 is the most recognised.</li>
</ul>
<h2>Vanity numbers</h2>
<p>A vanity number spells a word on the keypad, such as 1-800-FLOWERS. They are easy to remember from a billboard but slower to dial from a smartphone, and the best words are long gone. Many businesses advertise the word and print the digits beside it.</p>
<h2>Patterns that stick</h2>
<ul>
<li>Repeated digits: 777-7777, or a repeated block like 2020.</li>
<li>Round endings: numbers ending 000 or 100.</li>
<li>Short chunks: people remember groups of three or four digits.</li>
<li>Meaningful numbers: a founding year or a well-known local number.</li>
</ul>
<h2>Cultural preferences</h2>
<p>If your customers include Chinese-speaking communities, numbers with 8 or 6 are welcome and numbers with 4 are a small negative. The <a href="../tools/lucky-number.html">lucky-number reader</a> scores both cultural associations and memorability.</p>
<h2>Test before you commit</h2>
<p>Show three candidate numbers to five people for five seconds, then ask them to write each down an hour later. The one most people recall correctly wins.</p>
<p>Need a strategy for numbers across phone, domain and branding? <a href="../services.html?intent=Strategy">Ask us</a>.</p>
""",
"faqs": [
("Which toll-free prefixes exist in North America?", "800, 833, 844, 855, 866, 877 and 888."),
("Are vanity numbers still worth it?", "For broadcast and outdoor advertising, yes. For digital-only businesses, a short, patterned number is often more practical."),
("How do I test if a number is memorable?", "Show candidates briefly, wait an hour, and see which one people recall accurately.")
]},

{
"slug": "numerology-vs-number-science",
"title": "Numerology versus number science: enjoy one, rely on the other",
"desc": "Digital roots, angel numbers and life-path numbers explained honestly, alongside the measurable properties that actually matter in business and computing.",
"minutes": 5, "topic": "Numbers and culture",
"body": """
<p>Searches for number meanings are enormous, from angel numbers to life-path calculations. It helps to separate two kinds of meaning: the stories people attach to numbers, and the properties numbers actually have.</p>
<h2>What numerology does</h2>
<p>Most Western numerology reduces a number to a single digit by adding its digits repeatedly. 36118 becomes 3+6+1+1+8 = 19, then 1+9 = 10, then 1+0 = 1. That final figure is called the digital root, and numerology assigns each root a personality: 1 for leadership and beginnings, 8 for material success, and so on. Angel-number readings apply similar ideas to repeated sequences like 111 or 888.</p>
<h2>What number science does</h2>
<p>Number theory asks testable questions. Is the number prime? What are its divisors? Is it a square, a Fibonacci number, a palindrome? These answers are the same for everyone, everywhere, and they matter in practice: primes secure encryption, divisibility drives scheduling and packaging, and digit patterns affect how memorable a number is.</p>
<h2>Where they meet</h2>
<p>The digital root is a real mathematical tool: it equals the remainder when a number is divided by 9 (with 9 in place of 0), which is why "casting out nines" was used for centuries to check arithmetic. And cultural meaning, whether Western numerology or Chinese homophones, genuinely influences what people choose to buy, which makes it a market fact even though it does not predict anything.</p>
<h2>Our approach</h2>
<p>On 36118.com, cultural readings are clearly labelled as cultural and offered for interest. Mathematical facts are computed exactly. Try both on any number with the <a href="../tools/number-decoder.html">number decoder</a> and the <a href="../tools/lucky-number.html">lucky-number reader</a>.</p>
""",
"faqs": [
("What is the digital root of 36118?", "1. The digits sum to 19, then 1 + 9 = 10, then 1 + 0 = 1."),
("Is numerology scientific?", "No. It is a cultural and spiritual practice. The digital root it uses, however, has a real arithmetic meaning."),
("What are angel numbers?", "Repeated number sequences, such as 111 or 444, that some people interpret as spiritual messages. The interpretations are cultural, not mathematical.")
]},
]

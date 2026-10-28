"""
Mock data for the Kopi Kaki Co. scenario — the single fictional company that
runs through all ten labs (Day 1 Hermes Agent, Day 2 Paperclip).

Every file here is SYNTHETIC: the company, people, outlets, reviews, comments,
metrics and competitors are invented for training. Deterministic (seeded) so a
rebuild produces identical files.

FILES maps a logical name -> (relative filename, content-producing function).
build_labs.py copies the files each lab lists into labs/labNN-*/data/.
"""
import csv, io, random, datetime as dt

SEED = 20261118
COMPANY = "Kopi Kaki Co."
LAUNCH = "Gula Melaka Cold Brew"
OUTLETS = ["Tiong Bahru", "Tanjong Pagar", "Raffles Place", "Jurong East", "Punggol", "Paya Lebar",
           "Bishan", "Clementi", "Tampines", "Woodlands", "Holland Village", "Changi Airport T3"]

def _csv(rows, header):
    b = io.StringIO(); w = csv.writer(b, lineterminator="\n"); w.writerow(header); w.writerows(rows)
    return b.getvalue()

# ------------------------------------------------------------------ company context
def agents_md():
    return f"""# AGENTS.md — Kopi Kaki Co. workspace context

> Hermes Agent loads this file automatically when you start it inside this folder.
> It tells every agent who the company is, what the current campaign is and the rules.
> All company data in this workspace is fictional training data.

## Who we are
- **{COMPANY}** — a Singapore specialty kopi chain, founded 2019, 12 outlets, ~140 staff.
- Positioning: *Heritage kopi, modern craft.* Traditional Nanyang roasting, third-wave care.
- Customers: office workers 25–40 (weekday mornings), students 18–24 (afternoons), families (weekends).
- Channels we post on: Instagram, TikTok, Facebook, LinkedIn (corporate news only), Telegram broadcast channel.

## Current priority — the {LAUNCH} launch
- Launch date **1 Dec 2026**. Campaign window **17 Nov – 14 Dec 2026**. Hashtag **#ShiokColdBrew**.
- Budget SGD 15,000. KPIs: 2,500 app pre-orders · 8% average engagement rate · 40,000 short-video views.
- Read `campaign-brief.md` for the full brief and `brand-guide.md` before writing anything public.

## Rules every agent must follow
1. Follow `brand-guide.md` (voice, colours, words to avoid).
2. Check every public draft against `compliance-rules.md`. If unsure — **stop and ask the human**.
3. Never publish, send or post anything public without a human APPROVE.
4. Never invent prices, promotions, outlet hours or awards — use `product-catalogue.csv` and the brief.
5. Never include customers' personal data (names, phone numbers, emails) in any output.
6. Save work to `outputs/` using the file names the task asks for.
"""

def brand_guide():
    return f"""# Kopi Kaki Co. — Brand Guide (v3, Oct 2026)

## Brand idea
**Heritage kopi, modern craft.** We bring the kopitiam's warmth to a modern café: Nanyang-roasted beans,
slow-brewed, served with a smile. "Kaki" means buddy — every customer is a kopi kaki.

## Voice
| We are | We are not |
|---|---|
| Warm, neighbourly, upbeat | Loud, pushy, salesy |
| Light local flavour ("shiok", "kopi kaki") — max one Singlish word per post | Heavy Singlish or slang that excludes non-locals |
| Short sentences, sensory words (aroma, smooth, caramel) | Jargon, ALL CAPS, more than 2 emojis per post |
| Proud of heritage | Mocking other brands or cultures |

## Visual identity
- Kopi Brown `#5B3A29` · Pandan Green `#4E8A3E` · Condensed-Milk Cream `#F6EBD9` · Gula Melaka Amber `#C7782A`
- Typeface: rounded sans for headlines; logo always on cream or brown, never on busy photos.
- Photography: natural light, hands holding cups, kopitiam tiles, real outlets — no stock models.

## Words we love / avoid
- Love: shiok, kopi kaki, slow-brewed, smooth, kopitiam, heritage, craft, share a cup
- Avoid: "healthy", "boosts energy", "cure", "best in Singapore", "cheapest", competitor names

## Platform formats
| Platform | Format | Length |
|---|---|---|
| Instagram | 1:1 or 4:5 image, carousel, Reels 9:16 | Caption ≤ 125 words, 3–5 hashtags |
| TikTok | 9:16 video 15–30 s, hook in first 2 s | Caption ≤ 150 characters |
| Facebook | 1.91:1 image or video | ≤ 80 words, 1 link |
| LinkedIn | Corporate/people stories only | ≤ 150 words, no promo codes |
| Telegram channel | Image + short text | ≤ 60 words |
"""

def campaign_brief():
    return f"""# Campaign Brief — {LAUNCH} (#ShiokColdBrew)

**Owner:** Marketing Lead (human) · **Prepared:** 3 Nov 2026 · **Status:** Approved for planning

## The product
- **{LAUNCH}** — Nanyang-roast coffee steeped 12 hours, finished with gula melaka (palm sugar) syrup and
  coconut cream. Oat-milk option. Served over ice.
- Price: **SGD 6.80** (regular) · **SGD 7.80** (large) · available at all 12 outlets and the Kopi Kaki app from **1 Dec 2026**.

## Objectives & KPIs
| Objective | KPI | Target |
|---|---|---|
| Drive trial | App pre-orders 17 Nov – 30 Nov | 2,500 |
| Build buzz | Average engagement rate (IG + TikTok) | ≥ 8% |
| Reach | Short-video views (TikTok + Reels) | 40,000 |
| Loyalty | New app sign-ups | 1,200 |

## Audience
1. **Office kaki** (25–40) — want a smooth afternoon pick-me-up near the CBD outlets.
2. **Student kaki** (18–24) — share-worthy drinks, value, TikTok.

## Key message
*A taste of the kopitiam, slow-brewed cold.* Support points: 12-hour cold brew · real gula melaka · coconut cream.

## Offer (exact — do not change)
- Promo code **SHIOK20** — 20% off the first {LAUNCH} ordered in the app, valid **1–14 Dec 2026**, one per customer.
- Pre-order in app from 17 Nov; collect from 1 Dec.

## Budget — SGD 15,000
Paid social 9,000 · Creator collaborations 3,500 · Production 1,500 · Contingency 1,000

## Timeline
| Phase | Dates |
|---|---|
| Teaser | 17–23 Nov |
| Pre-order push | 24–30 Nov |
| Launch | 1–7 Dec |
| Sustain | 8–14 Dec |

## Mandatory
- Every public post must be approved by the Marketing Lead (human) before it goes live.
- Follow `brand-guide.md` and `compliance-rules.md`.
"""

def compliance_rules():
    return """# Compliance & Brand-Safety Rules (the Auditor's checklist)

Use this list to PASS / FAIL every public draft. One FAIL = the draft goes back for changes.

| # | Rule | Fail example |
|---|---|---|
| C1 | No health or medical claims (Singapore advertising code) | "boosts your energy", "healthy choice", "good for digestion" |
| C2 | Prices and promotions exactly match the brief | "SHIOK25", "30% off", "free drink" |
| C3 | Promo terms stated when a code is shown: "valid 1–14 Dec, first app order, one per customer" | Code shown without terms |
| C4 | **No halal claim** — halal certification is still pending | "halal", "Muslim-friendly" |
| C5 | No comparative or disparaging claims about competitors | "better than Starbucks", "best in Singapore" |
| C6 | No customer personal data (PDPA) | names, phone numbers, emails, faces of customers without consent |
| C7 | Brand voice: max 1 Singlish word, max 2 emojis, no ALL CAPS words | "SUPER SHIOK LAH 🔥🔥🔥" |
| C8 | Alcohol-free, kid-safe; no references to alcohol or gambling | "cocktail vibes", "bet you can't…" |
| C9 | AI-generated visuals or voices are disclosed in the caption or description | Undisclosed AI voice-over |
| C10 | Every claim has a source in the brief or product catalogue | "Award-winning" (no award exists) |

**Escalate to the human immediately** for: legal threats, food-safety complaints, allergic reactions,
media enquiries, any request for a refund above SGD 20, or anything you are unsure about.
"""

def product_catalogue():
    rows = [
        ("KK-01", "Kopi O", "Hot coffee", 2.20, "Black Nanyang-roast kopi with sugar", "core"),
        ("KK-02", "Kopi C", "Hot coffee", 2.50, "Kopi with evaporated milk and sugar", "core"),
        ("KK-03", "Kopi (classic)", "Hot coffee", 2.50, "Kopi with condensed milk", "core"),
        ("KK-04", "Kopi Peng", "Iced coffee", 3.20, "Iced kopi with condensed milk", "core"),
        ("KK-05", "Teh Tarik", "Tea", 2.80, "Pulled milk tea", "core"),
        ("KK-06", "Pandan Latte", "Specialty", 5.80, "Espresso, pandan syrup, fresh milk", "specialty"),
        ("KK-07", "Kaya Toast Set", "Food", 5.50, "Kaya toast, 2 soft-boiled eggs, kopi or teh", "food"),
        ("KK-08", "Nanyang Cold Brew", "Specialty", 5.80, "12-hour cold brew, black", "specialty"),
        ("KK-09", LAUNCH, "Specialty", 6.80, "12-hour cold brew, gula melaka syrup, coconut cream; oat option", "launch 1 Dec 2026"),
        ("KK-09L", LAUNCH + " (Large)", "Specialty", 7.80, "Large size of KK-09", "launch 1 Dec 2026"),
        ("KK-10", "Ondeh Ondeh Cake", "Food", 4.80, "Pandan sponge, gula melaka, coconut", "food"),
        ("KK-11", "Kopi Beans 250g", "Retail", 18.00, "Nanyang-roast whole beans", "retail"),
    ]
    return _csv(rows, ["sku", "name", "category", "price_sgd", "description", "status"])

def competitors():
    rows = [
        ("Brew & Bloom", "Specialty café chain", 18, "6.50–8.00", "Cold brew flights; strong Instagram aesthetic", "Launched yuzu cold brew Sep 2026"),
        ("Kopi Corner", "Heritage kopitiam brand", 40, "1.80–4.50", "Price leader; huge outlet network", "Weak on social; no app"),
        ("Bean Theory", "Third-wave roaster", 5, "6.00–9.00", "Single-origin focus; barista creators on TikTok", "Runs monthly latte-art challenges"),
        ("Daily Grind SG", "Office-tower kiosks", 22, "4.50–6.50", "Speed + app ordering in CBD", "App points promo every Friday"),
        ("Siang Lim Coffee", "Old-school roaster", 3, "2.00–5.00", "Nostalgia, family-run story", "Viral 2025 documentary"),
        ("Matcha & Co", "Tea-forward café", 9, "6.00–8.50", "Seasonal drinks, students", "Student 1-for-1 Tuesdays"),
    ]
    return _csv(rows, ["competitor (fictional)", "type", "outlets", "price_range_sgd", "strength", "recent_activity"])

_REVIEW_BITS = {
    5: ["Smooth kopi, just like my grandfather's kopitiam.", "Pandan latte is shiok!", "Friendly staff, fast queue at Raffles Place.",
        "Love the cold brew, not too sweet.", "Kaya toast set is perfect for breakfast.", "Great aroma, cosy outlet."],
    4: ["Good kopi but the queue at lunch is long.", "Nice cold brew, wish there was a large size.", "Tasty, slightly pricey vs kopitiam.",
        "App ordering works well, pickup was quick.", "Would love more oat milk options."],
    3: ["Kopi was okay, a bit too sweet today.", "Seats are limited at Tiong Bahru.", "Average, prefer the old menu.",
        "Cold brew tasted watery once."],
    2: ["Waited 20 minutes for an app order.", "Drink was lukewarm.", "Staff forgot my oat milk."],
    1: ["Found the cup leaking, nobody responded to my email.", "App charged me twice and no refund yet."],
}

def customer_reviews():
    rnd = random.Random(SEED)
    rows = []; d0 = dt.date(2026, 8, 1)
    weights = [(5, 30), (4, 18), (3, 7), (2, 4), (1, 3)]
    pool = [r for r, w in weights for _ in range(w)]
    for i in range(60):
        r = rnd.choice(pool); txt = rnd.choice(_REVIEW_BITS[r])
        rows.append((f"R{1001+i}", (d0 + dt.timedelta(days=rnd.randint(0, 80))).isoformat(), rnd.choice(OUTLETS),
                     rnd.choice(["Google", "App", "Instagram", "Facebook"]), r, txt))
    rows.sort(key=lambda x: x[1])
    return _csv(rows, ["review_id", "date", "outlet", "source", "rating", "text"])

def social_comments():
    rows = [
        ("C01", "instagram", "@kopi_lover88", "When can I order the gula melaka one?? 😍", "question"),
        ("C02", "tiktok", "@jiaxin.eats", "Is it very sweet? I take less sugar", "question"),
        ("C03", "facebook", "Mr Tan", "Is the cold brew halal?", "question-sensitive"),
        ("C04", "instagram", "@ravi.runs", "Does it come with oat milk?", "question"),
        ("C05", "instagram", "@sgfoodhunter", "Looks shiok! Tagging @mel_lim", "praise"),
        ("C06", "facebook", "Angela W", "My drink yesterday at Bishan had a plastic piece inside. Very disappointed. Call me at 9123 4567.", "complaint-food-safety"),
        ("C07", "tiktok", "@cheapcoffee_bot", "Get 1000 followers FREE click my bio", "spam"),
        ("C08", "instagram", "@marcus.k", "Is SHIOK20 usable for the large size?", "question"),
        ("C09", "facebook", "Daniel Ong", "App charged me twice for a $6.80 order. Please refund.", "complaint-billing"),
        ("C10", "tiktok", "@nightowl", "Which outlets open before 7am?", "question"),
        ("C11", "instagram", "@straitsfoodie", "Hi, I'm a journalist with a food magazine — can I interview your founder?", "media-enquiry"),
        ("C12", "instagram", "@amy.bakes", "The ondeh ondeh cake + cold brew combo please!!", "praise"),
        ("C13", "facebook", "Lim KH", "Your coffee is worse than Kopi Corner, overpriced", "negative-competitor"),
        ("C14", "tiktok", "@studentkaki", "Any student discount?", "question"),
        ("C15", "instagram", "@fitjoanne", "Is it healthy? Can I drink it after gym?", "question-health"),
        ("C16", "facebook", "Priya S", "I had an allergic reaction after the coconut drink, what's inside?", "complaint-allergy"),
        ("C17", "instagram", "@kopi_kaki_fan", "Been a fan since Tiong Bahru opened! 🧡", "praise"),
        ("C18", "tiktok", "@lawyerly", "You used my photo without permission. Remove it or I will take legal action.", "legal-threat"),
        ("C19", "instagram", "@hungry.hippo", "Delivery on Grab?", "question"),
        ("C20", "facebook", "Jason Teo", "Changi T3 outlet staff were super helpful 👍", "praise"),
    ]
    return _csv(rows, ["comment_id", "platform", "author_handle", "comment", "category_hint"])

def week1_metrics():
    rnd = random.Random(SEED + 1)
    posts = [("P01", "instagram", "image", "Teaser: something cold is brewing"), ("P02", "tiktok", "video", "POV: 12 hours of cold brew in 15 s"),
             ("P03", "facebook", "image", "Countdown: 14 days to launch"), ("P04", "instagram", "reel", "Barista pours gula melaka"),
             ("P05", "tiktok", "video", "Taste test with office kaki"), ("P06", "instagram", "carousel", "How we brew: 4 steps"),
             ("P07", "facebook", "video", "Founder story: grandfather's kopitiam"), ("P08", "tiktok", "video", "Guess the secret ingredient"),
             ("P09", "instagram", "image", "Pre-order now in the app"), ("P10", "linkedin", "image", "Meet our roasting team"),
             ("P11", "tiktok", "video", "Student kaki react"), ("P12", "instagram", "reel", "Kopitiam tiles ASMR")]
    rows = []; d = dt.date(2026, 11, 17)
    for i, (pid, plat, fmt, title) in enumerate(posts):
        base = {"tiktok": 9000, "instagram": 4200, "facebook": 2500, "linkedin": 1200}[plat]
        if fmt in ("video", "reel"): base *= 1.6
        reach = int(base * rnd.uniform(0.6, 1.5)); views = int(reach * rnd.uniform(1.1, 1.8)) if fmt in ("video", "reel") else 0
        eng_rate = rnd.uniform(0.025, 0.12) if plat != "linkedin" else rnd.uniform(0.01, 0.04)
        likes = int(reach * eng_rate * 0.75); comments = int(reach * eng_rate * 0.1); shares = int(reach * eng_rate * 0.15)
        clicks = int(reach * rnd.uniform(0.004, 0.025)); preorders = int(clicks * rnd.uniform(0.05, 0.22))
        spend = round(rnd.uniform(60, 420), 2)
        rows.append((pid, (d + dt.timedelta(days=i // 2)).isoformat(), plat, fmt, title, reach, views, likes, comments,
                     shares, clicks, preorders, spend))
    return _csv(rows, ["post_id", "date", "platform", "format", "title", "reach", "video_views", "likes", "comments",
                       "shares", "link_clicks", "app_preorders", "paid_spend_sgd"])

def sales_by_outlet():
    rnd = random.Random(SEED + 2)
    rows = []
    for o in OUTLETS:
        for wk, start in enumerate(["2026-11-17", "2026-11-24"]):
            cups = rnd.randint(1800, 5200); cold = int(cups * rnd.uniform(0.08, 0.2))
            rows.append((start, o, cups, cold, round(cups * rnd.uniform(3.1, 3.9), 2), rnd.randint(40, 260)))
    return _csv(rows, ["week_start", "outlet", "cups_sold", "cold_brew_cups", "revenue_sgd", "app_preorders"])

def content_calendar_template():
    return _csv([("2026-11-17", "Teaser", "instagram", "image", "", "", "", "draft")],
                ["date", "phase", "platform", "format", "hook", "caption", "hashtags", "status"])

def approval_log_template():
    return _csv([], ["timestamp", "item", "channel", "agent", "decision (APPROVE/EDIT/REJECT)", "human_note", "published_ref"])

def video_brief_template():
    return """# Video Brief — Kopi Kaki launch

| Field | Contract |
|---|---|
| Labs 4 / 8 | 15 seconds; three five-second scenes; 9:16, 1080x1920 |
| Lab 9 weekly variant | 20–30 seconds only when that routine's approved brief requests it |
| Facts | Approved campaign brief + catalogue; source IDs required |
| Promo | Optional; exact terms required if used |
| Assets | Supplied/licensed; AI assistance disclosed in description |
| Human checkpoints | Storyboard copy approval; full-video review; exact-version decision |
| Release | Local package only; no external posting |
"""


def video_qa_checklist():
    return """# Video QA Checklist (Auditor)

Score each item PASS / FAIL with a one-line reason. Any FAIL → `request-changes` back to the owner.

| # | Check |
|---|---|
| V1 | Hook lands in the first 2 seconds |
| V2 | Match approved duration: Labs 4/8 = 15 s; Lab 9 routine = 20–30 s. Always 9:16, 1080×1920 |
| V3 | Brand colours and logo (cream or brown background) used correctly |
| V4 | Main on-screen text readable (≥ 48 px), max 7 words per main line; disclosure remains readable |
| V5 | Approved price/date match the brief. If SHIOK20 is used, include all its exact terms; otherwise promo terms are not required |
| V6 | No compliance-rules.md violation (C1–C10) |
| V7 | AI assistance disclosed in caption/description (C9); identify whether voice-over was actually used |
| V8 | Approved call to action visible in the final scene |
| V9 | Local release package includes video path/hash, approved storyboard, description/disclosure, audit evidence and human decision. No external posting |
"""

# ------------------------------------------------------------------ skills (SKILL.md)
def skill_brand_voice():
    return """---
name: kopi-brand-voice
description: Write or rewrite any public-facing copy (social posts, captions, video scripts, replies) in the Kopi Kaki Co. brand voice and check it against the compliance rules. Use whenever drafting content for Kopi Kaki.
---

# Kopi Kaki brand voice

## When to use
Any time you write words a customer will read or hear for Kopi Kaki Co.

## Steps
1. Read `brand-guide.md`, `campaign-brief.md` and `compliance-rules.md` in the workspace.
2. Draft in the voice: warm, neighbourly, sensory; max ONE Singlish word; max TWO emojis; no ALL CAPS.
3. Use only facts, prices and promotions that appear in the brief or `product-catalogue.csv`.
4. If a promo code appears, add its terms: "valid 1–14 Dec, first app order, one per customer".
5. Run the self-check below and fix every FAIL before returning the draft.

## Self-check (print it under every draft)
| Rule | PASS/FAIL |
|---|---|
| C1 no health claims | |
| C2/C3 price & promo exact, terms shown | |
| C4 no halal claim | |
| C5 no competitor comparison | |
| C6 no personal data | |
| C7 voice limits | |
| C9 AI disclosure if AI visuals/voice | |

## Output format
Return: the draft, the platform it is for, character/word count, and the self-check table.
"""

def skill_campaign_planner():
    return """---
name: social-campaign-planner
description: Turn a campaign brief into a complete, dated multi-platform social media plan (strategy, content calendar CSV, captions, hashtags, image prompts, UTM links). Use when asked to plan or build a social media campaign.
---

# Social campaign planner

## Inputs
A campaign brief (objectives, KPIs, audience, offer, phases, budget) and the brand guide.

## Procedure
1. **Strategy (campaign-plan.md):** objective → audience → key message → 3 content pillars → phase plan → KPI targets → paid budget split.
2. **Calendar (content-calendar.csv):** one row per post with columns
   `date,phase,platform,format,pillar,hook,caption,hashtags,image_prompt,utm_link,status`.
   Respect each platform's format and length rules from the brand guide. Status = `draft`.
3. **Captions:** apply the `kopi-brand-voice` skill to every caption and include its self-check.
4. **Visuals:** write an image prompt per post (brand colours, natural light, no faces of customers).
   If an image-generation tool is available, generate the hero visuals and save them to `outputs/lab02/images/`.
5. **Links:** build UTM links as `https://kopikaki.example/app?utm_source=<platform>&utm_medium=social&utm_campaign=shiokcoldbrew&utm_content=<post_id>`.
6. **Check:** count posts per phase and platform; confirm every KPI has at least one post driving it.

## Output
`outputs/lab02/campaign-plan.md`, `outputs/lab02/content-calendar.csv`, `outputs/lab02/captions.md`, images (if generated),
and a 5-line summary for the human reviewer listing anything that needs a decision.
"""

def skill_compliance_audit():
    return """---
name: brand-compliance-audit
description: Audit a draft post, script, video or publish package against Kopi Kaki's compliance-rules.md (C1–C10) and video-qa-checklist.md (V1–V9) and return a PASS/FAIL table with fixes. Use for any review, audit or QA step.
---

# Brand compliance audit

1. Load `compliance-rules.md` (and `video-qa-checklist.md` for video).
2. For every rule, quote the exact text that passes or fails and give a one-line reason.
3. Verdict: **PASS** only if every rule passes. Otherwise **FAIL** with a numbered fix list.
4. Never fix the work yourself — return it to its owner with the fix list (Kanban: `request-changes`).
5. Escalate to the human if a rule is ambiguous.

Output: `audit-report.md` with the table, the verdict and the fix list.
"""

# ------------------------------------------------------------------ Day 2 (Paperclip) inputs
def paperclip_company():
    return f"""# Paperclip set-up sheet — Kopi Kaki Growth Studio

| Field | Value to enter |
|---|---|
| Organization name | Kopi Kaki Growth Studio |
| First agent | Ava — set role to CEO with the CLI (Lab 6 step 4) |
| Adapter | Claude Code (claude_local), Codex (codex_local), Gemini CLI (gemini_local) or Hermes (hermes_local) — whichever is signed in |
| Hiring gate | Settings → General → Hiring → "Require board approval for new hires" = ON |
| Company goal 1 (level: company) | Launch the {LAUNCH}: 2,500 app pre-orders by 30 Nov 2026 |
| Company goal 2 (level: company) | Publish one Board-approved short video every week |
| Company goal 3 (level: company) | Keep monthly AI spend under USD 60 with zero compliance breaches |
| Company budget | USD 60 / month → `budgetMonthlyCents: 6000` (training cap — use your own number) |
| CEO budget | USD 15 / month → `budgetMonthlyCents: 1500` |

Mission statement (put it in the organization Description and Ava's AGENTS.md):
> Grow Kopi Kaki Co.'s customer base by researching, creating, auditing and publishing on-brand marketing every week —
> safely, on budget, and with the Board's approval on everything public.

Upload `brand-guide.md`, `campaign-brief.md` and `compliance-rules.md` to Ava's Instructions (+ Add agent file).
"""

def paperclip_org_plan():
    return """# Proposed org chart (what a good CEO hiring plan looks like)

| Role | Reports to | Mandate | Suggested budget / month |
|---|---|---|---|
| Market Researcher | CEO | Live trend, competitor and audience research with Tavily; cites every source | USD 8 |
| Content Strategist | CEO | Turns research into the campaign plan, content calendar and briefs | USD 8 |
| Copywriter | Content Strategist | Captions, scripts, replies in the Kopi Kaki voice | USD 8 |
| Video Producer | Content Strategist | Storyboards and renders short videos; builds the publish package | USD 10 |
| Compliance Auditor | CEO | Audits every public item against C1–C10 / V1–V9; can block release | USD 5 |

Rules: no agent hires another agent without Board approval; the Auditor must not report to the people it audits.
"""

def paperclip_backlog():
    rows = [
        ("1", "Research: refresh the Day 1 research brief with current cold-brew trends & competitor moves", "Market Researcher", "high", "", "research-report.md updating outputs/lab01/research-brief.md with ≥ 5 dated, cited sources and the chosen angle"),
        ("2", "Extend the Day 1 two-week calendar into the full 4-week #ShiokColdBrew plan", "Content Strategist", "high", "1", "campaign-plan.md + content-calendar.csv reusing the Day 1 posts and adding the launch and sustain phases (≥ 30 posts across 4 platforms)"),
        ("3", "Write teaser-week captions (7 posts) in brand voice", "Copywriter", "medium", "2", "captions-teaser.md with self-check tables"),
        ("4", "Script & storyboard the 25-second launch video", "Video Producer", "high", "2", "video-script.md with scene list"),
        ("5", "Render the launch video and build the publish package", "Video Producer", "high", "4", "launch-video.mp4 (or storyboard frames) + publish-package.md"),
        ("6", "Compliance audit of captions and video", "Compliance Auditor", "high", "3,5", "audit-report.md — PASS/FAIL per rule"),
        ("7", "Board review & release pack", "CEO", "high", "6", "release-pack.md summarising what is ready for the Board to approve"),
    ]
    return _csv(rows, ["#", "issue title", "assign to", "priority", "blocked by #", "definition of done"])

def paperclip_routine():
    return """# Routine spec — Weekly Kopi Short

| Field | Value |
|---|---|
| Routine name | Weekly Kopi Short |
| Trigger | Schedule — every Monday 10:00 (Asia/Singapore) |
| Generated issue title | Produce this week's Kopi Short (research → script → production → audit → publish-ready) |
| Assignee | CEO (delegates to Researcher → Copywriter → Video Producer → Compliance Auditor) |
| Definition of done | publish-package.md + video (or storyboard) + audit-report.md PASS, sitting in **in_review** for the Board |
| Human gate | The Board approves before anything is published |

Issue description to paste:
> Pick one fresh angle from this week's research (cite 2 sources), write a 20–30 s script in the
> Kopi Kaki voice, produce the video (or a 6-frame storyboard if rendering is unavailable), run the
> brand-compliance audit, and hand the publish package to the Board for approval. Do NOT publish.
"""

def agent_scorecard():
    rows = [
        ("Ava (CEO)", "Coordination", 14, 13, 0, 1, 11.20, 15.00),
        ("Market Researcher", "Research", 9, 9, 0, 0, 6.10, 8.00),
        ("Content Strategist", "Planning", 7, 6, 1, 1, 7.90, 8.00),
        ("Copywriter", "Copy", 22, 18, 4, 3, 5.30, 8.00),
        ("Video Producer", "Video", 5, 3, 2, 2, 10.40, 10.00),
        ("Compliance Auditor", "QA", 27, 27, 0, 0, 2.20, 5.00),
    ]
    return _csv(rows, ["agent", "function", "issues_assigned", "issues_done", "audit_fails", "board_revisions",
                       "spend_usd_month_to_date", "budget_usd_month"])

# ------------------------------------------------------------------ registry
FILES = {
    "agents":      ("AGENTS.md", agents_md),
    "brand":       ("brand-guide.md", brand_guide),
    "brief":       ("campaign-brief.md", campaign_brief),
    "compliance":  ("compliance-rules.md", compliance_rules),
    "catalogue":   ("product-catalogue.csv", product_catalogue),
    "competitors": ("competitors.csv", competitors),
    "reviews":     ("customer-reviews.csv", customer_reviews),
    "comments":    ("social-comments.csv", social_comments),
    "metrics":     ("campaign-week1-metrics.csv", week1_metrics),
    "sales":       ("sales-by-outlet.csv", sales_by_outlet),
    "cal_tpl":     ("templates/content-calendar-template.csv", content_calendar_template),
    "approval_tpl":("templates/approval-log.csv", approval_log_template),
    "video_tpl":   ("templates/video-brief-template.md", video_brief_template),
    "video_qa":    ("video-qa-checklist.md", video_qa_checklist),
    "sk_voice":    ("skills/kopi-brand-voice/SKILL.md", skill_brand_voice),
    "sk_planner":  ("skills/social-campaign-planner/SKILL.md", skill_campaign_planner),
    "sk_audit":    ("skills/brand-compliance-audit/SKILL.md", skill_compliance_audit),
    "pc_company":  ("paperclip-company-setup.md", paperclip_company),
    "pc_org":      ("paperclip-org-plan.md", paperclip_org_plan),
    "pc_backlog":  ("paperclip-backlog.csv", paperclip_backlog),
    "pc_routine":  ("paperclip-routine-weekly-kopi-short.md", paperclip_routine),
    "scorecard":   ("agent-scorecard.csv", agent_scorecard),
}

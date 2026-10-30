"""v3.4 — one founder story: AI agents help you START Kopi Kaki Co., a Singapore kopi startup.

Topic 1  CEO assistant      Activity 1  Meta Muse / OpenAI Dots check your schedule and draft email (PP Task 1)
Topic 2  First AI employee  Guided setup (Hermes Desktop, MiniMax, Telegram, tools, skills, Firecrawl, gog, crons)
                            Activity 2  UX skills from skills.sh -> the Kopi Kaki website
                            Activity 3  PPT tool + skill -> the Kopi Kaki investor & launch deck (PP Task 2)
Topic 3  AI marketing teams Activity 4  Social media marketing team (researcher, LinkedIn/Facebook/Instagram writers, image creator)
                            Activity 5  Video production team (researcher, scriptwriter, producer, voice-over, reviewer) (PP Task 3)
Bonus    One-person company Paperclip: CEO -> Chief of Staff -> marketing team -> the video; compare with Hermes Kanban

Every lab carries `label` (shown to learners) and `code` (file names): Lab 1..5, "Setup" (S2) and "Bonus" (B).
Facts that change with vendor releases live in F (checked 31 Oct 2026 against official docs; see SOURCES).
"""
from copy import deepcopy
import re
from labs_v22 import step

WS = "~/kopi-kaki"
F = dict(
 desktop_url="https://hermes-agent.nousresearch.com/desktop",
 hermes_docs="https://hermes-agent.nousresearch.com/docs/",
)
SOURCES = []   # (title, url) — filled with the verified official sources

STORY = ("You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on "
         "1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take "
         "app pre-orders. Your team is two baristas — and the AI agents you set up in this course.")

def lab(**k):
    k.setdefault("prereq", []); k.setdefault("data", []); k.setdefault("decide", None)
    return k

# ============================================================== Topic 2 · guided setup (not an assessed activity)
def setup_t2():
    return lab(
 num=0, code="S2", label="Topic 2 Setup", day=1, topic=2, slug="setup02-hermes-first-ai-employee", icon="robot",
 title="Hire Your First AI Employee — Hermes Agent Setup",
 short="Hermes Setup", minutes=120, paradigm="One agent, many tools", lo="LO1/LO2",
 hook="Install Hermes Desktop, give it a brain, put it on Telegram, arm it with tools and skills, then let it read your inbox and brief you every morning.",
 scenario=STORY + " Today your first hire is Mia, a Hermes agent that works from your laptop: she reads your Kopi Kaki inbox and calendar, "
          "searches the web for cold-brew trends, and messages you a summary on Telegram every morning before you open the pop-up.",
 objective="Set up one Hermes Agent with a model, a messaging channel, tools, reviewed skills, web search, Google Workspace access and a schedule, and explain how each part changes what the agent can do (LO1, LO2).",
 deliverables=["Hermes Desktop running in ~/kopi-kaki with a working model (MiniMax demo or the trainer-assigned provider)",
               "Mia answering you on Telegram from your allow-listed user ID",
               "Tools and skills listed and tested; Firecrawl web search returning cited results",
               "gog reading Gmail and Calendar; one approved test email sent",
               "A daily 8:00 email-summary cron that delivers to Telegram"],
 agents="1 Hermes agent — Mia, your first AI employee", human="Choose the model and accounts, approve every send, own the schedule",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews"],
 concepts=["Model = the brain; Desktop/gateway = the body; tools = the hands; skills = the know-how",
           "A channel (Telegram) lets the agent reach you; an allow-list decides who can reach it",
           "Cron makes the agent proactive: it starts work without being asked",
           "Read and send are different permissions: approve every send"],
 flow=[("download", "Install", "Desktop + Kopi Kaki workspace.", "agent"), ("brain", "Model", "Connect MiniMax or the assigned provider.", "human"),
       ("phone", "Telegram", "Bot token + your user ID.", "human"), ("tool", "Tools & skills", "Enable, review, install, test.", "agent"),
       ("mail", "gog + Firecrawl", "Inbox, calendar, web search.", "agent"), ("clock", "Cron", "8:00 email summary to Telegram.", "agent")],
 check="Mia answers on Telegram, lists her tools and skills, returns cited web results, reads your inbox and calendar, and `hermes cron list` shows the 8:00 email summary.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 2 · website
def act2():
    return lab(
 num=2, code="02", label="Lab 2", day=1, topic=2, slug="lab02-kopi-kaki-website", icon="globe",
 title="Activity 2 — UX Skills from skills.sh Build the Kopi Kaki Website",
 short="Kopi Kaki Website", minutes=45, paradigm="One agent + installed UX skills",
 hook="A startup without a website does not exist. Install two UX skills from skills.sh and let Mia design, build and test your one-page site in 45 minutes.",
 scenario=STORY + " Customers who taste the cold brew at a pop-up search for you that evening — and find nothing. You need a one-page site "
          "before the flagship opens: hero, menu, the 1 Dec launch, pop-up locations and an app pre-order button. You have no designer, so you "
          "install design skills and brief Mia like an agency.",
 objective="Install third-party UX skills after reviewing their source, use them to brief a single agent, and judge the result against the brand guide (LO2).",
 deliverables=["outputs/website/index.html — responsive one-page Kopi Kaki site (hero, menu, launch, pop-ups, pre-order CTA)",
               "outputs/website/review.md — your design review: what the skill changed, what you corrected",
               "Two screenshots: desktop and mobile widths"],
 agents="1 Hermes agent (Mia) with UX skills from skills.sh", human="Brief the site, review the design against the brand guide, request one revision",
 data=["agents", "brand", "brief", "compliance", "catalogue"],
 concepts=["A skill is reusable know-how in a SKILL.md: install it once, every task benefits",
           "Read a third-party skill before you install it",
           "Brief an agent like an agency: audience, sections, brand, constraints, definition of done"],
 flow=[("search", "Find", "Pick UX skills on skills.sh.", "human"), ("eyecheck", "Review", "Read each SKILL.md before install.", "human"),
       ("puzzle", "Install", "npx skills add … into Hermes.", "agent"), ("code", "Build", "Mia writes index.html with the skill.", "agent"),
       ("user", "Review", "Check brand, mobile, facts; ask one change.", "human")],
 check="index.html opens offline, uses the Kopi Kaki colours and facts, works at phone width, and review.md records your one requested change.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 3 · PPT (PP Task 2)
def act3():
    return lab(
 num=3, code="03", label="Lab 3", day=1, topic=2, slug="lab03-kopi-kaki-pitch-deck", icon="file",
 title="Activity 3 — PPT Tool + Skill Build the Kopi Kaki Pitch Deck",
 short="Pitch Deck (PP Task 2)", minutes=45, paradigm="One agent + PPT tool and skill",
 hook="On Friday you pitch the bank for a SGD 50,000 loan. Mia turns your brief, reviews and competitors into a professional, editable deck — with a real chart.",
 scenario=STORY + " To open the flagship you need working capital, so you are pitching a bank relationship manager on Friday. "
          "You give Mia the campaign brief, the 60 tasting reviews from the pop-ups and the competitor list, plus a PPT tool and a presentation skill. "
          "She builds the deck; you check every number and approve it.",
 objective="Use a presentation tool and a reviewed skill with one agent to produce a professional, editable deck; verify its facts and design before you accept it (LO2; PP Task 2).",
 deliverables=["outputs/deck/kopi-kaki-pitch.pptx — 8–10 editable slides with one native chart",
               "outputs/deck/kopi-kaki-pitch.pdf — rendered copy you reviewed slide by slide",
               "outputs/deck/qa-report.md — facts checked against the source files, fixes made",
               "PP Task 2 evidence: ONE screenshot of Hermes Desktop/dashboard showing the PPT run and the deck"],
 agents="1 Hermes agent (Mia) with the PPT tool and presentation skill", human="Set the story, check every figure, approve the final deck",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews"],
 concepts=["Tool = does the work (python-pptx writes the file); skill = how to do it well (structure, design rules)",
           "A deck is a decision story: problem → product → proof → plan → ask",
           "Content errors and layout errors are different defects: check both"],
 flow=[("puzzle", "Equip", "Install the PPT skill; check python-pptx.", "agent"), ("pen", "Brief", "Audience, story, slide list.", "human"),
       ("chart", "Build", "Mia computes, charts and writes the .pptx.", "agent"), ("eye", "Render", "PDF of every slide.", "agent"),
       ("user", "Approve", "Check facts and layout; one revision.", "human")],
 check="The .pptx opens and is editable, the chart is a native chart, every number matches the source files, and your PP Task 2 screenshot is saved.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 4 · social media team
def act4():
    return lab(
 num=4, code="04", label="Lab 4", day=2, topic=3, slug="lab04-social-media-marketing-team", icon="megaphone",
 title="Activity 4 — Your Social Media Marketing Team",
 short="Social Media Team", minutes=60, paradigm="Multi-agent team on a Kanban board",
 hook="One researcher, three platform writers and an image creator work in parallel. In an hour you review a gallery of LinkedIn, Facebook and Instagram launch posts.",
 scenario=STORY + " Two weeks to launch. LinkedIn needs a founder story for investors and corporate catering buyers, Facebook needs the "
          "neighbourhood and the pop-up dates, Instagram needs a scroll-stopping image. One agent writing all three sounds the same everywhere, "
          "so you build a team: each specialist owns one platform, and you approve every post before anything goes public.",
 objective="Design a multi-agent team with profiles, a Kanban dependency graph and a human approval gate, and compare its output and effort with a single agent (LO2).",
 deliverables=["Five Hermes profiles: researcher, linkedin-writer, facebook-writer, instagram-writer, image-creator",
               "A Kanban board (tenant kopi-social) with dependencies and an unassigned HUMAN approval card",
               "outputs/social/research.md, linkedin.md, facebook.md, instagram.md and images/*.png",
               "outputs/social/gallery.html — every post shown as it would appear on its platform",
               "outputs/social/approval-log.md — APPROVE / EDIT / REJECT per post"],
 agents="5 Hermes profiles shown as bots: researcher → 3 platform writers (in parallel) → image creator", human="Brief the campaign, approve or edit each post, nothing is posted publicly",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews", "comments", "sk_voice"],
 concepts=["Profile = a separate agent: its own SOUL.md, memory, skills and model",
           "Kanban = the team's shared to-do list: assignee, parent dependency, status, history",
           "Parallel specialists + one human gate beat one generalist for multi-channel work",
           "Bots = profiles you can talk to by name"],
 flow=[("users", "Staff", "Create five profiles with roles.", "human"), ("search", "Research", "Angles and facts with sources.", "agent"),
       ("pen", "Write", "LinkedIn, Facebook, Instagram in parallel.", "agent"), ("image", "Images", "One on-brand image per post.", "agent"),
       ("eye", "Gallery", "All posts on one review page.", "agent"), ("user", "Approve", "APPROVE / EDIT / REJECT each post.", "human")],
 check="The board shows five owners, writers blocked on research, the image creator blocked on the writers, and every post in approval-log.md has your decision.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 5 · video team (PP Task 3)
def act5():
    return lab(
 num=5, code="05", label="Lab 5", day=2, topic=3, slug="lab05-video-production-team", icon="video",
 title="Activity 5 — Your Video Production Team",
 short="Video Team (PP Task 3)", minutes=130, paradigm="Multi-agent production line + human review",
 hook="Research, script, render, voice-over, review — five Hermes bots make the 20-second launch video, then send you a link. Nothing ships until you approve it.",
 scenario=STORY + " The launch video is your biggest bet: 40,000 views is the campaign target. Agencies quoted SGD 3,000 and two weeks. "
          "You build a production line instead: a researcher grounds every claim in your source files, a scriptwriter writes the scenes, a "
          "producer renders with HyperFrames, a voice-over artist narrates, and a reviewer checks the cut and sends you a link to watch.",
 objective="Run a multi-agent video team with Kanban dependencies, source checks and an independent review, and accept only the exact video version you have watched (LO3; PP Task 3).",
 deliverables=["Video skills installed: HyperFrames (Remotion, Manim for reference)",
               "Five profiles: researcher, scriptwriter, video-producer, voice-over, video-reviewer",
               "outputs/video/: research.md, script.md, narration.wav, final.mp4, review.md",
               "Review link on Telegram; your APPROVE with the video's SHA-256",
               "PP Task 3: TWO screenshots — Kanban board + video playing"],
 agents="5 Hermes profiles shown as bots on a Kanban board", human="Approve the script, watch the exact cut, approve or request one revision",
 data=["agents", "brand", "brief", "compliance", "catalogue", "video_qa", "sk_voice", "sk_audit"],
 concepts=["Grounding: the researcher may only use facts it can point to in a source file (the RAG idea)",
           "An independent reviewer catches what the maker misses",
           "A changed video needs a new review: approval belongs to one exact file",
           "Human gates are Kanban cards only you can complete"],
 flow=[("search", "Research", "Claims with source file references.", "agent"), ("pen", "Script", "4 scenes, 20 s; you approve the text.", "human"),
       ("film", "Produce", "HyperFrames renders 1080×1920 MP4.", "agent"), ("chat", "Voice-over", "Narration track mixed in.", "agent"),
       ("eyecheck", "Review", "Checks V1–V9; sends you a link.", "agent"), ("user", "Approve", "Watch it; APPROVE the exact file.", "human")],
 check="final.mp4 plays at 1080×1920, review.md passes V1–V9 with evidence, and your APPROVE names the same SHA-256 as the file you watched.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Bonus · Paperclip one-person company
def bonus():
    return lab(
 num=6, code="B", label="Bonus Lab", day=2, topic=4, slug="bonus-paperclip-one-person-company", icon="building",
 title="Paperclip: Run Kopi Kaki as a One-Person Company",
 short="Bonus · Paperclip OPC", minutes=60, paradigm="AI company with an org chart, governed by you",
 hook="You are the only human. A CEO agent hires a Chief of Staff, the Chief of Staff hires the marketing team, and you approve every hire from the Board seat.",
 scenario=STORY + " You have proved that agents can do the work. Now you decide to run Kopi Kaki as a one-person company (OPC): "
          "you sit on the Board, and an AI CEO runs the day-to-day. You set up Paperclip, write the CEO's instructions, and let the CEO hire a "
          "Chief of Staff, who hires the marketing team. Then you give the team the same launch-video brief as Activity 5 and compare.",
 objective="Set up a governed AI company with an org chart, hiring approvals and budgets, and compare it with the Hermes Kanban team (LO3).",
 deliverables=["Paperclip running at http://localhost:3100 with the company 'Kopi Kaki Co.'",
               "CEO agent with written instructions; a Chief of Staff hired through Board approval",
               "Marketing team hired by the Chief of Staff (researcher, writers, image creator, video producer, reviewer)",
               "Org chart screenshot: Board → CEO → Chief of Staff → team",
               "The launch-video task delivered by the team, and comparison.md: Paperclip vs Hermes Kanban"],
 agents="CEO → Chief of Staff → 6 marketing agents", human="You are the Board: write the mission, approve hires and budgets, accept the video",
 data=["pc_company", "brand", "brief", "compliance", "video_qa"],
 concepts=["OPC: one human founder, an AI workforce, governance by design",
           "Paperclip = the company; agents = employees; you = the Board",
           "Delegated hiring: managers propose, the Board approves",
           "Kanban organises tasks; Paperclip organises people, budgets and reporting lines"],
 flow=[("server", "Install", "npx onboard → localhost:3100.", "agent"), ("building", "Company", "Kopi Kaki Co., mission, budget.", "human"),
       ("briefcase", "CEO", "Instructions + task: hire a Chief of Staff.", "human"), ("users", "Chief of Staff", "Hires the marketing team.", "agent"),
       ("org", "Org chart", "Board → CEO → CoS → team.", "human"), ("film", "Deliver", "Team makes the video; you compare.", "agent")],
 check="The org chart shows Board → CEO → Chief of Staff → marketing team, every hire has a Board approval, and comparison.md answers when to use Kanban and when to use Paperclip.",
 steps=[], verify=[], trouble=[], challenge="")


def apply(labs, raw):
    """labs: the v3.3 list (Activity 1 is kept); raw: the original v2.0 labs (Telegram/cron and Paperclip steps are reused)."""
    a1 = deepcopy(labs[0])
    a1.update(code="01", label="Lab 1")
    a1["scenario"] = (STORY + " Your week is packed: a launch review with your two baristas, a supplier tasting for the gula melaka, a pop-up "
                      "site visit. Your always-on CEO assistant checks the calendar and drafts the replies. Use only the trainer-assigned Google "
                      "account with synthetic Kopi Kaki mail and events.")
    a1["title"] = "Activity 1 — Your Always-On CEO Assistant: Meta Muse or OpenAI Dots"
    a1["hook"] = "Before you hire anyone, get a CEO assistant that never clocks off: it checks your schedule and drafts your email while you talk to it."
    a1["deliverables"] = [d for d in a1["deliverables"] if "image B" not in d and "Hermes-generated" not in d]
    a1["deliverables"] = [("PP Task 1 evidence: ONE own Muse or Dots request/result screenshot showing a real schedule check or email draft"
                           if d.startswith("PP Task 1") else d) for d in a1["deliverables"]]
    a1["verify"] = [v.replace("PP1 image A is", "Your PP Task 1 screenshot is") for v in a1["verify"]]
    a1["check"] = a1["check"].replace("PP1 image A saved.", "PP Task 1 screenshot saved.")
    for st in a1["steps"]:
        for k in ("body", "expect"):
            if st.get(k):
                st[k] = (st[k].replace("Capture ONE readable own request/result screenshot as PP Task 1 image A", "Capture ONE readable own request/result screenshot for PP Task 1")
                         .replace("Own assistant image A", "Your PP Task 1 screenshot"))
                st[k] = re.sub(r" You will add a Hermes art[^.]*\.", "", st[k])
    from labs_v34_steps import fill
    out = [a1, setup_t2(), act2(), act3(), act4(), act5(), bonus()]
    for L in out: L.setdefault('lo', {'02': 'LO2', '03': 'LO2', '04': 'LO2', '05': 'LO3', 'B': 'LO3'}.get(L['code'], 'LO1'))
    fill(out, raw)
    labs[:] = out

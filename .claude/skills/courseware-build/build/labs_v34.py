"""v3.4 — one founder story: AI agents help you START Kopi Kaki Co., a Singapore kopi startup.

Topic 1  CEO assistant      Activity 1  Meta Muse / OpenAI Dots check your schedule and draft email (PP Task 1)
Topic 2  First AI employee  Guided setup in Hermes Desktop (model, Telegram QR, voice, tools, skills, Firecrawl, Gmail connector, scheduled jobs)
                            Activity 2  UX skills from skills.sh -> the Kopi Kaki website
                            Activity 3  PPT tool + skill -> the Kopi Kaki investor & launch deck (PP Task 2)
Topic 3  AI marketing teams Activity 4  Five named bots in one group chat write the social posts
                            Activity 5  One prompt builds a video team on a Kanban board (PP Task 3)
                            Activity 6  Scheduled jobs auto-generate next week's posts and video drafts
v3.5: no command lines for learners — every step is a Desktop click or a prompt the agent carries out.
Bonus    One-person company Paperclip: CEO -> Chief of Staff -> marketing team -> the video; compare with Hermes Kanban

Every lab carries `label` (shown to learners) and `code` (file names): Lab 1..6, "Setup" (S2) and "Bonus" (B).
Facts that change with vendor releases live in F (checked 31 Oct 2026 against official docs; see SOURCES).
"""
from copy import deepcopy
import re
from labs_v22 import step

WS = "~/Desktop/kopi-kaki"
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
 hook="Install one app, sign in, scan one QR code. No command line: by the end Mia reads your Gmail, searches the web and briefs you on Telegram every morning.",
 scenario=STORY + " Today your first hire is Mia, a Hermes agent that works from your laptop: she reads your Kopi Kaki inbox, "
          "searches the web for cold-brew trends, and messages you a summary on Telegram every morning before you open the pop-up.",
 objective="Set up one Hermes Agent in Hermes Desktop with a model, a messaging channel, voice, tools, reviewed skills, web search, Gmail access and a schedule, and explain how each part changes what the agent can do (LO1, LO2).",
 deliverables=["Hermes Desktop working in your Desktop/kopi-kaki folder with a model (Nous free tier, your ChatGPT Plus plan or a paid model)",
               "Mia answering you on Telegram (set up with Create with QR) and reading answers aloud",
               "Tools and skills checked in Capabilities; Firecrawl web search returning cited results",
               "Gmail connected with a Google sign-in; one approved test email sent",
               "A daily 8:00 email-summary scheduled job that delivers to Telegram"],
 agents="1 Hermes agent — Mia, your first AI employee", human="Choose the model and accounts, approve every send, own the schedule",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews"],
 concepts=["Model = the brain; Desktop = the body; tools = the hands; skills = the know-how",
           "A channel (Telegram) lets the agent reach you; an allow-list decides who can reach it",
           "A scheduled job (cron) makes the agent proactive: it starts work without being asked",
           "Read and send are different permissions: approve every send"],
 flow=[("download", "Install", "Desktop + Kopi Kaki folder.", "human"), ("brain", "Model", "Nous free tier or ChatGPT Plus.", "human"),
       ("phone", "Telegram", "Messaging → Create with QR.", "human"), ("tool", "Tools & skills", "Capabilities: review and switch on.", "agent"),
       ("mail", "Gmail + web", "Sign in with Google; Firecrawl key.", "agent"), ("clock", "Schedule", "8:00 email summary to Telegram.", "agent")],
 check="Mia answers on Telegram, lists her tools and skills, returns cited web results, reads your Gmail, and Scheduled jobs shows the 8:00 email summary.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 2 · website
def act2():
    return lab(
 num=2, code="02", label="Lab 2", day=1, topic=2, slug="lab02-kopi-kaki-website", icon="globe",
 title="Activity 2 — One Agent Builds the Kopi Kaki Website with UX Skills",
 short="Website · single agent", minutes=45, paradigm="Single agent + installed UX skills",
 hook="A startup without a website does not exist. Ask Mia to install two UX skills from skills.sh, then let her design, build and test your one-page site in 45 minutes.",
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
       ("puzzle", "Install", "Ask Mia to install them.", "agent"), ("code", "Build", "Mia writes index.html with the skill.", "agent"),
       ("user", "Review", "Check brand, mobile, facts; ask one change.", "human")],
 check="index.html opens offline, uses the Kopi Kaki colours and facts, works at phone width, and review.md records your one requested change.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 3 · PPT (PP Task 2)
def act3():
    return lab(
 num=3, code="03", label="Lab 3", day=1, topic=2, slug="lab03-kopi-kaki-pitch-deck", icon="file",
 title="Activity 3 — One Agent Builds the Kopi Kaki Pitch Deck with a PPT Tool and Skill",
 short="Pitch deck · single agent (PP Task 2)", minutes=45, paradigm="Single agent + PPT tool and skill",
 hook="On Friday you pitch the bank for a SGD 50,000 loan. Mia turns your brief, reviews and competitors into a professional, editable deck — with a real chart.",
 scenario=STORY + " To open the flagship you need working capital, so you are pitching a bank relationship manager on Friday. "
          "You give Mia the campaign brief, the 60 tasting reviews from the pop-ups and the competitor list, plus a PPT tool and a presentation skill. "
          "She builds the deck; you check every number and approve it.",
 objective="Use a presentation tool and a reviewed skill with one agent to produce a professional, editable deck; verify its facts and design before you accept it (LO2; PP Task 2).",
 deliverables=["outputs/deck/kopi-kaki-pitch.pptx — 8–10 editable slides with one native chart",
               "outputs/deck/kopi-kaki-pitch.pdf — PDF copy, if LibreOffice is installed",
               "outputs/deck/qa-report.md — facts checked against the source files, fixes made",
               "PP Task 2 evidence: ONE screenshot of Hermes Desktop showing the PPT run and the deck"],
 agents="1 Hermes agent (Mia) with the PPT tool and presentation skill", human="Set the story, check every figure, approve the final deck",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews"],
 concepts=["Tool = does the work (python-pptx writes the file); skill = how to do it well (structure, design rules)",
           "A deck is a decision story: problem → product → proof → plan → ask",
           "Content errors and layout errors are different defects: check both"],
 flow=[("puzzle", "Equip", "“Install the kopi pitch deck skill.”", "agent"), ("pen", "Brief", "Audience, story, slide list.", "human"),
       ("chart", "Build", "Mia computes, charts and writes the .pptx.", "agent"), ("eye", "Render", "PDF of every slide.", "agent"),
       ("user", "Approve", "Check facts and layout; one revision.", "human")],
 check="The .pptx opens and is editable, the chart is a native chart, every number matches the source files, and your PP Task 2 screenshot is saved.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 4 · social media team
def act4():
    return lab(
 num=4, code="04", label="Lab 4", day=2, topic=3, slug="lab04-social-media-marketing-team", icon="megaphone",
 title="Activity 4 — Your Social Media Team: Five Bots in One Group Chat",
 short="Social posts · bots + group", minutes=60, paradigm="Multiple named bots in one group chat",
 hook="Hire five bots with names and job titles, put them in one group chat, and post one brief. They hand off by @mention; you approve every post.",
 scenario=STORY + " Two weeks to launch. LinkedIn needs a founder story for investors and corporate catering buyers, Facebook needs the "
          "neighbourhood and the pop-up dates, Instagram needs a scroll-stopping image. One agent writing all three sounds the same everywhere, "
          "so you hire a team of bots: each specialist owns one platform, they talk in one group chat, and you approve every post before anything goes public.",
 objective="Design a multi-agent team of named bots with clear roles, coordinate them in a group chat with a human approval step, and compare its output and effort with a single agent (LO2).",
 deliverables=["Five bots created with New Agent: Rafi (researcher), Lin (LinkedIn), Farah (Facebook), Ivy (Instagram), Pixel (images)",
               "A group chat 'Kopi Social Team' where the bots hand off by @mention and ask you (@user) for decisions",
               "outputs/social/research.md, linkedin.md, facebook.md, instagram.md and images/*.png",
               "outputs/social/gallery.html — every post shown as it would appear on its platform",
               "outputs/social/approval-log.md — APPROVE / EDIT / REJECT per post"],
 agents="5 named bots in one group chat: Rafi → Lin, Farah, Ivy → Pixel", human="Post the brief, approve or edit each post; nothing is posted publicly",
 data=["agents", "brand", "brief", "compliance", "catalogue", "competitors", "reviews", "comments", "sk_voice"],
 concepts=["A bot = a separate agent with its own name, role, instructions, memory and skills",
           "A group chat lets bots talk to each other: @mention hands work to a teammate, @user asks you",
           "Specialists + one human decision beat one generalist for multi-channel work",
           "Hard caps (3 rounds, 10 messages per send) keep a room from spinning"],
 flow=[("users", "Hire", "Five bots: name, title, role.", "human"), ("search", "Research", "Rafi: angles and facts with sources.", "agent"),
       ("pen", "Write", "LinkedIn, Facebook, Instagram in parallel.", "agent"), ("image", "Images", "One on-brand image per post.", "agent"),
       ("eye", "Gallery", "All posts on one review page.", "agent"), ("user", "Approve", "APPROVE / EDIT / REJECT each post.", "human")],
 check="The group chat shows Rafi's research first, three platform drafts, Pixel's gallery, and every post in approval-log.md has your decision.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 5 · video team (PP Task 3)
def act5():
    return lab(
 num=5, code="05", label="Lab 5", day=2, topic=3, slug="lab05-video-production-team", icon="video",
 title="Activity 5 — Your Video Team on a Kanban Board",
 short="Video · Kanban team (PP Task 3)", minutes=115, paradigm="Agent team on a Kanban board + human gates",
 hook="One prompt hires a video team and builds its Kanban board. Research, script, voice-over, render, review: the board runs it; nothing ships until you approve.",
 scenario=STORY + " The launch video is your biggest bet: 40,000 views is the campaign target. Agencies quoted SGD 3,000 and two weeks. "
          "You build a production line instead: a researcher grounds every claim in your source files, a scriptwriter writes the scenes, a "
          "producer renders with HyperFrames, a voice-over artist narrates, and a reviewer checks the cut and sends you a link to watch.",
 objective="Run a multi-agent video team with Kanban dependencies, source checks and an independent review, and accept only the exact video version you have watched (LO3; PP Task 3).",
 deliverables=["Video skill installed from Capabilities → Skills: HyperFrames (Remotion, Manim for reference)",
               "A video team created by prompt: video-researcher, scriptwriter, voice-over, video-producer, video-reviewer",
               "outputs/video/: research.md, script.md, narration audio, final.mp4, review.md",
               "Review link on Telegram; your APPROVE with the video's SHA-256",
               "PP Task 3: TWO screenshots — Kanban board + video playing"],
 agents="5 agents created by Mia from one prompt, working on a Kanban board", human="Approve the script, watch the exact cut, approve or request one revision",
 data=["agents", "brand", "brief", "compliance", "catalogue", "video_qa", "sk_voice", "sk_audit"],
 concepts=["Grounding: the researcher may only use facts it can point to in a source file (the RAG idea)",
           "An independent reviewer catches what the maker misses",
           "A changed video needs a new review: approval belongs to one exact file",
           "Human gates are Kanban cards only you can complete"],
 flow=[("kanban", "Board", "One prompt: team + cards + gates.", "human"), ("search", "Research", "Claims with source file references.", "agent"), ("pen", "Script", "4 scenes, 20 s; you approve the text.", "human"),
       ("film", "Produce", "Voice-over + HyperFrames MP4.", "agent"),
       ("eyecheck", "Review", "Checks V1–V9; sends you a link.", "agent"), ("user", "Approve", "Watch it; APPROVE the exact file.", "human")],
 check="final.mp4 plays at 1080×1920, review.md passes V1–V9 with evidence, and your APPROVE names the same SHA-256 as the file you watched.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Activity 6 · content crons (v3.5)
def act6():
    return lab(
 num=6, code="06", label="Lab 6", day=2, topic=3, slug="lab06-content-crons", icon="clock",
 title="Activity 6 — Crons Make Next Week\'s Posts and Video While You Sleep",
 short="Content crons", minutes=30, paradigm="Scheduled jobs that start the team's work",
 hook="Your team works when you tell it to. A cron makes it work on Monday at 9:00 without you: fresh posts, a new video draft, waiting for your approval.",
 scenario=STORY + " The launch campaign runs for four weeks. You do not want to brief the team from scratch every Monday, so you schedule the work: "
          "every Monday the social bots draft the week's three posts, and every Friday the video team starts a new 15-second clip. "
          "The schedule starts the work; you still approve everything before it is used.",
 objective="Automate recurring content work with scheduled jobs, keep a human approval gate on every output, and test, pause and measure the jobs (LO3).",
 deliverables=["A Monday 9:00 job: the social bots draft three posts into outputs/social/weekly/ and tell you on Telegram",
               "A Friday 10:00 job: Mia starts a Kanban video run with your two HUMAN gates",
               "Both jobs tested once with Trigger now, then left scheduled (or paused after class)",
               "outputs/automation/cron-log.md: job, schedule, what it produced, what you approved"],
 agents="Mia and the Activity 4 and 5 teams, started by scheduled jobs", human="Choose the schedule, approve every post and video, pause a job that misbehaves",
 data=["agents", "brand", "brief", "compliance", "catalogue"],
 concepts=["A cron is a schedule plus a prompt: it starts work without being asked",
           "Automate the start of the work, never the approval",
           "Test with Trigger now before you trust a schedule; pause what you cannot watch",
           "Measure what the automation saves: drafts per week, your review minutes, model cost"],
 flow=[("clock", "Schedule", "Monday 9:00 and Friday 10:00.", "human"), ("chat", "Prompt", "Ask Mia to create both jobs.", "human"),
       ("bolt", "Test", "Trigger now; check the outputs.", "agent"), ("phone", "Notify", "Telegram: drafts are waiting.", "agent"),
       ("user", "Approve", "APPROVE / EDIT before use.", "human"), ("pause", "Control", "Pause, edit or delete the job.", "human")],
 check="Scheduled jobs lists both jobs with the right times, each test run produced drafts and a Telegram message, and nothing was published without your approval.",
 steps=[], verify=[], trouble=[], challenge="")

# ============================================================== Bonus · Paperclip one-person company
def bonus():
    return lab(
 num=7, code="B", label="Bonus Lab", day=2, topic=4, slug="bonus-paperclip-one-person-company", icon="building",
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
 flow=[("server", "Install", "Ask Mia to install it.", "agent"), ("building", "Company", "Kopi Kaki Co., mission, budget.", "human"),
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
    out = [a1, setup_t2(), act2(), act3(), act4(), act5(), act6(), bonus()]
    for L in out: L.setdefault('lo', {'02': 'LO2', '03': 'LO2', '04': 'LO2', '05': 'LO3', '06': 'LO3', 'B': 'LO3'}.get(L['code'], 'LO1'))
    fill(out, raw)
    labs[:] = out

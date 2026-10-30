"""v3.4 slides: the founder story. Topic 3 (AI marketing teams), the 5 principles of AI security,
the RAG/evaluation concepts the WA tests, and the bonus Paperclip one-person-company topic.
Topic 2 lives in slides_v34_t2.py. Every slide is written for this course; no repeated row templates."""
import os
from ccdeck import *
import ccdeck as K
from slides_2026 import tag

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'courseware', 'assets'))
def asset(*p): return os.path.join(ASSETS, *p)
PC = 'https://github.com/paperclipai/paperclip'
HK = 'https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban'
HP = 'https://hermes-agent.nousresearch.com/docs/user-guide/profiles'
HF = 'https://hyperframes.heygen.com/'

def link(s, x, y, w, label, url, size=10):
    t = text(s, x, y, w, .26, label, size, TEAL, autofit=False); t.text_frame.paragraphs[0].runs[0].hyperlink.address = url

def pills(D, kicker, title, sub, rows_, tipt):
    """The Claude Code course's '5 Principles of AI Security' layout: accent bar · name · dark pill · one-line rule."""
    s = D.new(); header(D, s, kicker, title, sub)
    top, rh, gap = 2.3, .7, .1
    for i, (name, pill, rule) in enumerate(rows_):
        y = top + i * (rh + gap)
        card(s, .6, y, 12.1, rh)
        box(s, .82, y + .2, .07, rh - .4, fill=ACC)
        text(s, 1.1, y, 2.9, rh, name, 15.5, ACC_D, bold=True, font=SERIF, anchor='m', autofit=False)
        box(s, 4.0, y + .2, 2.55, rh - .4, fill=CHAR, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        text(s, 4.0, y + .2, 2.55, rh - .4, pill.upper(), 9.5, WHITE, bold=True, align='c', anchor='m', autofit=False)
        text(s, 6.85, y + .04, 5.7, rh - .08, rule, 12.5, MUTED, anchor='m', minpt=9.5)
    tip(D, s, tipt, y=top + 5 * (rh + gap) + .02)
    return s

def big_number(D, kicker, number, line, small, dark=True):
    s = D.new(dark=dark)
    circle(s, 9.9, -1.4, 4.2, ACC)
    text(s, .9, 1.7, 9.0, .4, kicker.upper(), 14, ACC, bold=True, autofit=False)
    text(s, .85, 2.15, 9.0, 1.9, number, 96, WHITE if dark else INK, bold=True, font=SERIF, autofit=False)
    text(s, .9, 4.15, 10.5, 1.0, line, 26, WHITE if dark else INK, bold=True, font=SERIF, minpt=16)
    text(s, .9, 5.25, 10.5, 1.2, small, 15, SOFT if dark else MUTED, minpt=11)
    footer(D, s); return s

def before_after(D, kicker, title, sub, left, right, tipt=None):
    """left/right = (label, heading, [lines]) — left muted 'before', right dark 'after'."""
    s = D.new(); header(D, s, kicker, title, sub)
    for j, (lab, hd, lines) in enumerate((left, right)):
        x = .6 + j * 6.15; dark = j == 1
        card(s, x, 2.4, 5.95, 3.95, fill=CHAR if dark else WHITE)
        text(s, x + .35, 2.6, 5.3, .3, lab.upper(), 11, ACC, bold=True, autofit=False)
        text(s, x + .35, 2.95, 5.3, .6, hd, 21, WHITE if dark else INK, bold=True, font=SERIF, minpt=13)
        text(s, x + .35, 3.7, 5.3, 2.5, "\n".join(lines), 14.5, SOFT if dark else MUTED, lh=1.3, minpt=10)
    line(s, 6.45, 4.35, 6.85, 4.35, ACC, 3, arrow=True)
    if tipt: tip(D, s, tipt, y=6.45)
    return s

# ====================================================================== Topic 3
def topic3_open(D, C):
    section(D, 'Day 2 · Topic 3', C.TOPICS[2]['title'], C.TOPICS[2]['items'],
            sub='Recap: a CEO assistant, then your first AI employee. Today: AI teams.')
    big_number(D, 'Topic 3 · Two weeks to launch', '5 + 5',
               'Five marketers and five video makers. You hire none of them.',
               'Yesterday Mia worked alone. Today you split the launch into specialist jobs: a social media team writes for three platforms, '
               'a production team makes the launch video. You stay the founder who approves everything.')

def video_tools(D):
    s = D.new(); header(D, s, 'Topic 3 · Video skills and tools', 'Three Ways Your Agents Make Video with Code',
                        'No camera, no editor: the agent writes code, the tool renders an MP4. Pick the one that suits the job.')
    tools = [('HyperFrames', 'by HeyGen · HTML → MP4', 'Write each scene as HTML/CSS with GSAP timing; lint, snapshot, preview, render. Built-in local voice-over (Kokoro).',
              'Kopi Kaki uses it for the launch video.', 'hermes skills install \\\n  official/creative/hyperframes\nnpx hyperframes doctor', HF),
             ('Remotion', 'React → MP4', 'Each frame is a React component; strong for data-driven and templated videos at scale.',
              'Good for 50 personalised promo cuts.', 'npx skills add remotion-dev/skills \\\n  -a hermes-agent -g', 'https://www.remotion.dev/'),
             ('Manim', 'Python → MP4', 'The maths-animation engine behind 3Blue1Brown: precise diagrams, graphs and equations that move.',
              'Good for explaining how cold brew is made.', '# skill built in: manim-video\npip install manim   # + LaTeX', 'https://www.manim.community/')]
    for i, (name, tag_, what, use, cmd, url) in enumerate(tools):
        x = .6 + i * 4.1; dark = False
        card(s, x, 2.35, 3.9, 4.35, fill=CHAR if dark else WHITE)
        text(s, x + .3, 2.5, 3.3, .5, name, 22, WHITE if dark else INK, bold=True, font=SERIF, autofit=False)
        text(s, x + .3, 3.02, 3.3, .3, tag_, 11.5, ACC, bold=True, autofit=False)
        text(s, x + .3, 3.4, 3.3, 1.25, what, 12, SOFT if dark else MUTED, minpt=9.5)
        text(s, x + .3, 4.62, 3.3, .45, use, 12, WHITE if dark else INK, bold=True, minpt=9.5)
        card(s, x + .25, 5.12, 3.4, .95, fill=K.CODEBG, shadow=False)
        text(s, x + .38, 5.18, 3.2, .85, cmd, 10, 'F1EDE4', font=K.MONO, minpt=8, cw=.62)
        link(s, x + .3, 6.32, 3.4, url.replace('https://', '') + ' · click', url)
    tag(D, 'TOOLS', HF + ' ; https://www.remotion.dev/ ; https://www.manim.community/')

def profiles_kanban_bots(D):
    hub(D, 'Topic 3 · Profiles', 'A Profile Is a Separate Employee', 'Each profile:\nown SOUL · memory\nskills · model', [
        ('search', 'researcher', 'Facts with a source file'), ('pen', 'linkedin-writer', 'Founder story for investors'),
        ('chat', 'facebook-writer', 'Neighbours and pop-ups'), ('image', 'instagram-writer', 'Hook, caption, hashtags'),
        ('sparkles', 'image-creator', 'On-brand 1080×1350 images'), ('user', 'You', 'Approve every post')],
        sub='hermes profile create <name> --clone copies your model and keys; SOUL.md gives the job and the rules.')
    tag(D, 'ARCH', HP)
    image(D, 'Topic 3 · Profiles', 'Your Team in the Hermes Dashboard', asset('screenshots', 'hermes-profiles.png'),
          caption='Profiles listed side by side: each has its own configuration, memory and skills. Reference screenshot; capture your own team.')
    s = D.new(); header(D, s, 'Topic 3 · Kanban', 'Parents First: A Card Runs Only When Its Inputs Exist',
                        'The board is the team’s shared to-do list. A card with an open parent waits; your HUMAN card blocks everything after it.')
    nodes = [('Research', 'researcher', 1.0, 3.65), ('LinkedIn', 'linkedin-writer', 4.1, 2.45), ('Facebook', 'facebook-writer', 4.1, 3.65),
             ('Instagram', 'instagram-writer', 4.1, 4.85), ('Images + gallery', 'image-creator', 7.2, 3.65), ('HUMAN: approve', 'you, unassigned', 10.3, 3.65)]
    for lab, who, x, y in nodes:
        human = lab.startswith('HUMAN')
        card(s, x, y, 2.45, .95, fill=ACC_D if human else WHITE)
        text(s, x + .18, y + .08, 2.1, .4, lab, 14, WHITE if human else INK, bold=True, font=SERIF, autofit=False)
        text(s, x + .18, y + .5, 2.1, .35, who, 11, LIGHT if human else MUTED, autofit=False)
    for (x1, y1, x2, y2) in [(3.45, 4.12, 4.1, 2.92), (3.45, 4.12, 4.1, 4.12), (3.45, 4.12, 4.1, 5.32),
                             (6.55, 2.92, 7.2, 4.12), (6.55, 4.12, 7.2, 4.12), (6.55, 5.32, 7.2, 4.12), (9.65, 4.12, 10.3, 4.12)]:
        line(s, x1, y1, x2, y2, ACC, 1.75, arrow=True)
    tip(D, s, 'Hermes dispatches a card when every parent is done and the gateway is running. Bind parents when you create the card, not afterwards.', y=6.25)
    tag(D, 'ARCH', HK)
    image(D, 'Topic 3 · Kanban', 'Watch the Board Work', asset('screenshots', 'hermes-kanban.png'),
          caption='hermes kanban watch --tenant kopi-social in the terminal, or hermes dashboard → Kanban. Open a card for its run history and output path.')
    before_after(D, 'Topic 3 · Bots', 'Bots: Talk to Each Team Member by Name',
                 'A bot is how you reach a profile. The work is still tracked on the board.',
                 ('Without bots', 'One chat, one voice', ['You ask Mia to “be the LinkedIn writer”.', 'Roles blur; memory mixes three platforms.', 'Hard to tell who wrote what.']),
                 ('With bots', 'A roster of named specialists', ['Desktop Bot Mode (Bots tab) shows each profile as a bot.', 'Ask the researcher, brief the image creator, directly.', 'Optional: one Telegram bot per profile (<profile> gateway start).']),
                 tipt='A Telegram bot is a messaging account. Two Telegram chats do not make two agents: separate profiles do.')
    tag(D, 'ARCH', HP)

def activity4_team(D):
    s = D.new(dark=True); header(D, s, 'Topic 3 · Activity 4', 'One Brief, Three Platforms, Three Voices',
                                 'The same launch fact, written by the specialist for each audience.')
    posts = [('LinkedIn', 'linkedin', 'Founder story', '“I quit my bank job to bring back the kopitiam I grew up with. On 1 Dec our Tiong Bahru flagship opens…”'),
             ('Facebook', 'users', 'The neighbourhood', '“Tiong Bahru kakis! Catch our last pop-up this Saturday, then come say hi on 1 Dec. Gula Melaka Cold Brew, SGD 6.80.”'),
             ('Instagram', 'image', 'The scroll-stopper', '“Slow-brewed. Shiok cold. 🧋 12 hours, real gula melaka, coconut cream. #ShiokColdBrew”')]
    for i, (pl, ic, aud, q) in enumerate(posts):
        x = .6 + i * 4.1
        card(s, x, 2.45, 3.9, 3.7, fill=K.PANEL, shadow=False); icon(s, ic, x + .3, 2.7, .56)
        text(s, x + 1.05, 2.68, 2.6, .4, pl, 19, WHITE, bold=True, font=SERIF, autofit=False)
        text(s, x + 1.05, 3.08, 2.6, .3, aud, 11.5, ACC, bold=True, autofit=False)
        text(s, x + .3, 3.65, 3.3, 2.3, q, 14, SOFT, font=SERIF, minpt=10, lh=1.2)
    tip(D, s, 'Sample copy for illustration. Your team writes its own from the brief, and you approve every post.', y=6.35)

def video_team(D):
    s = D.new(); header(D, s, 'Topic 3 · Activity 5', 'Your Production Line: Five Bots, Two Human Gates',
                        'Research → script → YOU approve → voice-over and render → independent review → YOU approve the exact file.')
    steps = [('search', 'Researcher', 'Claim | source | quote', False), ('pen', 'Scriptwriter', '4 scenes · 20 s', False), ('user', 'You', 'Approve the script', True),
             ('chat', 'Voice-over', 'narration.wav', False), ('film', 'Producer', 'HyperFrames → MP4', False), ('eyecheck', 'Reviewer', 'V1–V9 + link', False), ('user', 'You', 'APPROVE <sha256>', True)]
    w = 1.58; gap = .14
    for i, (ic, t, d, human) in enumerate(steps):
        x = .6 + i * (w + gap)
        card(s, x, 2.6, w, 2.7, fill=ACC_D if human else WHITE)
        icon(s, ic, x + .5, 2.85, .56, fill=WHITE if human else ACC, glyph=ACC_D if human else WHITE)
        text(s, x + .1, 3.6, w - .2, .45, t, 14.5, WHITE if human else INK, bold=True, font=SERIF, align='c', minpt=10)
        text(s, x + .1, 4.1, w - .2, 1.0, d, 11.5, LIGHT if human else MUTED, align='c', minpt=9)
        if i < len(steps) - 1: line(s, x + w + .01, 3.95, x + w + gap - .01, 3.95, ACC, 1.5, arrow=True)
    text(s, .6, 5.6, 12.1, .7, 'The reviewer sends you a link (http://localhost:8765/final.mp4) and the file’s SHA-256. Your approval belongs to that exact file: change one frame and it needs a new review.', 14, MUTED, minpt=11)
    tag(D, 'ARCH', HK + ' ; ' + HF)

# ---------------------------------------------------------------- grounding / RAG (WA K2) — before Activity 5
def grounding(D):
    before_after(D, 'Topic 3 · Grounding', 'Grounded or Guessing? RAG versus a Standard LLM',
                 'Your researcher bot is a small RAG system: it may only say what a source file supports.',
                 ('Standard LLM', 'Answers from what it learned', ['Fluent, fast, cheap to set up.', 'Does not know your price, dates or latest policy.', 'Can state a wrong fact confidently.']),
                 ('Retrieval-augmented (RAG)', 'Answers from passages it retrieved', ['Quotes the approved source and its version.', 'Says INSUFFICIENT EVIDENCE when nothing supports a claim.', 'Needs owners, indexing, access control and refresh.']),
                 tipt='In Activity 5 the researcher writes claim | source file | exact quote. That table is your RAG audit trail.')
    tag(D, 'CONCEPT', 'Lewis et al. 2020, Retrieval-Augmented Generation; course design')
    cards(D, 'Topic 3 · Grounding', 'Four Small Tests Reveal Different Failure Modes', [
        ('Supported', '“What does the cold brew cost?” → the catalogue line: SGD 6.80.', 'check'),
        ('Partial', '“What is the SHIOK20 offer?” → the discount AND its terms, or it is incomplete.', 'file'),
        ('Unsupported', '“Is it healthier than soft drinks?” → INSUFFICIENT EVIDENCE. No source, no claim.', 'shield'),
        ('Conflicting', 'Two files disagree on the launch date → stop and ask the source owner.', 'alert')],
        cols=4, sub='Run all four against your researcher before you trust it with a public video.')
    tag(D, 'EVIDENCE', 'Course test design; Kopi Kaki source files')
    s = D.new(); header(D, s, 'Topic 3 · Grounding', 'Refresh Sources Without Reusing Obsolete Advice',
                        'A RAG system is only as current as its last refresh. Maintenance is part of feasibility, not an afterthought.')
    for i, (n, t, d) in enumerate([('1', 'Change', 'The owner approves price list v2 (SGD 6.80 → 7.20).'), ('2', 'Refresh', 'Re-index the changed passages; retire v1 so it cannot be retrieved.'),
                                   ('3', 'Retest', 'Re-run the four tests: supported, partial, unsupported, conflicting.'), ('4', 'Re-review', 'Every post and video that quoted v1 goes back to review.')]):
        x = .6 + i * 3.08
        text(s, x, 2.5, 2.9, 1.2, n, 72, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x, 3.8, 2.9, .5, t, 19, INK, bold=True, font=SERIF)
        text(s, x, 4.35, 2.85, 1.6, d, 13.5, MUTED, minpt=10)
    tip(D, s, 'For a regulated business (bank, insurer, clinic) add a named source owner, access control per document and an audit log of every refresh.', y=6.2)
    tag(D, 'CONCEPT', 'Course design')
    table(D, 'Topic 3 · Grounding', 'A Retrieval Evaluation Must Measure More Than Fluency', ['Measure', 'Question it answers', 'How to check it in Activity 5'],
          [('Relevance', 'Did search return the passage needed?', 'Each claim in research.md points to the right file'),
           ('Support', 'Does the passage actually justify the answer?', 'Read the quoted line yourself for two claims'),
           ('Latency', 'How long from question to reviewed answer?', 'Card start → reviewer PASS, from run history'),
           ('Cost', 'Ingestion + queries + human review', 'Model spend plus your review minutes')], colw=[2.2, 4.6, 5.3], size=13)
    tag(D, 'EVIDENCE', 'Course evaluation design')

# ---------------------------------------------------------------- evaluation (WA K3/K5) — after Activity 5
def evaluation(D):
    big_number(D, 'Topic 3 · Was the team worth it?', 'SGD 3,000', 'versus your agents’ model bill and your review time.',
               'The agency quote: SGD 3,000 and two weeks. Your team: a few dollars of model spend, an afternoon, and every minute you spent reviewing. '
               'Count all of it before you decide.')
    cards(D, 'Topic 3 · Evaluate and improve', 'Four Metrics Support an Improvement Decision', [
        ('Cycle time', 'Brief to accepted video, including your reviews and every retry.', 'clock'),
        ('First-pass acceptance', 'Share of outputs you approved without a revision.', 'check'),
        ('Cost per accepted item', 'Model and tool spend plus review minutes, per approved post or video.', 'coins'),
        ('Defect rate', 'Fact, brand and video-quality failures, counted separately.', 'alert')],
        cols=2, sub='Measure the same four numbers before and after any change to a skill, a SOUL.md or the team.')
    tag(D, 'EVIDENCE', 'Course evaluation design')

# ---------------------------------------------------------------- 5 principles of AI security
def security(D):
    pills(D, 'AI security', '5 Principles of AI Security',
          'Your agents read your inbox, spend your money and speak for your brand. These five controls keep what they see and do safe, reviewable and accountable.',
          [('Data Control', 'What AI can see', 'Classify your data (public, internal, confidential) and decide exactly which data the AI may access.'),
           ('Permission Control', 'What AI can do', 'Grant only the rights needed — read, write, edit, delete. Ask before anything destructive.'),
           ('Human in the Loop', 'Who approves', 'A person reviews and approves high-impact actions — sends, posts, payments, deletions.'),
           ('Traceability', 'What happened', 'Log every prompt, tool call and change so actions can be audited, explained and rolled back.'),
           ('Right-Sized Models', 'Not the most powerful', 'Do not use the most powerful model by default — the smallest model that does the job has less autonomy and risk.')],
          'In Hermes: read-only gog, a Telegram allow-list, approvals.mode manual, HUMAN Kanban cards, run history and file hashes, a smaller model per profile.')
    tag(D, 'POLICY', 'Same five principles as TGS-2025052468 Agentic AI Applications with Claude Code (slide 75)')

# ====================================================================== Bonus · Paperclip
def bonus(D, C, mark):
    mark('bonus')
    section(D, 'Bonus topic · optional', C.BONUS['title'].replace('Bonus (optional) — ', ''), C.BONUS['items'],
            sub='One founder. An AI company. You sit on the Board.')
    big_number(D, 'Bonus · The one-person company', '1 human', 'Kopi Kaki Co. decides to run as a one-person company.',
               'You are the founder, the Board and the only employee with a pulse. An AI CEO runs the day-to-day, hires a Chief of Staff, '
               'and the Chief of Staff hires the marketing team. Your job: set the mission, approve the hires, approve what goes public.')
    before_after(D, 'Bonus · What is Paperclip?', 'Kanban Organises Tasks. Paperclip Organises People.',
                 'Paperclip (open source) runs a company of AI agents: org chart, job titles, reporting lines, budgets and an approval inbox.',
                 ('Hermes Kanban (Activities 4–5)', 'You are the manager', ['You create every card and every dependency.', 'You decide who does what.', 'Budgets and hiring are not modelled.']),
                 ('Paperclip company (bonus)', 'You are the Board', ['A CEO agent breaks goals into tasks and hires.', 'Hires wait in your approval inbox.', 'Each agent has a budget and a manager.']),
                 tipt='Paperclip runs on agents you already have: Hermes, Claude Code, Codex or Gemini CLI become its “adapters”.')
    tag(D, 'ARCH', PC)
    image(D, 'Bonus · Install', 'Install Paperclip: One Command, Then localhost:3100', asset('paperclip', 'dashboard.png'),
          caption='npx paperclipai onboard --yes  →  open http://localhost:3100. Trainer’s demo company shown; you build Kopi Kaki Co. the same way.',
          side=[('terminal', 'Prerequisite', 'Node.js 24.11+ and one signed-in agent CLI (Hermes from Topic 2 works).'),
                ('server', 'Install', 'npx paperclipai onboard --yes (or Docker Compose).'),
                ('building', 'Company', 'Wizard: name it Kopi Kaki Co.; first agent Ava.')])
    image(D, 'Bonus · Set up the company', 'Kopi Kaki Co.: Mission, Budget, Hiring Gate', asset('paperclip', 'company-settings.png'),
          caption='Company settings hold the name, mission and budget. Then Settings → General → Hiring → “Require board approval for new hires” = ON.')
    s = D.new(); header(D, s, 'Bonus · The CEO', 'Write the CEO’s Job Description Before You Give Her Work',
                        'Agents → Ava → Instructions → AGENTS.md. These instructions steer every decision she makes.')
    card(s, .6, 2.35, 7.7, 4.4, fill=K.CODEBG)
    text(s, .85, 2.5, 7.3, 4.15, 'You are Ava, CEO of Kopi Kaki Co., a Singapore kopi startup run as a one-person company:\nthe founder is the Board and the only human.\n\n'
         'Mission: launch the Gula Melaka Cold Brew on 1 Dec 2026.\n\n- You do not do the marketing work. You hire and manage.\n- First hire: a Chief of Staff who runs the marketing team.\n'
         '- Every hire: mandate, reporting line, budget, Board approval.\n- Every public item: independent reviewer, then the Board.\n- Report weekly: progress, spend, risks, decisions.',
         12.5, 'F1EDE4', font=K.MONO, minpt=9, cw=.62, lh=1.12)
    for i, (ic, t, d) in enumerate([('briefcase', 'Role: CEO', 'Set with the CLI: agent update … role ceo'), ('file', 'Source files', 'Upload brand guide, brief, compliance rules'),
                                    ('gavel', 'First task', '“Hire a Chief of Staff” — it lands in your approval inbox')]):
        y = 2.45 + i * 1.45; icon(s, ic, 8.65, y, .52)
        text(s, 9.3, y - .03, 3.4, .4, t, 15, INK, bold=True, font=SERIF); text(s, 9.3, y + .4, 3.4, .9, d, 12, MUTED, minpt=9)
    tag(D, 'PROMPT', 'Bonus lab prompt; ' + PC)
    flow(D, 'Bonus · Delegated hiring', 'The CEO Hires a Chief of Staff; the Chief of Staff Hires the Team', [
        ('user', 'You', 'Task to Ava: hire a Chief of Staff.'), ('briefcase', 'CEO', 'Proposes mandate, budget, reporting line.'),
        ('gavel', 'Board', 'You approve in Pending Approvals.'), ('users', 'Chief of Staff', 'Proposes six marketing hires.'),
        ('gavel', 'Board', 'Approve, revise or reject each.')],
        sub='Managers propose; only the Board approves. That is how a one-person company keeps control.')
    image(D, 'Bonus · Org chart', 'Your One-Person Company on One Page', asset('paperclip', 'org-chart.png'),
          caption='Agents → Org chart view: Board → CEO → Chief of Staff → marketing team. Trainer’s demo company shown; yours shows the Kopi Kaki roles.')
    image(D, 'Bonus · Deliver', 'The Team Produces the Launch Video', asset('paperclip', 'tasks-board.png'),
          caption='Give the Chief of Staff the Activity 5 brief. Sub-tasks move through Todo → In Progress → In Review → Done, with your approvals in between.')
    table(D, 'Bonus · Compare', 'Same Video, Two Ways: Hermes Kanban vs Paperclip', ['', 'Hermes Kanban team (Activity 5)', 'Paperclip company (bonus)'],
          [('Who breaks down the work', 'You create every card and parent', 'The CEO and Chief of Staff create tasks'),
           ('Who decides the team', 'You create the profiles', 'Managers propose hires; you approve'),
           ('Control', 'HUMAN cards on the board', 'Approval inbox, budgets, hiring gate'),
           ('Visibility', 'Board, run history, files', 'Org chart, audit log, costs per agent'),
           ('Best for', 'A known pipeline you want to run exactly', 'An ongoing operation you want to delegate and govern')],
          colw=[2.6, 4.75, 4.75], size=13, tipt='Write comparison.md in the bonus lab: which would you use for Kopi Kaki next month, and why?')
    tag(D, 'EVIDENCE', 'Learner comparison; ' + PC + ' ; ' + HK)

# ---------------------------------------------------------------- multi-agent communication (trainer slides, v3.3 hand edit → native)
ACP = 'https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/'

def multi_intro(D):
    """General introduction to multiple agents (trainer request): why a team, and what every agent owns."""
    before_after(D, 'Topic 3 · Multiple agents', 'From One Employee to a Team of Agents',
                 'A multi-agent system splits one big goal into specialist jobs that hand work to each other — with a human in charge.',
                 ('One agent (Topic 2)', 'Mia does everything', ['One context window fills up with every task.', 'One set of instructions for every voice and job.', 'Jobs run one after another.']),
                 ('Multiple agents (Topic 3)', 'A team of specialists', ['Each agent sees only what its job needs.', 'Each has its own instructions, skills and tools.', 'Independent jobs run in parallel; a board tracks hand-offs.']),
                 tipt='More agents also means more hand-offs to check. Use a team when the jobs are truly different, not just because you can.')
    tag(D, 'CONCEPT', 'Course design; Hermes profiles and Kanban docs')
    s = D.new(); header(D, s, 'Topic 3 · Multiple agents', 'Every Agent Brings Its Own Five Things',
                        'In Hermes each agent is a profile. Change any of the five and you get a different employee.')
    five = [('tool', 'Tools', 'What it can do', 'web, terminal, image, voice …', 'image-creator: image tool on'),
            ('puzzle', 'Unique skills', 'How it does the job well', 'its own SKILL.md set', 'video-producer: hyperframes'),
            ('brain', 'Model', 'How it thinks', 'big or small, any provider', 'researcher: a careful model'),
            ('file', 'Instructions', 'Who it is and its rules', 'SOUL.md + AGENTS.md', 'reviewer: never approves for you'),
            ('layers', 'Context window', 'What it is holding in mind', 'its own memory and session', 'writers never see each other’s drafts')]
    for i, (ic, t, q, how, eg) in enumerate(five):
        x = .6 + i * 2.46; dark = i % 2 == 1
        card(s, x, 2.4, 2.3, 4.0, fill=CHAR if dark else WHITE)
        icon(s, ic, x + .85, 2.65, .62, fill=ACC)
        text(s, x + .15, 3.45, 2.0, .45, t, 17, WHITE if dark else INK, bold=True, font=SERIF, align='c', minpt=12)
        text(s, x + .15, 3.95, 2.0, .55, q, 12, ACC, bold=True, align='c', minpt=9)
        text(s, x + .15, 4.55, 2.0, .75, how, 12, SOFT if dark else MUTED, align='c', minpt=9)
        text(s, x + .15, 5.35, 2.0, .9, eg, 11, LIGHT if dark else INK, align='c', minpt=8.5)
    tip(D, s, 'hermes profile create <name> --clone, then edit its SOUL.md, skills, tools and model. Its context window starts empty and stays its own.', y=6.55)
    tag(D, 'ARCH', HP)

def each_can(D):
    s = D.new(dark=True); header(D, s, 'Topic 3 · How agents talk', 'Each Agent Can…',
                                 'That is why a team beats one big agent: every member is set up differently. In Hermes, each profile is one member.')
    for i, (ic, t, kk) in enumerate([('tool', 'have different tools', 'image-creator has the image tool; researcher has web search.'),
                                     ('brain', 'access different knowledge', 'facebook-writer knows the pop-up dates; linkedin-writer knows the founder story.'),
                                     ('lock', 'operate under different permissions', 'reviewer can read but not render; nobody can post — only you approve.'),
                                     ('users', 'perform distinct roles', 'each SOUL.md says what the role owns and must never do.')]):
        x = .6 + i * 3.08
        card(s, x, 2.5, 2.9, 3.85, fill=K.PANEL, shadow=False)
        icon(s, ic, x + .95, 2.8, 1.0)
        text(s, x + .2, 4.0, 2.5, .8, t, 17, WHITE, bold=True, font=SERIF, align='c', minpt=12)
        text(s, x + .25, 4.9, 2.4, 1.35, 'At Kopi Kaki: ' + kk, 12, SOFT, align='c', minpt=9)
    tag(D, 'CONCEPT', 'Trainer slide (v3.3 hand edit) recreated; Hermes profiles docs')

def handoff(D):
    s = D.new(dark=True); header(D, s, 'Topic 3 · How agents talk', '“My order arrived damaged. I need a replacement.”',
                                 'One customer message, four agents, one outcome. Each hands a structured message to the next.')
    ag = [('user', 'Support Agent', 'Understands the complaint, checks the order, opens a case.'),
          ('box', 'Logistic Agent', 'Checks stock and reserves a replacement item.'),
          ('send', 'Shipping Agent', 'Books the courier and returns a tracking number.'),
          ('loop', 'Customer Agent', 'Confirms the fix to the customer and asks for a rating.')]
    w = 2.75; gap = .37
    for i, (ic, t, d) in enumerate(ag):
        x = .6 + i * (w + gap)
        card(s, x, 2.55, w, 3.2, fill=K.PANEL, shadow=False)
        icon(s, ic, x + .85, 2.8, 1.05)
        text(s, x + .15, 4.0, w - .3, .45, t, 17, WHITE, bold=True, font=SERIF, align='c', minpt=12)
        text(s, x + .2, 4.5, w - .4, 1.15, d, 12.5, SOFT, align='c', minpt=9.5)
        if i < len(ag) - 1: line(s, x + w + .03, 4.15, x + w + gap - .03, 4.15, ACC, 2.25, arrow=True)
    tip(D, s, 'At Kopi Kaki: “My cold brew pre-order arrived spilled.” Same four hand-offs. A refund above SGD 20 waits for you: human in the loop.', y=6.1)
    tag(D, 'CONCEPT', 'Trainer slide (v3.3 hand edit) recreated')

def acp(D):
    s = D.new(dark=True); header(D, s, 'Topic 3 · How agents talk', 'What Is the Agent Communication Protocol?')
    card(s, .6, 2.0, 2.6, 2.6, fill=K.PANEL, shadow=False); icon(s, 'chat', 1.2, 2.6, 1.4)
    text(s, 3.6, 2.0, 9.1, 2.7, 'Agent Communication Protocol, or ACP, is a standardised framework that enables AI agents to communicate in a structured, '
         'secure and predictable way by defining how they exchange messages, interpret intent, share context, and coordinate actions reliably at scale.',
         20, WHITE, font=SERIF, minpt=14, lh=1.25)
    for i, (t, d) in enumerate([('Mar 2025', 'IBM Research launches ACP for its open-source BeeAI platform.'),
                                ('2025', 'BeeAI and ACP are donated to the Linux Foundation.'),
                                ('Aug 2025', 'ACP merges into the A2A (Agent2Agent) protocol: one open standard for agents to call agents.')]):
        x = .6 + i * 4.1
        text(s, x, 5.0, 3.9, .45, t, 18, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x, 5.45, 3.85, .9, d, 12.5, SOFT, minpt=9.5)
    text(s, .6, 6.55, 12, .26, 'Source: LF AI & Data Foundation, “ACP Joins Forces with A2A”, 29 Aug 2025; IBM Research ACP project page.', 10, SOFT, autofit=False)
    tag(D, 'CONCEPT', ACP + ' ; https://research.ibm.com/projects/agent-communication-protocol')

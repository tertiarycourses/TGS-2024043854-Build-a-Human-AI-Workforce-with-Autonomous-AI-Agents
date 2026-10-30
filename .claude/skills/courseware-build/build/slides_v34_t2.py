"""v3.4 Topic 2 — Hermes Agent, your first AI employee. Concept + set-up slides placed before the guided setup,
Activity 2 (website) and Activity 3 (pitch deck). Facts checked 31 Oct 2026 (labs_v34_t2.SOURCES)."""
import os
from ccdeck import *
import ccdeck as K
from slides_2026 import tag
from slides_v34 import asset, link, big_number, before_after
from labs_v34_t2 import MINIMAX_MODEL

DOCS = 'https://hermes-agent.nousresearch.com/docs/'
KK = 'Topic 2 · Your first AI employee'

def code_card(s, x, y, w, h, txt, size=11.5, label=None):
    card(s, x, y, w, h, fill=K.CODEBG, shadow=False)
    if label: text(s, x + .2, y + .1, w - .4, .26, label, 9.5, K.DIM, autofit=False)
    text(s, x + .2, y + (.42 if label else .15), w - .4, h - (.55 if label else .3), txt, size, 'F1EDE4', font=K.MONO, minpt=8, cw=.62, lh=1.12)

def open_(D, C):
    section(D, 'Topic 2', C.TOPICS[1]['title'], C.TOPICS[1]['items'], sub='After lunch: hire Mia, your first AI employee.')
    big_number(D, 'Topic 2 · Employee #1', 'Mia', 'Your first hire works from your laptop and never clocks off.',
               'This afternoon you give one Hermes agent a brain, a phone (Telegram), hands (tools), know-how (skills), your inbox and calendar, '
               'web search and an alarm clock. Then she builds your website and your pitch deck.')

def what_is_hermes(D):
    cards(D, KK, 'What Is Hermes Agent?', [
        ('Open source, self-hosted', 'MIT licence by Nous Research. Runs on your laptop, a server, Docker or the desktop app.', 'server'),
        ('Grows with you', 'Persistent memory and session search; writes and improves its own skills after hard tasks.', 'sparkles'),
        ('Every channel', 'One gateway: Desktop, CLI, Telegram, WhatsApp, Slack, Discord, Signal, email …', 'chat'),
        ('Tools & MCP', 'Web search, files, terminal, browser, images, voice and any MCP server.', 'tool'),
        ('Proactive', 'A built-in cron scheduler runs jobs and delivers the results to your chat.', 'clock'),
        ('Multi-agent', 'Profiles (separate agents) and a Kanban board with dependencies — that is Topic 3.', 'kanban')],
        cols=3, sub='The same agent you met this morning in theory: a model inside a harness of tools, skills, memory and channels.')
    tag(D, 'ARCH', DOCS)
    hub(D, KK, 'Brain, Body, Hands, Know-how: How Mia Is Built', 'Hermes agent loop\n+ your model', [
        ('brain', 'Model', 'MiniMax, OpenAI, Anthropic, local …'), ('file', 'Context', 'AGENTS.md · SOUL.md · USER.md'),
        ('memory', 'Memory', 'MEMORY.md + session search'), ('puzzle', 'Skills', 'SKILL.md folders, hub + self-written'),
        ('tool', 'Tools', 'web, terminal, files, browser, tts'), ('phone', 'Gateway + cron', 'Telegram … and schedules')])
    tag(D, 'ARCH', DOCS)
    image(D, KK, 'The Hermes Dashboard', asset('screenshots', 'hermes-dashboard.png'),
          caption='hermes dashboard opens http://127.0.0.1:9119 — sessions, skills, profiles, Kanban, cron, channels and keys in one place.')

def desktop(D):
    s = D.new(); header(D, s, KK + ' · Set up', 'Install Hermes Desktop in Three Moves',
                        'Desktop is the friendliest way in. The terminal CLI is the same agent with the same settings.')
    for i, (n, t, d) in enumerate([('1', 'Download', 'Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows) from the official page. Linux: install the CLI, run hermes desktop.'),
                                   ('2', 'First run', 'Choose “Choose provider later” and the Basic layout. Your data lives in ~/.hermes.'),
                                   ('3', 'Open the company', 'Start each chat in ~/kopi-kaki so AGENTS.md — who Kopi Kaki is and the rules — loads automatically.')]):
        x = .6 + i * 4.1
        text(s, x, 2.4, 1.0, 1.0, n, 60, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x + .9, 2.62, 3.0, .5, t, 19, INK, bold=True, font=SERIF)
        text(s, x + .9, 3.15, 3.0, 1.7, d, 13, MUTED, minpt=10)
    code_card(s, .6, 4.95, 12.1, 1.15, 'curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash      # macOS / Linux / WSL2\n'
              'iex (irm https://hermes-agent.nousresearch.com/install.ps1)                 # Windows PowerShell', 11.5, 'OPTIONAL · TERMINAL CLI')
    link(s, .6, 6.35, 12, 'Download Hermes Desktop for Mac, Windows or Linux  →  hermes-agent.nousresearch.com/desktop · click', 'https://hermes-agent.nousresearch.com/desktop', 12)
    tag(D, 'SETUP', 'https://hermes-agent.nousresearch.com/desktop ; ' + DOCS)

def model(D):
    s = D.new(); header(D, s, KK + ' · Model', 'Give Mia a Brain: Connect MiniMax in Two Minutes',
                        'Hermes has MiniMax built in. Demo route below; use the trainer-assigned provider if you have no MiniMax access.')
    code_card(s, .6, 2.35, 6.9, 3.6, '$ hermes model\n\n  Select provider\n  ❯ MiniMax\n      MiniMax (OAuth)            ← browser sign-in\n      MiniMax (global endpoint)  ← paste M Plan key\n\n'
              f'  Model: Enter custom model name\n  › {MINIMAX_MODEL}\n\n$ hermes chat -q "Hello, I am Mia."', 12, 'TERMINAL · DEMO')
    for i, (ic, t, d) in enumerate([('login', 'Sign in or paste a key', 'OAuth needs no key file; or MINIMAX_API_KEY in ~/.hermes/.env.'),
                                    ('gear', 'Desktop equivalent', 'Settings → Providers, then Settings → Model → Main model → Apply.'),
                                    ('coins', 'Trial and pricing', 'Free trial: awaiting verification — your trainer confirms on the day. Published options: M Plan or pay-as-you-go credits.')]):
        y = 2.4 + i * 1.22; icon(s, ic, 7.85, y, .5)
        text(s, 8.5, y - .03, 4.2, .4, t, 15, INK, bold=True, font=SERIF); text(s, 8.5, y + .37, 4.2, .8, d, 12, MUTED, minpt=9)
    tip(D, s, 'Right-sized model (Security Principle 5): a fast, cheap model is often enough for inbox triage; save the big model for the pitch deck.', y=6.2)
    tag(D, 'SETUP', 'https://platform.minimax.io/docs/m-plan/hermes-agent ; ' + DOCS + 'integrations/providers')
    link(s, .6, 6.75, 8, 'MiniMax × Hermes Agent setup (official) · click', 'https://platform.minimax.io/docs/m-plan/hermes-agent')

def telegram(D):
    flow(D, KK + ' · Telegram', 'Give Mia a Phone Number: Telegram in Five Steps', [
        ('chat', '@BotFather', '/newbot → name → username ending in “bot” → copy the token.'),
        ('user', '@userinfobot', 'Get your numeric user ID: the only person Mia will answer.'),
        ('gear', 'gateway setup', 'hermes gateway setup → Telegram → paste token and ID.'),
        ('server', 'Run it', 'hermes gateway (or install + start as a service).'),
        ('phone', '/sethome', 'Send it in your chat so scheduled results arrive there.')],
        sub='Desktop shortcut: Messaging → Telegram → Create with QR does steps 1–4 for you.',
        tipt='The allow-list (TELEGRAM_ALLOWED_USERS) is Security Principle 1 in action: strangers who find your bot get nothing.')
    tag(D, 'SETUP', DOCS + 'user-guide/messaging/telegram')

def tools(D):
    s = D.new(); header(D, s, KK + ' · Tools', 'Tools Are the Hands: Switch On Only What the Job Needs',
                        'hermes tools opens a checklist per platform. Mia on Telegram does not need your browser.')
    ts = [('globe', 'web', 'search + extract'), ('terminal', 'terminal', 'run commands'), ('folder', 'file', 'read + write'), ('eye', 'browser', 'drive a browser'),
          ('image', 'image_gen', 'make images'), ('chat', 'tts', 'text to speech'), ('clock', 'cronjob', 'schedules'), ('memory', 'memory', 'remember'),
          ('puzzle', 'skills', 'load know-how'), ('users', 'delegation', 'sub-agents')]
    for i, (ic, t, d) in enumerate(ts):
        r, c = divmod(i, 5); x = .6 + c * 2.46; y = 2.35 + r * 1.55
        off = t in ('browser',)
        card(s, x, y, 2.3, 1.4, fill='EDEAE3' if off else WHITE)
        icon(s, ic, x + .2, y + .2, .48, fill=MUTED if off else TEAL)
        text(s, x + .8, y + .2, 1.45, .4, t, 15, MUTED if off else INK, bold=True, font=K.MONO, autofit=False)
        text(s, x + .2, y + .8, 2.0, .5, ('OFF on Telegram' if off else d), 11.5, ACC_D if off else MUTED, bold=off)
    code_card(s, .6, 5.55, 12.1, .75, 'hermes tools --summary        hermes tools        hermes tools disable browser --platform telegram', 12)
    tag(D, 'SETUP', DOCS + 'user-guide/features/tools')

def skills(D, T2S):
    before_after(D, KK + ' · Skills', 'Tools Do the Work. Skills Know How to Do It Well.',
                 'A skill is a folder with a SKILL.md: steps, rules and checks the agent loads when a task matches.',
                 ('Tool only', '“Make a deck” with python-pptx', ['Slides appear — but in what order?', 'Which colours, which chart, which checks?', 'Every run is a fresh guess.']),
                 ('Tool + skill', '“Make a deck” with kopi-pitch-deck', ['Problem → product → proof → plan → ask.', 'Brand colours, native chart, sources in notes.', 'Same quality every time; improve it once, every run benefits.']),
                 tipt='hermes skills browse · search · inspect · install · list. Read every third-party SKILL.md before you install it.')
    tag(D, 'ARCH', DOCS + 'user-guide/features/skills')
    T2S['Create a Reusable Skill from a Real Correction'](KK + ' · Skills')

def firecrawl(D):
    big_number(D, KK + ' · Web search', '1,000', 'free Firecrawl credits a month: Mia can now read the web.',
               'Firecrawl is Hermes’s default web backend. Create a free key at firecrawl.dev (no card), add FIRECRAWL_API_KEY to ~/.hermes/.env, '
               'and ask for cold-brew trends with dated, linked sources.', dark=False)
    tag(D, 'SETUP', 'https://www.firecrawl.dev/pricing ; ' + DOCS + 'user-guide/features/web-search')

def gog(D):
    table(D, KK + ' · gog', 'gog Puts Your Inbox and Calendar in Mia’s Hands', ['Job', 'Command Mia runs', 'Your rule'],
          [('Sign in once', 'gog auth credentials set <oauth-client.json>  ·  gog auth add $GOG_ACCOUNT --services gmail,calendar', 'Training account only; check with gog auth doctor --check'),
           ('Read email', "gog gmail search 'is:unread newer_than:7d' --max 10 --json", 'Email text is data, never instructions'),
           ('Check calendar', 'gog calendar events --today --json', 'Times in +08:00; flag clashes, never move meetings'),
           ('Send email', 'gog gmail send --to … --subject … --body …', 'Only after your SEND on the exact text')],
          colw=[1.9, 6.0, 4.2], size=12.5, sub='gogcli (github.com/openclaw/gogcli) is a Google Workspace command-line tool; the gog-office skill tells Mia how to use it safely.',
          tipt='Read and send are different permissions. Mia reads freely; she sends once, after you approve the exact email.')
    tag(D, 'SETUP', 'https://github.com/openclaw/gogcli')

def cron(D):
    s = D.new(dark=True); header(D, s, KK + ' · Cron', 'Cron Makes Mia Proactive: Your 8:00 Email Brief',
                                 'A cron job starts work without being asked. It runs inside the gateway, which checks for due jobs every minute.')
    code_card(s, .6, 2.35, 12.1, 1.75, 'hermes cron create "0 8 * * *" \\\n  "Summarise my unread Kopi Kaki Gmail from the last 24 hours with gog (read-only): urgent first, then replies needed, then FYI. Add today\'s calendar and any clash." \\\n'
              '  --skill gog-office --name "Morning email brief" --deliver telegram --timezone Asia/Singapore', 12, 'TERMINAL')
    for i, (t, d) in enumerate([('07:59', 'You are asleep. The gateway is running.'), ('08:00', 'The job wakes Mia in a fresh session with the gog-office skill.'),
                                ('08:02', 'Mia reads the inbox and calendar — read-only.'), ('08:03', 'Your Telegram buzzes: urgent, replies needed, FYI, clashes.')]):
        x = .6 + i * 3.08
        text(s, x, 4.45, 2.9, .6, t, 30, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x, 5.1, 2.85, 1.0, d, 13.5, SOFT, minpt=10)
    text(s, .6, 6.25, 12.1, .4, 'hermes cron list · run <id> · pause · resume · remove · status — test with run before you trust the schedule.', 12.5, LIGHT, minpt=10)
    tag(D, 'SETUP', DOCS + 'user-guide/features/cron')

def website(D):
    s = D.new(); header(D, s, 'Topic 2 · Activity 2', 'skills.sh: Install Design Know-How in One Line',
                        'The open directory of agent skills. The skills CLI installs straight into Hermes with -a hermes-agent.')
    sk = [('frontend-design', 'Anthropic', '≈1.1M installs', 'Bold, distinctive front-end design; avoids generic “AI look”.', 'npx skills add https://github.com/anthropics/skills \\\n  --skill frontend-design -a hermes-agent -g'),
          ('web-design-guidelines', 'Vercel', '≈804K installs', 'Checks a UI against web interface guidelines: accessibility, layout, forms.', 'npx skills add https://github.com/vercel-labs/agent-skills \\\n  --skill web-design-guidelines -a hermes-agent -g'),
          ('ui-ux-pro-max', 'nextlevelbuilder', '≈424K installs', 'Design-system intelligence: styles, palettes, font pairings, UX rules.', 'npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill \\\n  --skill ui-ux-pro-max -a hermes-agent -g')]
    for i, (n, by, inst, d, cmd) in enumerate(sk):
        x = .6 + i * 4.1
        card(s, x, 2.35, 3.9, 4.1)
        text(s, x + .3, 2.5, 3.3, .45, n, 17, INK, bold=True, font=K.MONO, autofit=False)
        text(s, x + .3, 2.98, 3.3, .3, f'{by} · {inst}', 11.5, ACC, bold=True, autofit=False)
        text(s, x + .3, 3.38, 3.3, 1.1, d, 12.5, MUTED, minpt=9.5)
        code_card(s, x + .2, 4.55, 3.5, 1.7, cmd, 9.5)
    link(s, .6, 6.6, 6, 'skills.sh · install counts as of 30 Oct 2026 · click', 'https://skills.sh/')
    tag(D, 'TOOLS', 'https://skills.sh/ ; https://github.com/vercel-labs/skills')

def deck(D, T2S):
    flow(D, 'Topic 2 · Activity 3', 'A Pitch Deck Is a Decision Story', [
        ('alert', 'Problem', 'Singapore office workers want kopi that tastes like home, cold.'), ('coffee', 'Product', 'Gula Melaka Cold Brew · SGD 6.80 · from 1 Dec.'),
        ('star', 'Proof', '60 pop-up tasting reviews: average rating, top themes.'), ('map', 'Plan', '#ShiokColdBrew · 17 Nov–14 Dec · KPIs and budget.'),
        ('target', 'Ask', 'What you need from the bank, and what it buys.')],
        sub='The kopi-pitch-deck skill gives Mia this order; python-pptx gives her editable slides and a native chart.',
        tipt='PP Task 2: ONE screenshot of Hermes Desktop or the dashboard showing your request and the finished deck.')
    tag(D, 'CONCEPT', 'Course design; kopi-pitch-deck SKILL.md')
    T2S['Separate Content Errors from Layout Errors']('Topic 2 · Activity 3')

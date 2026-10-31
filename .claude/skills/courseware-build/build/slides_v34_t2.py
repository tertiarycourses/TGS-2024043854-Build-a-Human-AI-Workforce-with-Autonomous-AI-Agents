"""Topic 2 — Hermes Agent, your first AI employee (v3.5: Hermes Desktop only, no command lines).
Screens are the trainer's Hermes Desktop v0.22.5 screenshots (courseware/assets/screenshots/desktop/, 31 Oct 2026).
Nous Portal tiers checked at portal.nousresearch.com on 31 Oct 2026."""
import os
from ccdeck import *
import ccdeck as K
from slides_2026 import tag
from slides_v34 import asset, link, big_number, before_after

DOCS = 'https://hermes-agent.nousresearch.com/docs/'
PORTAL = 'https://portal.nousresearch.com/'
KK = 'Topic 2 · Your first AI employee'
def shot(n): return asset('screenshots', 'desktop', n + '.png')

def code_card(s, x, y, w, h, txt, size=11.5, label=None):
    card(s, x, y, w, h, fill=K.CODEBG, shadow=False)
    if label: text(s, x + .2, y + .1, w - .4, .26, label, 9.5, K.DIM, autofit=False)
    text(s, x + .2, y + (.42 if label else .15), w - .4, h - (.55 if label else .3), txt, size, 'F1EDE4', font=K.MONO, minpt=8, cw=.62, lh=1.12)

def open_(D, C):
    section(D, 'Topic 2', C.TOPICS[1]['title'], C.TOPICS[1]['items'], sub='After lunch: hire Mia, your first AI employee. One app, no command line.')
    big_number(D, 'Topic 2 · Employee #1', 'Mia', 'Your first hire works from your laptop and never clocks off.',
               'This afternoon you give one Hermes agent a brain, a phone (Telegram), a voice, hands (tools), know-how (skills), your Gmail, '
               'web search and an alarm clock — all from the Hermes Desktop window. Then she builds your website and your pitch deck.')

def what_is_hermes(D):
    cards(D, KK, 'What Is Hermes Agent?', [
        ('Open source, on your laptop', 'MIT licence by Nous Research. Hermes Desktop is the app: install it like any other.', 'server'),
        ('Grows with you', 'Persistent memory and session search; writes and improves its own skills after hard tasks.', 'sparkles'),
        ('Every channel', 'Desktop, Telegram, WhatsApp, Slack, Discord, Signal, email … one agent behind all of them.', 'chat'),
        ('Tools & connectors', 'Web search, files, browser, images, voice, and 100+ apps such as Gmail.', 'tool'),
        ('Proactive', 'Scheduled jobs run on their own and deliver the result to your chat.', 'clock'),
        ('Multi-agent', 'Bots, group chats and a Kanban board — that is Topic 3.', 'kanban')],
        cols=3, sub='The same agent you met this morning in theory: a model inside a harness of tools, skills, memory and channels.')
    tag(D, 'ARCH', DOCS)
    hub(D, KK, 'Brain, Body, Hands, Know-how: How Mia Is Built', 'Hermes Desktop\n+ your model', [
        ('brain', 'Model', 'ChatGPT Plus, Nous free models …'), ('file', 'Context', 'AGENTS.md in your kopi-kaki folder'),
        ('memory', 'Memory', 'What she chose to remember'), ('puzzle', 'Skills', 'Capabilities → Skills'),
        ('tool', 'Tools & connectors', 'web, files, voice, Gmail'), ('phone', 'Messaging + schedules', 'Telegram … and Scheduled jobs')])
    tag(D, 'ARCH', DOCS)
    image(D, KK, 'Hermes Desktop at a Glance: Everything Is One Click Away', shot('skills'),
          side=[('chat', 'New session', 'Talk to Mia; pick the working folder.'), ('puzzle', 'Capabilities', 'Skills, Plugins, Connectors, Tools.'),
                ('phone', 'Messaging', 'Telegram, WhatsApp, email …'), ('clock', 'Scheduled jobs', 'Mia starts work on time.'),
                ('kanban', 'Kanban · Bots', 'Your Day 2 teams live here.')],
          caption='The left sidebar is your control panel. You will not open a terminal in this course: Mia runs the technical steps for you.')

def desktop(D):
    s = D.new(); header(D, s, KK + ' · Set up', 'Install Hermes Desktop in Three Moves',
                        'Download, open, check the version. If you can install Zoom, you can install your first AI employee.')
    for i, (n, t, d) in enumerate([('1', 'Download', 'Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows) from the official page.'),
                                   ('2', 'First run', 'Choose “Choose provider later” and the Basic layout.'),
                                   ('3', 'Check', 'Settings → About → Version & updates: “You’re running the latest version.”')]):
        y = 2.3 + i * 1.3
        text(s, .6, y - .1, .8, 1.0, n, 50, ACC, bold=True, font=SERIF, autofit=False)
        text(s, 1.45, y, 3.9, .45, t, 18, INK, bold=True, font=SERIF)
        text(s, 1.45, y + .45, 3.9, .8, d, 12.5, MUTED, minpt=10)
    picture(s, shot('version'), 5.75, 2.3, maxw=6.95, maxh=4.15)
    link(s, .6, 6.55, 12, 'Download Hermes Desktop for Mac or Windows  →  hermes-agent.nousresearch.com/desktop · click', 'https://hermes-agent.nousresearch.com/desktop', 12)
    tag(D, 'SETUP', 'https://hermes-agent.nousresearch.com/desktop ; trainer screenshot, Hermes Desktop v0.22.5')

def folder(D):
    """Hand Mia the company rulebook: + → Folder… attaches the kopi-kaki folder (with AGENTS.md) to the session. No command line."""
    s = D.new(); header(D, s, KK + ' · Set up', 'Hand Mia the Company Rulebook: + → Folder…',
                        'AGENTS.md is your company rulebook. Attach the folder that holds it, and tell Mia to follow it.')
    steps = [('1', 'Fill the folder', 'Drag this lab’s data/ files into kopi-kaki on your Desktop. AGENTS.md comes with them.'),
             ('2', 'Attach it: + → Folder…', 'In the chat box click + (left of “Ask anything”) → Folder… → choose kopi-kaki.'),
             ('3', 'Ask Mia to follow it', 'Send the prompt on the right. Her three bullets must match AGENTS.md.')]
    for i, (n, t, d) in enumerate(steps):
        y = 2.35 + i * 1.12
        text(s, .6, y - .08, .7, .9, n, 40, ACC, bold=True, font=SERIF, autofit=False)
        text(s, 1.3, y, 4.6, .4, t, 17, INK, bold=True, font=SERIF)
        text(s, 1.3, y + .42, 4.6, .62, d, 12, MUTED, minpt=9.5)
    card(s, 6.3, 2.35, 6.4, 1.75, fill=K.CHAR)
    text(s, 6.55, 2.47, 5.9, .26, 'ATTACH', 9.5, K.DIM, bold=True, autofit=False)
    for i, (ic, t) in enumerate([('file', 'Files…'), ('folder', 'Folder…'), ('image', 'Images…'), ('globe', 'URL…')]):
        x = 6.55 + i * 1.5; hi = t == 'Folder…'
        card(s, x, 2.85, 1.38, .95, fill=ACC_D if hi else K.PANEL, shadow=False)
        s.shapes.add_picture(K.icon_png(ic, WHITE), Inches(x + .5), Inches(2.93), Inches(.38), Inches(.38))
        text(s, x, 3.36, 1.38, .32, t, 12, WHITE, bold=hi, align='c', autofit=False)
    code_card(s, 6.3, 4.3, 6.4, 1.75, 'Read AGENTS.md in the attached folder and follow it for this session. '
              'In three bullets: who Kopi Kaki is and the rules you must never break.', 12.5, 'FIRST PROMPT IN EVERY NEW SESSION')
    tip(D, s, 'Do this at the start of every lab: + → Folder… → kopi-kaki. Type @ to point Mia at one file, e.g. @AGENTS.md.', y=6.45)
    tag(D, 'SETUP', 'https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files ; trainer screenshot (chat box + → Attach)')

def model(D):
    s = D.new(); header(D, s, KK + ' · Provider and model', 'Provider and Model: Free Solar Mini 4 or Your ChatGPT Plus',
                        'The provider serves the model; the model is Mia’s brain. Start free on Nous Portal, or use the ChatGPT Plus plan this class runs on.')
    routes = [('FREE · NOUS PORTAL', 'Upstage Solar Mini 4 · $0', 'Status bar → Sign in (free Nous account) → Settings → Model → Provider: Nous Portal → Solar Mini 4.', False),
              ('PAID · THIS CLASS', 'Your ChatGPT Plus plan', 'Settings → Model → Provider: “ChatGPT or Codex Subscription” → sign in → pick a model → Apply.', True),
              ('WANT MORE?', 'Nous paid plans', 'Nous Portal Plus USD 20/month (Super 100, Ultra 200), or another provider’s key in Settings → Providers.', False)]
    for i, (lab, t, d, hi) in enumerate(routes):
        y = 2.3 + i * 1.38
        card(s, .6, y, 5.0, 1.25, fill=CHAR if hi else WHITE)
        text(s, .85, y + .1, 4.5, .28, lab, 10.5, ACC, bold=True, autofit=False)
        text(s, .85, y + .36, 4.5, .4, t, 16, WHITE if hi else INK, bold=True, font=SERIF, minpt=11)
        text(s, .85, y + .76, 4.6, .45, d, 11, SOFT if hi else MUTED, minpt=8.5)
    picture(s, shot('model'), 5.95, 2.3, maxw=6.75, maxh=4.0)
    tip(D, s, 'Solar Mini 4 is the most-used free model on Nous Portal (31 Oct 2026). “Applies to” sets the brain per bot: right-sized models are Principle 5.', y=6.45)
    tag(D, 'SETUP', PORTAL + ' ; https://portal.nousresearch.com/models (Upstage: Solar Mini 4 — FREE, checked 31 Oct 2026; also free: Beam 1.0, Step 3.7 Flash, Ornith 1.5) ; trainer screenshot')

def _shot_or(n, fallback):
    return shot(n) if os.path.exists(shot(n)) else shot(fallback)

def telegram(D):
    """Telegram, two ways: Quick setup (Create with QR) or the manual BotFather method."""
    s = D.new(); header(D, s, KK + ' · Telegram', 'Give Mia a Phone Number: Two Ways to Create Her Telegram Bot',
                        'Left sidebar → Messaging → Telegram. The quick way takes one scan; the manual way shows you what the scan does.')
    for i, (lab, t, pts) in enumerate([
            ('QUICK · RECOMMENDED', 'Create with QR', ['Messaging → Telegram → Quick setup → Create with QR.',
                                                      'Scan the code with Telegram on your phone, or open the link on this computer (it expires in 30 minutes).',
                                                      'Confirm in Telegram. Hermes creates the bot and finds your user ID.',
                                                      'Enabled → Save changes.']),
            ('MANUAL', 'BotFather + token', ['Talk to @BotFather in Telegram: /newbot.',
                                             'Name the bot; pick a username ending in bot.',
                                             'Copy the API token BotFather gives you.',
                                             'Paste it in Bot token; add your ID from @userinfobot under Allowed Telegram user IDs.'])]):
        x = .6 + i * 3.2
        card(s, x, 2.35, 3.0, 4.05, fill=CHAR if i == 0 else WHITE)
        text(s, x + .2, 2.5, 2.6, .28, lab, 10.5, ACC, bold=True, autofit=False)
        text(s, x + .2, 2.82, 2.6, .45, t, 18, WHITE if i == 0 else INK, bold=True, font=SERIF, minpt=12)
        text(s, x + .2, 3.4, 2.65, 2.9, '\n'.join(f'{k + 1}  ' + q for k, q in enumerate(pts)), 11.5, SOFT if i == 0 else MUTED, minpt=9, lh=1.15)
    picture(s, _shot_or('telegram-qr', 'telegram-setup'), 7.1, 2.35, maxw=5.6, maxh=4.05)
    tip(D, s, 'Either way, the bot answers only approved users: you. Next slide: the manual method, step by step.', y=6.55)
    tag(D, 'SETUP', DOCS + 'user-guide/messaging/telegram ; trainer screenshots, Hermes Desktop Messaging → Telegram')
    s = D.new(dark=True); header(D, s, KK + ' · Telegram', 'The Manual Method: Create the Bot with BotFather',
                                 'Three chats with Telegram’s official bot-maker, then one paste into Hermes Desktop.')
    steps = [('chat', 'Step 1 · Talk to BotFather', ['Open Telegram and search BotFather (blue verification tick).', 'Tap Start.', 'Send /newbot.']),
             ('pen', 'Step 2 · Name your bot', ['Display name, e.g. Mia · Kopi Kaki.', 'Username ending in bot or _bot, e.g. kopikaki_mia_bot.', 'Taken? BotFather asks for another.']),
             ('lock', 'Step 3 · Get your API token', ['BotFather replies with an API token.', 'Copy it and keep it safe: it is the password to your bot.']),
             ('phone', 'Step 4 · Paste it into Hermes', ['Messaging → Telegram → Bot token: paste.', 'Allowed Telegram user IDs: your ID from @userinfobot.', 'Enabled → Save changes.'])]
    w, gap = 2.9, .17
    for i, (ic, t, pts) in enumerate(steps):
        x = .6 + i * (w + gap)
        card(s, x, 2.4, w, 3.75, fill=K.PANEL if i < 3 else ACC_D, shadow=False)
        icon(s, ic, x + .25, 2.6, .58, fill=ACC if i < 3 else CHAR)
        text(s, x + .25, 3.32, w - .45, .62, t, 15.5, WHITE, bold=True, font=SERIF, minpt=11)
        text(s, x + .25, 4.0, w - .45, 2.05, '\n'.join('•  ' + q for q in pts), 12, LIGHT if i == 3 else SOFT, minpt=9, lh=1.15)
        if i < 3: line(s, x + w + .01, 4.25, x + w + gap - .01, 4.25, ACC, 1.75, arrow=True)
    tip(D, s, 'Never paste the token into a chat, a prompt or a slide. Without an allowed user ID, anyone can message your bot.', y=6.45, label='SECURITY')
    tag(D, 'SETUP', DOCS + 'user-guide/messaging/telegram ; https://core.telegram.org/bots/features#botfather ; trainer steps')
    s = D.new(); header(D, s, KK + ' · Telegram', 'Paste the Token, Allow Only Yourself, Save',
                        'Manual method, last step: the Bot token and Allowed Telegram user IDs fields in Messaging → Telegram.')
    picture(s, _shot_or('telegram-allowed-ids', 'telegram-setup'), .6, 2.3, maxw=6.0, maxh=3.75)
    picture(s, shot('telegram-connected'), 6.9, 2.3, maxw=5.8, maxh=3.75)
    for x, t in [(.6, '1 · Bot token: paste · Allowed user IDs: your numeric ID.'),
                 (6.9, '2 · Enabled + Save changes: Connected; only you are approved.')]:
        text(s, x, 6.12, 5.9, .5, t, 12.5, INK, bold=True, minpt=10)
    tip(D, s, 'Send hi to your bot: Mia answers. Then send /sethome so scheduled results arrive in this chat. The approved-users list is Security Principle 1.', y=6.6)
    tag(D, 'SETUP', DOCS + 'user-guide/messaging/telegram ; trainer screenshots')

def voice(D):
    s = D.new(dark=True); header(D, s, KK + ' · Voice', 'Talk to Mia. Hear Her Answer.',
                                 'Settings → Voice. Speak your prompts, read the transcript, and let Mia read her replies aloud with a free voice.')
    for i, (n, t, d) in enumerate([('voice-conversation', 'Voice conversation', 'Chained: speech-to-text → Hermes → text-to-speech.'),
                                   ('speech-to-text', 'Speech to text', 'On, with Live Transcription as you speak.'),
                                   ('text-to-speech', 'Text to speech', 'Provider Edge (free) · Read Responses Aloud on.')]):
        x = .6 + i * 4.1
        picture(s, shot(n), x, 2.4, maxw=3.9, maxh=2.75)
        text(s, x, 5.35, 3.9, .4, t, 16, WHITE, bold=True, font=SERIF, minpt=11)
        text(s, x, 5.78, 3.9, .6, d, 12, SOFT, minpt=9)
    tip(D, s, 'The same free Edge voice narrates your launch video in Activity 5. Wispr Flow from Activity 1C also works in Hermes.', y=6.5)
    tag(D, 'SETUP', 'Trainer screenshots, Hermes Desktop v0.22.5 Settings → Voice')

def tools(D):
    s = D.new(); header(D, s, KK + ' · Tools', 'Tools Are the Hands: Switch On Only What the Job Needs',
                        'Capabilities → Tools shows every toolset, per bot. Mia on Telegram does not need your browser.')
    ts = [('globe', 'web', 'search + extract'), ('terminal', 'terminal', 'Mia runs it, not you'), ('folder', 'file', 'read + write'), ('eye', 'browser', 'drive a browser'),
          ('image', 'image_gen', 'make images'), ('chat', 'tts', 'text to speech'), ('clock', 'cronjob', 'schedules'), ('memory', 'memory', 'remember'),
          ('puzzle', 'skills', 'load know-how'), ('users', 'delegation', 'sub-agents')]
    for i, (ic, t, d) in enumerate(ts):
        r, c = divmod(i, 5); x = .6 + c * 2.46; y = 2.35 + r * 1.55
        off = t in ('browser',)
        card(s, x, y, 2.3, 1.4, fill='EDEAE3' if off else WHITE)
        icon(s, ic, x + .2, y + .2, .48, fill=MUTED if off else TEAL)
        text(s, x + .8, y + .2, 1.45, .4, t, 15, MUTED if off else INK, bold=True, font=K.MONO, autofit=False)
        text(s, x + .2, y + .8, 2.0, .5, ('OFF on Telegram' if off else d), 11.5, ACC_D if off else MUTED, bold=off)
    tip(D, s, 'Principle 2, permission control: every tool you switch off is one less thing that can go wrong. The terminal tool is how Mia installs things for you.', y=5.7)
    tag(D, 'SETUP', DOCS + 'user-guide/features/tools')

def skills(D, T2S):
    image(D, KK + ' · Skills', 'Install a Skill by Asking: “install the kopi pitch deck skill”', shot('install-skill-by-asking'),
          side=[('chat', 'You ask', 'One plain sentence in the chat.'), ('puzzle', 'Mia installs', 'Loads, copies and verifies the skill.'),
                ('check', 'You check', 'Readiness: available. It now shows in Capabilities → Skills.')],
          caption='No terminal, no file copying: the agent does the technical step and reports where the skill lives.')
    T2S['Create a Reusable Skill from a Real Correction'](KK + ' · Skills')

def firecrawl(D):
    big_number(D, KK + ' · Web search', '1,000', 'free Firecrawl credits a month: Mia can now read the web.',
               'Firecrawl is Hermes’s default web search. Create a free key at firecrawl.dev (no card), paste it in Settings → Tools & Keys, '
               'and ask for cold-brew trends with dated, linked sources. Keys go in Settings, never in a chat.', dark=False)
    tag(D, 'SETUP', 'https://www.firecrawl.dev/pricing ; ' + DOCS + 'user-guide/features/web-search')

def gmail(D):
    image(D, KK + ' · Gmail', 'Gmail in One Click: Sign In with Google, No OAuth Set-up', shot('connectors'),
          side=[('login', 'Sign in to Nous', 'Status bar → Sign in. The free account is enough.'),
                ('plug', 'Connectors → Gmail', 'Capabilities → Connectors → search “Gmail” → Connect.'),
                ('mail', 'Sign in with Google', 'Pick the training account → Allow. Done.'),
                ('shield', 'Read ≠ send', 'Mia reads freely; she sends once, after your SEND on the exact email.')],
          caption='Connectors are managed apps served through your Nous sign-in. Free-tier connector access: awaiting verification — your trainer confirms before class.')
    tag(D, 'SETUP', DOCS + 'user-guide/features/tool-search#connectors-remote-tools ; trainer screenshot')

def cron(D):
    image(D, KK + ' · Scheduled jobs', 'Scheduled Jobs Make Mia Proactive', shot('scheduled-jobs'),
          side=[('list', 'Blueprints', 'Morning briefing, Important-mail monitor, Weekly review …'),
                ('chat', 'Or just ask', '“Every day at 8:00, summarise my unread Gmail and send it to Telegram.”'),
                ('bolt', 'Trigger now', 'Test it today, not tomorrow morning.'), ('pause', 'Pause', 'Stop a job you cannot watch.')],
          caption='A scheduled job (a “cron”) = a schedule + a prompt + where to deliver. It starts work without being asked.')
    s = D.new(dark=True); header(D, s, KK + ' · Scheduled jobs', 'Your 8:00 Email Brief, Before You Open the Pop-up',
                                 'One sentence to Mia creates the job. Hermes Desktop must be running at 8:00.')
    code_card(s, .6, 2.35, 12.1, 1.5, 'Create a scheduled job called “Morning email brief”, every day at 8:00 Asia/Singapore, delivered to my Telegram:\n'
              'use the kopi-email-brief skill and the Gmail connector to summarise my unread Kopi Kaki email — urgent first, then replies needed, then FYI.\n'
              'Read only: never send or change anything.', 12, 'ASK MIA')
    for i, (t, d) in enumerate([('07:59', 'You are asleep. Hermes Desktop is running.'), ('08:00', 'The job wakes Mia with the kopi-email-brief skill.'),
                                ('08:02', 'Mia reads Gmail through the connector — read-only.'), ('08:03', 'Your Telegram buzzes: urgent, replies needed, FYI.')]):
        x = .6 + i * 3.08
        text(s, x, 4.2, 2.9, .6, t, 30, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x, 4.85, 2.85, 1.0, d, 13.5, SOFT, minpt=10)
    text(s, .6, 6.1, 12.1, .4, 'Scheduled jobs → your job → Trigger now. Check Telegram before you trust the schedule.', 12.5, LIGHT, minpt=10)
    tag(D, 'SETUP', DOCS + 'user-guide/features/cron')

def web_skills(D):
    """Tools and skills in action · Web design: UX skills from skills.sh."""
    s = D.new(); header(D, s, KK + ' · Tools and skills · Web design', 'Web Design: Install Design Know-How from skills.sh',
                        'The open directory of agent skills. Read the SKILL.md on skills.sh, then ask Mia to install it.')
    sk = [('frontend-design', 'Anthropic', '≈1.1M installs', 'Bold, distinctive front-end design; avoids generic “AI look”.', '“Install frontend-design from\ngithub.com/anthropics/skills”'),
          ('web-design-guidelines', 'Vercel', '≈804K installs', 'Checks a UI against web interface guidelines: accessibility, layout, forms.', '“Install web-design-guidelines from\ngithub.com/vercel-labs/agent-skills”'),
          ('ui-ux-pro-max', 'nextlevelbuilder', '≈424K installs', 'Design-system intelligence: styles, palettes, font pairings, UX rules.', '“Install ui-ux-pro-max from\nskills.sh” (stretch challenge)')]
    for i, (n, by, inst, d, ask) in enumerate(sk):
        x = .6 + i * 4.1
        card(s, x, 2.35, 3.9, 4.1)
        text(s, x + .3, 2.5, 3.3, .45, n, 17, INK, bold=True, font=K.MONO, autofit=False)
        text(s, x + .3, 2.98, 3.3, .3, f'{by} · {inst}', 11.5, ACC, bold=True, autofit=False)
        text(s, x + .3, 3.38, 3.3, 1.1, d, 12.5, MUTED, minpt=9.5)
        code_card(s, x + .2, 4.6, 3.5, 1.6, ask, 10.5, 'ASK MIA')
    link(s, .6, 6.6, 6, 'skills.sh · install counts as of 30 Oct 2026 · click', 'https://skills.sh/')
    tag(D, 'TOOLS', 'https://skills.sh/')

def website(D):
    image(D, 'Topic 2 · Activity 2 · Single agent', 'What One Agent Built: The Kopi Kaki Website', shot('kopi-website'),
          caption='One agent, two UX skills, one brief: hero, price, launch date and a pre-order button, in Kopi Kaki’s colours. Your version will differ; check every fact.')
    tag(D, 'EVIDENCE', 'Trainer’s Activity 2 run (Hermes Desktop, 31 Oct 2026)')

def deck(D, T2S):
    flow(D, 'Topic 2 · Activity 3 · Single agent', 'A Pitch Deck Is a Decision Story', [
        ('alert', 'Problem', 'Singapore office workers want kopi that tastes like home, cold.'), ('coffee', 'Product', 'Gula Melaka Cold Brew · SGD 6.80 · from 1 Dec.'),
        ('star', 'Proof', '60 pop-up tasting reviews: average rating, top themes.'), ('map', 'Plan', '#ShiokColdBrew · 17 Nov–14 Dec · KPIs and budget.'),
        ('target', 'Ask', 'What you need from the bank, and what it buys.')],
        sub='The kopi-pitch-deck skill gives Mia this order; python-pptx gives her editable slides and a native chart.',
        tipt='PP Task 2: ONE screenshot of Hermes Desktop showing your request and the finished deck.')
    tag(D, 'CONCEPT', 'Course design; kopi-pitch-deck SKILL.md')
    T2S['Separate Content Errors from Layout Errors']('Topic 2 · Activity 3')

def pptx_skill(D):
    """Tools and skills in action · PPTX: python-pptx (tool) + kopi-pitch-deck (skill)."""
    before_after(D, KK + ' · Tools and skills · PPTX', 'Tools Do the Work. Skills Know How to Do It Well.',
                 'A skill is a folder with a SKILL.md: steps, rules and checks the agent loads when a task matches.',
                 ('Tool only', '“Make a deck” with python-pptx', ['Slides appear — but in what order?', 'Which colours, which chart, which checks?', 'Every run is a fresh guess.']),
                 ('Tool + skill', '“Make a deck” with kopi-pitch-deck', ['Problem → product → proof → plan → ask.', 'Brand colours, native chart, sources in notes.', 'Same quality every time; improve it once, every run benefits.']),
                 tipt='Browse Capabilities → Skills (88 built in). Read every third-party SKILL.md before you install it.')
    tag(D, 'ARCH', DOCS + 'user-guide/features/skills')

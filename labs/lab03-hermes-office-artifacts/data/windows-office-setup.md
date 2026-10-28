# Native Windows Desktop office setup

Use Hermes Desktop on its local Windows connection. These PowerShell commands run in that same Windows environment, not in WSL. The trainer installs Python and the official Windows gog ZIP first and checks gog.exe is on PATH.

```powershell
$launchWorkspace = Join-Path $env:USERPROFILE 'kopi-kaki'
New-Item -ItemType Directory -Force -Path $launchWorkspace | Out-Null
Set-Location $launchWorkspace
python -m venv .office-venv
& .\.office-venv\Scripts\python.exe -m pip install openpyxl python-pptx Pillow
gog --version
$env:GOG_ACCOUNT = 'REPLACE_WITH_ASSIGNED_GOOGLE_EMAIL'
gog auth credentials (Join-Path $env:USERPROFILE 'Downloads\training-oauth-client.json')
gog auth add $env:GOG_ACCOUNT --services gmail,calendar,drive --gmail-scope readonly
gog auth list --check
gog --account $env:GOG_ACCOUNT me
gog --account $env:GOG_ACCOUNT --readonly --gmail-no-send --json gmail search 'subject:Kopi newer_than:30d' --max 10
gog --account $env:GOG_ACCOUNT --readonly --json calendar events --today
gog --account $env:GOG_ACCOUNT --readonly --json drive ls --max 10
& .\.office-venv\Scripts\python.exe tools/office_artifacts.py analyse --input campaign-data.xlsx --out outputs/lab02
& .\.office-venv\Scripts\python.exe tools/office_artifacts.py dashboard --out outputs/lab02
& .\.office-venv\Scripts\python.exe tools/office_artifacts.py ppt --out outputs/lab02
```

Copy the reviewed tools and skills folders from this lab's data/ into the workspace. Use the Desktop profile's actual Skills directory (inspect it in the app; do not assume the Unix ~/.hermes path). For example, after the trainer confirms the destination path:

```powershell
$profileSkillsPath = Read-Host 'Paste the selected local profile Skills directory'
Copy-Item -Recurse -Force .\skills\gog-office, .\skills\office-analytics, .\skills\interactive-dashboard, .\skills\professional-ppt $profileSkillsPath
```

Restart/reload the selected Desktop session if required and verify the four skills are visible. Desktop/gateway tools must find the same gog.exe, Python environment and authorised account. If PATH changed after gateway startup, restart the training gateway through Desktop and recheck. Do not copy credential files between Windows and WSL or paste them into chat.


## Day 2: native Windows Hermes video commands

Use the same native workspace/runtime. Inspect real profiles, assigned tasks and gateway status:

```powershell
hermes profile list
hermes kanban create --help
hermes gateway status
& .\.office-venv\Scripts\python.exe tools/render_launch_video.py --out outputs/team/video
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json outputs/team/video/final.mp4
Get-FileHash outputs/team/video/final.mp4 -Algorithm SHA256
```

Use the supplied kanban-studio-runbook.md for task dependencies and unassigned human gates. No extra agent platform is required. Confirm ffmpeg/ffprobe and Python are on the native PATH used by Desktop/gateway. Do not run Bash `source` or Unix environment assignment in PowerShell.

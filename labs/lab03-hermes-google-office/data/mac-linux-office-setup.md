# Native macOS/Linux office setup

Use the confirmed local Hermes Desktop workspace. Copy this activity's data contents into ~/kopi-kaki first; preserve existing AGENTS.md. Linux uses the official supported Hermes installation route where Desktop is unavailable. The trainer preflights a supported native Python,gog,FFmpeg/ffprobe and PPT/PDF renderer; app installation alone does not install these tools.

```bash
cd ~/kopi-kaki
python3 -m venv .office-venv
.office-venv/bin/python -m pip install openpyxl python-pptx Pillow
.office-venv/bin/python -c 'import openpyxl, pptx, PIL; print("Office imports OK")'
gog --version
ffprobe -version
```

Run the probes through the selected Desktop runtime as well. The exact .office-venv/bin/python path is used by Activities3–4. If the trainer prepared it, verify the imports instead of recreating it. If a required dependency fails, record the block and resolve it before the timed artifact run.

Review/install five supplied skill folders into the actual selected profile's Skills directory: gog-office,office-analytics,interactive-dashboard,professional-ppt,launch-video. Confirm all five are visible after reload. A skill directory is not an executable or an OAuth grant. Do not overwrite personal profile files or copy credentials into the course folder.

After authorizing the assigned Google account, use --readonly and Gmail --gmail-no-send for reads. Activity4's one test send is a separate exact-content human-approved procedure in approved-test-send.md.

```bash
.office-venv/bin/python tools/office_artifacts.py analyse --input campaign-data.xlsx \
  --out outputs/lab02
.office-venv/bin/python tools/office_artifacts.py dashboard --out outputs/lab02
.office-venv/bin/python tools/office_artifacts.py ppt --out outputs/lab02
# Only after human scene-text approval:
.office-venv/bin/python tools/render_launch_video.py --out outputs/single-video
```

Read the relevant skill first, inspect actual output,render/open every PPT slide,watch the full video and verify source totals and metadata. Keep Day1 outputs/single-video separate from Day2 outputs/team/video.

Official sources: https://hermes-agent.nousresearch.com/docs/user-guide/desktop ; https://gogcli.sh/install.html ; https://docs.python.org/3/library/venv.html

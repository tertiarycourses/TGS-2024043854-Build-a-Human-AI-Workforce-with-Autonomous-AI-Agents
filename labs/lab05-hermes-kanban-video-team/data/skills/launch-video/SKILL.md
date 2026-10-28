---
name: launch-video
description: Produce a reviewed local launch video from the human-approved storyboard and licensed/supplied assets.
---
# launch-video

1. Read the approved scene text, brand rules and verified product facts.
2. Inspect tools/render_launch_video.py as a deterministic FFmpeg baseline. Copy it into the producer-owned output folder before adapting scene copy/layout; do not edit the shared tool while another worker runs.
3. Produce three five-second scenes, 1080x1920, H.264 MP4. Use no unlicensed music, likeness or unsupported claim.
4. Inspect every frame and ffprobe metadata; watch the full playable video.
5. Reviewer records evidence and the human requests one revision. Re-render and re-audit.
6. Save final file hash and exact-version decision. Do not publish externally.
Optional alternative: use a reviewed HyperFrames/Remotion skill after checking its current official docs and dependencies; require the same output and QA.

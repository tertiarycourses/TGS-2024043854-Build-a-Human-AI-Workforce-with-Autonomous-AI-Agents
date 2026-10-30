# Images and review gallery
For each of linkedin.md, facebook.md and instagram.md make one image with
`.office-venv/bin/python tools/make_post_image.py --headline "<max 6 words>" --sub "<max 10 words>" --out outputs/social/images/<platform>.png`
(Windows: .office-venv\Scripts\python.exe). Then build outputs/social/gallery.html: one card per platform styled like that platform, with image, copy and hashtags. Offline, no external libraries.

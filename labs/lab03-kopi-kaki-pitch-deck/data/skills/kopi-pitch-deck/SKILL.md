---
name: kopi-pitch-deck
description: Build a professional, editable investor/launch pitch deck for Kopi Kaki Co. from the source files with python-pptx.
---
# kopi-pitch-deck

1. Read AGENTS.md, campaign-brief.md, brand-guide.md, product-catalogue.csv, competitors.csv and customer-reviews.csv.
2. Story (8-10 slides): title · the problem · the product (Gula Melaka Cold Brew, SGD 6.80) · proof from 60 tasting reviews (average rating, top themes with review IDs) · market and 6 competitors · launch plan (17 Nov-14 Dec, #ShiokColdBrew) · KPIs (2,500 pre-orders, 8% engagement, 40,000 views) · budget SGD 15,000 · the ask.
3. Design: 16:9, brand colours Kopi Brown #5B3A29, Pandan Green #4E8A3E, Cream #F6EBD9, Amber #C7782A; one idea per slide; headline that states the point; at most 5 short bullets; readable 18 pt+ body text.
4. Use a NATIVE editable chart (python-pptx chart, not an image) for the review ratings or KPI targets. Put the source file in the speaker notes of every slide with a number.
5. Never invent figures, awards, partners or a loan amount the founder did not give. Mark assumptions.
6. Save outputs/deck/kopi-kaki-pitch.pptx, render outputs/deck/kopi-kaki-pitch.pdf (soffice --headless --convert-to pdf), open every page and fix clipping or overlap.
7. Write outputs/deck/qa-report.md: each number → source file, each fix you made. Do not send or publish.

---
name: social-campaign-planner
description: Turn a campaign brief into a complete, dated multi-platform social media plan (strategy, content calendar CSV, captions, hashtags, image prompts, UTM links). Use when asked to plan or build a social media campaign.
---

# Social campaign planner

## Inputs
A campaign brief (objectives, KPIs, audience, offer, phases, budget) and the brand guide.

## Procedure
1. **Strategy (campaign-plan.md):** objective → audience → key message → 3 content pillars → phase plan → KPI targets → paid budget split.
2. **Calendar (content-calendar.csv):** one row per post with columns
   `date,phase,platform,format,pillar,hook,caption,hashtags,image_prompt,utm_link,status`.
   Respect each platform's format and length rules from the brand guide. Status = `draft`.
3. **Captions:** apply the `kopi-brand-voice` skill to every caption and include its self-check.
4. **Visuals:** write an image prompt per post (brand colours, natural light, no faces of customers).
   If an image-generation tool is available, generate the hero visuals and save them to `outputs/lab02/images/`.
5. **Links:** build UTM links as `https://kopikaki.example/app?utm_source=<platform>&utm_medium=social&utm_campaign=shiokcoldbrew&utm_content=<post_id>`.
6. **Check:** count posts per phase and platform; confirm every KPI has at least one post driving it.

## Output
`outputs/lab02/campaign-plan.md`, `outputs/lab02/content-calendar.csv`, `outputs/lab02/captions.md`, images (if generated),
and a 5-line summary for the human reviewer listing anything that needs a decision.

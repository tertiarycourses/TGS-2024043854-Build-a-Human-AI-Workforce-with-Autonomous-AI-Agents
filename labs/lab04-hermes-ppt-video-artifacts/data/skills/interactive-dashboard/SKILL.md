---
name: interactive-dashboard
description: Build and test an offline HTML dashboard from verified synthetic office metrics.
---
# interactive-dashboard

1. Use verified analysis.json only. Embed synthetic aggregates and all code; no external libraries or network dependency.
2. Provide outlet selector, revenue KPI, native SVG/CSS bar chart, sortable table, CSV export and reset.
3. Keep labels readable and controls keyboard accessible. Never insert untrusted HTML; use textContent.
4. Test all outlets, one outlet, sort, reset and export. Visible totals and exported rows must match analysis.xlsx.
5. Inspect desktop and narrow screens; record exact checks in qa-report.md. A static screenshot does not prove interactivity.

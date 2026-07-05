# Auto Lighting Radar

Automotive lighting news radar based on the static pipeline from
`LearnPrompt/ai-news-radar`.

It tracks vehicle lighting topics with zero paid API budget:

- headlamps / headlights
- tail lamps and signal lamps
- ADB, matrix LED, pixel headlights, DLP and OLED
- FMVSS 108 / ECE / GB regulation watch
- IIHS safety and headlight ratings
- supplier news from Valeo, KOITO and free news feeds
- Google News RSS keyword feeds for English and Chinese industry coverage

## How it works

```text
free RSS / public JSON / static page monitors
  -> scripts/update_news.py
  -> relevance scoring in scripts/ai_relevance.py
  -> data/*.json
  -> GitHub Pages static site
```

No database is required. The GitHub Action writes JSON files into `data/`.
`data/archive.json` is a rolling archive controlled by `--archive-days`.

## Run locally

```bash
python -m pip install -r requirements.txt
python scripts/update_news.py --output-dir data --window-hours 168 --archive-days 21 --translate-max-new 0 --rss-opml feeds/follow.example.opml --rss-max-feeds 20
python -m http.server 8080
```

Open `http://localhost:8080`.

## Source plan

See `docs/SOURCES_AUTOLIGHTING.md`.

## Deploy on GitHub Pages

1. Create a public GitHub repository named `auto-lighting-radar`.
2. Push this project to the default branch.
3. In repository settings, enable Pages from the default branch root.
4. The included GitHub Action updates `data/*.json` every 30 minutes.

## Add more free sources

Add RSS feeds to `feeds/follow.example.opml`, or keep a private
`feeds/follow.opml` injected by the `FOLLOW_OPML_B64` GitHub Secret.

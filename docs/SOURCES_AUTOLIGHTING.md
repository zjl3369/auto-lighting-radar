# Auto Lighting Radar source plan

This fork keeps the upstream static GitHub Pages pipeline but changes the topic
from AI to automotive lighting. It is designed for zero budget: no paid API, no
login cookies, no private database.

## Live sources

| Source | Type | Why |
| --- | --- | --- |
| Valeo Press Releases | RSS | Tier-1 supplier news; stable free feed. |
| IIHS News | RSS | Safety and headlight-rating context; stable free feed. |
| Electrive | RSS | EV and supplier news; filtered by lighting keywords. |
| Google News: automotive lighting | RSS search | Broad English news discovery for headlamp, ADB, vehicle lighting. |
| Google News: 车灯/汽车照明 | RSS search | Broad Chinese news discovery for 车灯, 汽车照明, 矩阵大灯, 智能车灯. |
| Google News: supplier lighting | RSS search | Watches Valeo, HELLA, Koito, Marelli and lighting terms. |
| Google News: ADB / Matrix LED | RSS search | Watches technical terms such as ADB, matrix LED, pixel headlights and DLP headlamps. |
| KOITO English News | Public JSON | KOITO publishes its page data at `/english/news/include/news_list_for_index.json`; no key required. |
| eCFR FMVSS 108 | Static page monitor | U.S. lamps/reflective-devices regulation watch. |
| IIHS ratings page | Static page monitor | Headlight rating index watch. |

## Not enabled yet

| Source | Reason |
| --- | --- |
| FORVIA HELLA newsroom | Direct RSS/page requests returned 403 in testing. Add later through an official feed if found. |
| LEDs Magazine | Direct RSS requests returned 403 in testing. Use Google News RSS first. |
| Automotive World / Just Auto | Direct feed requests returned 403 or closed connection in testing. Use Google News RSS first. |
| NHTSA recalls page | Browser page returned 403 in testing. A free no-key NHTSA API can be added later if a stable endpoint is chosen. |
| Google Patents / CNIPA | Useful, but patent search result pages are better handled as a weekly report; not included in the 30-minute news pipeline. |

## How to add your own free sources

Add RSS feeds to `feeds/follow.example.opml` or use a private `feeds/follow.opml`.
The GitHub Action will copy the example file when no private OPML secret exists.

Good keywords:

- English: `automotive lighting`, `headlamp`, `headlight`, `adaptive driving beam`, `matrix LED`, `pixel headlight`, `DLP headlamp`, `OLED tail lamp`, `DRL`, `FMVSS 108`, `ECE R48`, `R149`
- Chinese: `车灯`, `汽车照明`, `前照灯`, `矩阵大灯`, `像素大灯`, `激光大灯`, `智能车灯`, `自适应远光`, `贯穿式尾灯`, `光导`, `透镜`, `车规LED`

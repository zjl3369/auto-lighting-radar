# Auto Lighting Radar source plan

This fork keeps the upstream static GitHub Pages pipeline but changes the topic
from AI to automotive lighting. It is designed for zero budget: no paid API, no
login cookies, no private database. Public output is split into `core`,
`adjacent` and `broad` relevance tiers; the default page shows the full
30-day intelligence pool.

## Live sources

| Source | Type | Why |
| --- | --- | --- |
| Valeo Press Releases | RSS | Tier-1 supplier news; stable free feed. |
| IIHS News | RSS | Safety and headlight-rating context; stable free feed. |
| Electrive | RSS | EV and supplier news; filtered by lighting and supplier keywords. |
| 36Kr | RSS | Domestic smart-car and supplier news; filtered by Chinese keywords. |
| InfoQ China | RSS | Domestic intelligent-vehicle technology context. |
| 盖世汽车搜索 | HTML search page | Domestic automotive industry source for 车灯, 汽车照明, 矩阵大灯, 智能车灯, 尾灯, 大灯, 灯组, 氛围灯, 车规 LED. |
| Google News: automotive lighting | RSS search | Broad English discovery for headlamp, ADB, vehicle lighting. |
| Google News: 车灯/汽车照明 | RSS search | Broad Chinese discovery for 车灯, 汽车照明, 矩阵大灯, 智能车灯. |
| Google News: 智能大灯技术 | RSS search | Tracks ADB, 像素大灯, DLP 大灯, 自适应远光. |
| Google News: 尾灯/贯穿式/OLED | RSS search | Tracks tail-lamp design and signal-lamp trends. |
| Google News: 车灯法规/召回 | RSS search | Tracks GB 4785, GB 4599, FMVSS 108, ECE R149 and recall news. |
| Google News: 国内车灯供应商 | RSS search | Tracks 华域视觉, 星宇股份, 曼德光电, 常诚车灯, 嘉利股份. |
| Google News: 国际车灯供应商中文 | RSS search | Tracks 法雷奥, 海拉, 小糸, 马瑞利, ZKW Chinese coverage. |
| Google News: 主机厂灯光配置 | RSS search | Tracks lighting configuration in BYD, Xiaomi, AITO, Li Auto, NIO, XPeng, Geely, Chery. |
| Google News: LED/光学产业链 | RSS search | Tracks automotive LED, OLED, lens, light-guide supply-chain updates. |
| Google News: 车型灯组/灯光配置 | RSS search | Tracks OEM launches and lighting feature mentions in Chinese auto media. |
| Google News: 智能座舱/氛围灯 | RSS search | Tracks cabin lighting, ambient light and automotive display context. |
| Google News: 车规LED/显示/光学 | RSS search | Tracks automotive LED, display, HUD and optical upstream news. |
| Google News: 站点限定-汽车媒体 | RSS search | Site-limited queries for 汽车之家, 易车, 太平洋汽车 and 懂车帝. |
| Google News: 站点限定-LED/产业链 | RSS search | Site-limited queries for OFweek, LEDinside, TrendForce and 行家说. |
| Google News: supplier lighting | RSS search | Watches Valeo, HELLA, Koito, Marelli and lighting terms. |
| Google News: ADB / Matrix LED | RSS search | Watches technical terms such as ADB, matrix LED, pixel headlights and DLP headlamps. |
| Bing News RSS | RSS search | Optional fast supplemental source; HTML fallbacks are skipped automatically. |
| KOITO English News | Public JSON | KOITO publishes page data at `/english/news/include/news_list_for_index.json`; no key required. |
| eCFR FMVSS 108 | Static page monitor | U.S. lamps/reflective-devices regulation watch. |
| IIHS ratings page | Static page monitor | Headlight rating index watch. |

## Good extra sources to add later

These are useful for domestic users, but they need more careful page parsing
than simple RSS:

| Source | Suggested access | Notes |
| --- | --- | --- |
| 盖世汽车 | Page list / Google News query | Good for supplier and OEM business news. |
| 汽车之家 / 车家号 | Page list / Google News query | Good for model launches and lighting configuration. |
| 易车 / 懂车帝 / 太平洋汽车 | Page list / Google News query | Good for consumer-facing model and lamp-design updates. |
| OFweek / 高工 LED / 行家说 Display | Page list / Google News query | Good for LED, optical module and display/light-source chain. |
| 国家市场监督管理总局缺陷产品管理中心 | Page/API candidate | Good for recall risk; should be parsed separately to avoid false dates. |
| 工信部公告 / 标准公开系统 | Page monitor | Good for standards and regulatory changes, but update frequency is lower. |
| Google Patents / CNIPA | Weekly report | Useful for patents, not ideal for 30-minute news refresh. |

## Good keywords

- Chinese: `车灯`, `汽车照明`, `前照灯`, `大灯`, `尾灯`, `信号灯`, `矩阵大灯`, `像素大灯`, `DLP 大灯`, `激光大灯`, `ADB`, `自适应远光`, `贯穿式尾灯`, `OLED 尾灯`, `光导`, `透镜`, `车规 LED`, `GB 4785`, `GB 4599`
- Domestic suppliers: `华域视觉`, `星宇股份`, `曼德光电`, `常诚车灯`, `嘉利股份`, `佛山照明`, `鸿利智汇`
- International suppliers: `法雷奥`, `海拉`, `小糸`, `马瑞利`, `斯坦雷`, `ZKW`, `ams OSRAM`, `Nichia`
- English: `automotive lighting`, `headlamp`, `headlight`, `adaptive driving beam`, `matrix LED`, `pixel headlight`, `DLP headlamp`, `OLED tail lamp`, `DRL`, `FMVSS 108`, `ECE R48`, `ECE R149`

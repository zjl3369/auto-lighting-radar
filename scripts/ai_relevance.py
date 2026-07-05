#!/usr/bin/env python3
"""Explainable relevance scoring for automotive lighting news records.

The upstream template names these fields ai_* because the frontend expects them.
In this fork they mean "automotive lighting relevance".
"""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

PRIMARY_KEYWORDS = [
    "automotive lighting",
    "vehicle lighting",
    "car lighting",
    "headlamp",
    "headlight",
    "tail lamp",
    "taillamp",
    "rear lamp",
    "signal lamp",
    "turn signal",
    "adaptive driving beam",
    "adaptive headlight",
    "matrix led",
    "pixel led",
    "pixel headlight",
    "dlp headlamp",
    "laser headlight",
    "oled tail",
    "daytime running light",
    "drl",
    "fmvss 108",
    "ece r48",
    "r148",
    "r149",
    "r150",
    "gb 4785",
    "gb 5920",
    "gb 4660",
    "车灯",
    "汽车照明",
    "前照灯",
    "大灯",
    "尾灯",
    "信号灯",
    "转向灯",
    "日行灯",
    "位置灯",
    "雾灯",
    "贯穿式尾灯",
    "矩阵大灯",
    "像素大灯",
    "激光大灯",
    "智能车灯",
    "自适应远光",
    "远光辅助",
    "灯语",
    "氛围灯",
    "光导",
    "透镜",
]

TECH_KEYWORDS = [
    "led",
    "mini led",
    "micro led",
    "oled",
    "laser",
    "projector",
    "lens",
    "optics",
    "optical",
    "thermal",
    "heat dissipation",
    "phosphor",
    "driver ic",
    "light source",
    "illumination",
    "luminous",
    "lumens",
    "glare",
    "beam pattern",
    "adas",
    "homologation",
    "recall",
    "compliance",
    "regulation",
    "standard",
    "led",
    "mini led",
    "micro led",
    "oled",
    "激光",
    "投影",
    "光学",
    "光源",
    "配光",
    "眩光",
    "散热",
    "车规",
    "法规",
    "标准",
    "召回",
    "缺陷",
    "认证",
]

COMPANY_KEYWORDS = [
    "valeo",
    "hella",
    "forvia",
    "koito",
    "stanley electric",
    "marelli",
    "zkw",
    "sl corporation",
    "mobis",
    "hyundai mobis",
    "varroc",
    "ams osram",
    "osram",
    "lumileds",
    "nichia",
    "seoul semiconductor",
    "星宇",
    "华域视觉",
    "曼德光电",
    "佛山照明",
    "国星光电",
    "瑞丰光电",
    "聚飞光电",
]

NOISE_KEYWORDS = [
    "home lighting",
    "street lighting",
    "architectural lighting",
    "stage lighting",
    "smart home",
    "grow light",
    "植物照明",
    "家居照明",
    "景观照明",
    "舞台灯",
    "路灯",
    "篮球",
    "足球",
    "明星",
    "娱乐",
]

EN_PRIMARY_RE = re.compile(
    r"(?i)(?<![a-z0-9])(headlamp|headlight|taillamp|tail lamp|adaptive driving beam|matrix led|pixel led|drl|fmvss 108|ece r48|r149|automotive lighting|vehicle lighting)(?![a-z0-9])"
)

RELEVANCE_THRESHOLD = 0.55

SOURCE_PRIORS = {
    "lighting_regulatory": 0.34,
    "lighting_official": 0.30,
    "lighting_media": 0.18,
    "lighting_search": 0.12,
    "opmlrss": 0.10,
}


def _text(record: dict[str, Any]) -> str:
    url = str(record.get("url") or "")
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        host = ""
    return " ".join(
        str(record.get(k) or "")
        for k in ("title", "source", "site_name")
    ).lower() + " " + host


def _matched(haystack: str, keywords: list[str]) -> list[str]:
    return sorted({kw for kw in keywords if kw.lower() in haystack})


def _label(text: str) -> str:
    if any(k in text for k in ["fmvss", "ece r", "gb ", "regulation", "standard", "法规", "标准", "认证"]):
        return "regulation_standard"
    if any(k in text for k in ["recall", "defect", "complaint", "召回", "缺陷", "投诉"]):
        return "quality_recall"
    if any(k in text for k in ["headlamp", "headlight", "前照灯", "大灯", "adb", "adaptive driving beam"]):
        return "headlamp"
    if any(k in text for k in ["tail lamp", "taillamp", "尾灯", "signal", "信号灯", "转向灯"]):
        return "signal_rear_lamp"
    if any(k in text for k in ["led", "oled", "laser", "光源", "光学", "散热", "透镜"]):
        return "lighting_technology"
    if any(k in text for k in COMPANY_KEYWORDS):
        return "supplier_oem"
    return "lighting_general"


def _result(
    is_related: bool,
    score: float,
    label: str,
    reason: str,
    signals: list[str] | None = None,
    noise: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "is_ai_related": bool(is_related),
        "score": round(max(0.0, min(1.0, score)), 2),
        "label": label,
        "reason": reason,
        "signals": signals or [],
        "noise": noise or [],
    }


def score_ai_relevance(record: dict[str, Any]) -> dict[str, Any]:
    site_id = str(record.get("site_id") or "")
    text = _text(record)
    primary = _matched(text, PRIMARY_KEYWORDS)
    tech = _matched(text, TECH_KEYWORDS)
    companies = _matched(text, COMPANY_KEYWORDS)
    noise = _matched(text, NOISE_KEYWORDS)
    prior = SOURCE_PRIORS.get(site_id, 0.0)

    has_primary = bool(primary) or EN_PRIMARY_RE.search(text) is not None
    has_context = bool(tech or companies)

    if site_id in {"lighting_regulatory", "lighting_official"}:
        score = prior + 0.34 + min(0.18, 0.04 * len(primary)) + min(0.12, 0.03 * len(tech + companies))
        if noise and not has_primary:
            score -= 0.18
        return _result(
            score >= RELEVANCE_THRESHOLD,
            score,
            _label(text),
            "trusted_lighting_source",
            primary + tech + companies or [site_id],
            noise,
        )

    if not (has_primary or (has_context and site_id in {"lighting_media", "lighting_search", "opmlrss"})):
        return _result(
            False,
            prior + min(0.28, 0.06 * len(tech + companies)),
            "not_lighting",
            "missing_lighting_signal",
            primary + tech + companies,
            noise,
        )

    score = prior + (0.48 if has_primary else 0.30) + min(0.18, 0.04 * len(primary)) + min(0.12, 0.025 * len(tech + companies))
    if noise and not has_primary:
        score -= min(0.20, 0.05 * len(noise))

    return _result(
        score >= RELEVANCE_THRESHOLD,
        score,
        _label(text),
        "matched_lighting_signal",
        primary + tech + companies,
        noise,
    )


def is_ai_related_record(record: dict[str, Any]) -> bool:
    return bool(score_ai_relevance(record)["is_ai_related"])


def add_ai_relevance_fields(record: dict[str, Any]) -> dict[str, Any]:
    relevance = score_ai_relevance(record)
    out = dict(record)
    out["ai_is_related"] = relevance["is_ai_related"]
    out["ai_score"] = relevance["score"]
    out["ai_label"] = relevance["label"]
    out["ai_relevance_reason"] = relevance["reason"]
    out["ai_signals"] = relevance["signals"]
    out["ai_noise"] = relevance["noise"]
    return out

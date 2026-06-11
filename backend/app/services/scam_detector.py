from __future__ import annotations

import base64
import re
from typing import Optional

from app.models.schemas import FraudAnalyzeResult, FraudClassification

SCAM_SIGNALS = {
    "otp": 22,
    "urgent": 15,
    "immediately": 10,
    "suspended": 18,
    "blocked": 18,
    "verify": 12,
    "kyc": 18,
    "bank": 10,
    "lottery": 25,
    "prize": 18,
    "refund": 12,
    "claim": 12,
    "link": 15,
    "gift": 10,
    "account": 8,
}


def attempt_ocr(image_base64: str) -> Optional[str]:
    if not image_base64:
        return None
    try:
        decoded = base64.b64decode(image_base64)
        if decoded:
            sample = decoded[:160].decode("utf-8", errors="ignore").strip()
            if len(sample) > 20 and " " in sample:
                return sample
    except Exception:
        return None
    return None


def analyze_message(message_text: str = "", image_base64: Optional[str] = None) -> FraudAnalyzeResult:
    extracted_text = attempt_ocr(image_base64 or "")
    combined_text = f"{message_text} {extracted_text or ''}".strip().lower()
    score = 8

    if re.search(r"https?://|www\.", combined_text):
        score += 20
    if re.search(r"\b\d{6}\b", combined_text):
        score += 10
    if re.search(r"click|tap|open", combined_text):
        score += 10
    if re.search(r"dear customer|dear user", combined_text):
        score += 8

    for keyword, weight in SCAM_SIGNALS.items():
        if keyword in combined_text:
            score += weight

    if image_base64 and not combined_text:
        score = 55

    score = max(0, min(100, score))

    if score >= 75:
        classification = FraudClassification.SCAM
        explanation = "This message looks dangerous because it creates panic, asks for action, and imitates a trusted service. These are strong scam signs."
        action = "Do not reply, do not click links, and report it to family or police."
    elif score >= 40:
        classification = FraudClassification.SUSPICIOUS
        explanation = "Some parts of this message look unsafe or manipulative. It should be verified before you trust it."
        action = "Avoid sharing personal information and confirm with the real organization first."
    else:
        classification = FraudClassification.SAFE
        explanation = "No major scam signals were found in the available text, but stay careful with unknown links and requests."
        action = "You can still verify the sender if you are unsure."

    if image_base64 and not extracted_text:
        explanation += " The screenshot could not be fully read in local mode, so the result is conservative."

    return FraudAnalyzeResult(
        extractedText=extracted_text,
        riskScore=score,
        classification=classification,
        aiExplanation=explanation,
        recommendedAction=action,
    )

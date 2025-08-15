"""Webhook notifier utilities."""
from __future__ import annotations

from typing import Optional

import httpx

from .config import settings


def send_webhook(message: str, url: Optional[str] = None) -> None:
    """Send message to webhook URL if provided."""
    url = url or settings.telegram_webhook or settings.discord_webhook
    if not url:
        return
    try:
        httpx.post(url, json={"text": message}, timeout=5)
    except Exception:  # pragma: no cover - logging omitted for brevity
        pass

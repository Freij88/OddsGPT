"""Lightweight client for The Odds API v4."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import settings

BASE_URL = "https://api.the-odds-api.com/v4"
CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


class APIError(RuntimeError):
    """Raised when the API returns an error."""


class OddsAPI:
    """Simple synchronous wrapper around The Odds API."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or settings.odds_api_key
        self.client = httpx.Client(timeout=10)

    def _cache_path(self, name: str) -> Path:
        return CACHE_DIR / f"{name}.json"

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if not self.api_key:
            raise APIError("ODDS_API_KEY missing")
        params = params or {}
        params["apiKey"] = self.api_key
        url = f"{BASE_URL}/{endpoint}"
        response = self.client.get(url, params=params)
        if response.status_code >= 400:
            raise APIError(f"API error {response.status_code}: {response.text}")
        return response.json()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=4))
    def list_sports(self) -> List[Dict[str, Any]]:
        """Return list of sports from API with simple disk cache."""
        cache_file = self._cache_path("sports")
        if cache_file.exists():
            return json.loads(cache_file.read_text())
        data = self._get("sports")
        cache_file.write_text(json.dumps(data))
        return data

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=4))
    def get_odds(self, sport: str, **params: Any) -> List[Dict[str, Any]]:
        """Fetch odds for given sport."""
        endpoint = f"sports/{sport}/odds"
        return self._get(endpoint, params)

"""Configuration handling for OddsBot."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import yaml
from pydantic import BaseModel, Field, validator
from dotenv import load_dotenv

CONFIG_PATH = Path("config.yaml")
ENV_PATH = Path(".env")


class Settings(BaseModel):
    """Application settings loaded from YAML and environment."""

    regions: List[str] = Field(default_factory=lambda: ["eu"])
    markets: List[str] = Field(default_factory=lambda: ["h2h", "spreads", "totals"])
    bookmakers: List[str] = Field(default_factory=list)
    min_ev: float = 0.02
    kelly_factor: float = 0.25
    max_bet_pct: float = 0.05
    min_odds: float = 1.01
    max_odds: float = 10.0
    min_time_to_start: int = 0
    sport_filter: List[str] = Field(default_factory=list)
    ui_autorefresh: int = 30
    odds_api_key: str | None = None
    telegram_webhook: str | None = None
    discord_webhook: str | None = None

    @validator("kelly_factor", "max_bet_pct")
    def _validate_positive(cls, v: float) -> float:  # noqa: D401
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v


def load_config(path: Path = CONFIG_PATH) -> Settings:
    """Load Settings from YAML file and .env variables."""
    load_dotenv(ENV_PATH)
    if path.exists():
        data: Dict[str, Any] = yaml.safe_load(path.read_text()) or {}
    else:
        data = {}
    return Settings(**data)


settings = load_config()

# OddsBot

OddsBot is a demonstration value betting toolkit. It fetches odds from [The Odds API](https://theoddsapi.com/), removes vig, scans for value bets and exposes a simple Streamlit dashboard.

![Dashboard](docs/screenshot_dashboard.png)

## Installation

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your `ODDS_API_KEY` (optional).

## Usage

Run the UI:

```bash
streamlit run ui/app.py
```

Run tests:

```bash
pytest
```

Docker:

```bash
docker-compose up --build
```

## CLI

```bash
python -m oddsbot.cli list-sports
```

## Configuration

Settings are loaded from `config.yaml` and `.env`.

## Disclaimer

This project is for educational purposes only. Betting involves risk. Use at your own responsibility and respect the terms of service of data providers and bookmakers.

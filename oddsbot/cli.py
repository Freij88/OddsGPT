"""Command line interface for OddsBot."""
from __future__ import annotations

import os
from pathlib import Path

import click

from . import backtest
from .config import settings
from .execution import place_paper_bet
from .odds_api import APIError, OddsAPI


@click.group()
def cli() -> None:
    """OddsBot command group."""
    pass


@cli.command()
def list_sports() -> None:
    """List sports from The Odds API."""
    api = OddsAPI(api_key=settings.odds_api_key or "demo")
    try:
        sports = api.list_sports()
    except APIError:
        sports = [{"key": "soccer"}, {"key": "basketball"}]
    for s in sports:
        click.echo(s["key"])


@cli.command()
@click.option("-e", "event_id", required=True)
@click.option("-s", "stake", type=float, required=True)
@click.option("-o", "odds", type=float, required=True)
def paper_bet(event_id: str, stake: float, odds: float) -> None:
    """Simulate placing a bet."""
    ticket = place_paper_bet(event_id, stake, odds)
    click.echo(f"Placed paper bet on {ticket.event_id} for {ticket.stake} @ {ticket.odds}")


@cli.command()
@click.argument("path", type=click.Path(exists=False))
def backtest_cmd(path: str) -> None:
    """Run simple backtest on directory of CSV snapshots."""
    result = backtest.run_backtest(path)
    click.echo(f"PnL: {result['pnl']:.2f}")


@cli.command()
def ui() -> None:
    """Launch Streamlit UI."""
    os.system("streamlit run ui/app.py")


if __name__ == "__main__":
    cli()

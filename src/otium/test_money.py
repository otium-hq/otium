"""Unit tests for money analysis — pure arithmetic, no network."""

from .models import Account
from .money import idle_cash

_SAVINGS = Account(name="Everyday Savings", balance_cents=1_240_000, apy=0.0001)


def test_idle_cash_should_price_the_gap_to_the_best_available_rate() -> None:
    """$12,400 at 0.01% against 4.2% available is $519.56 a year."""
    # Arrange
    best_apy = 0.042

    # Act
    finding = idle_cash(_SAVINGS, best_apy)

    # Assert
    assert finding is not None
    assert finding.costing_cents_per_year == 51_956


def test_idle_cash_should_find_nothing_when_the_account_already_earns_the_best_rate() -> (
    None
):
    """No gap, no Finding — OTIUM stays quiet when there is nothing to say."""
    # Arrange
    best_apy = 0.0001

    # Act
    finding = idle_cash(_SAVINGS, best_apy)

    # Assert
    assert finding is None

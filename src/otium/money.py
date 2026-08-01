"""What the money is costing — analysis over connected accounts.

Prices the gap and stops. No view on what the money is for (ADR-014, ADR-015).
"""

from .models import Account, Finding


def idle_cash(account: Account, best_apy: float) -> Finding | None:
    """Price what an account loses by sitting below the best available rate.

    Args:
        account: The account holding the money
        best_apy: The best rate available at comparable access

    Returns:
        A priced Finding, or None when the account already earns it

    Example:
        >>> idle_cash(savings, best_apy=0.042).costing_cents_per_year
        51956

    """
    gap = best_apy - account.apy
    if gap <= 0:
        return None
    return Finding(
        what=f"{account.name} earns {account.apy:.2%}",
        costing_cents_per_year=round(account.balance_cents * gap),
        instead=f"{best_apy:.2%} at comparable access",
    )

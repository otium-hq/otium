"""Sorting a Demand against the Rules.

The model proposes; this module decides. Everything here is deterministic, and
the gates can overrule the model (ADR-004).
"""

from typing import Final

from .models import Demand, Outcome, Proposal

CONFIDENCE_FLOOR: Final[float] = 0.8


def decide(proposal: Proposal, demand: Demand, grants: frozenset[str]) -> Outcome:
    """Apply the authority and confidence gates to a Proposal.

    Handled requires that the user granted this Demand's source and that the
    model was sure. Anything else is Brought — never silently dropped.

    Args:
        proposal: What the model proposed
        demand: The Demand being sorted
        grants: Demand sources the user has granted autonomous handling

    Returns:
        The Outcome actually taken

    Example:
        >>> decide(proposal, demand, grants=frozenset())
        <Outcome.BROUGHT: 'BROUGHT'>

    """
    if proposal.outcome is not Outcome.HANDLED:
        return proposal.outcome
    if demand.source not in grants:
        return Outcome.BROUGHT
    if proposal.confidence < CONFIDENCE_FLOOR:
        return Outcome.BROUGHT
    return Outcome.HANDLED

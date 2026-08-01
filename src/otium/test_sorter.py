"""Unit tests for the Sort gates — pure functions, no model, no network."""

from datetime import UTC, datetime

from .models import Demand, Outcome, Proposal
from .sorter import decide

_DEMAND = Demand(
    source="plaid",
    detail="Acme Cloud subscription — $79.99",
    occurred_at=datetime(2026, 8, 1, tzinfo=UTC),
)


def test_decide_should_bring_a_handled_proposal_when_the_source_is_not_granted() -> (
    None
):
    """The authority gate overrules the model (ADR-004)."""
    # Arrange
    proposal = Proposal(outcome=Outcome.HANDLED, confidence=1.0, why="routine")

    # Act
    result = decide(proposal, _DEMAND, grants=frozenset())

    # Assert
    assert result is Outcome.BROUGHT


def test_decide_should_bring_a_handled_proposal_when_the_model_is_unsure() -> None:
    """When it isn't sure, it asks — even where authority was granted."""
    # Arrange
    proposal = Proposal(outcome=Outcome.HANDLED, confidence=0.4, why="ambiguous")

    # Act
    result = decide(proposal, _DEMAND, grants=frozenset({"plaid"}))

    # Assert
    assert result is Outcome.BROUGHT


def test_decide_should_handle_when_granted_and_sure() -> None:
    """Both gates open, so the Demand is Handled without the user."""
    # Arrange
    proposal = Proposal(outcome=Outcome.HANDLED, confidence=0.95, why="routine")

    # Act
    result = decide(proposal, _DEMAND, grants=frozenset({"plaid"}))

    # Assert
    assert result is Outcome.HANDLED


def test_decide_should_pass_through_a_pushed_back_proposal() -> None:
    """The gates only constrain Handled; refusals need no authority."""
    # Arrange
    proposal = Proposal(outcome=Outcome.PUSHED_BACK, confidence=0.1, why="not yours")

    # Act
    result = decide(proposal, _DEMAND, grants=frozenset())

    # Assert
    assert result is Outcome.PUSHED_BACK

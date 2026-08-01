"""Domain types — the contract every module speaks."""

import enum
from datetime import datetime

from pydantic import BaseModel, Field


class Outcome(enum.StrEnum):
    """What a Sort resolves to. There is no fourth (ADR-002)."""

    HANDLED = "HANDLED"
    BROUGHT = "BROUGHT"
    PUSHED_BACK = "PUSHED_BACK"


class Demand(BaseModel):
    """Something that wants a piece of the user's time."""

    source: str
    detail: str
    occurred_at: datetime


class Account(BaseModel):
    """A connected account holding money."""

    name: str
    balance_cents: int
    apy: float = Field(ge=0.0)


class Finding(BaseModel):
    """Something the money is costing the user, priced.

    A Finding states the cost and what is available instead. It never says
    what the user should do about it (ADR-015).
    """

    what: str
    costing_cents_per_year: int
    instead: str


class Proposal(BaseModel):
    """What the model proposes for a Demand.

    A Proposal is not an Outcome. The gates in `sorter` decide what actually
    happens, and may overrule it (ADR-004).
    """

    outcome: Outcome
    confidence: float = Field(ge=0.0, le=1.0)
    why: str

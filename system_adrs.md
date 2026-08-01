# System ADRs

ADR-001 to ADR-010 are promises made on otium.run. Breaking one is a product decision, not an engineering one.

## ADR-001 — The Rules are the only standard

No built-in idea of a good life. Nothing ranks, scores, or advises. Every judgment resolves against the user's Rules or is not made.

## ADR-002 — Three outcomes, no fourth

Every Demand is sorted against the Rules to exactly one of Handled, Brought, Pushed back. Nothing is silently dropped.

## ADR-003 — Rules are user-owned markdown

Plain markdown the user writes and edits whenever they want. No schema, no migration, no approval step. An edit takes effect on the next Demand.

## ADR-004 — Nothing happens behind the user's back

Control is granted one capability at a time, at the user's pace. Default is ask. An action outside granted control is not taken.

## ADR-005 — Every action carries its undo

No action ships without a reversal path. If it cannot be undone it is Brought, never Handled.

## ADR-006 — The weekly look reports, never grades

Life beside the stated Rules. No score, no ranking, no recommendation.

## ADR-007 — No fixed screens

Views are generated on request and disposable. No view is privileged; discarding one loses nothing.

## ADR-008 — The user leaves with everything

Rules, event log, and action log export in full to open formats. No capability is reachable only through the hosted service.

## ADR-009 — Each step stands alone

Finances, voice and email, robot. Each is independently complete and none requires the next. Stopping at one is a supported end state, not an unfinished setup.

## ADR-010 — Bring your own hardware

Physical work is a Demand with an executor — person, service, or robot. Executors are swappable. No robot-specific abstraction in the core.

## ADR-011 — One log is the product surface

Every Demand and every action appends to one ordered log. Generated views, the weekly look, and undo are all queries over it. No second store.

## ADR-012 — The core names no vendor

Provider and model are a `provider:model` key in `cfg.yml`; credentials come from the environment. Two wire formats are implemented natively, each on its own SDK — no compatibility shim standing in for the other. Application code names no vendor.

## ADR-013 — No agent framework until a test needs one

Sorting a Demand is one call with structured output. The seam is a one-method Protocol; unit tests inject a fake, so no network and no key. pydantic-ai when multi-step execution arrives, not before.

## ADR-014 — Prompts and Rules are both markdown

Prompts ship as `.md` files inside the package. Rules are the user's own `.md`. Neither is a Python string.

## ADR-015 — Approval lives in the log, not inside a durable run

An action awaiting approval is a log entry, not a paused process. Durable replay and interactive approval are in tension; the log is ours either way.

## ADR-016 — Aggregators, not vendors

One adapter per domain — home, car, finance — never one per device or institution. Vendor fan-out is the aggregator's problem, not ours.

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

## ADR-005 — Every action records its way back

Undo is the user's remedy, not an inverse operation — resubscribe, correct, call back. Handled is gated on granted authority and confidence, never on reversibility; otherwise the irreversible chores the user most wants gone are the exact ones handed back to them.

## ADR-006 — The weekly look reports, never grades

Life beside the stated Rules. No score, no ranking, no recommendation.

## ADR-007 — No fixed screens

Views are generated on request and disposable. No view is privileged; discarding one loses nothing.

## ADR-008 — The user leaves with everything

Rules, event log, and action log export in full to open formats. No capability is reachable only through the hosted service.

## ADR-009 — Each step stands alone

Finances, voice and email, robot. Each is independently complete and none requires the next. Stopping at one is a supported end state, not an unfinished setup.

## ADR-010 — Physical work routes to an executor

Physical work is a Demand with an executor — person, service, or robot. The core knows only "executor" and never learns a specific robot. Which units are supported is a product decision that starts small, not an architectural one.

## ADR-011 — One log is the product surface

Every Demand and every action appends to one ordered log. Generated views, the weekly look, and undo are all queries over it. No second store.

## ADR-012 — What the user keeps is never Handled

The Rules name what to hand over and what to keep. OTIUM only Handles the first. A Demand touching what they kept is Brought — that friction is the life they asked to protect, and removing it removes the thing.

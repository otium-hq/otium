# OTIUM 🕰️

![](https://img.shields.io/gitlab/pipeline-status/otium-hq/otium?branch=main&logo=gitlab)
![](https://gitlab.com/otium-hq/otium/badges/main/coverage.svg)
![](https://img.shields.io/badge/3.13.2-gray?logo=python)
![](https://img.shields.io/badge/ty_checked-gray?logo=astral)
![](https://img.shields.io/badge/uv-gray?logo=uv)
![](https://img.shields.io/badge/site-otium.run-9A671D)

> A life spent on what you meant it to be.

You tell OTIUM once, in depth, what you want your life to look like. That becomes
your **Rules**. Every **Demand** on your time is then **Sorted** against them:
**Handled** quietly, **Brought** to you, or **Pushed back**.

- [`system_adrs.md`](system_adrs.md) — the rules this is built to
- [`UBIQUITOUS_LANGUAGE.md`](UBIQUITOUS_LANGUAGE.md) — the vocabulary

# Diagrams

## Context

```plantuml
actor user
file rules <<markdown>>
database log
rectangle sorter
cloud model
cloud adapters <<finance | comms | executor>>

user -d-> rules : writes, edits anytime
adapters -r-> sorter : Demand
sorter -u-> rules : reads
sorter -r-> model : prompt
sorter -d-> log : append
sorter -u-> user : Brought
sorter -d-> adapters : Handled
log -u-> user : views, the honest look
```

## Sequence — the core loop

```plantuml
actor user
participant adapter
participant sorter
participant model
database log

adapter -> sorter : Demand
sorter -> sorter : read Rules
sorter -> model : prompt
model --> sorter : Outcome

alt Handled
  sorter -> adapter : act
  sorter -> log : append action + way back
else Brought
  sorter -> user : ask
  user --> sorter : decide
  sorter -> log : append decision
else Pushed back
  sorter -> adapter : decline
  sorter -> log : append refusal
end
```

# Structure

```
src/otium/
├── config.py
├── models.py            Demand, Outcome, Rules
├── sorter.py            Sorter — Demand + Rules → Outcome
├── test_sorter.py
├── log_service.py       LogService — the one log
├── test_log_service.py
└── clients/             one module per external system, named for the system
    ├── anthropic.py
    ├── test_anthropic.py
    ├── openai.py
    ├── plaid.py
    └── twilio.py

tests/
├── fixtures/containers.py
└── test_integration.py
```

Unit tests colocated as `test_foo.py`, dependencies patched — no network, no keys.
Integration in `tests/`, testcontainers where a real service is needed.

Suffixes: `_service`, `_client`, `_controller`, `_module`, `_dto`, `_entity`.
Never `_adapter`.

# OTIUM 🕰️

![](https://img.shields.io/badge/site-otium.run-9A671D)

> A life spent on what you meant it to be.

# Overview

## Project Description

Most people don't live the way they meant to. Not from weakness — staying on
track is a full-time job nobody has. OTIUM does that job.

You tell it, once and in depth, what you want your life to look like. That
becomes your **Rules**. From then on every **Demand** on your time is **Sorted**
against them: **Handled** quietly, **Brought** to you, or **Pushed back**.

Three steps, in your own time, stop at any one:

| | Step | Reach |
|---|---|---|
| 01 | Connect your finances | read, reconcile, dispute |
| 02 | Let it speak for you | email and phone calls |
| 03 | Add a robot | the physical world |

## Decisions

The rules this system is built to. Every one is testable, and the first ten are
promises made on [otium.run](https://otium.run) — see [`system_adrs.md`](system_adrs.md).

## Language

Terms in **bold** above are ubiquitous language, taken from the site copy. If a
word isn't on the site it doesn't belong in the domain layer — see
[`UBIQUITOUS_LANGUAGE.md`](UBIQUITOUS_LANGUAGE.md).

# Diagrams

## Context

The user owns the Rules. Everything else exists to Sort Demands against them and
write what happened to one log.

```plantuml
actor user

file rules <<markdown, user-owned>>
database log <<append-only>>

rectangle sorter
rectangle honest_look
rectangle views

cloud model <<vendor-neutral seam>>
cloud finance <<aggregator>>
cloud comms <<email + voice>>
rectangle executor <<person | service | robot>>

user -d-> rules : writes, edits anytime
user -d-> views : describes what to see

finance -r-> sorter : Demand
comms -r-> sorter : Demand
executor -r-> sorter : Demand

sorter -u-> rules : reads
sorter -r-> model : prompt
sorter -d-> log : append

sorter -u-> user : Brought
sorter -d-> comms : Handled
sorter -d-> executor : Handled

log -u-> views
log -u-> honest_look
honest_look -u-> user : weekly
```

## Sequence — the core loop

Exactly three Outcomes, and nothing is silently dropped. An action that cannot
be undone is never Handled.

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
  sorter -> adapter : act, with its undo
  sorter -> log : append action + undo
else Brought
  sorter -> user : ask
  user --> sorter : decide
  sorter -> log : append decision
else Pushed back
  sorter -> adapter : decline
  sorter -> log : append refusal
end
```

## Sequence — the honest look

Once a week. Reports, never grades.

```plantuml
actor user
participant honest_look
database log
file rules

honest_look -> log : read the week
honest_look -> rules : read what was said
honest_look -> user : life beside the Rules
note right of user
  no score
  no advice
  the gap, stated plainly
end note
```

## Deployment

One deployable today. The monoapp arrives when there is a second.

```plantuml
node device {
  rectangle monoapp <<future>>
}
node service {
  rectangle otium
  database log
  file rules
}
cloud providers <<model | finance | comms>>

monoapp -d-> otium : HTTP
otium -d-> providers : HTTPS
otium -r-> log
otium -r-> rules
```

# Project Structure

## Repositories

| | |
|---|---|
| [`otium`](.) | this repo — the Sorter, the log, the adapters |
| [`website`](../website) | [otium.run](https://otium.run) — static, S3 + CloudFront |

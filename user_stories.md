# User Stories

Each story is the Rules, a Demand, and the Outcome. S-01 to S-06 exercise one capability alone. C-01 to C-05 combine them.

## S-01 — money

**Rules** Flag anything that looks like a double charge.
**Demand** Two identical $79.99 charges from Acme Cloud, four minutes apart.
**Outcome** Brought, both charges side by side. Nothing acted on — read only.

## S-02 — email

**Rules** I don't read newsletters. Get me off lists I ignore.
**Demand** A newsletter arrives that hasn't been opened in a year.
**Outcome** Handled — unsubscribed by reply. Way back is resubscribing.

## S-03 — sms

**Rules** Keep weekday mornings clear.
**Demand** "Reply Y to confirm your appointment Thursday 3pm."
**Outcome** Handled — confirmed; the slot is outside the protected hours.

## S-04 — phone

**Rules** Haircut every six weeks, Thursdays if possible.
**Demand** Six weeks since the last cut. The barber takes no online bookings.
**Outcome** Handled — called, booked Thursday, told the user who and when.

## S-05 — web

**Rules** Cancel anything unused for six months.
**Demand** A subscription untouched since February. No API; only a retention flow in a portal.
**Outcome** Handled where the terms permit automated access to the user's own account — cancelled, confirmation in the log. Where they forbid it, Brought with the direct link and the account details (ADR-013).

## S-06 — robot

**Rules** Bins go out Tuesday night.
**Demand** It is Tuesday, 8pm.
**Outcome** Handled by the executor. No API, no comms — the cleanest test of the executor seam.

## C-01 — money + web · the slow leak

**Rules** Subscriptions under $150 a month. Tell me when the month won't cover itself.
**Demand** The month is $220 short. Six recurring charges have crept up 9% since last year.
**Outcome** Brought — the leak, the four ways out (shop it, inflation, cancel, bite the bullet), and a recommendation with the figures behind it. The shortfall is the trigger, not the price rise.

## C-02 — money + phone · the disputed charge

**Rules** Dispute anything I didn't authorise, up to $500, without asking me.
**Demand** A $312 charge from a merchant the user has never used.
**Outcome** Handled — called the issuer, opened the dispute, case number logged. Way back is a call to withdraw it.

## C-03 — email + phone · the reschedule

**Rules** Keep Thursday evenings free. Never move something I said mattered without asking.
**Demand** The clinic emails to move Tuesday's appointment; their booking line is the only way to rebook.
**Outcome** Handled — called, took the first slot that fits the Rules, replied to confirm.

## C-04 — money + email + phone + web · the denied claim

**Rules** Fight anything wrongly billed. Keep me out of it until you need me.
**Demand** A $1,400 claim denied that the policy covers.
**Outcome** Handled over six weeks — the policy pulled, the denial letter read, two calls, one written appeal, resolution logged. Brought only at the point of appeal, because signing is the user's.

## C-05 — all six · sort out the trip

**Rules** Two weeks in October, under $4,000, no red-eyes. The itinerary is mine to choose.
**Demand** "Sort out the trip."
**Outcome** Brought once — the options, priced. Then Handled: flights and rooms booked, calendar filled, confirmations filed, day-of updates by sms, bags at the door. What the user keeps is choosing where to go and being there (ADR-012).

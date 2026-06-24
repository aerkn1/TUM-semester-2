# Weekly Study Calendar

Generated: 2026-06-24
Coverage window: 2026-06-24 to 2026-06-30
Source of truth: `learning-system/review-dashboard.md`
Schedule semantics: chained model per `Spaced Repetition Schedule Semantics` in root `AGENTS.md`. `First Pass` = first active-recall completion date. Each `D+n` chains off the prior actual completion date (`D+1 = First Pass + 1`, `D+3 = D+1 completion + 3`, ...). Items with no `First Pass` are pending-first-pass candidates, not overdue repairs.

## Priority Warning

Today is 2026-06-24. The Finance Redemptions/Annuities/Capital Budgeting clarification was saved today, but it did not complete a first active-recall pass. No `First Pass` or `D+n` cell was advanced.

The dashboard has no recorded completions for the June 14-19 repair placements. Treat those items as an unrecorded repair backlog until the user confirms completion or a repair session is done. Do not let pending-first-pass topics crowd out missed chained reviews.

Finance-specific boundary from today's clarification:

```text
Capital Budgeting = operating FCF + WACC -> project NPV.
Redemptions       = loan terms -> debt-service schedule.
Annuities         = repeated-payment formula inside Redemptions.
```

For the next Finance study block, repair the time-value/annuity base before a formal Redemptions first pass: interest conventions -> annuity-immediate/due -> grace-period repayment base -> redemption schedule -> Capital Budgeting bridge.

## Exam Countdown And Allocation

| Priority | Course | Exam Date | Days From Today | Current Allocation Rule |
|---:|---|---:|---:|---|
| 1 | Supply Chain Management | 2026-07-20 | 26 | Lead new coverage and numerical/sample-exam practice after overdue repairs are audited. |
| 2 | Marketing | 2026-07-22 | 28 | Alternate with SCM; preserve Chapter 01 -> 05 sequence. |
| 3 | Business Law | 2026-07-28 | 34 | Finish repair routers, then Agency and remaining doctrine. |
| 4 | Finance and Investment Management | 2026-08-03 | 40 | Keep calculation repairs current; do Annuities before Redemptions and Capital Budgeting before Cost of Capital. |
| 5 | Organization | 2026-08-06 | 43 | Start Session 01 when capacity opens; do not jump to Sessions 07-09 before prerequisites. |

German A1.1 has no exam date recorded. Keep the saved continuation compact and reassess its allocation when the date or assessment requirement is provided.

## Today Plan

| Order | Course | Item | Type | Target | Notes |
|---:|---|---|---|---|---|
| 1 | Finance | Redemptions + Annuities + Capital Budgeting bridge | Clarification and note refinement | Completed | Saved grace-period capitalization, repayment-base logic, annuity-due/immediate timing, and PV-versus-NPV distinction. No first-pass dates advanced. |
| 2 | All courses | June 14-19 repair backlog | Audit/repair | Due before heavy new starts | Confirm whether any old repairs were completed outside the saved record; otherwise treat them as missed/unrecorded. |
| 3 | Finance | Interest -> Annuities -> Redemptions | First-pass prerequisite chain | Next Finance route | Do Annuities before a formal Redemptions first pass; use today's clarification as the bridge. |

## Completed Recently

| Date | Course | Item | Type | Result | Next Planned Review |
|---|---|---|---|---|---|
| 2026-06-24 | Finance | Exercise 05 Redemptions + Exercise 03-04 Annuities + Capital Budgeting bridge | Clarification and wiki refinement | Added repayment-base logic, capitalized-interest grace mechanics, annuity-due/immediate timing, and PV-versus-NPV boundary | First pass still pending; compact targeted check for the new weak spots on 2026-06-27. |
| 2026-06-14 | Finance | Capital Budgeting + Exercise 05 Redemptions | Clarification and wiki refinement | Added full worked slide/exercise cases, analogies, context language, WACC-versus-loan-rate clarification, and a project-value-versus-financing-feasibility bridge | Both remain first-pass pending; bridge repair now unrecorded and should be folded into the next Finance calculation block. |
| 2026-06-13 | Finance | Session 05-06 Capital Budgeting | Clarification | Decision-use bridge, FCF position, incremental logic, positive `Delta NWC`, alternatives, further adjustments, and NPV scenario matrix saved | Compact bridge check remains needed before Cost of Capital. |
| 2026-06-13 | Organization | Sessions 07-08 Informal Organization + Session 09 Dynamic Perspectives | Material ingestion | Integrated exam-ready notes, context companions, case analysis, and lecture graph generated | Pending first pass; maintain Session 01 -> 09 prerequisite order. |
| 2026-06-13 | Marketing | Chapter 01 - Basic Concepts | First pass | Completed by user report; answer-level evidence was not captured in this chat | `D+1` completion not recorded; audit before Chapter 02 if not already done. |
| 2026-06-12 | SCM | EOQ, Production Systems, Batching | First pass | Completed by user report; answer-level evidence was not captured in this chat | `D+1` repair from June 17 is unrecorded. |
| 2026-06-07 | Finance | Investment Analysis | Delayed `D+1` repair | Completed by user report; answer-level evidence was not captured in this chat | `D+3` repair from June 17 is unrecorded. |

## Unrecorded Repair Backlog

These items were scheduled before 2026-06-24 but do not have recorded completion dates in the dashboard. If the user completed any of them outside this chat, update the dashboard before rescheduling.

| Original Date | Course | Item | Checkpoint | Current Handling |
|---|---|---|---|---|
| 2026-06-14 | Business Law | Contract Law III + Standard Business Terms | Two overdue `D+1` repairs | Audit first; if not completed, repair before new legal material. |
| 2026-06-14 | Marketing | Chapter 01 - Basic Concepts | `D+1` | Audit before Chapter 02. |
| 2026-06-15 | Finance | Exercise 01-02 Interest Calculation | Overdue `D+1` repair | Repair before Annuities, Redemptions, and Bonds. |
| 2026-06-16 | Business Law | Week 01-02 Introduction + Contract Law I + Contract Law II | `D+3` Intro plus `D+1` Contract I/II | Audit before Agency if not completed. |
| 2026-06-17 | SCM | Forecasting + Random Variables + Newsvendor + EOQ/EPQ | `D+7` demand pipeline plus Topic 05 `D+1` | Audit before Kristen Cookie/OceanCove expansion. |
| 2026-06-17 | Finance | Investment Analysis Session 03-04 | Overdue `D+3` repair | Combine with Capital Budgeting bridge before Cost of Capital. |
| 2026-06-18 | German A1.1 | Lektion 4 plus Lektion 2/3 continuation | `D+1` Lektion 4 plus in-progress continuation | Audit before new German A1.1 overview work. |
| 2026-06-19 | Finance | Financial Analysis + Fundamental Analysis | Overdue `D+1` repair | Audit before later Finance valuation topics if time permits. |

## Active First-Pass Sessions In Progress

| Resume Priority | Course | Item | Session File | Next Prompt |
|---:|---|---|---|---|
| 1 | German A1.1 | Lektion 2 - Hobbies, Verb Position, Appointments | `german-a1-1/wiki/lektion-02-hobbies-verb-position-and-appointments/lektion-02-hobbies-verb-position-and-appointments-active-recall-session-2026-06-04.md` | Rewrite: `Sie ist Journalistin`; `Er ist Journalist`; `Hast du am Freitag Zeit?`; `Ich habe am Freitag keine Zeit`; `Wir treffen uns am Freitag`. |
| 2 | German A1.1 | Lektion 3 - City, Articles, Negation, Adjectives | `german-a1-1/wiki/lektion-03-city-articles-negation-and-adjectives/lektion-03-city-articles-negation-and-adjectives-active-recall-session-2026-06-04.md` | Rewrite: `Nein, das ist kein modernes Hotel` and `Nein, das sind keine guten Restaurants`. |

## Pending-First-Pass Queue

Topics with a wiki note but no completed first active-recall session. They are candidates, not D+n overdue, until `First Pass` is completed.

| Candidate Priority | Course | Item | Note Generated | Prerequisite / Warning |
|---:|---|---|---|---|
| 1 | SCM | Kristen Cookie Case | 2026-05-14 | Earliest exam; audit SCM repair backlog first. |
| 2 | Marketing | Chapter 02 Branding | 2026-05-14 | Do after Chapter 01 `D+1` audit/repair. |
| 3 | Finance | Exercise 03-04 Annuities | 2026-05-16 | Required before formal Redemptions first pass. |
| 4 | Finance | Exercise 05 Redemptions | 2026-05-16 | Clarification saved 2026-06-24; do after Annuities first pass. |
| 5 | Finance | Session 05-06 Capital Budgeting | 2026-06-06 | Bridge clarification saved; formal retrieval still pending before Cost of Capital. |
| 6 | Finance | Session 07-08 Cost of Capital | 2026-06-06 | Do after Capital Budgeting first pass; WACC/CAPM discount project FCF risk. |
| 7 | Business Law | Agency | 2026-06-04 | Do after Contract Law/SBT repair audit. |
| 8 | Organization | Session 01 - Definitional Basics | 2026-05-16 | Required foundation for all later Organization sessions. |
| 9 | Organization | Sessions 07-08 and Session 09 | 2026-06-13 | Deferred until Sessions 01-06 first passes are complete. |

## Recommended Next Starts

| Priority | Course | Subject | Why |
|---:|---|---|---|
| 1 | Backlog | Audit June 14-19 completions | The dashboard has stale planned repairs; source-of-truth status should be corrected before new scheduling. |
| 2 | Finance | Interest Calculation repair, then Annuities first pass | This gates Redemptions and Bonds; today's clarification depends on annuity timing. |
| 3 | SCM | Kristen Cookie Case first pass | Earliest exam and process/capacity foundation once SCM repair backlog is checked. |
| 4 | Marketing | Chapter 02 Branding first pass | Second exam and direct continuation from Chapter 01. |
| 5 | Finance | Redemptions first pass | Now conceptually clarified, but should follow Annuities. |
| 6 | Finance | Capital Budgeting first pass | Needed before Cost of Capital; include WACC/redemption boundary. |
| 7 | Business Law | Agency first pass | Next legal doctrine after Contract Law/SBT repair. |
| 8 | Organization | Session 01 Definitional Basics first pass | Required prerequisite for all later Organization sessions. |

## Weekly Mixed Practice Suggestions

| Block | Courses | Task | Hint |
|---|---|---|---|
| A | Finance Interest Calculation + Annuities + Redemptions | One loan drill: convert rate/periods, identify annuity-immediate or annuity-due, then calculate the post-grace repayment base and equal payment. | Grace changes the base; timing changes the annuity factor. |
| A2 | Finance Investment Analysis + Capital Budgeting | One project case: choose NPV as the decision rule, build incremental FCF, then compare downside/base/upside NPVs. | Known adjustments complete FCF first; scenarios test ranking robustness. |
| A3 | Finance Capital Budgeting + Redemptions | One oven case: calculate operating project NPV, then build a loan schedule with one capitalized-interest grace variant and compare annual FCF with debt service. | Positive NPV answers value creation; redemption answers financing feasibility. |
| A4 | Finance Capital Budgeting + Cost Of Capital | Build project FCF, then justify whether WACC, CAPM, or comparable asset beta gives the right discount rate. | Cash-flow risk first; formula second. |
| B | SCM Forecasting + Random Variables + Newsvendor + EOQ/EPQ | Route one demand case from forecast error to uncertainty model to order quantity. | One-shot uncertain commitment = Newsvendor; recurring replenishment = EOQ/EPQ plus reorder logic. |
| C | Marketing Chapter 01 + Branding | Explain customer value, then define one brand association and how it affects retention or willingness to pay. | Customer value first; brand meaning second. |
| D | Business Law Contract Law I-III + SBT + Agency | One full case: who is bound, was a contract formed, are SBT valid, and what exit route applies? | Who is bound before which clause applies before which remedy. |
| E | Organization Formal Design + Informal Organization | Compare formal roles and informal culture/power/knowledge mechanisms in one case. | Formal structure explains authority; informal mechanisms explain behavior. |

## End-Of-Session Update Checklist

After every study session:

1. If this session completed a first pass, write the completion date into `First Pass` for that row in `learning-system/review-dashboard.md` and carry the planned `D+1 = First Pass + 1` date in the status field.
2. If this session closed a `D+n` checkpoint, write the actual completion date into the `D+n` cell and compute the next planned date by adding the next interval to that completion date.
3. Add weak spots to the Mistake Ledger with the next review date.
4. Mark any missed planned dates explicitly in the status field; schedule a repair date for the missed checkpoint.
5. Refresh this weekly calendar with the new current date and chained next actions.
6. Keep Weekly Mixed Practice populated with concrete, low-context continuation hints.

# Session 03-04 Investment Analysis Active Recall Session - 2026-05-31

Source note: `session-03-04-investment-analysis.md`
Bridge note: `annuity-bridge-to-investment-analysis.md`
Context companion: `CONTEXT.md`
Course: Finance and Investment Management
Session type: first active-recall pass, completed after clarification-based retrieval

## Completion Status

First Pass completed: 2026-05-31

This session began as a clarification session and developed into retrieval practice with user answers, corrections, and applied classification tasks. At the user's request, and because the user successfully answered multiple closed-form classification and interpretation prompts after correction, it is counted as the first active-recall pass for Session 03-04 Investment Analysis.

Next checkpoint:

```text
D+1 review due 2026-06-01
```

## Recall Prompts, User Answers, And Feedback

| Prompt | User Answer | Feedback |
|---|---|---|
| Case A: saving EUR 2,000 at the end of every year for 10 years, asking future value. Is this Annuities or Investment Analysis? | "1-annuity - asking the value of money at a certain time" | Green. This asks for value of a repeated payment stream at a target date, not an accept/reject project decision. |
| Case B: a company pays EUR 50,000 for a machine generating EUR 12,000 per year for 6 years; should it buy? | "2-investment analysis - decision for the investment to accpet or reject" | Green. The final output is an investment decision. Annuity valuation may be a substep. |
| For a project costing EUR 100,000 today and paying EUR 30,000 at the end of each year for 5 years at 10%, what goes into NPV and where does annuity logic enter? | "project cost, IRR and the cost of capital is required for NPV... Annuity caluclation comes in when we need to find out the time value of money..." | Yellow. Correct bridge intuition, but IRR is not an NPV input. NPV needs cash flows, timing, and cost of capital. IRR is solved separately from the same cash flows. |
| What is the difference between annuity-immediate and annuity-due? | "not sure what is the difference..." | Red-to-yellow repair. Immediate = end-of-period payments; due = beginning-of-period payments. |
| A project pays EUR 10,000 at the beginning of each year for 4 years. Immediate or due? | "annuity due" | Green. Add reason: payments occur at the beginning of each period. |
| Project costs EUR 80,000 and pays EUR 20,000 at the beginning of each year for 5 years. Write NPV setup. | "NPV = -80000 + 2000/1.10 + 2000/1.10^2 + 2000/1.10^3" | Yellow repair. Use EUR 20,000, five payments, and because it is annuity-due the first payment is at `t=0`: `-80,000 + 20,000 + 20,000/1.10 + ... + 20,000/1.10^4`. |
| If the same payments are at the end of each year, what do the exponents go up to? | "up to 5" | Green. End-of-period five-payment annuity-immediate uses `t=1` through `t=5`. |
| Why is annuity-due worth more than annuity-immediate? | "because it provides ome extra payment period" | Yellow repair. Same number of payments, each one period earlier. Higher PV comes from earlier timing, not an extra payment. |
| If two projects cost EUR 80,000 and pay EUR 20,000 five times, but A pays at the beginning and B at the end, which has higher NPV? | "project A due to the upfront cash payment with high NPV" | Green with wording correction. Project A has higher NPV because payments arrive one period earlier and are discounted less. |
| A firm deposits EUR 20,000 at the beginning of each year for 4 years at 6%. Formula type? | "annuity due, payment at the beginning" | Green. More precise: FV of annuity-due because the target is a future fund. |
| Same firm deposits EUR 20,000 at the end of each year for 4 years. What changes? | "payment period shifts and relatively low NPV" | Yellow repair. Say lower FV, not lower NPV, because the task asks how much the fund grows to. |
| If the question asks "how much will we have in 4 years?", PV or FV? | "fv" | Green. Future target means compound forward. |
| Company must repay EUR 100,000 in 5 years and deposits at the end of each year at 5%. Formula type? | "pv of annuity immeditte?" | Yellow repair. Correct type is FV of annuity-immediate: future target plus end-of-period deposits. |
| Same repayment target, deposits at beginning of each year. Formula type? | "fv with annuity due" | Green. Future target plus beginning-of-period deposits. |

## Refined Mental Models

| Concept | Refined Mental Model | Quality |
|---|---|---|
| NPV | Bring all project cash flows to today and compare PV of benefits with cost. | green |
| IRR | The break-even discount rate solved from cash flows, not an input into NPV. | yellow |
| Annuity bridge | Annuity valuation gives the PV or FV of a repeated stream; Investment Analysis uses PV in NPV to decide accept/reject. | green |
| Annuity-immediate | Payments occur at the end of each period, e.g. `t=1` to `t=5`. | green |
| Annuity-due | Payments occur at the beginning of each period, e.g. `t=0` to `t=4`. | green |
| Due vs immediate value | Same number of payments; due is more valuable because cash arrives one period earlier. | yellow |
| PV vs FV direction | PV/NPV for today's value or accept/reject decisions; FV for accumulation and sinking-fund targets. | yellow |
| Mixed-flow comparison | Split cash flows by pattern, value each part at the same date, then compare NPV. | yellow |

## Weak Spots

| Weak Spot | Error Type | Corrective Action | Next Review |
|---|---|---|---|
| IRR treated as an input into NPV | `comparison` | State NPV inputs first: cash flows, timing, cost of capital. Then state IRR is solved separately. | 2026-06-01 |
| Annuity-due described as an extra payment | `concept` | Draw the timeline and count payments; due has same count, shifted one period earlier. | 2026-06-01 |
| PV vs FV direction in sinking-fund cases | `comparison` | Ask whether the target date is today or future before choosing PV/FV. | 2026-06-01 |
| Mixed annuity-flow comparison | `application` | Split by flow type, compute each PV at `t=0`, add PVs, subtract cost, compare NPV. | 2026-06-01 |

## Next Recall Prompts

1. Explain why IRR is not an input into NPV.
2. Draw a five-payment annuity-immediate and a five-payment annuity-due timeline.
3. A project costs EUR 100,000 and pays EUR 30,000 at the end of each year for 5 years at 10%. Set up NPV and name the annuity type.
4. A company must accumulate EUR 100,000 in 5 years with end-year deposits. Name the formula type and set it up.
5. Compare two mixed-flow projects by splitting cash flows, computing PV of each part, and choosing the higher NPV.

## References

- `session-03-04-investment-analysis.md`
- `annuity-bridge-to-investment-analysis.md`
- `CONTEXT.md`
- `session-03-04-investment-analysis-clarification-session-2026-05-31.md`


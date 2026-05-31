# Investment Analysis Clarification Session - 2026-05-31

Source note: `session-03-04-investment-analysis.md`
Context companion: `CONTEXT.md`
Course: Finance and Investment Management
Session type: clarification before first active recall

## User Clarification Questions

1. "I need a clearer relationship and comparison frame for NPV and IRR. What they actually means and how it is interpreted properly for decision making over investments?"
2. "What actually is the cost of capital? Give me example from real life. Is it the cost of investment? How it becomes percentage?"
3. "Where the IRR comes from? How it is determined?"
4. "So basically this is the continuation of the cash flow calculations?"
5. "Given that, give some example use cases with end to end calculations and interpretation."
6. "How about discount rate?"
7. "How about the IRR pitfalls mentioned? Like delayed investments and multiple IRRs and nonexistency?"
8. "What we mean by payback period ignores time value of money, ignores cash flow and arbitrary cutoff?"
9. "I also noticed that we refer session 03-04 as investment analysis whereas the exercise 03-04 is called annuities. When I check the session 03-04, no annuities mentioned. Could you double check?"
10. "Maybe prepare a wiki document within session 03-04 also for annuities first for me to understand as linked with the topic about how we interpret and map it to the actual required topic."
11. "How this difference actually attracts the investor in real life use cases? Give me some examples."
12. "How this also differs for varying annuities like perpetuity, and other varying annuities while comparing the firms or operations? From both investment and annuity calculations interpretation."
13. "Give some real use case examples with calculations."
14. "Also do the comparsional evaluation via calculation based cases for mixed annuity flow types with also immediate and due annuity mixes."
15. "Maybe we continue to the same clarification session also from the future value point of view. We just covered present value so far."

## Professor-Level Clarification

Investment analysis continues the earlier time-value-of-money track. First, individual cash flows are moved across time using PV/FV logic. Then a whole project is treated as a cash-flow timeline and judged with decision metrics.

The core chain is:

```text
cash-flow timeline -> discount cash flows -> calculate NPV -> compare to zero -> use IRR/payback/PI only with their limits
```

NPV is the primary rule because it measures value in money today. A positive NPV means the project creates value after compensating capital providers for time, risk, and opportunity cost.

IRR is a support metric. It is not chosen externally. It is solved from the project cash flows as the discount rate that makes NPV equal zero.

Cost of capital is not the euro amount invested. It is the required return percentage demanded by lenders and equity investors. It becomes the discount rate when the project risk matches that required return.

## Refined Mental Models

| Topic | Refined Mental Model | Quality |
|---|---|---|
| NPV | "How many euros of value does this project create today after paying the required return?" | green |
| IRR | "What break-even return rate is implied by this project cash-flow pattern?" | green |
| Cost of capital | "The required return percentage, not the initial investment cost." | yellow |
| Discount rate | "The rate used to translate future cash flows into today's money." | green |
| Payback | "A liquidity recovery measure, not a value-maximization measure." | yellow |
| IRR pitfalls | "When cash flows are non-normal, IRR can reverse logic, multiply, or not exist." | yellow |
| Lecture vs exercise numbering | "Session 03-04 Investment Analysis and Exercise 03-04 Annuities are separate tracks; annuities support NPV when cash flows repeat." | green |
| Annuity-immediate vs annuity-due | "Immediate pays at period end; due pays at period beginning. Due has the same number of payments, one period earlier." | yellow |
| Annuity result vs investment decision | "Annuity valuation gives PV of a stream; Investment Analysis compares PV with cost via NPV." | green |
| Mixed annuity flows | "Split cash flows by pattern, value each part at one date, add PVs, subtract cost, then compare NPV." | yellow |
| Future value direction | "If the target is a future fund or repayment amount, compound forward with FV rather than discounting back with PV." | yellow |

## Worked Examples

### Normal Project

```text
CF_0 = -1,000
CF_1 = +450
CF_2 = +450
CF_3 = +450
r = 10%

NPV = -1,000 + 450/1.10 + 450/1.10^2 + 450/1.10^3
NPV = 119.08
```

Interpretation: accept. The project creates EUR 119.08 today after meeting the 10% required return.

The IRR is about 16.7%. This is the break-even rate. Since `16.7% > 10%`, IRR agrees with NPV for this normal stand-alone project.

### One-Year IRR

```text
CF_0 = -100
CF_1 = +112

0 = -100 + 112/(1+IRR)
IRR = 12%
```

If the cost of capital is 10%, the project creates value. If the cost of capital is 15%, the project destroys value.

### Mutually Exclusive Scale Conflict

| Project | Cash Flows | IRR | NPV at 10% |
|---|---|---:|---:|
| A | `-100, +140` | 40% | 27.27 |
| B | `-1,000, +1,250` | 25% | 136.36 |

Choose B if only one can be accepted and both are feasible. A has the higher percentage return; B creates more euro value.

## IRR Pitfall Corrections

| Pitfall | What Goes Wrong | Correction |
|---|---|---|
| Delayed investment | Cash arrives before later costs, so higher discount rates can make the project look better. | Use NPV at the relevant cost of capital. |
| Multiple IRRs | More than one sign change can create multiple rates where NPV equals zero. | Do not choose the "best-looking" IRR; use NPV. |
| Nonexistent IRR | The NPV curve may never cross zero. | State that IRR cannot be used; use NPV. |

## Payback Corrections

| Limitation | Meaning | Exam Correction |
|---|---|---|
| Ignores time value of money | Simple payback treats earlier and later euros equally. | Mention discounted cash flows or NPV. |
| Ignores later cash flows | It stops caring after the initial investment is recovered. | Compare total value creation with NPV. |
| Arbitrary cutoff | The maximum acceptable payback period is chosen without valuation logic. | Say it may be useful for liquidity risk, but not value maximization. |

## Annuity Bridge Clarification

Finance has two numbering systems:

| Track | Topic | Role |
|---|---|---|
| Lecture Session 03-04 | Investment Analysis | Project decision framework: NPV, IRR, payback, PI. |
| Exercise 03-04 | Annuities | Calculation tool for repeated cash-flow streams. |

Clarification outcome: the Investment Analysis lecture does not teach annuities as its main topic. Annuities are a mathematical-basics tool that enters Investment Analysis when project cash flows are repeated, growing, or perpetual.

High-yield bridge:

```text
Annuities tell me what a repeated cash-flow stream is worth.
Investment Analysis tells me whether the whole project creates value.
```

The user correctly classified:

| Prompt | User answer | Feedback |
|---|---|---|
| Saving EUR 2,000 at end of every year for 10 years, asking FV | Annuity | Green: asks for value at a target date, not accept/reject. |
| Machine costs EUR 50,000 and generates EUR 12,000 for 6 years, asking buy/not buy | Investment Analysis | Green: final output is an investment decision. |

## Annuity Timing Corrections

| Prompt Or Confusion | User Answer | Feedback |
|---|---|---|
| What is needed for NPV? | Included project cost, IRR, cost of capital. | Correction: NPV needs cash flows, timing, and cost of capital. IRR is not an input into NPV; it is separately solved from the same cash flows. |
| Difference between annuity-immediate and annuity-due | Not sure. | Clarified: immediate = end-of-period payments; due = beginning-of-period payments. |
| Project pays EUR 10,000 at beginning of each year for 4 years | Annuity due. | Green. Add reason: payments occur at the beginning of each period. |
| NPV setup for EUR 80,000 cost and EUR 20,000 beginning-of-year payments | Used 2,000 and only three discounted payments. | Correction: use EUR 20,000, five payments, first payment at `t=0`, then discount through `t=4`. |
| Why annuity-due is worth more | "Because it provides one extra payment period." | Correction: same number of payments, each one period earlier. |
| Real-life intuition | "Works for liquidity and cash flow of operational side." | Green: earlier cash improves operational cash cycle and can increase NPV. |

## Saved Real-Use Calculation Examples

These examples were saved in `annuity-bridge-to-investment-analysis.md`.

| Case | Result | Interpretation |
|---|---:|---|
| Constant annuity machine savings: cost EUR 80,000, EUR 20,000 end-year payments for 5 years, 10% rate | NPV = -4,184.26 | Reject; stable savings are not enough. |
| Same machine with beginning-year payments | NPV = 3,397.31 | Accept; same payments arrive earlier. |
| Growing SaaS revenue: cost EUR 120,000, EUR 30,000 year 1, 5% growth, 6 years, 12% rate | NPV = 17,599.65 | Accept if growth is credible. |
| Stable license perpetuity: EUR 15,000 forever, 10% rate, price EUR 130,000 | NPV = 20,000 | Accept. |
| Growing perpetuity: EUR 10,000 next year, 3% growth, 9% rate, price EUR 140,000 | NPV = 26,666.67 | Attractive but sensitive to `r - g`. |
| Arithmetic savings: cost EUR 35,000, savings EUR 10,000 then +EUR 2,000 per year for 4 years, 10% rate | NPV = 5,454.89 | Accept; gradual operational improvement creates value. |

## Saved Mixed-Flow Comparison Cases

| Case | Winner | Reason |
|---|---|---|
| Same EUR 20,000 payments for 5 years, immediate vs due, cost EUR 80,000, rate 10% | Due version | Same payments arrive one period earlier; NPV moves from -4,184.26 to 3,397.31. |
| Stable due payments vs growing immediate payments, cost EUR 100,000, rate 10% | Stable due | Growth alone did not beat higher and earlier cash flows. |
| Lower beginning payments vs higher end payments, cost EUR 55,000, rate 8% | Higher end-payment project | Earlier timing helps, but larger cash-flow amount can dominate. |
| Finite cash flows plus perpetuity, cost EUR 180,000, rate 10% | Reject | Even a perpetual stream can be overpriced; NPV = -40,105.18. |

## Future Value Clarification

Clarification frame:

```text
Present value asks: What is this future cash-flow stream worth today?
Future value asks: What will this cash-flow stream grow to at a future date?
```

PV is more common in Investment Analysis because NPV brings everything to `t=0`. FV is used for accumulation, savings plans, sinking funds, reinvestment plans, and future target amounts.

### User Answers And Corrections

| Prompt | User Answer | Feedback |
|---|---|---|
| Firm deposits EUR 20,000 at the beginning of each year for 4 years at 6%. Formula type? | Annuity due, payment at the beginning. | Green: FV of annuity-due because target value is future and deposits are at the beginning. |
| Same firm deposits EUR 20,000 at the end of each year for 4 years at 6%. What changes? | Payment period shifts and relatively low NPV. | Correction: say lower FV, not lower NPV, because the task asks how much the fund grows to. |
| If the question asks "how much will we have in 4 years?", PV or FV? | FV. | Green. |
| Company must repay EUR 100,000 in 5 years and deposits at end of each year at 5%. Formula type? | PV of annuity-immediate. | Correction: FV of annuity-immediate because the target is a future amount and deposits are end-of-period. |
| Same repayment target, deposits at beginning of each year. Formula type? | FV with annuity due. | Green. |

### Saved FV Examples

FV of annuity-immediate:

```text
FV = 10,000 x [(1.08)^5 - 1] / 0.08
FV = 58,666.01
```

FV of annuity-due:

```text
FV_due = 58,666.01 x 1.08
FV_due = 63,359.29
```

Sinking fund with end-year deposits:

```text
100,000 = C x [(1.05)^5 - 1] / 0.05
```

Sinking fund with beginning-year deposits:

```text
100,000 = C x [(1.05)^5 - 1] / 0.05 x 1.05
```

Exam correction:

```text
Use FV when the task asks for a future accumulated amount.
Use PV/NPV when the task asks for today's value or an accept/reject decision.
```

## Weak Spots Logged

| Weak Spot | Error Type | Corrective Action | Next Review |
|---|---|---|---|
| Cost of capital vs initial investment cost | `concept` | State cost of capital as required return percentage; initial investment as `CF_0`. | 2026-06-01 |
| NPV vs IRR decision hierarchy | `comparison` | Use: NPV = euro value today; IRR = break-even rate; trust NPV if conflict. | 2026-06-01 |
| IRR pitfalls under non-normal cash flows | `application` | Check sign changes before applying the IRR rule. | 2026-06-01 |
| Payback limitations | `comparison` | Payback measures liquidity recovery, not value creation. | 2026-06-01 |
| IRR mistakenly treated as NPV input | `comparison` | Use: NPV inputs are cash flows, timing, and cost of capital; IRR is a separate output/rule. | 2026-06-01 |
| Annuity-due vs annuity-immediate timing | `concept` | Immediate = end of period; due = beginning of period. Draw the timeline before applying formulas. | 2026-06-01 |
| Due annuity described as extra payment | `concept` | Same number of payments, each one period earlier; higher PV because discounting is lighter. | 2026-06-01 |
| Mixed-flow valuation order | `application` | Split by cash-flow pattern, value each part at one date, add PVs, subtract cost, compare NPV. | 2026-06-01 |
| PV vs FV direction in accumulation problems | `comparison` | If the target date is future, use FV; reserve PV/NPV for today's value or accept/reject decisions. | 2026-06-01 |

## Next Active Recall Prompts

1. A project costs EUR 1,000 and pays EUR 450 for three years. At a 10% cost of capital, calculate NPV and interpret the decision.
2. Explain why cost of capital is a percentage and not the same thing as the initial investment.
3. Derive IRR for `CF_0 = -100`, `CF_1 = +112`.
4. Give one example where IRR and NPV conflict, and state which rule wins.
5. Explain all three payback limitations in exam language.
6. Explain how annuity valuation becomes an input into NPV.
7. Draw timelines for a five-payment annuity-immediate and a five-payment annuity-due.
8. Compare two mixed-flow projects by splitting cash flows, valuing each stream, and choosing the higher NPV.
9. Classify funding cases as PV or FV, then as immediate or due based on payment timing.
10. Explain why beginning-year deposits require a lower sinking-fund payment than end-year deposits.

## References Back To Note

- `## Cash Flow Timeline`
- `## Net Present Value`
- `## Clarification: NPV, IRR, Cost Of Capital, And Discount Rate`
- `## IRR Pitfalls`
- `## Payback Rule`
- `## Worked Clarification Examples`
- `annuity-bridge-to-investment-analysis.md`

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

## Weak Spots Logged

| Weak Spot | Error Type | Corrective Action | Next Review |
|---|---|---|---|
| Cost of capital vs initial investment cost | `concept` | State cost of capital as required return percentage; initial investment as `CF_0`. | 2026-06-01 |
| NPV vs IRR decision hierarchy | `comparison` | Use: NPV = euro value today; IRR = break-even rate; trust NPV if conflict. | 2026-06-01 |
| IRR pitfalls under non-normal cash flows | `application` | Check sign changes before applying the IRR rule. | 2026-06-01 |
| Payback limitations | `comparison` | Payback measures liquidity recovery, not value creation. | 2026-06-01 |

## Next Active Recall Prompts

1. A project costs EUR 1,000 and pays EUR 450 for three years. At a 10% cost of capital, calculate NPV and interpret the decision.
2. Explain why cost of capital is a percentage and not the same thing as the initial investment.
3. Derive IRR for `CF_0 = -100`, `CF_1 = +112`.
4. Give one example where IRR and NPV conflict, and state which rule wins.
5. Explain all three payback limitations in exam language.

## References Back To Note

- `## Cash Flow Timeline`
- `## Net Present Value`
- `## Clarification: NPV, IRR, Cost Of Capital, And Discount Rate`
- `## IRR Pitfalls`
- `## Payback Rule`
- `## Worked Clarification Examples`

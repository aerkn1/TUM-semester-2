# Exercise 01-02 Interest Calculation Clarification Session - 2026-05-25

Primary source note: `exercise-01-02-interest-calculation.md`
Related source note: `../session-01-02-financial-analysis/session-01-02-financial-analysis-clarification-session-2026-05-25.md`

Course: Finance and Investment Management
Session mode: clarification and formula-selection repair
Scope boundary: simple interest, compound interest, intra-year compounding, continuous compounding, nominal/periodic/effective rates, present value, future value, and rate comparison. Annuities, redemptions, and bonds remain separate later topics.

## Outcome

Status: completed
Quality: green-yellow

The user asked for a general, exam-ready comparison of simple, compound, and continuous compounding with different interest-rate conventions tailored to finding values and comparing alternatives. The clarification focused on choosing the correct formula before substituting numbers.

## Clarification Prompt

User prompt: "give in general the all interest types simple, compound and continous compounding with different interest types tailored for finding values and comparisons"

## Professor Explanation

Start every interest problem with the direction of value movement:

```text
Move money forward  -> Future Value
Move money backward -> Present Value
Compare alternatives -> Convert rates to the same effective period
```

Then choose the interest convention:

| Convention | Future value | Present value | Use when |
|---|---|---|---|
| Simple interest | `FV = PV x (1 + r x n)` | `PV = FV / (1 + r x n)` | The problem explicitly says simple interest. |
| Compound interest | `FV = PV x (1 + r)^n` | `PV = FV / (1 + r)^n` | Interest is reinvested once per period. |
| Intra-year compounding | `FV = PV x (1 + r/m)^(m x n)` | `PV = FV / (1 + r/m)^(m x n)` | Nominal annual rate is compounded monthly, quarterly, etc. |
| Continuous compounding | `FV = PV x e^(r x n)` | `PV = FV / e^(r x n)` | The problem says continuously compounded. |

For comparing offers:

```text
Periodic rate = nominal annual rate / m
Number of periods = years x m
Effective annual rate = (1 + r_nominal / m)^m - 1
Continuous effective annual rate = e^r - 1
```

## Refined Mental Models

- **Simple interest** is linear growth: interest is earned only on original principal.
- **Compound interest** is exponential growth: interest earns interest.
- **Intra-year compounding** requires unit matching: monthly rate with months, quarterly rate with quarters.
- **Continuous compounding** is the limit case and uses `e`, not `(1+r)^n`.
- **Nominal rate** is quoted; **effective rate** is comparable.
- The one-period growth factor is `1 + r`, not `r`.

## Weak Spots And Current Status

| Weak Spot | Quality | Correction |
|---|---|---|
| Formula selection before calculation | green-yellow | Ask direction first, then convention. |
| Growth factor versus rate | green-yellow | Use `1 + r` as the multiplier under compound interest. |
| Nominal versus effective comparison | green-yellow | Convert offers to effective annual rates before comparing. |
| Intra-year unit matching | green-yellow | Use `r/m` and `m x n`; do not mix monthly rates with annual periods. |
| Continuous compounding | green-yellow | Use `e^(r x n)` only when the task says continuous. |

## Wiki Updates Made

- Added an `Interest-Type Selection For Values And Comparisons` section to `exercise-01-02-interest-calculation.md`.
- Refreshed `CONTEXT.md` with canonical terms for growth factor, periodic rate, matching units, simple interest, annual compound interest, intra-year compounding, and continuous compounding.
- Added exam-trap corrections for comparing nominal rates, forgetting `m x n`, and confusing annual with continuous compounding.

## Next Recall Prompts

1. EUR 1,500 invested for 4 years at 6% simple interest. Calculate future value.
2. EUR 1,500 invested for 4 years at 6% annual compound interest. Calculate future value and compare with simple interest.
3. Convert 9% nominal compounded monthly into an effective annual rate.
4. EUR 2,000 invested for 3 years at a continuously compounded rate of 5%. Calculate future value.
5. Given two bank offers with different compounding frequencies, decide which rate is better after converting to effective annual rates.

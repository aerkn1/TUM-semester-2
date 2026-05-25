# Exercise 01-02 Interest Calculation Active Recall Session - 2026-05-24

Primary source note: `exercise-01-02-interest-calculation.md`
Related full session record: `../session-01-02-financial-analysis/session-01-02-financial-analysis-active-recall-session-2026-05-24.md`

Course: Finance and Investment Management
Session mode: case-driven active recall
Scope boundary: This file records the Interest Calculation part of the Finance 01-02 session.

## Covered Prompts

- Present value with monthly interest.
- Nominal annual rate vs effective annual rate.
- Simple interest rate from beginning and ending values.
- Continuous compounding.
- Final mixed case with DuPont and quick ratio.

## Outcome

Status: completed
Quality: yellow

The user can identify present value, set up monthly discounting, distinguish nominal from effective annual rates conceptually, and solve simple ratio calculations. Main remaining weakness is choosing the exact compounding formula and keeping arithmetic precise.

## Key Feedback

- Growth factor is `1 + r`; the interest rate alone is not the growth factor.
- Effective annual rate with monthly compounding is `(1 + r/m)^m - 1`.
- Simple interest rate for EUR 3,000 to EUR 5,000 over 12 years is `(5000/3000 - 1)/12 = 5.56%`.
- Continuous compounding uses `C_n = C_0 x e^(r x n)`, not `(1+r)^n`.
- Annual compounding at 4% for two years on EUR 3,000 is `3000 x 1.04^2 = 3244.80`; continuous compounding is `3000 x e^0.08 = 3249.86`.

## Weak Spots

| Weak Spot | Quality | Correction |
|---|---|---|
| Formula convention selection | red-yellow | Decide simple, annual compound, intra-year, or continuous before substituting numbers. |
| Effective annual rate notation | yellow | Use decimals and subtract 1. |
| Simple-interest arithmetic | yellow | Formula was correct; recompute carefully before stating the percentage. |
| Continuous compounding | red-yellow | Use `e^(r x n)` and compare it to annual compounding only after calculating both. |

## Next Recall Prompts

1. EUR 2,500 must become EUR 3,000 in 10 months at monthly 0.4%; calculate present value.
2. Convert 8% nominal compounded quarterly into an effective annual rate.
3. Solve for a simple interest rate from start value, end value, and years.
4. Calculate a continuous-compounding future value and compare it with annual compounding.

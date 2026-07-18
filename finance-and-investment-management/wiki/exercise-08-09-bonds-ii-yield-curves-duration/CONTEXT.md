# Ubiquitous Language: Exercise 08-09 Bonds II

Source note: `exercise-08-09-bonds-ii-yield-curves-duration.md`
Course: Finance and Investment Management
Processed: 2026-07-09

This context file defines the term-structure and duration language needed for Exercises 8 and 9.

## Yield-Curve Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Spot Rate** | Rate from today to a future maturity, such as `I_2` from `t=0` to `t=2`. | one-year rate always |
| **Forward Rate** | Implied rate for a future interval, such as `r_2` from `t=1` to `t=2`. | spot rate |
| **Yield Curve** | Set of rates by maturity. Normal means longer maturities have higher rates; inverse means lower long rates. | one market rate |
| **Bootstrap** | Method that uses traded bond prices to infer spot and forward rates step by step. | guessing the rate |
| **Maturity-Specific Discounting** | Discounting each cash flow with the rate that matches its payment date. | one flat discount rate |

## Duration Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Macaulay Duration** | Present-value weighted average payment date of a bond's cash flows. | maturity |
| **Modified Duration** | `D / (1+r)`; first-order approximation of percentage price sensitivity to yield changes. | duration without adjustment |
| **Interest-Rate Sensitivity** | How much bond price changes when market yield changes. | default risk |
| **Convexity Caveat** | Duration is linear; true bond price response is curved, so large rate changes need convexity for accuracy. | duration failure |
| **Immunization** | Choosing portfolio duration equal to the planning horizon to offset price and reinvestment effects. | no risk at all |
| **Planning Horizon** | Investor's target date for wealth, such as `t=4` in the immunization exercise. | bond maturity |

## Core Formulas

| Formula | Meaning | Use |
|---|---|---|
| `(1 + I_2)^2 = (1 + r_1)(1 + r_2)` | Spot-forward equivalence | Solve missing forward rate. |
| `B_0 = sum CF_t / [(1+r_1)...(1+r_t)]` | Pricing from forward rates | Use when forward rates are given. |
| `D = (1/B_0) x sum[t x PV(CF_t)]` | Macaulay duration | Compute weighted average timing. |
| `D_mod = D/(1+r)` | Modified duration | Convert duration to price sensitivity. |
| `Delta B/B approx -D_mod x Delta r` | Duration approximation | Estimate small yield-change price impact. |
| `D_PF = sum x_i D_i` | Portfolio duration | Immunize by solving weights. |

## Relationships

- **Forward Rates** compound into **Spot Rates**.
- **Spot Rates** determine **Maturity-Specific Discounting**.
- **Macaulay Duration** becomes **Modified Duration** before a price-change estimate.
- **Immunization** uses **Portfolio Duration** to match the **Planning Horizon**.
- **Convexity Caveat** matters when `Delta r` is large.

## Example Dialogue

Student: "The two-year spot rate is 7%, so the second-year forward rate is also 7%."

Professor: "No. The two-year spot rate covers both years together. Use compound equivalence: `(1+I_2)^2 = (1+r_1)(1+r_2)`."

Student: "Bond B has a higher coupon, so it must have shorter duration."

Professor: "Usually higher coupons shorten duration, but maturity also matters. Bond B has six years, so its duration is still longer than Bond A."

## Flagged Ambiguities

| Ambiguity | Canonical recommendation |
|---|---|
| `r_1`, `r_2` | Treat as one-period forward rates unless the slide labels them as spot rates. |
| `I_2`, `I_3` | Treat as multi-period spot rates from today. |
| Duration versus maturity | Duration is weighted timing; maturity is final payment date. |
| Immunized | Say approximately protected around the planning horizon, not risk-free in every sense. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Averaging rates. | Use compounding, not arithmetic averages. |
| Using one flat yield when a term structure is given. | Match rate maturity to cash-flow date. |
| Forgetting the sign in duration approximation. | Yield up -> price down, so the sign is negative. |
| Treating duration approximation as exact. | For larger rate changes, convexity matters. |
| Calling all rates "interest rate". | Specify spot rate, forward rate, market yield, or discount rate. |

## Cheat-Sheet Language

```text
Yield curve question: identify spot vs forward rates -> build compound-equivalent rates -> discount each cash flow with the matching maturity.
Duration question: compute price -> compute PV-weighted payment dates -> divide by price -> convert to modified duration if estimating price change.
Immunization question: solve portfolio weights so portfolio duration equals the planning horizon.
```

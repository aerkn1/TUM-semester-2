# Exercise 03-04: Annuities

Source files:

- `finance-and-investment-management/raw/Exercise_3.pdf`
- `finance-and-investment-management/raw/Exercise_3_Annuities_Solutions.pdf`
- `finance-and-investment-management/raw/Exercise_4.pdf`
- `finance-and-investment-management/raw/Exercise_4_Annuities_Solutions.pdf`
- `finance-and-investment-management/raw/Formulary.pdf`

Lecture folder: `finance-and-investment-management/`  
Date processed: 2026-05-16

## High-Yield 80/20 Summary

Annuities are repeated cash flows. The exam risk is timing: beginning vs end of period, present vs future value, constant vs growing payments, and whether payments grow arithmetically or geometrically.

Core logic:

1. Identify whether payments are equal, arithmetically growing, or geometrically growing.
2. Identify whether payments occur at the beginning (`annuity-due`) or end (`annuity-immediate`) of each period.
3. Decide whether the question asks for present value, future value, payment amount, or duration.
4. Use the formulary, but map variables carefully.

## Core Principles

### Time Value Of Money

Only compare values at the same point in time. Annuity formulas are shortcuts for discounting or compounding each payment separately.

### No Arbitrage

Two securities with the same future cash flows and the same risk should have the same price. This underlies annuity valuation: the value of a payment stream equals the sum of the discounted cash flows.

## Annuity-Immediate vs Annuity-Due

### Annuity-Immediate

Payments are made at the end of each period.

```text
Timeline: t1, t2, ..., tN
```

### Annuity-Due

Payments are made at the beginning of each period.

```text
Timeline: t0, t1, ..., tN-1
```

Relationship:

```text
C_immediate = C_due x q
q = 1 + r
```

Intuition: annuity-due payments occur one period earlier, so they are worth one extra period of interest.

## Constant Annuities

### Future Value

Annuity-immediate:

```text
FV = C x (q^N - 1) / (q - 1)
```

Annuity-due:

```text
FV_due = C_due x q x (q^N - 1) / (q - 1)
```

### Present Value

Annuity-immediate:

```text
PV = C x (q^N - 1) / (q^N x (q - 1))
```

Annuity-due:

```text
PV_due = C_due x q x (q^N - 1) / (q^N x (q - 1))
```

## Building Loan Example Pattern

A grandmother pays EUR 2,500 at the end of each year for 30 years at 3%.

Decision problem and method choice:

- The question asks how much the repeated savings stream grows to by the end.
- Payments happen at the end of each year, so use future value of an annuity-immediate.

Known inputs:

```text
C = EUR 2,500
r = 3% = 0.03
q = 1.03
N = 30 years
```

Formula, substitution, and arithmetic:

```text
FV = C x (q^N - 1)/(q - 1)
FV = 2,500 x (1.03^30 - 1)/(1.03 - 1)
1.03^30 = 2.42726
FV = 2,500 x (2.42726 - 1)/0.03
FV = EUR 118,938.54
```

If paid at the beginning of each year:

```text
FV_due = FV_immediate x q
FV_due = 118,938.54 x 1.03
FV_due = EUR 122,506.70
```

Interpretation: beginning-of-period payments are larger in future value because every payment earns one more period of interest.

Analogy: annuity-immediate is putting each yearly deposit into the account at closing time. Annuity-due is depositing at opening time, so every deposit has one extra year inside the account.

Exam trap: do not add one extra payment for annuity-due. The number of payments stays 30; only the timing shifts one period earlier.

## Perpetuities

A perpetuity is an annuity with no finite horizon.

```text
PV = C / r
PV_due = q x C_due / r
```

Growing perpetuity, with growth rate `w` and `g = 1 + w`:

```text
PV = C / (r - w), only if w < r
PV_due = q x C_due / (r - w)
```

Exam trap: if `w >= r`, the growing perpetuity formula is invalid.

## Varying Annuities

### Arithmetic Progression

Payment changes by a fixed amount `d` each period.

```text
C_k = C + (k - 1)d
```

Use when the payment increases by a fixed euro amount, e.g. EUR 1,000 more each year.

### Geometric Progression

Payment changes by a fixed growth factor `g`.

```text
C_k = C x g^(k-1)
g = 1 + growth rate
```

Use when the payment increases by a percentage, e.g. 5% per year.

Special case: many formulas split into `g = q` and `g != q`. Always check this first.

## Worked Calculations And Analogies

### Pattern 1: Solve For Duration

A business is sold for EUR 300,000. The seller receives EUR 20,000 annually, growing 4% per year. Interest rate = 5%.

Decision problem and method choice:

- The sale price is today's value of a growing payment stream.
- The unknown is the number of payments `N`.
- Payments grow by a fixed percentage, so use the geometric growing annuity formula.

Known inputs:

```text
PV = EUR 300,000
C_1 = EUR 20,000
r = 5% = 0.05
w = 4% = 0.04
g = 1.04
q = 1.05
g/q = 1.04/1.05 = 0.990476
```

For annuity-immediate:

```text
PV = C_1/(r-w) x [1 - (g/q)^N]
300,000 = 20,000/(0.05-0.04) x [1 - 0.990476^N]
300,000 = 2,000,000 x [1 - 0.990476^N]
0.150000 = 1 - 0.990476^N
0.990476^N = 0.850000
N = ln(0.850000) / ln(0.990476)
N = 16.98 years
```

For annuity-due, payments arrive one period earlier, so the PV of the same stream is multiplied by `q`:

```text
300,000 = 1.05 x 2,000,000 x [1 - 0.990476^N]
300,000 / 2,100,000 = 1 - 0.990476^N
0.857143 = 0.990476^N
N = ln(0.857143) / ln(0.990476)
N = 16.11 years
```

Interpretation: the annuity-due duration is shorter because payments start earlier, so fewer years are needed to reach the same EUR 300,000 present value.

Analogy: the seller is filling a EUR 300,000 bucket with discounted payments. If the first payment arrives immediately instead of one year later, the bucket fills faster.

Exam trap: do not use the constant annuity formula when payments grow by 4%. The payment pattern is geometric growth.

### Pattern 2: Compare Arithmetic vs Geometric Growth

A seller can choose:

- EUR 24,000 with fixed EUR 1,000 annual increase.
- EUR 24,000 with 6% annual growth.

At 5% and 10 years, compare both alternatives at the same future date.

Decision problem and method choice:

- The options have different payment patterns, so compare them at one common date.
- Here the target date is year 10, so compound each payment forward to year 10.

Arithmetic-growth option:

```text
Payment pattern = 24,000; 25,000; 26,000; ...; 33,000

FV = 24,000 x 1.05^9
   + 25,000 x 1.05^8
   + 26,000 x 1.05^7
   + ...
   + 33,000
FV = EUR 353,427.27
```

Geometric-growth option:

```text
Payment pattern = 24,000; 24,000 x 1.06; 24,000 x 1.06^2; ...; 24,000 x 1.06^9

FV = 24,000 x 1.05^9
   + 24,000 x 1.06 x 1.05^8
   + 24,000 x 1.06^2 x 1.05^7
   + ...
   + 24,000 x 1.06^9
FV = EUR 388,687.37
```

Decision: the geometric-growth option has the higher future value by:

```text
388,687.37 - 353,427.27 = EUR 35,260.10
```

Decision logic: compare both alternatives at the same date using the same discount/interest rate.

Analogy: arithmetic growth adds the same euro step each year; geometric growth makes each increase build on the previous increase. Over longer horizons, percentage growth can pull away.

Exam trap: do not compare only the first payment or only the final payment. The full stream and timing determine value.

## Exam Decision Tree

1. Are payments repeated?
   - If no, use single cash-flow PV/FV.
   - If yes, annuity logic applies.
2. Equal payments?
   - Use constant annuity.
3. Fixed euro increase?
   - Use arithmetic progression.
4. Fixed percentage increase?
   - Use geometric progression.
5. Payment at beginning?
   - Use annuity-due or multiply immediate value by `q` where appropriate.
6. Payment at end?
   - Use annuity-immediate.
7. Ask for PV or FV?
   - Choose discounting or compounding formula.

## Common Mistakes

- Using annuity-immediate when payments occur at the beginning.
- Forgetting the extra `q` factor for annuity-due.
- Confusing arithmetic growth `d` with geometric growth `g`.
- Forgetting to check `g = q` special case.
- Comparing alternatives at different dates.
- Treating a perpetuity as a long finite annuity without justification.

## Practice Questions

1. A person saves EUR 1,000 at the end of each year for 10 years at 4%. What formula applies?
   - Answer: constant annuity-immediate future value.
2. Same payment, but at the beginning of each year. How does the value change?
   - Answer: multiply the immediate future value by `q = 1.04`.
3. Payments grow from EUR 5,000 by EUR 500 per year. Arithmetic or geometric?
   - Answer: arithmetic progression.
4. Payments grow by 3% per year. Arithmetic or geometric?
   - Answer: geometric progression, `g = 1.03`.
5. Why must `w < r` for a growing perpetuity?
   - Answer: otherwise the discounted series does not converge.

## Mermaid Knowledge Map

```mermaid
graph TD
    ANN[Annuities] --> TIMING[Payment Timing]
    TIMING --> IMM[Annuity-Immediate]
    TIMING --> DUE[Annuity-Due]
    ANN --> VALUE[Valuation Target]
    VALUE --> PV[Present Value]
    VALUE --> FV[Future Value]
    ANN --> PATTERN[Payment Pattern]
    PATTERN --> CONST[Constant]
    PATTERN --> ARITH[Arithmetic Growth]
    PATTERN --> GEO[Geometric Growth]
    GEO --> GQ[Check g = q]
    ANN --> PERP[Perpetuity]
    PERP --> GPERP[Growing Perpetuity]
    GPERP --> COND[w < r]
    DUE --> EXTRA[One Extra Period Of Interest]
```

## Subject Knowledge Graph

| Node | Meaning |
|---|---|
| Annuity | Stream of repeated payments |
| Annuity-immediate | Payments at end of period |
| Annuity-due | Payments at beginning of period |
| Present value | Value of payment stream today |
| Future value | Accumulated value at final date |
| Arithmetic growth | Fixed absolute increase per period |
| Geometric growth | Fixed percentage increase per period |
| Perpetuity | Infinite annuity |

| From | Relationship | To |
|---|---|---|
| Annuity-due | occurs earlier than | annuity-immediate |
| Earlier payment | increases | value |
| Constant annuity | assumes | equal payments |
| Arithmetic annuity | grows by | fixed amount |
| Geometric annuity | grows by | fixed factor |
| Growing perpetuity | requires | growth below discount rate |
| Annuity formulas | compress | repeated discounting/compounding |

## Links

- Previous exercise: `finance-and-investment-management/wiki/exercise-01-02-interest-calculation/exercise-01-02-interest-calculation.md`
- Next exercise: `finance-and-investment-management/wiki/exercise-05-redemptions/exercise-05-redemptions.md`
- Bridge to lecture Session 03-04 Investment Analysis: `finance-and-investment-management/wiki/session-03-04-investment-analysis/annuity-bridge-to-investment-analysis.md`

# Exercise 01-02: Interest Calculation

Source files:

- `finance-and-investment-management/raw/exercise_1.pdf`
- `finance-and-investment-management/raw/exercise 2.pdf`
- `finance-and-investment-management/raw/Exercise 2 - Solutions.pdf`
- `finance-and-investment-management/raw/T01_Interests - Solution Part 1.pdf`
- `finance-and-investment-management/raw/Formulary.pdf`

Lecture folder: `finance-and-investment-management/`  
Date processed: 2026-05-16

## High-Yield 80/20 Summary

Interest calculation is the foundation for nearly every finance exercise: valuation, annuities, redemptions, bonds, NPV, and capital budgeting. The exam risk is usually not the formula alone; it is recognizing the timing convention, compounding frequency, and whether the question asks for present value, future value, time, or interest rate.

Core principles:

1. Values at different dates cannot be directly compared.
2. Move cash flows forward by compounding.
3. Move cash flows backward by discounting.
4. Simple interest has no interest-on-interest.
5. Compound interest has interest-on-interest.
6. More frequent compounding increases the effective annual rate.
7. Continuous compounding is the limit case.

## Time Value Of Money

```text
Only compare or combine values at the same point in time.
Future value: move cash flow forward.
Present value: move cash flow backward.
```

Real-life example: EUR 1,000 today and EUR 1,000 in two years are not economically equal because today's money can earn interest.

## Interest Rate Types

Examples from the lecture:

- Deposit rate: received for bank deposits.
- Borrowing/debt rate: paid for borrowing capital.
- Prime rate: rate for most creditworthy clients.
- Central bank policy rates: ECB deposit facility, main refinancing, marginal lending.
- Money market rates: short-term rates.
- Interbank rates: banks lending to each other.
- Bond yields: yields on mid/long-term instruments.
- Nominal rate: contract-stated rate.
- Effective rate: actual earned/paid rate after compounding.
- Real rate: yield above inflation.

## Simple Interest

No compounding effect; interest is paid only on the initial capital.

```text
Future Value: C_n = C_0 x (1 + n x r)
Present Value: C_0 = C_n / (1 + n x r)
Time: n = (C_n / C_0 - 1) / r
Interest Rate: r = (C_n / C_0 - 1) / n
```

For fractional periods:

```text
C_f = C_0 x (1 + f x r)
```

Day-count conventions:

- 30/360: every month = 30 days, year = 360 days.
- Actual/360: actual days, year = 360 days.
- Actual/Actual: actual days and actual year length.

Exam trap: for partial-year questions, compute `f` using the required convention before applying the formula.

## Compound Interest

Interest is reinvested and earns interest.

```text
Future Value: C_n = C_0 x (1 + r)^n = C_0 x q^n
Present Value: C_0 = C_n / (1 + r)^n = C_n / q^n
Time: n = (ln C_n - ln C_0) / ln q
Interest Rate: r = (C_n / C_0)^(1/n) - 1
```

Where `q = 1 + r`.

Example from solution logic:

- EUR 1 at 1% simple interest for 1,217 years becomes EUR 13.17.
- EUR 1 at 1% compound interest for 1,217 years becomes EUR 181,598.35.

The difference illustrates compounding power.

## Intra-Year Compounding

Contracts often state an annual nominal rate, but interest can be compounded monthly or quarterly.

```text
Effective Annual Rate: r_eff = (1 + r/m)^m - 1
Future Value: C_n = C_0 x (1 + r/m)^(m x n)
Alternative: C_n = C_0 x (1 + r_eff)^n
```

Where:

- `r` = nominal annual rate.
- `m` = compounding periods per year.
- `n` = years.

Example:

Monthly interest of 1% means:

```text
Nominal annual rate = 12 x 1% = 12%
r_eff = (1.01)^12 - 1 = 12.68%
```

## Continuous Compounding

Interest is calculated and reinvested continuously.

```text
Future Value: C_n = C_0 x e^(r x n)
Present Value: C_0 = C_n / e^(r x n)
Effective Annual Rate: r_eff = e^r - 1
Time: n = (ln C_n - ln C_0) / r
Interest Rate: r = (ln C_n - ln C_0) / n
```

Example:

Nominal continuous rate 6%:

```text
r_eff = e^0.06 - 1 = 6.18%
```

## Worked Exercise Patterns

### Pattern 1: Needed Present Value

Question: You need EUR 1,000 in 18 months. Monthly interest = 0.35%. How much invest now?

```text
C_0 = 1000 / 1.0035^18 = 939.05
```

Alternative using effective annual rate:

```text
r_eff = 1.0035^12 - 1 = 4.28%
C_0 = 1000 / 1.0428^1.5 = 939.05
```

### Pattern 2: Compare Compounding Frequencies

Question: EUR 4,000 invested for 3 years at 6% nominal.

```text
Yearly: 4000 x 1.06^3 = 4764.06
Six-monthly: 4000 x (1 + 0.06/2)^(2 x 3) = 4776.21
Continuous: 4000 x e^(0.06 x 3) = 4788.87
```

Higher compounding frequency increases future value.

### Pattern 3: Infer Continuous Rate From Two Balances

Given `C_1 = 100,000` and `C_2 = 110,000`:

```text
r = ln(C_2 / C_1) = ln(1.10) = 9.53%
C_0 = C_1 / e^r = 90,909.09
```

## Exam Decision Rules

- Asked for payoff/final amount: future value.
- Asked how much to invest today: present value.
- Asked how long: solve for `n`, often using logs.
- Asked what interest rate: solve for `r`.
- Asked monthly/quarterly: convert via `m` or `r_eff`.
- Asked continuous: use `e^(r x n)`.
- Asked less than one year: check day-count convention.

## Common Mistakes

- Using nominal rate as effective rate.
- Forgetting to multiply years by `m` for intra-year compounding.
- Applying compound formula to simple-interest questions.
- Comparing cash flows at different dates.
- Rounding rates too early.
- Ignoring day-count conventions.

## Practice Questions

1. EUR 3,000 grows to EUR 5,000 over 12 years with simple interest. What is `r`?
   - Answer: `r = (5000/3000 - 1)/12 = 5.56%`.
2. EUR 1,000 grows to EUR 5,000 at 10% compound interest. How long?
   - Answer: `n = ln(5)/ln(1.10) = 16.89 years`.
3. Nominal annual rate is 6%, compounded semiannually for 3 years on EUR 4,000. Future value?
   - Answer: `4000 x (1.03)^6 = 4776.21`.
4. Continuous rate 4% for two years on EUR 3,000. Future value?
   - Answer: `3000 x e^0.08 = 3249.86`.

## Mermaid Knowledge Map

```mermaid
graph TD
    TVM[Time Value Of Money] --> SAME[Compare Same Date Only]
    TVM --> FV[Future Value]
    TVM --> PV[Present Value]
    FV --> SIMPLE[Simple Interest]
    FV --> COMPOUND[Compound Interest]
    FV --> INTRA[Intra-Year Compounding]
    FV --> CONT[Continuous Compounding]
    SIMPLE --> NOINT[No Interest On Interest]
    COMPOUND --> Q[q = 1 + r]
    INTRA --> REFF[Effective Annual Rate]
    CONT --> E[e^(r x n)]
    REFF --> NOM[Nominal vs Effective Rate]
    SAME --> VAL[Valuation And NPV]
```

## Subject Knowledge Graph

| Node | Meaning |
|---|---|
| Time value of money | Money has different value at different dates |
| Simple interest | Interest on initial capital only |
| Compound interest | Interest earns interest |
| Nominal rate | Contract-stated annual rate |
| Effective rate | Actual annual rate after compounding |
| Continuous compounding | Infinite compounding frequency |
| Day-count convention | Rule for fractional period calculation |

| From | Relationship | To |
|---|---|---|
| Future value | compounds | present cash flow |
| Present value | discounts | future cash flow |
| Compound interest | grows faster than | simple interest |
| Intra-year compounding | increases | effective rate |
| Continuous compounding | is limit of | intra-year compounding |
| Day-count convention | determines | fractional period |
| Interest calculation | supports | annuities, bonds, NPV |

## Links

- Related note: `finance-and-investment-management/wiki/session-03-04-investment-analysis/session-03-04-investment-analysis.md`
- Next exercise: `finance-and-investment-management/wiki/exercise-03-04-annuities/exercise-03-04-annuities.md`

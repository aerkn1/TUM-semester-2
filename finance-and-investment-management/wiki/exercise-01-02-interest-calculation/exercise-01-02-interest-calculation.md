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

## Interest-Type Selection For Values And Comparisons

Before choosing a formula, identify the direction of movement and the interest convention.

```text
Move money forward  -> Future Value
Move money backward -> Present Value
Compare alternatives -> Convert rates to the same effective period
```

| Interest type | Future value formula | Present value formula | Use when | Decision interpretation |
|---|---|---|---|---|
| Simple interest | `C_n = C_0 x (1 + r x n)` | `C_0 = C_n / (1 + r x n)` | The problem explicitly says simple interest or interest is not reinvested. | Growth is linear; interest is earned only on original principal. |
| Annual compound interest | `C_n = C_0 x (1 + r)^n` | `C_0 = C_n / (1 + r)^n` | Interest is reinvested once per year. | Growth is exponential; interest earns interest. |
| Intra-year compounding | `C_n = C_0 x (1 + r/m)^(m x n)` | `C_0 = C_n / (1 + r/m)^(m x n)` | A nominal annual rate is compounded monthly, quarterly, semiannually, etc. | Match the periodic rate and number of periods before calculating. |
| Continuous compounding | `C_n = C_0 x e^(r x n)` | `C_0 = C_n / e^(r x n)` | The problem explicitly says continuously compounded. | This is the limit case of infinitely frequent compounding. |

For the same stated annual rate and time horizon:

```text
Simple interest < Annual compounding < Intra-year compounding < Continuous compounding
```

Example with `C_0 = 1000`, `r = 10%`, `n = 2`:

```text
Simple:     1000 x (1 + 0.10 x 2) = 1200.00
Compound:   1000 x 1.10^2 = 1210.00
Continuous: 1000 x e^(0.10 x 2) = 1221.40
```

The values differ because the interest convention changes how often interest is added to the interest-earning base.

### Nominal, Periodic, And Effective Rates

Use rate conversion when the task compares bank offers or when the compounding interval is not annual.

```text
Periodic rate = nominal annual rate / m
Number of periods = years x m
Effective annual rate = (1 + r_nominal / m)^m - 1
Continuous effective annual rate = e^r - 1
```

Example: 12% nominal annual rate compounded monthly:

```text
Monthly rate = 0.12 / 12 = 0.01 = 1%
EAR = (1 + 0.12/12)^12 - 1 = 12.68%
```

Decision use: if two bank offers quote different compounding frequencies, convert both to effective annual rates before comparing. A higher nominal rate is not automatically better if compounding conventions differ.

### Formula Choice Checklist

```text
1. What is unknown: C_0, C_n, r, or n?
2. Are we moving money forward or backward?
3. Is interest simple, compound, intra-year, or continuous?
4. Do rate and period units match?
5. If comparing offers, did we convert to the same effective period?
```

## Worked Calculations And Analogies

### Pattern 1: Needed Present Value

Question: You need EUR 1,000 in 18 months. Monthly interest is 0.35%. How much must be invested today?

Decision problem and method choice:

- The target cash flow is in the future and the unknown amount is today, so this is a present value problem.
- The rate is monthly, so the period count must also be monthly.

Known inputs:

```text
Future value C_n = EUR 1,000
Monthly rate r_m = 0.35% = 0.0035
Time = 18 months
Growth factor per month q = 1.0035
```

Formula and substitution:

```text
C_0 = C_n / q^n
C_0 = 1,000 / 1.0035^18
```

Arithmetic:

```text
1.0035^18 = 1.06491
C_0 = 1,000 / 1.06491
C_0 = EUR 939.05
```

Alternative using effective annual rate:

```text
r_eff = 1.0035^12 - 1
r_eff = 1.04280 - 1
r_eff = 4.28%

C_0 = 1,000 / 1.0428^1.5
C_0 = EUR 939.05
```

Interpretation: investing EUR 939.05 today at 0.35% per month grows to EUR 1,000 in 18 months.

Analogy: this is walking backward down an escalator. You know where you want to stand after 18 monthly steps; discounting tells you where to start today.

Exam trap: do not use `n = 1.5` with the monthly rate. Either use monthly rate with 18 months, or convert to an effective annual rate and use 1.5 years.

### Pattern 2: Compare Compounding Frequencies

Question: EUR 4,000 invested for 3 years at a 6% stated annual rate. Compare yearly, six-monthly, and continuous compounding.

Decision problem and method choice:

- The question asks for the ending amount, so use future value.
- The nominal rate is the same, but the compounding convention changes the effective return.

Known inputs:

```text
C_0 = EUR 4,000
Nominal annual rate r = 6% = 0.06
n = 3 years
```

Yearly compounding:

```text
C_3 = 4,000 x 1.06^3
1.06^3 = 1.191016
C_3 = EUR 4,764.06
```

Six-monthly compounding:

```text
Periodic rate = 0.06 / 2 = 0.03
Number of periods = 2 x 3 = 6
C_3 = 4,000 x 1.03^6
1.03^6 = 1.194052
C_3 = EUR 4,776.21
```

Continuous compounding:

```text
C_3 = 4,000 x e^(0.06 x 3)
C_3 = 4,000 x e^0.18
e^0.18 = 1.197217
C_3 = EUR 4,788.87
```

Interpretation: higher compounding frequency gives interest more chances to earn interest, so the same nominal rate produces a higher future value.

Analogy: yearly compounding pays rent to the principal once per year; six-monthly compounding lets the new interest start working halfway through the year; continuous compounding keeps putting every tiny bit of interest back to work immediately.

Exam trap: the nominal 6% is not always the effective annual return. Match the compounding frequency before comparing offers.

### Pattern 3: Infer Continuous Rate From Two Balances

Question: a continuously compounded account grows from `C_1 = 100,000` to `C_2 = 110,000` over one year. Find the continuous rate and the value one year before `C_1`.

Decision problem and method choice:

- Continuous compounding is stated, so use the exponential/log formula.
- First solve the rate from the observed growth, then discount one year backward.

Known inputs:

```text
C_1 = EUR 100,000
C_2 = EUR 110,000
n = 1 year
```

Rate formula and arithmetic:

```text
C_2 = C_1 x e^r
e^r = C_2 / C_1 = 110,000 / 100,000 = 1.10
r = ln(1.10)
r = 0.09531 = 9.53%
```

Backward value:

```text
C_0 = C_1 / e^r
C_0 = 100,000 / 1.10
C_0 = EUR 90,909.09
```

Interpretation: a continuously compounded rate of 9.53% creates exactly 10% effective annual growth over one year.

Analogy: continuous compounding reports the engine's smooth running speed; the effective growth is the total distance covered after one year.

Exam trap: a 9.53% continuous rate is not the same statement as a 9.53% annual effective rate. The effective growth here is 10%.

## Exam Decision Rules

- Asked for payoff/final amount: future value.
- Asked how much to invest today: present value.
- Asked how long: solve for `n`, often using logs.
- Asked what interest rate: solve for `r`.
- Asked monthly/quarterly: convert via `m` or `r_eff`.
- Asked continuous: use `e^(r x n)`.
- Asked less than one year: check day-count convention.
- Asked to compare offers: convert all quoted rates to the same effective period.
- If `r` is monthly, `n` must be months; if `r` is annual, `n` must be years.

## Common Mistakes

- Using nominal rate as effective rate.
- Forgetting to multiply years by `m` for intra-year compounding.
- Applying compound formula to simple-interest questions.
- Comparing cash flows at different dates.
- Rounding rates too early.
- Ignoring day-count conventions.
- Using the interest rate `r` as the growth factor instead of `1 + r`.
- Using continuous compounding formula when the problem only says annual compounding.

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
    INTRA --> PERIOD[Match Rate And Periods]
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
| Periodic rate | Rate per compounding interval |
| Effective annual rate | Comparable annual rate after compounding |

| From | Relationship | To |
|---|---|---|
| Future value | compounds | present cash flow |
| Present value | discounts | future cash flow |
| Compound interest | grows faster than | simple interest |
| Intra-year compounding | increases | effective rate |
| Nominal rate | converts into | periodic rate |
| Periodic rate | must match | number of periods |
| Continuous compounding | is limit of | intra-year compounding |
| Day-count convention | determines | fractional period |
| Interest calculation | supports | annuities, bonds, NPV |

## Links

- Related note: `finance-and-investment-management/wiki/session-03-04-investment-analysis/session-03-04-investment-analysis.md`
- Next exercise: `finance-and-investment-management/wiki/exercise-03-04-annuities/exercise-03-04-annuities.md`

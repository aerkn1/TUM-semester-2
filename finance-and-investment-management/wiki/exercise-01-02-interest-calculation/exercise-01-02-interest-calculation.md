# Exercise 01-02: Interest Calculation

Source files:

- `finance-and-investment-management/raw/exercise_1.pdf`
- `finance-and-investment-management/raw/exercise 2.pdf`
- `finance-and-investment-management/raw/Exercise 2 - Solutions.pdf`
- `finance-and-investment-management/raw/T01_Interests - Solution Part 1.pdf`
- `finance-and-investment-management/raw/Formulary.pdf`

Lecture folder: `finance-and-investment-management/`  
Date processed: 2026-05-16
Source worked solutions refreshed: 2026-07-31

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

## Source Exercise Worked Solutions

Use these after you have first written the route yourself. The exam move is always: unknown -> time direction -> interest convention -> rate-period match -> arithmetic.

Source note: no A.8 label appears in the extracted Interest exercise/solution PDFs, so the worked solutions follow the visible source numbering.

### A.1: Simple-Interest Future Value

Decision problem: calculate the payoff after three years when interest is not compounded.

Known inputs:

```text
C_0 = EUR 20,000
r = 5.5% = 0.055
n = 3 years
```

Formula and arithmetic:

```text
C_n = C_0 x (1 + n x r)
C_3 = 20,000 x (1 + 3 x 0.055)
C_3 = 20,000 x (1 + 0.165)
C_3 = 20,000 x 1.165
C_3 = EUR 23,300.00
```

Interpretation: the account earns `20,000 x 0.055 = EUR 1,100` per year, for three years, so total interest is EUR 3,300. Exam trap: do not use `1.055^3`; the task is simple interest.

### A.2: Simple-Interest Present Value

Decision problem: find the amount to invest today to receive EUR 5,000 in two years without compounding.

Known inputs:

```text
C_n = EUR 5,000
r = 8.00% = 0.08
n = 2 years
```

Formula and arithmetic:

```text
C_0 = C_n / (1 + n x r)
C_0 = 5,000 / (1 + 2 x 0.08)
C_0 = 5,000 / 1.16
C_0 = EUR 4,310.34
```

Interpretation: EUR 4,310.34 plus two years of simple interest at 8% reaches EUR 5,000. Exam trap: present value must be lower than the future payoff when the rate is positive.

### A.3: Simple Interest With 30/360 Day Count

Decision problem: calculate a partial-year payoff from May 15 to September 16 using the 30/360 method.

Known inputs:

```text
C_0 = EUR 7,500
r = 2.85% = 0.0285
Day-count convention = 30/360
```

Interest days:

```text
Full months June, July, August = 3 x 30 = 90 days
Remaining May days = 15 days
September days = 16 days
Total interest days = 90 + 15 + 16 = 121 days
f = 121 / 360
```

Formula and arithmetic:

```text
C_f = C_0 x (1 + f x r)
C_121 = 7,500 x (1 + (121/360) x 0.0285)
C_121 = 7,500 x (1 + 0.009579)
C_121 = 7,500 x 1.009579
C_121 = EUR 7,571.84
```

Interpretation: partial-year interest is earned only for 121/360 of a year. Exam trap: compute the day-count fraction before applying the simple-interest formula.

### A.4: Simple-Interest Present Value With 30/360 Day Count

Decision problem: find the 14 April 2018 deposit needed to have EUR 22,500 on 23 December 2018.

Known inputs:

```text
C_f = EUR 22,500
r = 2.85% = 0.0285
Day-count convention = 30/360
```

Interest days:

```text
Full months May to November = 7 x 30 = 210 days
Remaining April days = 16 days
December days = 23 days
Total interest days = 210 + 16 + 23 = 249 days
f = 249 / 360
```

Formula and arithmetic:

```text
C_0 = C_f / (1 + f x r)
C_0 = 22,500 / (1 + (249/360) x 0.0285)
C_0 = 22,500 / (1 + 0.0197125)
C_0 = 22,500 / 1.0197125
C_0 = EUR 22,065.04
```

Interpretation: the current deposit is below EUR 22,500 because it earns interest until the car purchase date. Exam trap: do not use a full-year interest factor when the task gives exact dates.

### A.5a: Compound-Interest Rate From A Growth Multiple

Decision problem: find the annual compound rate that makes an investment double in 10 years, then the rate that makes it become 1.5 times the initial amount.

Formula:

```text
C_n = C_0 x (1 + r)^n
C_n / C_0 = (1 + r)^n
r = (C_n / C_0)^(1/n) - 1
```

Double in 10 years:

```text
r = 2^(1/10) - 1
r = 1.071773 - 1
r = 0.071773 = 7.18%
```

1.5 times the initial amount in 10 years:

```text
r = 1.5^(1/10) - 1
r = 1.041380 - 1
r = 0.041380 = 4.14%
```

Interpretation: compounding lets a moderate annual rate create a large multi-year growth multiple. Exam trap: do not divide the total growth by 10; that would be simple-interest logic.

### A.5b: Compound-Interest Time To Double

Decision problem: find how long it takes to double when the annual compound rate is 5%.

Known inputs:

```text
C_n / C_0 = 2
r = 5% = 0.05
q = 1.05
```

Formula and arithmetic:

```text
n = ln(C_n / C_0) / ln(q)
n = ln(2) / ln(1.05)
n = 0.693147 / 0.048790
n = 14.21 years
```

Interpretation: at 5% compound interest, doubling takes slightly more than 14 years. Exam trap: use logs when time is unknown under compounding.

### A.6a: Quarterly Compounding And Effective Annual Rate

Decision problem: convert nominal annual rates into quarterly periodic rates and effective annual rates.

Formula:

```text
Periodic rate = r / m
r_eff = (1 + r/m)^m - 1
m = 4 quarters
```

For `r = 2.35%`:

```text
r/m = 0.0235 / 4 = 0.005875 = 0.59% per quarter
r_eff = (1 + 0.0235/4)^4 - 1
r_eff = 1.005875^4 - 1
r_eff = 0.023708 = 2.37%
```

For `r = 2.00%`:

```text
r/m = 0.0200 / 4 = 0.005000 = 0.50% per quarter
r_eff = 1.005^4 - 1
r_eff = 0.020151 = 2.02%
```

For `r = 1.75%`:

```text
r/m = 0.0175 / 4 = 0.004375 = 0.44% per quarter
r_eff = 1.004375^4 - 1
r_eff = 0.017615 = 1.76%
```

Interpretation: the effective annual rate is slightly above the nominal annual rate because quarterly interest earns interest within the year. Exam trap: do not compare nominal rates with effective rates.

### A.6b: Quarterly Versus Six-Monthly Compounding

Decision problem: compare EUR 50,000 invested for one year at the same nominal annual rate, but with different compounding frequencies.

Known inputs:

```text
C_0 = EUR 50,000
r = 2.50% = 0.025
n = 1 year
Quarterly: m = 4
Six-monthly: m = 2
```

Quarterly compounding:

```text
C_1 = 50,000 x (1 + 0.025/4)^4
C_1 = 50,000 x 1.00625^4
C_1 = EUR 51,261.77
```

Six-monthly compounding:

```text
C_1 = 50,000 x (1 + 0.025/2)^2
C_1 = 50,000 x 1.0125^2
C_1 = EUR 51,257.81
```

Difference:

```text
51,261.77 - 51,257.81 = EUR 3.96
```

Interpretation: quarterly compounding is better by EUR 3.96 because interest is reinvested earlier. Exam trap: same nominal rate does not mean same final value.

### A.7: Effective Interest Rate Of A Two-Installment Loan

Decision problem: infer the annual effective rate that makes the loan proceeds equal the present value of two repayments.

Known inputs:

```text
Loan principal / computer price = EUR 1,250
Repayment after 6 months = EUR 784
Repayment after 12 months = EUR 784
Unknown = annual effective interest rate r_eff
```

Present-value equation:

```text
1,250 = 784 / (1 + r_eff)^0.5 + 784 / (1 + r_eff)
```

Let `y = sqrt(1 + r_eff)`. Then `(1 + r_eff) = y^2`:

```text
1,250 = 784/y + 784/y^2
1,250y^2 = 784y + 784
1,250y^2 - 784y - 784 = 0
y = 1.165389
1 + r_eff = y^2 = 1.358132
r_eff = 0.358132 = 35.81%
```

Interpretation: the instalment loan is expensive because the two repayments have a much higher present value burden than the EUR 1,250 price. Exam trap: the 6-month payment is discounted by a half-year exponent, not by one full year.

### A.9: Continuous-Compounding Effective Annual Rate

Decision problem: convert a continuously compounded nominal annual rate into an effective annual rate.

Known input:

```text
r = 6% = 0.06
```

Formula and arithmetic:

```text
r_eff = e^r - 1
r_eff = e^0.06 - 1
r_eff = 1.061837 - 1
r_eff = 0.061837 = 6.18%
```

Interpretation: a 6% continuous rate produces 6.18% effective annual growth. Exam trap: continuous rate and effective annual rate are not the same number.

### A.10: Annual Compounding Versus Continuous Compounding

Decision problem: choose the better investment for EUR 3,000 over two years.

Option a, annual compounding at 5%:

```text
C_2a = 3,000 x 1.05^2
C_2a = 3,000 x 1.1025
C_2a = EUR 3,307.50
```

Option b, continuous compounding at 4%:

```text
C_2b = 3,000 x e^(0.04 x 2)
C_2b = 3,000 x e^0.08
C_2b = 3,000 x 1.083287
C_2b = EUR 3,249.86
```

Comparison:

```text
C_2a - C_2b = 3,307.50 - 3,249.86
C_2a - C_2b = EUR 57.64
```

Interpretation: option a is better even though option b compounds continuously, because the nominal rate gap is large enough. Exam trap: continuous compounding is not automatically better than a higher annual-compound rate.

### A.11: Simple-Interest Rate

Decision problem: find the simple annual interest rate that turns EUR 3,000 into EUR 5,000 after 12 years.

Known inputs:

```text
C_0 = EUR 3,000
C_n = EUR 5,000
n = 12 years
```

Formula and arithmetic:

```text
C_n = C_0 x (1 + n x r)
C_n / C_0 = 1 + n x r
r = (C_n / C_0 - 1) / n
r = (5,000/3,000 - 1) / 12
r = (1.666667 - 1) / 12
r = 0.055556 = 5.56%
```

Interpretation: the investment needs a simple annual rate of 5.56%. Exam trap: the compound-rate answer would be lower because interest would earn interest.

### A.12: Simple Interest Versus Compound Interest Over A Long Horizon

Decision problem: compare the 2017 value of EUR 1 deposited in year 800 at 1% under simple versus compound interest.

Known inputs:

```text
C_0 = EUR 1
r = 1% = 0.01
n = 2017 - 800 = 1,217 years
```

Simple interest:

```text
C_2017(simple) = 1 x (1 + 1,217 x 0.01)
C_2017(simple) = 1 x 13.17
C_2017(simple) = EUR 13.17
```

Compound interest:

```text
C_2017(compound) = 1 x 1.01^1,217
C_2017(compound) = EUR 181,598.35
```

Difference:

```text
181,598.35 - 13.17 = EUR 181,585.18
```

Interpretation: over very long horizons, interest-on-interest dominates the final value. Exam trap: simple interest grows linearly; compound interest grows exponentially.

### A.13: Time To Reach EUR 5,000

Decision problem: compare the time needed for EUR 1,000 to become EUR 5,000 at 10% under simple versus compound interest.

Known inputs:

```text
C_0 = EUR 1,000
C_n = EUR 5,000
r = 10% = 0.10
C_n / C_0 = 5
```

Simple interest:

```text
C_n = C_0 x (1 + n x r)
n = (C_n / C_0 - 1) / r
n = (5 - 1) / 0.10
n = 40.00 years
```

Compound interest:

```text
C_n = C_0 x (1 + r)^n
n = ln(C_n / C_0) / ln(1 + r)
n = ln(5) / ln(1.10)
n = 1.609438 / 0.095310
n = 16.89 years
```

Interpretation: compounding reaches the target much faster because interest is reinvested. Exam trap: when `n` is unknown in compound interest, use logs.

### A.14: Required Rate For EUR 1,500 After 2.5 Years

Decision problem: find the annual rate that turns EUR 1,000 into EUR 1,500 in 2.5 years under simple versus compound interest.

Known inputs:

```text
C_0 = EUR 1,000
C_n = EUR 1,500
n = 2.5 years
C_n / C_0 = 1.5
```

Simple interest:

```text
r = (C_n / C_0 - 1) / n
r = (1.5 - 1) / 2.5
r = 0.20 = 20.00%
```

Compound interest:

```text
r = (C_n / C_0)^(1/n) - 1
r = 1.5^(1/2.5) - 1
r = 1.176079 - 1
r = 0.176079 = 17.61%
```

Interpretation: the compound rate is lower because interest also earns interest during the 2.5-year horizon. Exam trap: do not use the simple-interest rearrangement for a compound-interest question.

### A.15a: Monthly Interest, Nominal Annual Rate, And Effective Annual Rate

Decision problem: translate a monthly interest rate of 1% into a nominal annual rate and an effective annual rate.

Known inputs:

```text
Monthly rate = 1% = 0.01
m = 12 months
```

Nominal annual rate:

```text
r_nominal = 12 x 0.01
r_nominal = 0.12 = 12.00%
```

Effective annual rate:

```text
r_eff = (1 + monthly rate)^12 - 1
r_eff = 1.01^12 - 1
r_eff = 1.126825 - 1
r_eff = 0.126825 = 12.68%
```

Interpretation: 12% nominal compounded monthly creates 12.68% effective annual growth. Exam trap: nominal annual rate is not the earned annual return when interest compounds within the year.

### A.15b: Six-Monthly Rate For A 9% Effective Annual Rate

Decision problem: find the six-month periodic rate that produces an effective annual rate of 9%.

Known inputs:

```text
r_eff = 9% = 0.09
m = 2 half-year periods
```

Formula and arithmetic:

```text
1 + r_eff = (1 + i_6m)^2
i_6m = sqrt(1.09) - 1
i_6m = 1.044031 - 1
i_6m = 0.044031 = 4.40%
```

Interpretation: each six-month period must earn about 4.40% to create 9% effective annual growth. If this were quoted as a nominal annual rate with semiannual compounding, the nominal annual rate would be about `2 x 4.40% = 8.81%`. Exam trap: the task asks for the six-month rate, not the effective annual rate.

### A.16: Present Value With Monthly Interest

Decision problem: find how much to deposit today to have EUR 1,000 in 18 months at 0.35% monthly interest.

Known inputs:

```text
C_n = EUR 1,000
Monthly rate = 0.35% = 0.0035
n = 18 months
```

Monthly-rate solution:

```text
C_0 = C_n / (1 + 0.0035)^18
C_0 = 1,000 / 1.0035^18
C_0 = 1,000 / 1.06491
C_0 = EUR 939.05
```

Effective-annual-rate solution:

```text
r_eff = 1.0035^12 - 1
r_eff = 0.0428 = 4.28%
C_0 = 1,000 / (1 + 0.0428)^1.5
C_0 = EUR 939.05
```

Interpretation: both methods agree if the rate and period units are matched. Exam trap: do not use `n = 1.5` with the monthly rate.

### A.17: Future Value Under Yearly, Six-Monthly, And Continuous Compounding

Decision problem: calculate the final value of EUR 4,000 over three years at a 6% nominal annual rate under three compounding conventions.

Known inputs:

```text
C_0 = EUR 4,000
r = 6% = 0.06
n = 3 years
```

Yearly compounding:

```text
C_3 = 4,000 x 1.06^3
C_3 = 4,000 x 1.191016
C_3 = EUR 4,764.06
```

Six-monthly compounding:

```text
Periodic rate = 0.06 / 2 = 0.03
Number of periods = 2 x 3 = 6
C_3 = 4,000 x 1.03^6
C_3 = 4,000 x 1.194052
C_3 = EUR 4,776.21
```

Continuous compounding:

```text
C_3 = 4,000 x e^(0.06 x 3)
C_3 = 4,000 x e^0.18
C_3 = 4,000 x 1.197217
C_3 = EUR 4,788.87
```

Interpretation: with the same nominal rate, more frequent compounding produces a higher final value. Exam trap: if the problem says continuous, use `e^(r x n)`.

### A.18: Infer Continuous Rate And Initial Investment

Decision problem: infer the continuous rate from the growth from year 1 to year 2, then find the initial investment one year before `C_1`.

Known inputs:

```text
C_1 = EUR 100,000
C_2 = EUR 110,000
Continuous compounding
```

Rate from year 1 to year 2:

```text
C_2 = C_1 x e^r
e^r = C_2 / C_1
e^r = 110,000 / 100,000
e^r = 1.10
r = ln(1.10)
r = 0.09531 = 9.53%
```

Initial investment:

```text
C_1 = C_0 x e^r
C_0 = C_1 / e^r
C_0 = 100,000 / 1.10
C_0 = EUR 90,909.09
```

Interpretation: the continuous rate is 9.53%, which corresponds to 10% effective growth over one year. Exam trap: do not report 10% as the continuous rate; 10% is the effective one-year growth.

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

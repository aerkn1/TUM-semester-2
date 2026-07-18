# Exercise 06-07: Bonds I

Source files:

- `finance-and-investment-management/raw/Exercise_6_Bonds_I_Without_Solutions.pdf`
- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260604/Investment and  950881761 (S26)_2026064_1514/CW 21  19.05. _ 20.05./Exercise 6 - Solutions.pdf`
- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260604/Investment and  950881761 (S26)_2026064_1514/CW 23  02.06. _ 03.06./Exercise 7.pdf`
- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260709/CW 23  02.06. _ 03.06./Exercise 7 - Solutions.pdf`
- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260709/CW 23  02.06. _ 03.06./Video Resource - Excel Sheet.xlsx`
- `finance-and-investment-management/raw/Formulary.pdf`

Lecture folder: `finance-and-investment-management/`
Date processed: 2026-05-16; refreshed with solution and Exercise 7 material on 2026-06-06; refreshed with Exercise 7 solutions and Excel return-resource source on 2026-07-09

## High-Yield 80/20 Summary

Bond valuation applies discounted cash flow logic to financial securities. A bond price is the present value of promised coupon payments and principal repayment, discounted at a risk-adjusted rate. The most important exam intuition is the inverse relationship between interest rates and bond prices.

Core logic:

1. Identify the bond type: zero-coupon or coupon bond.
2. Identify promised cash flows and timing.
3. Discount at the appropriate risk-adjusted rate or term structure.
4. Interpret price changes when market interest rates change.
5. Know that creditworthiness, coupon, rights, liquidity, and interest rates affect bond prices.
6. For coupon bonds, separate market price, accrued interest, and final settlement price.
7. Understand that discount bonds move upward toward face value over time, while premium bonds move downward toward face value.
8. Connect bond yields to Cost of Capital: market YTM on comparable debt can estimate `r_D`, the debt-cost input in WACC.

## Bond Definition

A bond is a long-term contract where the issuer borrows money and commits to repay debt at a specified date and, if applicable, pay coupons at predetermined dates.

Bond cash flows are often easier to predict than stock cash flows, except for:

- Variable coupons.
- Insolvency / default risk.
- Embedded rights such as convertibility or issuer options.

## Bond Price Drivers

The slides highlight these drivers:

- Creditworthiness.
- Interest rate / discount rate.
- Coupon.
- Rights attached to the bond.
- Liquidity.

Real-life interpretation: a German government bond and a risky corporate bond with the same face value and maturity should not have the same discount rate because their credit risks differ.

## Bond Types

| Bond Type | Meaning |
|---|---|
| Coupon bond | Fixed coupon payments plus principal at maturity |
| Zero-coupon bond | No coupons; repayment at maturity only |
| Floater | Coupon adjusts to market interest rates |
| Perpetual / consol bond | No maturity date |
| Convertible bond | Can be exchanged for shares under defined conditions |
| Warrant / option bond | Includes option rights traded separately |
| Reverse convertible | Issuer may repay with shares instead of cash |

## Core Variables

```text
B_0 = present bond price
B_0^ZB = present zero-bond price
B_N = face value / redemption value at maturity
C = coupon
C_k = coupon payment at time k
r = risk-adjusted discount rate
N = maturity in periods
D = duration
D_mod = modified duration
q = 1 + r
```

## General Pricing Principle

```text
PV = sum of all CF_n / (1+r)^n
```

Equivalent principle: the present value of a group of cash flows equals the sum of the present values of each individual cash flow.

## Zero-Coupon Bond

A zero-coupon bond pays only the face value at maturity.

```text
B_0^ZB = B_N / (1+r)^N = B_N x q^(-N)
```

Example from slides:

A zero bond with face value 100, maturity 20 years, and annual rate 6.75%:

```text
B_0 = 100 / 1.0675^20 = 27.08
```

Interpretation: the investor pays far below face value because all return comes from price appreciation to face value at maturity.

## Coupon Bond

A coupon bond pays coupons and face value.

```text
B_0 = sum from k=1 to N of C/(1+r)^k + B_N/(1+r)^N

Equivalent annuity form:
B_0 = C x [1 - 1/(1+r)^N] / r + B_N/(1+r)^N
```

Equivalent interpretation:

```text
Bond price = PV(coupon annuity) + PV(face value)
```

Exam trap: if coupon is given as a percentage of face value, convert it into the coupon cash flow before using the formula.

### Face Value, PV Of Face Value, And Coupon Annuity

Keep three layers separate:

| Concept | Meaning | Example with face value 1,000 and 6% coupon |
|---|---|---|
| Face value | Principal amount contractually repaid at maturity | `1,000` repaid at maturity |
| Coupon cash flow | Periodic promised interest payment | `1,000 x 6% = 60` each year |
| Coupon annuity | Repeated coupon cash flows valued as an annuity | `60, 60, 60, ...` discounted to today |
| PV of face value | Today's discounted value of the future principal repayment | `1,000 / (1+r)^N` |

This means the amount repaid at maturity is not the discounted number. If `1,000 / (1+r)^N = 244.35`, then `244.35` is the **present value of the future face-value repayment**, while the contractual maturity repayment remains `1,000`.

For a coupon bond, the final-year cash flow is:

```text
Final-year CF = coupon + face value
```

Example:

```text
Face value = 1,000
Coupon rate = 6%
Annual coupon = 60
Final-year cash flow = 60 + 1,000 = 1,060
```

Exam trap: do not answer the maturity repayment with the present value of the face value. The PV belongs in the price calculation; the face value is the amount paid at maturity.

### Par, Discount, And Premium

The refreshed Exercise 7 slides categorize coupon-bond prices relative to face value:

| Price relation | Meaning | Typical condition |
|---|---|---|
| `B_0 = 100` | Bond trades at par | Coupon rate equals market yield |
| `B_0 < 100` | Bond trades below par / at discount | Coupon rate below market yield |
| `B_0 > 100` | Bond trades above par / at premium | Coupon rate above market yield |

For a 10% coupon bond with face value 100 and market interest rate 10%, the price is 100 because the coupon rate equals the market-required return.

## Accrued Interest And Settlement Price

If bond ownership changes between coupon dates, the buyer compensates the seller for the interest earned since the last coupon date.

The lecture separates:

| Term | Meaning |
|---|---|
| Market price / ex-coupon price | Quoted fair price of the bond excluding accrued interest |
| Accrued interest | Pro-rata coupon compensation between the last coupon date and sale date |
| Settlement / dirty price | Market price plus accrued interest, and in real markets possibly fees |

The simplified accrued-interest formula in the slides is:

```text
I_0 = (t_1 - t_0) x (1/360) x C
```

where `t_1 - t_0` is the number of days between the last coupon payment date and the selling date, and `C` is the annual coupon amount.

Exam trap: the exchange quote is usually the clean market price. The cash paid by the buyer can be higher because accrued interest is added.

## Price Path Toward Maturity

The Exercise 7 deck emphasizes how bond prices move as maturity approaches:

- At maturity, the price equals nominal/face value, assuming repayment at par.
- A discount bond tends to increase toward face value as maturity approaches.
- A premium bond tends to decrease toward face value as maturity approaches.

This is separate from market-yield shocks. Even if market rates do not change, time-to-maturity changes the present-value calculation.

## Yield To Maturity

Yield to maturity is the annual return earned if the bond is held to maturity and the assumptions of the calculation hold.

```text
Bond price = PV(promised coupons and redemption discounted at YTM)
```

The Exercise 7 slides add the reinvestment assumption: coupon cash flows are assumed to be reinvested at the market rate used in the YTM logic.

Exam trap: YTM is not the same as coupon rate. YTM is solved from price and cash flows.

## 2026-07-09 Exercise 7 Solution Refresh

The later Moodle export added the official Exercise 7 solution deck and an Excel video resource. These do not create a separate spaced-repetition topic; they confirm and support the existing Bonds I note.

Solution-backed confirmations:

- Coupon-bond price remains `PV(coupons) + PV(redemption value)`.
- Par, discount, and premium bond categories depend on coupon rate versus market yield.
- Accrued interest must be separated from the quoted clean market price.
- Yield to maturity is solved from market price and promised cash flows, not copied from the coupon rate.
- The price path toward maturity must be interpreted separately from an unexpected market-yield shock.

The Excel video resource contains monthly Daimler return data. Treat it as source support for return-series handling rather than a new examinable formula topic inside Bonds I. If a later exercise asks for return statistics from the file, make the calculation route explicit: identify monthly returns, compute the requested statistic, state the period unit, then interpret the result.

### Bridge To Cost Of Capital

Full bridge note: [Bridge: Bonds To Cost Of Capital](../session-07-08-cost-of-capital/bonds-to-cost-of-capital-bridge.md).

In the Bonds exercise, YTM is solved from a bond's price and promised cash flows. In Cost of Capital, that same market-required yield can help estimate `r_D`, the pre-tax debt cost of capital, when the bond has similar maturity, seniority, liquidity, and credit risk.

Clean route:

```text
Bond price + promised coupons/principal
-> YTM / comparable bond yield
-> debt cost of capital r_D
-> after-tax r_D inside WACC
-> project NPV
```

Important boundary: the bond yield is not the whole project discount rate. It is the debt component. WACC blends after-tax `r_D` with the equity cost of capital when project risk and target financing match.

Value-added language:

```text
Bond investor value = PV(promised bond cash flows at required yield) - market price.
Project value added = PV(operating FCF at WACC) - initial investment.
```

Both use discounted cash flow, but the decision question is different.

## Interest Rate And Price Relationship

Bond prices move inversely with market yields:

- If discount rates rise, existing fixed cash flows are discounted more heavily, so bond price falls.
- If discount rates fall, existing fixed cash flows become more valuable, so bond price rises.

Zero-coupon bonds are especially sensitive because all cash flow occurs at maturity.

For coupon bonds:

- If the market yield falls below the coupon rate, the bond trades above par.
- If the market yield rises above the coupon rate, the bond trades below par.
- Investors who sell before maturity face interest-rate risk because the sale price depends on the market yield at the sale date.
- If an investor holds a fixed promised-payment bond to maturity and all payments occur as promised, interim market price changes matter less for cash-flow receipt, but reinvestment assumptions can still matter for realized return.

## Sloping Yield Curves And Term Structure

If rates differ by maturity, discount each cash flow with the rate corresponding to its time.

The formulary includes:

```text
(1 + I_t,T)^(T-t) = (1 + I_t,S)^(S-t) x (1 + r_S,T)^(T-S)
```

Meaning: long-term spot rates can be decomposed into earlier spot rates and forward rates.

Exam implication: if a question gives a term structure, do not use one flat discount rate unless explicitly allowed.

## Duration

Duration measures the weighted average timing of bond cash flows and approximates interest-rate sensitivity.

From the formulary:

```text
D = (1/B_0) x [sum from k=1 to N of k x C_k/(1+r)^k + N x B_N/(1+r)^N]
D_mod = D / (1+r)
Approximate price change: Delta B_0 / B_0 ≈ -D_mod x Delta r
```

Interpretation:

- Higher duration means higher interest-rate sensitivity.
- Longer maturity usually increases duration.
- Lower coupons usually increase duration because more value is paid later.

## Worked Calculations And Analogies

### Calculation 1: Zero-Coupon Bond Price

Decision problem and method choice:

- A zero-coupon bond has one promised cash flow at maturity.
- Use single-cash-flow present value.

Known inputs:

```text
Face value B_N = 100
Maturity N = 20 years
Discount rate r = 6.75% = 0.0675
q = 1.0675
```

Formula, substitution, and arithmetic:

```text
B_0 = B_N / q^N
B_0 = 100 / 1.0675^20
1.0675^20 = 3.69282
B_0 = 100 / 3.69282
B_0 = 27.08
```

Interpretation: the investor pays 27.08 today for the promise of 100 in 20 years. The return is created by price appreciation toward face value, not by coupon income.

Analogy: a zero bond is a locked box sold at a discount. You buy the box today for 27.08 and it opens at maturity with 100 inside.

Exam trap: do not add coupons to a zero-coupon bond. Its only cash flow is the maturity payment.

### Calculation 2: Coupon Bond Price

Decision problem and method choice:

- A coupon bond is a package of coupon cash flows plus final principal repayment.
- Value each promised cash flow at the same date and add the PVs.

Known inputs:

```text
Face value = 100
Annual coupon = 4
Maturity = 3 years
Discount rate = 5%
q = 1.05
```

Expanded cash-flow route:

```text
B_0 = 4/1.05 + 4/1.05^2 + 104/1.05^3

PV coupon year 1 = 4 / 1.05 = 3.81
PV coupon year 2 = 4 / 1.1025 = 3.63
PV coupon plus face year 3 = 104 / 1.157625 = 89.84

B_0 = 3.81 + 3.63 + 89.84
B_0 = 97.28
```

Interpretation: because the 4% coupon is below the 5% required return, the bond trades below face value.

Analogy: the bond is two products stapled together: a small coupon annuity and a big maturity repayment. Price each piece, then add them.

Exam trap: the final cash flow is not just the coupon. In the final year the investor receives coupon plus face value.

### Calculation 3: Accrued Interest And Settlement Price

Decision problem and method choice:

- A bond sold between coupon dates gives the seller compensation for coupon interest already earned.
- Add accrued interest to the clean market price to get the simplified settlement price.

Known inputs:

```text
Annual coupon C = 6
Days since last coupon = 120
Day-count convention = 360-day year
Clean market price = 102
```

Formula and arithmetic:

```text
Accrued interest = (120/360) x 6
Accrued interest = 0.3333 x 6
Accrued interest = 2.00

Settlement price = clean price + accrued interest
Settlement price = 102 + 2
Settlement price = 104
```

Interpretation: the quoted bond value is 102, but the buyer pays 104 because the seller has earned part of the next coupon.

Analogy: buying a bond between coupon dates is like taking over a rental apartment halfway through the month. The old tenant is compensated for the rent period already earned.

Exam trap: do not confuse clean market price with the cash paid at settlement.

### Calculation 4: Duration Price-Sensitivity Approximation

Decision problem and method choice:

- If the question asks for the approximate price effect of a small yield change, use modified duration.

Known inputs:

```text
Bond price B_0 = 100
Macaulay duration D = 4.20
Yield r = 5%
Yield change Delta r = +1 percentage point = +0.01
```

Formula and arithmetic:

```text
D_mod = D / (1+r)
D_mod = 4.20 / 1.05
D_mod = 4.00

Delta B_0 / B_0 approximately = -D_mod x Delta r
Delta B_0 / B_0 approximately = -4.00 x 0.01
Delta B_0 / B_0 approximately = -0.04 = -4.00%

Approximate price change = 100 x (-4.00%) = -4.00
Approximate new price = 96.00
```

Interpretation: a one percentage point yield increase reduces the bond price by approximately 4%.

Analogy: duration is the bond's interest-rate lever arm. Longer duration gives the rate change more leverage over price.

Exam trap: the sign is negative. Yield up means price down for fixed promised cash flows.

## Exam Decision Tree

1. Does the bond pay coupons?
   - No: zero-coupon formula.
   - Yes: coupon bond = PV coupons + PV face value.
2. Is coupon annual, semiannual, or another frequency?
   - Match periods, coupon, and rate frequency.
3. Is the rate flat or term-structure based?
   - Flat rate: one `r`.
   - Yield curve: discount each cash flow with its maturity-specific rate.
4. Is the question about price change from rate movement?
   - Use inverse relation or duration approximation.
5. Is credit risk mentioned?
   - Higher risk requires higher discount rate, lowering price.
6. Is the bond sold between coupon dates?
   - Add accrued interest to the quoted market price to obtain the simplified settlement price.
7. Is the question asking for YTM?
   - Solve the discount rate that equates price to promised cash flows; do not use coupon rate automatically.

## Common Mistakes

- Forgetting to include face value for coupon bonds.
- Using coupon rate as discount rate automatically.
- Failing to convert coupon percentage into euro coupon.
- Mixing annual and intra-year periods.
- Assuming bond price is always face value.
- Thinking rate increases raise bond prices.
- Ignoring credit risk and liquidity effects.
- Forgetting accrued interest when a bond is sold between coupon dates.
- Confusing clean market price with settlement price.
- Confusing coupon rate with YTM.
- Forgetting that discount and premium bonds converge toward face value as maturity approaches.

## Practice Questions

1. A zero bond pays EUR 100 in 10 years. Discount rate is 5%. What is price?
   - Answer: `100 / 1.05^10`.
2. A coupon bond has face value 100, annual coupon 4, maturity 3 years, discount rate 5%. What is price setup?
   - Answer: `4/1.05 + 4/1.05^2 + 104/1.05^3`.
3. What happens to a fixed-rate bond price when market rates fall?
   - Answer: price rises.
4. Why does a zero-coupon bond tend to have high duration?
   - Answer: all cash flow occurs at maturity.
5. What does modified duration approximate?
   - Answer: percentage price change for a small yield change.
6. A 6% coupon bond is priced with a market yield of 4%. Is it below or above par?
   - Answer: above par.
7. What is accrued interest?
   - Answer: pro-rata coupon compensation paid by the buyer to the seller between coupon dates.
8. Why can the settlement price differ from the quoted market price?
   - Answer: accrued interest is added to the clean market price.

## Mermaid Knowledge Map

```mermaid
graph TD
    BOND[Bonds] --> CONTRACT[Debt Contract]
    CONTRACT --> CF[Promised Cash Flows]
    CF --> PRICE[Discounted Cash Flow Pricing]
    BOND --> ZB[Zero-Coupon Bond]
    BOND --> CB[Coupon Bond]
    ZB --> FACE[Face Value At Maturity]
    CB --> COUPON[Coupons]
    CB --> FACE
    CB --> ACC[Accrued Interest]
    CB --> YTM[Yield To Maturity]
    PRICE --> RATE[Risk-Adjusted Discount Rate]
    RATE --> INVERSE[Rate Up Price Down]
    RATE --> PAR[Coupon Vs Yield Determines Par Discount Premium]
    BOND --> DRIVERS[Price Drivers]
    DRIVERS --> CREDIT[Creditworthiness]
    DRIVERS --> LIQ[Liquidity]
    DRIVERS --> RIGHTS[Embedded Rights]
    BOND --> DURATION[Duration]
    DURATION --> SENS[Interest-Rate Sensitivity]
```

## Subject Knowledge Graph

| Node | Meaning |
|---|---|
| Bond | Debt security with promised payments |
| Zero-coupon bond | Bond with only maturity payment |
| Coupon bond | Bond with coupons plus redemption value |
| Face value | Amount repaid at maturity |
| Coupon | Periodic interest payment |
| Discount rate | Risk-adjusted required return |
| Clean price | Quoted bond market price excluding accrued interest |
| Accrued interest | Pro-rata coupon earned since last coupon date |
| Settlement price | Clean price plus accrued interest in the simplified exercise setting |
| Yield to maturity | IRR that equates price to promised cash flows through maturity |
| Duration | Weighted average timing of cash flows |
| Modified duration | Price sensitivity approximation |

| From | Relationship | To |
|---|---|---|
| Bond price | equals | present value of promised cash flows |
| Zero-coupon bond | pays | face value only |
| Coupon bond | pays | coupons plus face value |
| Higher discount rate | decreases | bond price |
| Coupon rate below market yield | implies | discount bond |
| Coupon rate above market yield | implies | premium bond |
| Accrued interest | added to | clean market price |
| Yield to maturity | solves | bond price equation |
| Lower creditworthiness | increases | discount rate |
| Duration | measures | timing and rate sensitivity |
| Modified duration | approximates | percentage price change |
| Term structure | determines | maturity-specific discounting |

## Links

- Previous exercise: `finance-and-investment-management/wiki/exercise-05-redemptions/exercise-05-redemptions.md`
- Related concept: `finance-and-investment-management/wiki/exercise-01-02-interest-calculation/exercise-01-02-interest-calculation.md`
- Bridge to Cost of Capital: `finance-and-investment-management/wiki/session-07-08-cost-of-capital/bonds-to-cost-of-capital-bridge.md`

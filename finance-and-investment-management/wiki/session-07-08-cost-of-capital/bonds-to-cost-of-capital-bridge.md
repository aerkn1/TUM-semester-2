# Bridge: Bonds To Cost Of Capital

Source notes:

- [Session 07-08: Cost Of Capital](session-07-08-cost-of-capital.md)
- [Exercise 06-07: Bonds I](../exercise-06-bonds-i/exercise-06-bonds-i.md)
- [Finance course logistics](../_course-logistics.md)

Date prepared: 2026-07-06
Course: Finance and Investment Management

## Why This Bridge Exists

Finance uses two related but separate tracks:

| Track | Local file | Topic | Exam role |
|---|---|---|---|
| Corporate-finance lecture | `session-07-08-cost-of-capital.md` | Cost of Capital | Estimate the required return used to discount operating project FCF. |
| Mathematical-basics exercise | `exercise-06-bonds-i.md` | Bonds | Value promised debt cash flows and solve or interpret yields. |

Use this bridge to avoid the naming trap:

```text
Bonds = price promised debt cash flows at a required yield.
Cost of Capital = estimate required returns for capital providers and test project value.
```

## The Plain-Language Router

Bonds ask:

```text
What is this promised coupon-and-principal stream worth today?
```

Cost of Capital asks:

```text
What return do debt and equity providers require for this risk, and does the project still create value after paying that required return?
```

The bridge is strongest on the debt side. A traded bond or comparable bond can reveal the market yield investors demand for debt with similar maturity, seniority, liquidity, and credit risk. That market yield helps estimate `r_D`, the debt cost of capital used in WACC.

## Core Connection

```text
Bond cash flows + market price
-> solve or observe YTM
-> estimate debt cost of capital r_D
-> after-tax debt cost r_D x (1 - tau_c)
-> WACC
-> discount operating FCF
-> NPV / value added
```

The issuer and investor see opposite sides of the same required return:

| Perspective | Bond calculation meaning | Cost-of-capital meaning |
|---|---|---|
| Bond investor | Required yield is the return needed to buy/hold the bond at that risk. | This is the investor's opportunity-cost benchmark. |
| Firm / issuer | The same market yield approximates what the firm must pay to borrow similar debt. | This becomes pre-tax `r_D` for WACC, adjusted after tax. |
| Project analyst | Bond yield helps price the debt component, not the whole project. | Project value still comes from operating FCF discounted at risk-matched WACC. |

## Face Value Versus Coupon Annuity

When using a bond to estimate debt cost, first separate the bond's promised cash flows:

```text
Face value = principal repaid at maturity.
Coupon = periodic promised interest payment.
Coupon annuity = repeated coupon payments.
PV of face value = today's discounted value of the future principal repayment.
```

Example:

```text
Face value = 1,000
Coupon rate = 6%
Annual coupon = 1,000 x 6% = 60
Maturity repayment = 1,000
Final-year cash flow = 60 + 1,000 = 1,060
```

If discounting the `1,000` face value gives `244.35`, then `244.35` is the **PV of the face value**, not the amount repaid at maturity.

This matters for the bridge because the bond price equation uses present values, while the debt contract promises future nominal cash flows:

```text
Bond price today = PV(coupon annuity) + PV(face value)
Debt cost r_D    = yield that makes those PVs equal the market price
```

## Calculation Bridge: From Bond Yield To WACC To Value Added

### Stage 1: Estimate Debt Cost From A Bond

Suppose a firm's outstanding five-year bond has:

```text
Face value = 100
Annual coupon = 6
Market price = 95.90
Maturity = 5 years
```

The YTM is the rate `y` that solves:

```text
95.90 = 6/(1+y) + 6/(1+y)^2 + 6/(1+y)^3 + 6/(1+y)^4 + 106/(1+y)^5
```

Here, `y` is approximately 7%.

Interpretation:

```text
The bond market requires about 7% on this promised debt stream.
```

For a healthy firm with debt of similar maturity and risk, this 7% can be used as a practical estimate of pre-tax `r_D`. If the bond is very risky, promised YTM may overstate expected debt cost because promised payments may not be fully received. Then use the course correction:

```text
r_D approx y - p x L
```

where `p` is default probability and `L` is loss rate.

### Stage 2: Put Debt Cost Into WACC

Assume:

```text
Market value of equity E = 60
Market value of debt D = 40
Equity cost r_E = 12%
Debt cost r_D = 7%
Corporate tax rate tau_c = 30%
```

Formula:

```text
r_WACC = r_E x E/(E+D) + r_D x D/(E+D) x (1 - tau_c)
```

Substitution and arithmetic:

```text
r_WACC = 12% x 60/(60+40) + 7% x 40/(60+40) x (1 - 0.30)
r_WACC = 12% x 0.60 + 7% x 0.40 x 0.70
r_WACC = 7.20% + 1.96%
r_WACC = 9.16%
```

Interpretation:

```text
The project must beat a 9.16% blended hurdle rate before it creates value for capital providers.
```

The bond calculation did not value the project by itself. It supplied the debt-return input for WACC.

### Stage 3: Test Added Value Against Cost Of Capital

Suppose a project costs EUR 100,000 today and generates EUR 35,000 at the end of each of the next four years. Use the WACC from above because the project risk and target financing match the assumptions.

Decision problem:

```text
Does this project create value after compensating debt and equity investors at the required return?
```

Formula:

```text
NPV = -100,000 + 35,000/1.0916 + 35,000/1.0916^2 + 35,000/1.0916^3 + 35,000/1.0916^4
```

Equivalent annuity form:

```text
PV inflows = 35,000 x [1 - 1/1.0916^4] / 0.0916
PV inflows = EUR 112,993.12

NPV = -100,000 + 112,993.12
NPV = EUR 12,993.12
```

Interpretation:

```text
The project creates EUR 12,993.12 of value today after paying the required 9.16% cost of capital.
```

This is the "added value against cost of capital": value is not just positive cash flow. Value is the surplus left after discounting cash flows at the risk-matched required return.

## Bond Investor Value Versus Project Value

Bonds and projects both use discounted cash flow, but the decision question changes:

| Decision | Formula logic | Positive signal |
|---|---|---|
| Buy a bond? | `Intrinsic bond value = PV(promised coupons + face value at required yield)` | Buy only if intrinsic value exceeds market price. |
| Accept a project? | `NPV = PV(operating FCF at WACC) - investment` | Accept if NPV is positive. |
| Estimate WACC? | Use `r_E`, `r_D`, tax rate, and market-value weights | Use WACC only when project risk and financing match. |

Mini example for the bond investor:

```text
If required return = 7%,
PV of a 5-year 6% coupon bond with face value 100 = 95.90.
If market price = 105, the bond NPV to the investor is 95.90 - 105 = -9.10.
```

Interpretation: at a 7% required return, paying 105 destroys EUR 9.10 of value per EUR 100 face value. The same logic becomes project NPV when the cash flows are operating FCF and the required return is WACC.

## What Bonds Add To Cost Of Capital

Bond calculations add three high-value pieces to Session 07-08:

1. **Market evidence for `r_D`.** Outstanding bonds or comparable bonds can show what lenders/investors currently require for similar debt risk.
2. **Required-return intuition.** The discount rate is the investor's opportunity cost; a price is fair only if discounted promised cash flows justify it.
3. **Default-risk warning.** Promised YTM is not automatically expected return when default risk is material.

The bridge does not say "use bonds as the project investment." Bonds are reference securities for estimating required debt returns and practicing the same DCF logic.

## Common Exam Traps

| Trap | Correction |
|---|---|
| Using coupon rate as the debt cost of capital. | Use market-required yield/YTM or comparable debt yield; coupon is a contractual cash payment. |
| Using bond YTM as the whole project discount rate. | Bond YTM estimates `r_D`; WACC blends after-tax `r_D` with `r_E` when project risk and financing match. |
| Treating bond price calculation as project NPV. | Bond pricing values promised debt cash flows; project NPV values operating FCF net of investment. |
| Ignoring default risk in risky bonds. | Promised YTM can overstate expected debt return; adjust conceptually for default probability and loss. |
| Saying positive cash flow means value added. | Value added means positive NPV after discounting at the required cost of capital. |

## Retrieval Prompts

1. How can a traded bond help estimate `r_D` for WACC?
2. Why is coupon rate not automatically the debt cost of capital?
3. In WACC, why is the debt component after tax?
4. Explain "value added against cost of capital" in one sentence.
5. Distinguish bond investor NPV from project NPV.
6. Why can promised YTM overstate debt cost for risky debt?
7. Build the route: bond price -> YTM -> `r_D` -> WACC -> project NPV.

# Session 07-08 Cost Of Capital Clarification Session - 2026-07-06

Source note: [Session 07-08: Cost Of Capital](session-07-08-cost-of-capital.md)

Companion context: [CONTEXT.md](CONTEXT.md)

Bridge note: [Bridge: Bonds To Cost Of Capital](bonds-to-cost-of-capital-bridge.md)

Session type: clarification and wiki refinement

Status: clarification saved; first active recall still pending

## Clarification Prompt And Raw User Question

User question:

> okay, now I want to incorporate the bonds as I think relevant to session 07-08 cost of capital in finance and investment management. How it relates with the calculations and the added value against cost of capital? give the bridging point as we did previously in other sections

## Professor Feedback

- The connection is valid, especially on the debt side of WACC.
- Bonds are part of the mathematical-basics exercise track, while Cost of Capital is part of the corporate-finance lecture track.
- Bond valuation gives a market-required yield for promised debt cash flows.
- That yield can estimate `r_D`, the pre-tax debt cost of capital, when the bond is comparable in maturity, seniority, liquidity, and credit risk.
- WACC uses after-tax `r_D` together with equity cost `r_E`.
- Project NPV then measures value added after the project has paid the required cost of capital.

## Refined Mental Model

```text
Bond price + promised coupons/principal
-> YTM / comparable bond yield
-> debt cost of capital r_D
-> after-tax r_D in WACC
-> operating FCF discounted at WACC
-> positive NPV = value added against cost of capital
```

Short sentence:

```text
Bonds can reveal the market debt return input; WACC turns that input into a project hurdle; NPV measures the surplus after the hurdle.
```

## Worked Bridge Preserved In The Note

The Cost of Capital note and bridge file now use this route:

```text
r_D = 7% from comparable bond yield
r_E = 12%
E = 60, D = 40
tax rate = 30%

r_WACC = 12% x 0.60 + 7% x 0.40 x (1 - 0.30)
r_WACC = 9.16%
```

Project example:

```text
CF_0 = -100,000
FCF_1-4 = 35,000

PV inflows at 9.16% = 112,993.12
NPV = 12,993.12
```

Interpretation:

```text
The project creates EUR 12,993.12 of value today after compensating debt and equity investors at the 9.16% required return.
```

## Quality Labels

| Concept | Quality | Correction rule |
|---|---|---|
| Bonds as debt-cost evidence | `green/yellow` | Use YTM or comparable bond yield as evidence for `r_D`, not as the whole project discount rate. |
| Value added against cost of capital | `yellow` | Say value added means positive NPV after discounting operating FCF at the required return. |
| Coupon rate versus debt cost | `yellow` | Coupon sets promised payments; market yield/YTM reflects the current required return. |
| Bond investor NPV versus project NPV | `yellow` | Bond value is `PV(promised debt CF) - price`; project NPV is `PV(operating FCF at WACC) - investment`. |

## Files Updated

- [bonds-to-cost-of-capital-bridge.md](bonds-to-cost-of-capital-bridge.md)
- [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md)
- [CONTEXT.md](CONTEXT.md)
- [../exercise-06-bonds-i/exercise-06-bonds-i.md](../exercise-06-bonds-i/exercise-06-bonds-i.md)
- [../exercise-06-bonds-i/CONTEXT.md](../exercise-06-bonds-i/CONTEXT.md)
- [../_course-knowledge-graph.md](../_course-knowledge-graph.md)

## Next Recall Prompts

1. How can an outstanding bond help estimate `r_D` for WACC?
2. Why is coupon rate not automatically debt cost of capital?
3. In one sentence, explain "value added against cost of capital."
4. Given `r_E`, `r_D`, tax rate, and market-value weights, compute WACC and interpret it as a hurdle rate.
5. Distinguish bond investor value from project NPV.
6. Explain why risky promised YTM can overstate expected debt return.

## Follow-Up Clarification: Face Value Versus PV Of Face Value

Coach prompt:

> if a bond has face value 1,000 and coupon rate 6%, what is the annual coupon cash flow, and what is repaid at maturity?

User raw answer:

> annual cash flow is 60, repaid = 244,35

Professor feedback:

- `60` is correct: annual coupon cash flow is `1,000 x 6% = 60`.
- `244.35` is not the maturity repayment. It is the **PV of face value** if it came from discounting `1,000` back to today.
- The contractual amount repaid at maturity is the **face value**, `1,000`.
- For a coupon bond, the final-year cash flow is coupon plus face value: `60 + 1,000 = 1,060`.

User follow-up:

> what I found is the pv of face value?

Professor feedback:

- Yes. If `244.35 = 1,000 / (1+r)^N`, then `244.35` is today's value of the future `1,000` repayment.
- The bridge sentence is:

```text
Face value = amount repaid at maturity.
PV of face value = today's discounted value of that future repayment.
Coupon annuity = repeated coupon payments.
Bond price = PV(coupon annuity) + PV(face value).
```

Quality label: `green/yellow`. The coupon-cash-flow calculation is green; the face-value versus PV-of-face-value distinction needed correction.

Correction rule:

```text
Do not answer a maturity-repayment question with the discounted PV number.
Use face value for repayment, PV of face value for pricing.
```

## References Back To Notes

- Main bridge: [bonds-to-cost-of-capital-bridge.md](bonds-to-cost-of-capital-bridge.md)
- Debt cost section: [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md) section `Debt Cost Of Capital`
- Bonds bridge section: [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md) section `Bridge From Bonds To Cost Of Capital`
- Terminology boundaries: [CONTEXT.md](CONTEXT.md) section `Clarification Bridge Language`

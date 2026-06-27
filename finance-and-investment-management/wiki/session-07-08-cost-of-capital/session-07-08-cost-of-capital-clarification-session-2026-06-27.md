# Session 07-08 Cost Of Capital Clarification Session - 2026-06-27

Source note: [Session 07-08: Cost Of Capital](session-07-08-cost-of-capital.md)

Companion context: [CONTEXT.md](CONTEXT.md)

Session type: clarification and wiki refinement

Status: clarification completed; first active recall still pending

## Clarification Prompts And Raw User Questions

### Prompt 1: CAPM Grounding

User question:

> Okay, how about the CAPM? I did not get the grounding on it. Is it basically the market risk via estimation formula and not using volatility and relies on beta coefficient. However, what is the actual market that is taken into account for estimation, the financial market like stocks, bonds, commodities etc.?

Professor feedback:

- The grounding was mostly correct: CAPM estimates required return for equity-like systematic market risk.
- CAPM uses beta, not total volatility.
- In theory, the CAPM market portfolio contains all risky assets; in practice, the course and most applications use a broad equity index as a market proxy.
- The market proxy is a reference for comparable systematic risk, not the project investment itself.

Refined mental model:

```text
CAPM = risk-free rate + beta x market risk premium.
Beta = sensitivity to broad market movements.
Market proxy = observable reference for comparable systematic risk.
```

Quality label: `yellow` before clarification, `green/yellow` after clarification.

### Prompt 2: Why CAPM Enters WACC

User question:

> But what is the point of incorporating this into the WACC calculation via CAPM? Is the financing source determined as the stocks or bonds invested in for the desired project with viable NPV?

Professor feedback:

- The project is not buying stocks or bonds.
- Stocks, bonds, and comparable traded securities help estimate what investors require for risk.
- CAPM estimates the cost of equity because shareholders do not have a fixed promised interest rate.
- WACC blends that equity required return with after-tax debt cost.

Refined mental model:

```text
Capital Budgeting gives project FCF.
CAPM estimates equity required return.
Debt market data estimates debt required return.
WACC blends them.
NPV tests whether project FCF still creates value.
```

Quality label: `yellow` before clarification, `green` after clarification.

### Prompt 3: Market As Reference

User question:

> So you mean the reason why we look at the market is to align the forecasting and assumption for the expected risk rate for identical or similar projects out in the market already? like referencing? so that they can ensure even with this estimated/expected risk rate the project can still generate value on paper?

Professor feedback:

- Correct. Market data is used as a reference required return for comparable systematic risk.
- CAPM/WACC does not forecast the project FCF; it prices the risk of those FCFs.
- NPV asks whether value remains after charging the project the required return.

Refined mental model:

```text
Comparable market risk -> required return estimate -> discount rate -> NPV test.
```

Exam sentence:

```text
CAPM uses market data to estimate the opportunity cost of equity for comparable systematic risk; WACC then uses that required return to test whether project operating FCF creates value after compensating capital providers.
```

Quality label: `green`.

### Prompt 4: Redemptions And Debt Cost

User question:

> Okay, and also the redemption calculations works for the debt part of cost of capital right?

Professor feedback:

- Connected, but not the same.
- Debt cost of capital is the return lenders require; it enters WACC.
- Redemptions calculate actual contractual interest, principal repayment, ending debt, and debt service.

Refined mental model:

```text
Debt cost of capital = required return for lenders.
Redemption schedule = actual repayment path for the chosen loan.
```

Quality label: `yellow` before clarification, `green/yellow` after clarification.

### Prompt 5: Debt Cost Versus Project Cost Of Capital

User question:

> What actually debt and project cost of capital?

Professor feedback:

- Debt cost of capital prices the lender claim.
- Project cost of capital prices the project's operating cash-flow risk.
- They are not automatically the same rate.
- The project cost may equal firm WACC only if project risk and financing policy match the firm.

Refined mental model:

```text
Debt cost of capital = required return for lenders.
Equity cost of capital = required return for shareholders.
WACC = blended required return from debt + equity.
Project cost of capital = discount rate appropriate for this project's operating risk.
```

Best sentence:

```text
Debt cost of capital prices the financing risk for lenders; project cost of capital prices the operating risk of the project's cash flows.
```

Quality label: `green/yellow`.

## Consolidated Bridge

```text
Capital Budgeting
= forecast the operating FCF.

CAPM
= estimate the equity return required for comparable systematic market risk.

Debt Cost Of Capital
= estimate the return required by lenders for the debt claim.

WACC
= blend equity cost and after-tax debt cost into a discount rate.

Project NPV
= test whether operating FCF creates value after compensating capital providers.

Redemptions
= test whether the chosen debt terms can be serviced year by year.
```

## Weak Spots To Revisit

| Weak spot | Quality | Correction rule | Next prompt |
|---|---|---|---|
| Market proxy in CAPM | `yellow` | The market proxy estimates comparable systematic risk; the project does not invest in the index. | Explain what the "market" in CAPM means and why beta uses it. |
| CAPM inside WACC | `green/yellow` | CAPM estimates `r_E`; WACC blends `r_E` and after-tax `r_D`. | Build WACC from CAPM equity cost and debt cost. |
| Debt cost versus redemptions | `yellow` | Debt cost enters WACC; redemptions calculate contractual debt-service cash flows. | Given a loan rate and maturity, identify which number goes into WACC and which goes into the repayment schedule. |
| Project cost versus debt cost | `green/yellow` | Project cost prices operating FCF risk; debt cost prices lender claim risk. | Decide whether to use firm WACC, project-specific CAPM, or debt cost in a project NPV setup. |

## Next Recall Prompts

1. In one sentence, why does CAPM use beta instead of volatility?
2. What does the market proxy represent in CAPM?
3. Why does CAPM enter WACC if the project is not investing in stocks?
4. Distinguish `r_E`, `r_D`, WACC, project cost of capital, and contractual loan rate.
5. For a positive-NPV project financed with debt, explain why a redemption schedule is still needed.

## References Back To Notes

- Main CAPM explanation: [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md) section `CAPM`.
- Market-proxy clarification: [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md) section `Clarification: Why The Market Appears In CAPM`.
- WACC and bridge: [session-07-08-cost-of-capital.md](session-07-08-cost-of-capital.md) section `Bridge From Capital Budgeting To Redemptions`.
- Terminology boundaries: [CONTEXT.md](CONTEXT.md) section `Clarification Bridge Language`.

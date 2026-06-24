# Capital Budgeting Clarification Session - 2026-06-13

Source note: [Session 05-06: Capital Budgeting](session-05-06-capital-budgeting.md)

Session type: clarification and mental-model repair

Status: clarification completed 2026-06-13 and extended 2026-06-14; first active recall remains pending

## Session Goal

Connect the direct formulas in the note to the managerial decision sequence: forecast assumptions, incremental FCF, NPV, working-capital effects, choice among alternatives, further adjustments, and risk analysis.

## User Clarification Questions And Raw Statements

1. "Does that means if there are two options to be invested, even if there is a one opportunity with better npv, you must check the cash flow forecast anyway that impacts decision making?"
2. "We are basically amplifying the decision making based on the initial NPV outcomes via digging deeper on metrics and values that defines the forecasting outcome to ensure that the used discount rate in forecast is not fragile."
3. "Where FCF actually sits in that context? It is the forecast itself? Also what incremental cash flow means in this context and what its added value?"
4. "How about capital budgeting and net working capital?"
5. "When NWC delta is positive, isn't it means more assets gained compared to liabilities? How that delta in positive affects the NPV and FCF negatively?"
6. "Regarding choosing among alternatives, I need better examples and explanation to comprehend it fully."
7. "Over this example, how the risk analysis and further adjustments are applied and impacts the decision making and the value of NPV and FCF?"
8. "For the evaluation, first better to investigate risk analysis and during investigations also apply further adjustments for all scenarios to have the NPV matrix at the end for all scenarios?"
9. "What is actually WACC?"
10. "Capital budgeting and NPV distinguish the operational gains of the project for acceptance via cash flow, whereas redemptions evaluates it from financing point of view like how the taken loan or debt will be able to be maintained with this cash flow model?"
11. "So the redemption comes after project acceptance via NPV; it defines the financing to cover the initial cost of the accepted project that can be reliably paid under forecasted free cash flow?"

## Professor Feedback And Corrections

### NPV Is Downstream Of The Forecast

The user's initial intuition correctly recognized that a higher NPV must be investigated for credibility. The ordering was corrected:

```text
Business assumptions
-> incremental cash-flow filter
-> project FCF
-> discount rate
-> NPV
-> risk analysis and decision
```

Capital budgeting does not calculate NPV first and then separately check cash flows. Forecasted incremental FCF is the input to NPV.

### FCF Is The Cash Result Of The Forecast

FCF is not the whole forecasting process. Revenue, price, volume, operating cost, tax, CapEx, working capital, and terminal assumptions are translated into the project's dated incremental FCF. NPV then converts those FCFs into value today.

### Incremental Means Caused By The Decision

```text
Incremental project FCF
= company FCF with the project
- company FCF without the project
```

This filter excludes sunk costs and unchanged overhead while including opportunity cost, cannibalization, new CapEx, and new working-capital requirements. Its added value is causal accuracy.

### Positive Delta NWC Is A Cash Use

The user correctly noticed that higher NWC can mean more net current assets. The missing distinction was asset ownership versus available cash. More inventory and receivables tie cash up in operations; more payables preserve cash through supplier financing.

```text
positive Delta NWC -> subtract from FCF -> lower current NPV
negative Delta NWC -> add to FCF -> higher current NPV
```

Working-capital recovery at project end increases final FCF, but later recovery is worth less than the same amount paid earlier.

### Alternatives Require A Decision-Type Router

- Independent projects: accept all positive-NPV projects if constraints permit.
- Mutually exclusive projects: choose the highest credible NPV.
- Capital rationing: choose the feasible combination with the highest total NPV.

The Machine A versus Machine B example showed that incremental NPV answers whether the extra investment in A creates extra value over B.

### Adjustments Before Scenarios

Known adjustments complete the FCF model. Risk analysis varies uncertain assumptions inside the completed model.

```text
known adjustments -> corrected base-case FCF and NPV
uncertain assumptions -> scenario FCFs and NPV matrix
```

The final matrix reveals upside, downside, and ranking stability. Risk analysis does not replace NPV; it produces several NPVs under defensible assumptions.

### WACC Is The Weighted Required Return

WACC combines the required returns of debt and equity providers according to their financing weights:

```text
WACC = E/(D+E) x r_E + D/(D+E) x r_D x (1-tax rate)
```

It is the hurdle rate used to discount operating project FCF when the project's risk matches the assets underlying that WACC. It is not the project's initial euro cost and it is not identical to the bank-loan interest rate.

### Project Value Versus Financing Feasibility

The user's final understanding was substantially correct and was refined into this router:

```text
Capital Budgeting and NPV
-> determine whether incremental operating FCF creates value

Financing choice
-> selects debt, equity, or a combination

Redemption schedule
-> tests how a proposed loan is repaid and whether annual debt service fits cash availability
```

Redemption does not select the financing source. It models repayment after debt amount, rate, maturity, and structure are proposed. Financing feasibility may be investigated alongside final approval, but loan interest and principal remain outside WACC-based project FCF.

A positive NPV does not guarantee a safe repayment schedule. An affordable repayment schedule does not prove that the project creates value.

## Refined Mental Model

```text
Operating story
-> cash-flow drivers
-> incremental filter
-> FCF by period
-> known adjustments
-> corrected base-case NPV
-> sensitivity / break-even / scenarios
-> NPV matrix
-> value and robustness decision
-> choose financing mix
-> build redemption schedule for proposed debt
-> test debt-service liquidity
```

Exam-ready summary:

> Capital budgeting constructs complete incremental project FCF. NPV values those cash flows today. Further adjustments correct the model, while risk analysis tests whether the NPV ranking survives reasonable uncertainty.

> WACC is the weighted required return used to value operating FCF. After a value-creating project is identified, a redemption schedule tests whether proposed debt can be repaid reliably from the project's cash-generation pattern.

## Quality Labels

| Area | Label | Evidence |
|---|---|---|
| Capital budgeting to NPV link | green | User correctly reframed the purpose as validating the assumptions supporting the NPV decision after the ordering correction. |
| Position of FCF | green | Clarified as the cash result of forecasting and the direct input to NPV. |
| Incremental cash-flow logic | yellow | Concept explained, but no closed-book include/exclude case was completed. |
| Positive `Delta NWC` intuition | yellow | Asset-versus-cash confusion was repaired through inventory, receivables, and payables examples; retrieval still needed. |
| Choice among alternatives | yellow | Independent, mutually exclusive, and capital-rationing routes were explained but not independently reproduced. |
| Further adjustments versus risk analysis | green | User proposed an NPV matrix and accepted the correction that known adjustments precede scenario variation. |
| WACC decision role | green | User linked WACC to project valuation and accepted that it is the combined debt/equity hurdle rather than the loan rate alone. |
| Capital Budgeting versus Redemptions | green | User correctly separated operating-value acceptance from financing repayment feasibility. |
| Financing sequence precision | yellow | Corrected the wording: redemption follows a proposed financing mix and may be tested alongside final approval, not only after an irreversible acceptance. |
| Full calculation fluency | red | No complete FCF table, discounted NPV calculation, or scenario calculation was performed by the user. |

## Next Recall Prompts

1. Without looking at the note, reproduce the chain from business assumptions to the final investment decision.
2. Explain why FCF is the result of the forecast but not the entire forecasting process.
3. Classify sunk R&D, warehouse opportunity cost, cannibalized margin, interest expense, inventory growth, and salvage value as include or exclude.
4. Explain why a positive `Delta NWC` reduces current FCF even though net current assets increased.
5. Given two machines, identify whether the projects are independent, mutually exclusive, or capital rationed and state the correct decision rule.
6. Build one complete base-case FCF, apply a known working-capital adjustment, and recalculate NPV.
7. Create downside, base, and upside assumptions, calculate an NPV matrix, and interpret ranking stability.
8. Define WACC, identify its debt and equity components, and explain why it is not the bank-loan rate.
9. Given a positive-NPV project and a proposed loan, separate project FCF from debt service and state what each analysis proves.
10. Explain why an aggressive redemption schedule should trigger financing redesign rather than automatic rejection of a positive-NPV project.

## References

- [High-Yield 80/20 Summary](session-05-06-capital-budgeting.md#high-yield-8020-summary)
- [Where FCF Sits In The Forecast](session-05-06-capital-budgeting.md#where-fcf-sits-in-the-forecast)
- [Incremental Cash Flow Rules](session-05-06-capital-budgeting.md#incremental-cash-flow-rules)
- [Why Positive Delta NWC Reduces FCF](session-05-06-capital-budgeting.md#why-positive-delta-nwc-reduces-fcf)
- [Choosing Among Alternatives](session-05-06-capital-budgeting.md#choosing-among-alternatives)
- [Known Adjustments Before Risk Analysis](session-05-06-capital-budgeting.md#known-adjustments-before-risk-analysis)
- [From Corrected FCF To An NPV Matrix](session-05-06-capital-budgeting.md#from-corrected-fcf-to-an-npv-matrix)
- [What WACC Actually Means](session-05-06-capital-budgeting.md#what-wacc-actually-means)
- [Redemptions To Capital Budgeting Bridge](../exercise-05-redemptions/redemptions-to-capital-budgeting-bridge.md)

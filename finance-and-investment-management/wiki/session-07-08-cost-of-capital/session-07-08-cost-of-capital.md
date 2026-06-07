# Session 07-08: Cost Of Capital

Source file: `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260604/Investment and  950881761 (S26)_2026064_1514/CW 23  02.06. _ 03.06./Lecture 78 Cost of Capital.pdf`
Lecture folder: `finance-and-investment-management/`
Date processed: 2026-06-06
Course position: Corporate Finance lecture, sessions 07+08, after Capital Budgeting.

## High-Yield 80/20 Summary

Cost of capital is the required return for an investment with the same risk. It is the discount rate used to turn risky future FCFs into present value.

Core exam logic:

1. Match the discount rate to the risk of the cash flows.
2. Estimate the equity cost of capital with CAPM: `r_i = r_f + beta_i x (E[r_Mkt] - r_f)`.
3. Estimate debt cost from YTM, debt ratings, or debt beta.
4. Use comparable companies to estimate project risk when the project is not publicly traded.
5. Unlever comparable equity beta to asset beta, then relever if needed.
6. Use WACC only when the project has similar risk and financing to the firm or target financing.

High-yield interpretation:

```text
Cost of capital is not "the amount invested."
It is the required percentage return for bearing the project's risk.
```

## The Equity Cost Of Capital

The cost of capital of any investment opportunity equals the expected return of available investments with the same risk.

The lecture lists three estimation methods:

- Capital Asset Pricing Model, CAPM.
- Dividend discount model.
- Bond yield plus risk premium.

The deck focuses mainly on CAPM.

## CAPM

CAPM estimates the expected return required for bearing systematic market risk.

```text
r_i = r_f + beta_i x (E[r_Mkt] - r_f)
```

Variables:

- `r_i` = equity cost of capital for security or project `i`.
- `r_f` = risk-free rate.
- `beta_i` = sensitivity of the security's return to market return.
- `E[r_Mkt]` = expected market return.
- `E[r_Mkt] - r_f` = expected market risk premium, also called equity risk premium.

Interpretation:

- Investors like high returns and dislike risk.
- Diversification can remove unsystematic risk.
- Systematic risk remains and is priced.
- Beta measures exposure to systematic market risk.

Exam trap: volatility measures total risk; beta measures market risk. CAPM prices beta, not total volatility.

### Disney And Domino Example

The slides compare:

- Disney: volatility 20%, beta 1.29.
- Domino's: volatility 30%, beta 0.62.
- Risk-free rate 3%, expected market return 8%, market risk premium 5%.

Calculations:

```text
r_DIS = 3% + 1.29 x (8% - 3%) = 9.45%
r_DPZ = 3% + 0.62 x (8% - 3%) = 6.10%
```

Domino has more total volatility, but Disney has more market risk and therefore the higher equity cost of capital under CAPM.

## Implementing CAPM

Step 1: construct or proxy the market portfolio.

- The market portfolio is value-weighted.
- Common proxies include broad market indexes.
- The deck contrasts value-weighted indexes such as the S&P 500 with price-weighted indexes such as the DJIA.

Step 2: determine the risk-free rate and market risk premium.

- Practitioners often use long-term government bond yields as risk-free-rate proxies.
- Historical market risk premia can be noisy and backward-looking.
- A fundamental market risk premium can be inferred from index valuation:

```text
r_Mkt = Div_1 / P_0 + g
```

Step 3: estimate beta.

- Regression beta is the slope of security excess returns against market excess returns.
- Formula intuition:

```text
beta_i = Cov(r_i, r_Mkt) / Var(r_Mkt)
```

Beta interpretation:

- `beta > 1`: more market-sensitive than the market, higher required return.
- `beta < 1`: less market-sensitive than the market, lower required return.

## Estimation Risk In Beta

Beta is estimated, not observed with certainty. Choices matter:

- estimation period,
- market index,
- return frequency,
- smoothing,
- small-firm or private-firm adjustments.

Example from the deck:

```text
beta estimate = 1.76
r_f = 3%
market risk premium = 5%
r_E = 3% + 1.76 x 5% = 11.8%
```

If the 95% confidence interval for beta is 1.5 to 2.0, then:

```text
lower r_E = 3% + 1.5 x 5% = 10.5%
upper r_E = 3% + 2.0 x 5% = 13.0%
```

Exam implication: the cost of capital is an estimate with uncertainty, not an exact truth.

## Debt Cost Of Capital

The debt cost of capital should reflect the current market rate investors require for the firm's debt risk.

Methods:

| Method | Logic | Caveat |
|---|---|---|
| Yield-to-maturity approach | Use YTM on outstanding debt | Overstates expected return if default risk is high |
| Debt-rating approach | Use yield on similarly rated debt with similar maturity | Depends on comparable bond data |
| Beta-CAPM approach | Estimate debt beta and use CAPM | Debt betas are hard because bonds trade infrequently |

YTM definition:

```text
YTM = IRR earned by holding the bond to maturity and receiving promised payments
```

If default is possible, promised YTM is not the same as expected return.

Simplified default-adjusted expected return from the slides:

```text
r_d = y - p x L
```

Variables:

- `y` = yield to maturity.
- `p` = probability of default.
- `L` = expected loss per EUR 1 of debt in default.

Exam trap: for risky debt, YTM generally overstates debt cost of capital because not all promised payments are expected to be received.

## Project Cost Of Capital

The project cost of capital should match the project's own risk, not mechanically the firm's average WACC.

When the project is like a single-product public firm:

```text
r_project = r_f + beta_comparable x market risk premium
```

Example:

- Lululemon beta = 1.20.
- Risk-free rate = 3%.
- Market risk premium = 5%.

```text
r_project = 3% + 1.20 x 5% = 9%
```

Managerial interpretation: if investors can earn 9% by buying a comparable publicly traded firm, the private project must be expected to earn at least 9% for the same risk.

## Levered Comparables And Asset Beta

When comparable firms have debt, their equity beta includes both business risk and financial leverage. To estimate project business risk, remove leverage first.

Asset cost of capital:

```text
r_U = r_E x E/(E + D) + r_D x D/(E + D)
```

Asset beta:

```text
beta_U = beta_E x E/(E + D) + beta_D x D/(E + D)
```

With taxes, a common unlever/relever approximation in the deck is:

```text
beta_asset = beta_equity / [1 + (1 - tau) x D/E]

beta_equity_project = beta_asset x [1 + (1 - tau) x D/E_project]
```

Exam workflow for non-public companies:

1. Select comparable firms with similar business risk.
2. Estimate each comparable's equity beta.
3. Unlever beta to asset beta.
4. Average asset betas across comparables if available.
5. Relever beta for the project's target financial risk if needed.
6. Use CAPM to estimate the project cost of capital.

## Cash And Net Debt

Cash is a risk-free asset that lowers the average risk of a firm's total assets. For enterprise risk, use net debt:

```text
Net debt = debt - excess cash and short-term investments
Enterprise value = equity value + net debt
```

Garmin example from the slides:

- Market capitalization: USD 18.8 billion.
- Debt: USD 0.1 billion.
- Cash: USD 1.6 billion.
- Equity beta: 0.93.
- Net debt: `0.1 - 1.6 = -1.5`.
- Enterprise value: `18.8 - 1.5 = 17.3`.

With risk-free debt/cash beta assumed zero:

```text
beta_U = 18.8 / 17.3 x 0.93 + (-1.5 / 17.3) x 0 = 1.01
```

Interpretation: because Garmin holds large cash balances, its equity is less risky than the underlying operating business.

## Project Risk Characteristics

Firm asset beta reflects the average risk of the firm's assets. A specific project may have different risk.

Project risk drivers:

- line of business,
- cyclicality of demand,
- fixed versus variable cost structure,
- operating leverage.

Operating leverage:

```text
Higher fixed cost share -> cash flows more sensitive to sales shocks -> higher beta -> higher cost of capital
```

Exam rule: multi-divisional firms should evaluate projects using asset betas from similar lines of business, not the parent firm's average beta when risks differ.

## WACC

With taxes, WACC uses the after-tax cost of debt:

```text
r_WACC = r_E x E/(E + D) + r_D x D/(E + D) x (1 - tau_c)
```

Given target leverage:

```text
r_WACC = r_U - [D/(E + D)] x tau_c x r_D
```

Interpretation:

- `r_U` is the unlevered or pre-tax WACC: the expected return investors earn by holding the firm's assets.
- With taxes, WACC is below the expected return on assets because interest is tax deductible.
- WACC can evaluate a project with the same risk and same financing policy as the firm.

## Exam Relevance

Likely prompts:

- "Compute equity cost of capital with CAPM."
- "Explain beta versus volatility."
- "Estimate debt cost of capital and explain why YTM can overstate it."
- "Unlever and relever a comparable beta."
- "Explain when firm WACC is appropriate for a project."
- "Calculate WACC with tax-deductible debt."

Common traps:

- Using volatility instead of beta in CAPM.
- Using one company WACC for every project.
- Treating YTM as expected debt return for distressed debt.
- Forgetting market-value weights.
- Forgetting the after-tax debt term in WACC.
- Ignoring cash when estimating enterprise beta.

## Visual Knowledge Map

```mermaid
flowchart TD
    FCF[Project FCF] --> RATE[Need Discount Rate]
    RATE --> RISK[Match Project Risk]
    RISK --> EQUITY[Equity Cost Of Capital]
    EQUITY --> CAPM[CAPM]
    CAPM --> RF[Risk-Free Rate]
    CAPM --> BETA[Beta]
    CAPM --> ERP[Market Risk Premium]
    RATE --> DEBT[Debt Cost Of Capital]
    DEBT --> YTM[YTM]
    DEBT --> RATING[Debt Rating]
    DEBT --> DBETA[Debt Beta]
    RISK --> COMP[Comparable Firms]
    COMP --> UNLEV[Unlever To Asset Beta]
    UNLEV --> RELEV[Relever For Target Capital Structure]
    EQUITY --> WACC[WACC]
    DEBT --> WACC
    WACC --> NPV[Discount Project FCF]
```

## Subject Knowledge Graph

| Node | Meaning | Exam Relevance |
|---|---|---|
| Cost of capital | Required return for an investment with the same risk | Discount-rate selection |
| Equity cost of capital | Required return for equity investors | CAPM calculation |
| CAPM | Model linking required return to systematic risk | Main formula in the deck |
| Beta | Sensitivity to market excess returns | Risk input that CAPM prices |
| Market risk premium | Expected market return over risk-free rate | CAPM input |
| Debt cost of capital | Expected return required by debt investors | WACC input |
| Yield to maturity | IRR from promised bond payments | Can overstate risky debt return |
| Asset beta | Business-risk beta without financial leverage | Comparable-project risk estimate |
| Net debt | Debt minus excess cash | Enterprise-risk adjustment |
| Operating leverage | Fixed-cost intensity of the project | Raises project beta |
| WACC | Weighted average after-tax financing cost | Project discount rate when risk/financing match |

| From | Relationship | To | Why It Matters |
|---|---|---|---|
| Cost of capital | discounts | project FCF | Converts expected cash flows to value |
| CAPM | estimates | equity cost of capital | Main required-return method |
| Beta | measures | systematic risk | Diversifiable risk is not priced in CAPM |
| YTM | may overstate | debt cost of capital | Default risk means promised return exceeds expected return |
| Comparable firms | estimate | asset beta | Private projects lack traded beta |
| Leverage | increases | equity beta | Debt makes equity cash flows riskier |
| Cash holdings | reduce | observed equity risk | Use net debt/enterprise value logic |
| WACC | combines | equity and after-tax debt costs | Used for FCF valuation under matching assumptions |

## Retrieval Prompts

Closed-book questions:

1. State the CAPM formula and define every input.
2. Why does CAPM price beta rather than volatility?
3. Why can YTM overstate the debt cost of capital?
4. What is the difference between equity beta and asset beta?
5. When is WACC an appropriate project discount rate?

Application prompts:

1. Compute equity cost of capital for `r_f = 3%`, `beta = 1.4`, and market risk premium `5%`.
2. A firm has high cash holdings and no risky debt. Is its equity beta above or below the beta of its operating assets?
3. A project has higher fixed costs than the firm's average project. What happens to project beta and cost of capital?
4. A bond has YTM 9%, default probability 4%, and loss rate 50%. Set up the expected debt return.
5. Explain why a food-retail project should not automatically use the WACC of a software company.

## Practice Tasks

1. CAPM drill: calculate required returns for three betas: 0.6, 1.0, 1.5.
2. Comparable-company drill: unlever a comparable beta, then relever it for a target D/E.
3. WACC drill: compute WACC from market values of debt and equity, debt cost, equity cost, and tax rate.
4. Interpretation drill: explain why using too low a discount rate can make bad projects look positive NPV.

## Connections

Previous notes:

- `finance-and-investment-management/wiki/session-05-06-capital-budgeting/session-05-06-capital-budgeting.md`
- `finance-and-investment-management/wiki/session-03-04-investment-analysis/session-03-04-investment-analysis.md`
- `finance-and-investment-management/wiki/exercise-06-bonds-i/exercise-06-bonds-i.md`

Future notes:

- `finance-and-investment-management/wiki/session-09-10-capital-structure/session-09-10-capital-structure.md`
- `finance-and-investment-management/wiki/session-11-12-capital-structure-and-taxes/session-11-12-capital-structure-and-taxes.md`

Cross-course links:

- SCM uncertainty: both ask how uncertainty affects decisions, but finance prices systematic risk through required return.
- Organization/strategy: project risk can differ by division, technology, and operating model.

## Weakness Flags

- First active recall pending.
- Drill beta versus volatility.
- Drill "same risk" matching before formulas.
- Drill when WACC is appropriate versus when a project-specific rate is needed.

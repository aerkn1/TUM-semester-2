# Ubiquitous Language: Exercise 10-11 Stocks Valuation

Source note: `exercise-10-11-stocks-valuation.md`
Course: Finance and Investment Management
Processed: 2026-07-09

This context file defines the stock valuation terms, formulas, and decision language from Exercises 10 and 11.

## Dividend And Return Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Dividend Per Share** | Total dividend payments divided by shares entitled to dividends. | total dividend |
| **Dividend Yield** | Dividend per share divided by current share price. | total return |
| **Payout Ratio** | Fraction of EPS distributed as dividends: `DPS / EPS`. | dividend yield |
| **Retention Ratio** | Fraction of EPS retained: `1 - payout ratio`. | cash reserves only |
| **Cost Of Equity** | Required return shareholders demand for the stock's risk. | growth rate |
| **Dividend Growth Rate** | Growth rate of dividends and EPS under stable payout assumptions. | return on equity |

## Valuation Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Dividend Discount Model** | Stock valuation as the PV of expected future dividends. | price multiple |
| **Zero-Growth Stock** | Stock with constant dividend forever: `P_0 = D/r_e`. | no-value stock |
| **Gordon Growth Model** | Constant-growth DDM: `P_0 = D_1/(r_e - w)`. | any growth model |
| **Two-Phase Growth Model** | DDM with high growth for a finite period and stable growth afterward. | average growth model |
| **Terminal Value** | Value at the end of explicit forecast period for dividends beyond that date. | final dividend |
| **PVGO** | Present value of growth opportunities: `P_0 - EPS_1/r_e`. | growth rate |
| **P/E Ratio** | Price divided by expected EPS. | profitability |
| **P/B Ratio** | Price divided by book value per share. | market-to-book always |
| **Multiple Valuation** | Valuation by applying peer P/E or P/B multiples to firm fundamentals. | DCF |

## Core Formulas

| Formula | Meaning | Use |
|---|---|---|
| `DPS = total dividends / eligible shares` | Dividend per share | Remove treasury shares if not dividend-entitled. |
| `Dividend yield = DPS / P_0` | Dividend yield | Compare income return to share price. |
| `p = DPS / EPS` | Payout ratio | Dividend policy. |
| `w = (1-p) x ROE` | Sustainable growth under stable policy | Growth from retained earnings. |
| `P_0 = (D_1 + P_1)/(1+r_e)` | One-year stock value | Single-period holding. |
| `P_0 = D/r_e` | Zero-growth DDM | Constant dividends forever. |
| `P_0 = D_1/(r_e-w)` | Constant-growth DDM | Mature firm with stable growth. |
| `PVGO = P_0 - EPS_1/r_e` | Growth value | Tests whether reinvestment creates value. |
| `P/E = P_0/EPS_1` | Earnings multiple | Peer or growth comparison. |
| `P/B = P_0/BVPS` | Book multiple | ROE versus cost-of-equity comparison. |

## Relationships

- **Retention Ratio** increases **Dividend Growth Rate** only if retained earnings are productively invested.
- **ROE** above **Cost Of Equity** creates positive **PVGO**.
- **ROE** equal to **Cost Of Equity** leaves value unchanged.
- **ROE** below **Cost Of Equity** destroys value when earnings are retained.
- **P/E Ratio** and **P/B Ratio** summarize valuation but depend on growth, risk, and peer comparability.

## Example Dialogue

Student: "A higher dividend is always better for stock value."

Professor: "Not always. If retained earnings can earn `ROE > r_e`, a lower payout can increase value because growth opportunities are positive."

Student: "So high growth always means a good stock?"

Professor: "No. Growth matters only relative to the cost of equity. Growth below the required return destroys value."

## Flagged Ambiguities

| Ambiguity | Canonical recommendation |
|---|---|
| `D` | Say dividend per share and specify `D_0` or `D_1`. |
| `w` | Say dividend/EPS growth rate, not required return. |
| `r_e` | Say cost of equity or required shareholder return. |
| "Price" | Say intrinsic value from model or market price. |
| "High payout" | Distinguish income preference from value creation. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Using `D_0` as Gordon numerator. | Use next dividend `D_1`. |
| Assuming retention is always good. | Check `ROE` versus `r_e`. |
| Treating P/E or P/B as a full valuation proof. | Use peer comparability and growth/risk interpretation. |
| Forgetting treasury shares in DPS. | Use dividend-entitled shares. |
| Missing the terminal value in two-phase DDM. | Value explicit dividends plus terminal value. |

## Cheat-Sheet Language

```text
Stock valuation route:
dividend metrics -> required return -> dividend forecast model -> intrinsic price -> compare with market price.

Growth value rule:
ROE > r_e creates value; ROE = r_e neutral; ROE < r_e destroys value.

Multiple route:
peer multiple x firm fundamental -> implied price -> compare to actual price, but check peer comparability.
```

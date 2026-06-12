# Ubiquitous Language: Chapter 04 Price

Source note: `chapter-04-price.md`

Definition source: local lecture deck and note, enriched with standard pricing terminology where needed.

## Behavioral Price Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Willingness To Pay (WTP)** | Maximum sacrifice a customer accepts for an offering. | market price, actual payment |
| **Reference Price** | Internal or external benchmark used to evaluate an observed price. | fair price always |
| **Price Fairness** | Judgment about whether a price and the process producing it are acceptable. | low price |
| **Compromise Effect** | Increased choice of an intermediate option after an extreme alternative is introduced. | decoy effect |
| **Decoy Effect** | Preference shift caused by an asymmetrically dominated option that favors a target. | compromise effect |
| **Price Threshold** | Price at which evaluation or demand changes discontinuously. | average price |
| **Price Knowledge** | Price-related information stored in long-term memory. | perfect recall |

## Strategy Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Price Differentiation** | Charging different prices for the same or slightly modified benefit to capture heterogeneous WTP. | any discount |
| **Dynamic Pricing** | Algorithmic or managerial adjustment of price as market conditions change. | yield management always |
| **Yield Management** | Joint control of price and perishable capacity using demand forecasts and booking information. | surge pricing only |
| **Skimming Pricing** | High introductory price followed by reductions across the life cycle. | premium pricing permanently |
| **Penetration Pricing** | Low introductory price intended to accelerate diffusion and market share. | predatory pricing |
| **Two-Part Tariff** | Fixed access fee plus per-unit usage price. | bundle |
| **Full Bundling** | Products are available only as a package. | mixed bundling |
| **Mixed Bundling** | Products are available separately and as a package. | quantity discount |

## Formula Language

| Symbol or term | Meaning and unit | Decision role |
|---|---|---|
| `p` | price per unit | revenue and contribution per sale |
| `x` | units sold in the planning period | demand response |
| `c_var` | variable cost per unit | marginal cost in the simple model |
| `C_fix` | fixed cost per planning period | amount contribution must cover |
| `p - c_var` | contribution margin per unit | funds fixed cost and profit |
| `CMR` | contribution margin divided by revenue | share of each revenue euro available for fixed cost and profit |
| `epsilon` | percentage quantity response divided by percentage price change | demand sensitivity |

```text
Profit = (p - c_var)x - C_fix
x_crit = C_fix/(p - c_var)
CMR = (p - c_var)/p
R_crit = C_fix/CMR
epsilon = (dx/dp)(p/x)
Monopoly optimum: MR = MC
```

## Canonical Relationships

- **Customer value** supports **WTP**, but WTP is also shaped by alternatives, context, and fairness.
- **Reference price** influences **price fairness** and perceived savings.
- **Price differentiation** requires heterogeneous **WTP** plus segment separation.
- **Bundling** pools WTP across products; **two-part tariffs** separate access from usage.
- **Contribution margin** links price to **break-even volume**.
- **Price elasticity** links price changes to demand response.

## Visual Memory Aid

```mermaid
flowchart LR
    WTP[Willingness to pay] --> Price[Price choice]
    Reference[Reference price] --> Fairness[Fairness judgment]
    Fairness --> Demand[Demand response]
    WTP --> Differentiate[Differentiate or bundle]
    Price --> Margin[Contribution margin]
    Demand --> Profit[Profit]
    Margin --> Profit
```

## Example Dialogue

> **Manager:** "Our algorithm says demand is high, so should we raise the airport price?"
>
> **Analyst:** "First separate **dynamic pricing** from customer acceptance. Estimate elasticity and contribution, then test the **reference price** and **price fairness** response."
>
> **Manager:** "And if business travelers value flexibility more?"
>
> **Analyst:** "That supports benefit-based **price differentiation**, provided the segment can self-select and resale is controlled."

## Flagged Ambiguities

- Use **revenue** for `p*x`; use **profit** only after subtracting variable and fixed cost.
- Use **contribution margin** for revenue remaining after variable cost; it is not net profit.
- Use **dynamic pricing** broadly; reserve **yield management** for demand-and-capacity control of perishable inventory.
- Use **price differentiation** for a deliberate WTP/segment mechanism, not every temporary discount.
- The lecture's `a` and `b` depend on whether demand is written as `x(p)` or inverse demand `p(x)`; define the chosen function before calculating.

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Price cut of 10% means volume need rise 10%. | Recalculate contribution per unit; required volume can rise far more. |
| Break-even revenue and volume are identical. | `R_crit` is currency; `x_crit` is units. |
| Revenue maximum equals profit maximum. | Profit includes cost; optimize with `MR = MC`. |
| Inelastic demand means quantity does not change. | It changes proportionally less than price. |
| High WTP proves a price is fair. | Fairness is a separate judgment about level and procedure. |

## Cheat-Sheet Language

```text
Price decision = contribution economics + demand response + competitor response + fairness.
For calculations: formula -> substitution -> result -> unit -> managerial interpretation.
```

# Chapter 04: Price - Exam Cheatsheet

Source note: [chapter-04-price.md](chapter-04-price.md)

Created: 2026-07-15

Updated: 2026-07-22 - aligned with mock/example exam calculation routes and behavioral-pricing option traps.

Exam context: Marketing exam on 2026-07-22 is a 90-minute written exam with a non-programmable calculator allowed. Price is the most calculation-heavy Marketing topic. This sheet does not mark `First Pass` as completed.

## Core Exam Move

```text
Pricing objective -> customer WTP/context -> price mechanism
-> calculation if needed -> demand/competition/fairness check
-> managerial decision.
```

Never end a numerical answer with only a number. Add the unit and the decision meaning.

## Formula Block

```text
Profit = (p - c_var)x - C_fix
Contribution per unit = p - c_var
x_crit = C_fix / (p - c_var)
CMR = (p - c_var) / p
R_crit = C_fix / CMR
Expected profit = sum(probability_j * profit_j)
epsilon = (dx/dp)(p/x)
Revenue from inverse demand: R(x) = p(x) * x
Monopoly optimum: MR = MC
```

Variable meanings:

| Symbol | Meaning | Unit |
|---|---|---|
| `p` | unit price | currency/unit |
| `x` | quantity sold | units |
| `c_var` | variable unit cost | currency/unit |
| `C_fix` | fixed cost | currency/period |
| `CMR` | contribution margin ratio | percent or decimal |
| `epsilon` | price elasticity | percent quantity response / percent price response |

## Fast Calculation Routines

Break-even volume:

```text
x_crit = C_fix / (p - c_var)
```

Target-profit volume:

```text
x_target = (C_fix + target profit) / (p - c_var)
```

Required volume after price change:

```text
Old contribution = (p_old - c_var) * x_old
New contribution per unit = p_new - c_var
x_needed = old contribution / new contribution per unit
```

Expected-value decision:

```text
For each path: profit = (p - c_var)x - C_fix
Then: EV = probability-weighted sum of path profits
```

PapaTurk inverse-demand move:

```text
p = 5 - x/3000
R = p*x = 5x - x^2/3000
MR = dR/dx = 5 - 2x/3000
Profit maximum: MR = MC
```

## Behavioral Pricing Router

| Effect | Meaning | Exam use |
|---|---|---|
| Reference price | benchmark used to judge a price | fairness and perceived savings |
| Compromise effect | middle option becomes attractive after adding an extreme | choice architecture |
| Decoy effect | inferior option makes target option look better | asymmetrically dominated alternative |
| Relative savings | same euro saving feels different by base price | framing |
| Pain of paying | payment salience changes sacrifice feeling | cash vs card/subscription |
| Price fairness | acceptability of price and process | dynamic pricing risk |

Exam structure:

```text
pricing tactic -> psychological mechanism -> expected behavior
-> fairness/transparency risk -> safeguard.
```

## Strategy Router

| Strategy | Core logic | Best fit | Danger |
|---|---|---|---|
| Price differentiation | capture heterogeneous WTP | identifiable/self-selecting segments | unfairness, arbitrage, complexity |
| Yield management | match perishable capacity with demand at changing prices | airlines, hotels, capacity expiry | opacity and gouging perception |
| Two-part tariff | access fee plus usage price | falling marginal WTP, controllable access | wrong access fee kills entry |
| Skimming | high initial price, later reductions | high-WTP early buyers, scarce/differentiated innovation | slow diffusion |
| Penetration | low initial price to build adoption | scale economies, network effects, price-sensitive market | weak margin, hard later increases |
| Bundling | combine products to pool WTP | negatively correlated valuations | forced purchase, cannibalization |

## Written-Exam Answer Skeletons

Price-change case:

```text
1. Calculate old contribution/profit.
2. Calculate new contribution per unit.
3. Estimate or compute demand response.
4. Compare profit/contribution, not only revenue or sales.
5. Add customer fairness and competitor reaction caveat.
```

Price differentiation case:

```text
Heterogeneous WTP? -> segment identifiable/self-selecting?
-> arbitrage controlled? -> incremental revenue > complexity/fairness cost?
-> choose temporal/geographic/demographic/benefit/quantity/dynamic/bundling form.
```

Elasticity case:

```text
Use elasticity to forecast quantity response, then calculate contribution or profit.
Elasticity alone does not decide the price.
```

## Mock And Example Exam Upgrade

Price questions are easiest if you compute before looking at answer choices.

Practice-exam routines:

| Exam pattern | Fast solution | Reject options that |
|---|---|---|
| 10% price cut from `EUR 200`, `c_var = EUR 100` | Old contribution `100`; new contribution `80`; required multiplier `100/80 = 1.25`; volume increase `25%`. | Say a 10% price cut needs only 10% more volume. |
| Break-even with `p = 80`, `c_var = 30`, `C_fix = 40,000` | Contribution `50`; `x_crit = 40,000 / 50 = 800 units`. | Divide fixed cost by variable cost or report revenue as units. |
| CMR with `p = 80`, `c_var = 30` | `CMR = 50/80 = 62.5%`. | Use variable-cost ratio `30/80 = 37.5%`. |
| Expected-profit pricing | Compute branch profit first, then probability-weight. | Choose higher price just because unit margin is higher. |
| Bundling WTP table | For each option, count actual buyers and revenue. | Assume mixed bundling automatically wins. |
| Monopoly inverse demand | Build `R = p(x)*x`, derive `MR`, set `MR = MC`. | Treat the `2x` in marginal revenue as arbitrary. |

Behavioral-pricing statement traps:

```text
Compromise effect = middle option becomes attractive.
Decoy effect = asymmetrically dominated option shifts preference.
Reference price = internal or external benchmark.
Relative savings = same euro discount feels different by base price.
Dynamic/surge pricing can be efficient and still feel unfair.
High-stakes urgency may reduce price sensitivity, even while fairness risk rises.
```

Price strategy count logic:

```text
Price differentiation needs heterogeneous WTP, identifiable/self-selecting segments,
limited arbitrage/resale, and fairness/complexity control.
Penetration = low initial price for adoption/scale/share/network effects.
Skimming = high initial price to harvest high-WTP early buyers.
```

## Traps And Corrections

| Trap | Correction |
|---|---|
| Revenue = profit. | Profit subtracts variable and fixed costs. |
| A 10% price cut needs only 10% more volume. | Recalculate contribution per unit. |
| Fixed cost is marginal cost. | Marginal cost is the extra cost of one more unit. |
| Dynamic pricing is accepted if efficient. | Fairness and reference prices can block acceptance. |
| Every discount is price differentiation. | Identify the segmentation or self-selection mechanism. |
| Max sales means max profit. | Contribution margin and fixed cost matter. |
| Revenue max = profit max. | Profit max uses `MR = MC`. |
| The `2x` in MR is arbitrary. | It comes from differentiating `x^2`. |

## Last Line

```text
Price decision = contribution economics + demand response + competitor response + fairness.
```

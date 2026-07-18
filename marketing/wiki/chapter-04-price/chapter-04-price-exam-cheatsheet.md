# Chapter 04: Price - Exam Cheatsheet

Source note: [chapter-04-price.md](chapter-04-price.md)

Created: 2026-07-15

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


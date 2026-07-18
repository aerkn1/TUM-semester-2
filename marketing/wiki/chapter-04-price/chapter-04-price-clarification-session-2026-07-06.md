# Chapter 04 Price - Clarification Session - 2026-07-06

Linked source note: [chapter-04-price.md](chapter-04-price.md)

Linked context file: [CONTEXT.md](CONTEXT.md)

Session type: targeted clarification and wiki refinement

Schedule status: clarification saved only. `First Pass` remains pending because this was not a closed-book active-recall completion.

## Clarification Questions And Corrections

| Prompt / user wording | User answer or confusion point | Professor feedback and correction | Quality |
|---|---|---|---|
| "I wanna understand the quantity based and two part pricing but the example given in wiki notes is not very clear." | Needed the mechanism behind the beer example. | Quantity-based pricing is the broad family where price changes with amount bought or used. A two-part tariff is a specific version: fixed access fee plus per-unit usage price. In the beer example, setting the beer price at marginal cost creates efficient consumption; the access fee captures the surplus. | yellow -> green |
| "due to the dynamic consumer surplus consumption, the value of extra consumption reduces by time" | Treated the reduction in extra value as dynamic/time-based consumer surplus. | Cleaner exam wording: **decreasing marginal willingness to pay** or **diminishing marginal utility** across additional units. The issue is the next beer is worth less than the previous beer, not that surplus changes over calendar time. | yellow |
| "how about the skimming and pentration?" | Asked for the strategic distinction. | Skimming starts high, then lowers price to capture high-WTP early buyers and recover fixed/development investment. Penetration starts low to accelerate adoption, scale, market share, or network effects. | green/yellow |
| "I thikn skimming to cover the marginal cost faster..." | Connected skimming to marginal cost recovery. | Correction: skimming mainly helps recover fixed development/launch/capacity investment faster. Marginal cost is the extra cost of one unit and is usually covered unit by unit if price exceeds variable cost. | yellow |
| "...limited-seat is a kind of approach that not reaching to broader customers and expecting high adoption" | Correctly sensed limited seats are not broad-market penetration, but mixed in high adoption. | Limited-seat executive courses, scarce workshops, and luxury launches fit skimming because they screen for high-WTP customers and protect scarcity. They do not aim for broad adoption immediately. | yellow -> green |
| "Regarding the pricing under uncertainty, we apply marginal analysis. For the variables like unit cost, epsilon, price etc. what is the definition behind?" | Blended pricing under uncertainty with marginal analysis. | Route the tools separately. Pricing under uncertainty uses expected value/decision trees. Marginal analysis uses demand, elasticity, `MR = MC`, and contribution/profit formulas. | yellow |
| "also give a example calculation for expected value for given uncertain competitor/sales outcomes" | Needed a numerical probability example. | Added headset example: high price EV = EUR 32,000 and low price EV = EUR 32,000, so the manager then decides using risk, positioning, capacity, fairness, and strategy. | green |
| "due to the probability of occurence" | Identified probability as the reason for expected value. | Correct but incomplete: each probability weights a profit outcome. The profit outcome itself depends on price, unit cost, fixed cost, and quantity. | green/yellow |
| "also, how we utilize the epsilon? give another example" | Needed practical elasticity use. | `epsilon` estimates the percentage quantity response to a percentage price change. Then compute contribution/profit. With `p = 100`, `x = 1,000`, `c_var = 40`, a 10% price rise lowers contribution if `epsilon = -2`, but raises contribution if `epsilon = -0.5`. | green/yellow |
| "also in papturk example, p is given with x but in revenue maximizaition calculation we make it 2x in equation. Why?" | Asked why `p = 5 - x/3000` becomes `MR = 5 - 2x/3000`. | Revenue is `R = p*x = (5 - x/3000)x = 5x - x^2/3000`. Marginal revenue is the derivative, so `d(x^2)/dx = 2x`. The economic intuition: selling one more unit requires lowering price on all units, so MR falls faster than price. | green/yellow |

## Refined Mental Models

- Two-part tariff: **access fee captures surplus; usage price guides consumption**.
- The beer example should be explained through **marginal WTP decreasing with each additional unit**, not through time dynamics.
- Skimming: **high early price for high-WTP customers and fixed/development investment recovery**.
- Penetration: **low early price for adoption, scale, market share, or network effects**.
- Expected value under uncertainty: **probability-weighted profit**, not probability-weighted sales alone.
- Elasticity: **quantity-response forecast**; contribution/profit calculation decides whether the price change is good.
- PapaTurk `2x`: **algebra derivative plus monopoly pricing intuition**.

## Worked Calculation Anchors Saved

### Two-Part Tariff Beer Example

```text
Beer marginal cost = EUR 1
WTP sequence = 2.50, 2.00, 1.50, 1.00, 0.50

At usage price EUR 1:
surplus = 1.50 + 1.00 + 0.50 + 0.00 = EUR 3.00

Access fee = EUR 3
Usage price = EUR 1
Profit from access fee = EUR 3
```

### Expected-Profit Example

```text
c_var = EUR 30
C_fix = EUR 10,000

High price EUR 80:
0.60*((80 - 30)*1,000 - 10,000) + 0.40*((80 - 30)*600 - 10,000)
= 0.60*40,000 + 0.40*20,000
= EUR 32,000

Low price EUR 60:
0.50*((60 - 30)*1,600 - 10,000) + 0.50*((60 - 30)*1,200 - 10,000)
= 0.50*38,000 + 0.50*26,000
= EUR 32,000
```

### Elasticity Example

```text
Current: p = EUR 100, x = 1,000, c_var = EUR 40
Current contribution = (100 - 40)*1,000 = EUR 60,000

If epsilon = -2 and price rises 10%:
x falls 20% to 800
new contribution = (110 - 40)*800 = EUR 56,000

If epsilon = -0.5 and price rises 10%:
x falls 5% to 950
new contribution = (110 - 40)*950 = EUR 66,500
```

### PapaTurk Marginal Revenue

```text
p = 5 - x/3000
R = p*x = 5x - x^2/3000
MR = dR/dx = 5 - 2x/3000
```

## Weak Spots To Review

| Weak spot | Label | Correction rule |
|---|---|---|
| Two-part tariff mechanism | yellow | First separate access fee from per-unit usage price. |
| Consumer surplus wording | yellow | Say decreasing marginal WTP, not dynamic surplus over time. |
| Skimming cost logic | yellow | Skimming recovers fixed/development investment, not marginal cost faster. |
| Expected value | yellow/green | Probability weights profit outcomes; profit includes contribution and fixed cost. |
| Elasticity | yellow/green | Use epsilon to forecast quantity change, then calculate contribution/profit. |
| PapaTurk `2x` | yellow/green | Derive revenue first; marginal revenue is the derivative of revenue. |

## Next Recall Prompts

1. Explain the beer two-part tariff example in 60 seconds using access fee, usage price, marginal cost, marginal WTP, and consumer surplus.
2. Give one example where skimming is better than penetration, and one where penetration is better than skimming.
3. Build a two-price expected-value table and decide using expected profit rather than expected sales.
4. Given `epsilon = -1.5`, `p = 100`, `x = 1,000`, and `c_var = 40`, test a 10% price increase.
5. Starting from `p = 5 - x/3000`, derive `R`, `MR`, revenue-maximizing `x`, and profit-maximizing `x` if `MC = 0.80`.

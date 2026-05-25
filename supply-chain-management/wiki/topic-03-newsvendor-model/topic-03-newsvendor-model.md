# Topic 03: Newsvendor Model

Source files:

- `supply-chain-management/raw/TUM_PL_2026_03_Newsvendor.pdf`
- `supply-chain-management/raw/2. PL- Newsvendor-Exercise-Task.xlsx`
- `supply-chain-management/raw/Newsvendor Model Answer Key.pdf`

Course: Supply Chain Management
Processed: 2026-05-14
Wiki note: `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`

Course logistics checked: the SCM exam includes numerical/open-ended questions and allows a one-page handwritten cheat sheet. The Newsvendor critical fractile formulas and normal/uniform quantile logic are high-priority cheat-sheet candidates.

## 80/20 Exam Summary

The Newsvendor model decides how much to order when demand is uncertain, the order decision must be made before demand is known, and leftover inventory has a cost.

High-yield points:

- The model balances underage cost and overage cost.
- Underage cost is the opportunity cost of ordering one unit too few.
- Overage cost is the cost of ordering one unit too many.
- The optimal service level is the critical fractile:

```text
SL = c_u / (c_u + c_o)
```

- In the simple no-salvage newspaper version:

```text
c_u = p - c
c_o = c
SL = (p - c) / p
```

- The optimal order quantity is the demand quantile:

```text
Q* = F^{-1}(SL)
```

- If demand is normal:

```text
Q* = mu + z(SL) * sigma
```

- Service level is the probability of meeting all demand: `P(D <= Q)`.

## Core Concepts

### Model Purpose

The Newsvendor model translates a forecast distribution into an order quantity.

It applies when:

- demand is uncertain
- ordering happens before demand is known
- there is a cost to leftover inventory
- there is a cost to lost sales or unmet demand
- the decision is effectively single-period or perishable

Examples:

- newspapers
- fresh donuts
- flowers
- fashion items
- seasonal products
- event merchandise

### Fundamental Tradeoff

Ordering one more unit has:

- benefit if demand exceeds the current quantity
- cost if demand is at or below the current quantity

Underage cost:

```text
c_u = marginal loss from ordering one unit too few
```

Overage cost:

```text
c_o = marginal loss from ordering one unit too many
```

Decision intuition:

- high underage cost -> order more -> higher service level
- high overage cost -> order less -> lower service level

### Critical Fractile

General formula:

```text
P(D <= Q*) = c_u / (c_u + c_o)
```

The right side is the optimal service level.

In the basic no-salvage newspaper model:

```text
c_u = p - c
c_o = c
SL = (p - c) / p
```

Where:

- `p`: selling price
- `c`: unit cost
- `D`: demand
- `Q`: order quantity
- `F(Q) = P(D <= Q)`: cumulative distribution

Thus:

```text
Q* = F^{-1}(SL)
```

### Interpreting Service Level

Service level is the probability of meeting all demand.

- `SL = 50%`: order the median demand.
- `SL > 50%`: order above the median because underage is more painful than overage.
- `SL < 50%`: order below the median because overage is more painful than underage.

Exam trap: service level is driven by cost tradeoff, not by the standard deviation. Demand variability affects the order quantity for a given service level, not the service level itself.

## Lecture Examples

### Uniform Demand Example

Demand is uniform and continuous between 2,000 and 5,000:

```text
P(D <= Q) = (Q - 2000) / 3000
```

Costs:

```text
c = 0.50
p = 1.50
```

Service level:

```text
SL = (p - c) / p = (1.50 - 0.50) / 1.50 = 2/3
```

Solve:

```text
(Q - 2000) / 3000 = 2/3
Q - 2000 = 2000
Q* = 4000
```

### Initial Forecast Example

Demand forecast:

```text
mu = 1000
sigma = 50
normal distribution
```

Profit if sold:

```text
c_u = 10
```

Loss if unsold:

```text
c_o = 5
```

Service level:

```text
SL = 10 / (10 + 5) = 2/3
```

Normal quantile:

```text
Q* = F^{-1}(2/3; mu=1000, sigma=50) = 1021.54
```

Lecture rounds down to:

```text
Q* = 1021 units
```

## Exercise Answer Key

### Task 1: Donuts

Given:

- cost `c = 0.50`
- price `p = 2.00`
- zero salvage value

Service level:

```text
SL = (p - c) / p = (2.00 - 0.50) / 2.00 = 0.75 = 75%
```

Answer key:

- probability of meeting all demand: 75%
- order quantity: 9 donuts

Interpretation: order the smallest quantity where cumulative probability reaches the critical fractile.

### Task 2: Flower Vendor

Given:

- cost `c = 16.5`
- price `p = 50`
- mean demand `mu = 2500`
- standard deviation `sigma = 450`
- no salvage value

Service level:

```text
SL = (50 - 16.5) / 50 = 0.67 = 67%
```

Normal quantile:

```text
z(0.67) = 0.4399
Q* = 2500 + 0.4399 * 450 = 2697.96
```

Answer key:

```text
Q* = 2698
```

Effect of standard deviation:

- Service level is independent of the demand distribution's standard deviation.
- If `SL > 50%`, increasing standard deviation increases `Q*`.
- If `SL < 50%`, increasing standard deviation decreases `Q*`.
- If `SL = 50%`, changing standard deviation does not change `Q*` because the median/mean point stays at `mu` for a symmetric normal distribution.

### Task 3: Watches

Given:

- underage cost `c_u = 3495`
- overage cost `c_o = 2840`
- daily demand normal with `mu = 20`, `sigma = 4`

Service level:

```text
SL = 3495 / (3495 + 2840) = 0.5517 = 55.17%
```

Normal quantile:

```text
z(0.5517) = 0.12995
```

Sunday-only quantity:

```text
Q* = 20 + 0.12995 * 4 = 20.52
```

Answer key rounds to:

```text
20 units
```

Monday-Saturday weekly quantity:

```text
mu_week = 6 * 20 = 120
sigma_week = sqrt(6) * 4 = 9.798
Q*_week = 120 + 0.12995 * 9.798 = 121.27
```

Answer key:

```text
121 units
```

Exam note: weekly standard deviation adds by square root of time if daily demands are independent.

## Visual Knowledge Map

```mermaid
flowchart TD
    Forecast[Forecast demand distribution] --> Decision[Choose order quantity before demand is known]
    Decision --> Tradeoff[Balance marginal underage and overage costs]

    Tradeoff --> Underage[Underage cost c_u: ordered too few]
    Tradeoff --> Overage[Overage cost c_o: ordered too many]

    Underage --> Critical[Critical fractile]
    Overage --> Critical
    Critical --> SL[Service level = c_u / (c_u + c_o)]
    SL --> Quantile[Choose demand quantile]
    Quantile --> Q[Q* = F^-1(SL)]

    Q --> Uniform[Uniform demand: solve CDF equation]
    Q --> Normal[Normal demand: Q* = mu + z sigma]

    SL --> Interpretation[Probability of meeting all demand]
    Interpretation --> HighSL[SL > 50%: order above median]
    Interpretation --> LowSL[SL < 50%: order below median]
    Interpretation --> EqualSL[SL = 50%: order median]

    Q --> Outcome[Operational outcome]
    Outcome --> Stockout[Too low: stockout/lost margin]
    Outcome --> Leftover[Too high: leftover disposal/loss]
```

## Subject Knowledge Graph

| Node | Meaning | Exam Relevance |
|---|---|---|
| Newsvendor Model | Single-period order decision under uncertainty | Core model |
| Underage Cost | Cost of ordering one unit too few | Drives service level upward |
| Overage Cost | Cost of ordering one unit too many | Drives service level downward |
| Critical Fractile | `c_u / (c_u + c_o)` | Main formula |
| Service Level | Probability of meeting all demand | Main interpretation |
| Demand Distribution | CDF used to convert service level into quantity | Needed for `Q*` |
| Quantile | Inverse CDF value | Converts SL into order quantity |
| Normal Demand | `Q* = mu + z sigma` | Common calculation format |
| Uniform Demand | Solve linear CDF equation | Common calculation format |

| From | Relationship | To | Why It Matters |
|---|---|---|---|
| Underage Cost | increases | Service Level | Higher lost-margin risk means order more |
| Overage Cost | decreases | Service Level | Higher leftover risk means order less |
| Service Level | determines | Demand Quantile | `Q* = F^-1(SL)` |
| Forecasting | supplies | Demand Distribution | Newsvendor depends on forecast mean/uncertainty |
| Standard Deviation | affects | Order Quantity | More uncertainty moves quantity away from mean depending on SL |
| Service Level | is independent of | Standard Deviation | Cost ratio determines SL |

## Exam Relevance

Likely exam prompts:

- Calculate critical fractile/service level.
- Identify underage and overage costs from a word problem.
- Compute `Q*` for uniform demand.
- Compute `Q*` for normal demand using `mu`, `sigma`, and z-score.
- Explain how standard deviation affects `Q*` depending on whether `SL` is above, below, or equal to 50%.
- Interpret service level as probability of meeting demand.
- Decide whether to round up or down based on context/table answer conventions.

Common traps:

- Confusing service level with forecast accuracy.
- Thinking standard deviation changes service level.
- Using `c_o / (c_u + c_o)` instead of `c_u / (c_u + c_o)`.
- Forgetting salvage value if it appears in a modified problem.
- Using daily standard deviation times 6 instead of `sqrt(6)` for weekly demand.
- Treating `Q*` as mean demand regardless of cost asymmetry.

## Cheat-Sheet Candidates

```text
General Newsvendor:
SL = c_u / (c_u + c_o)
Q* = F^-1(SL)

No salvage, price p, cost c:
c_u = p - c
c_o = c
SL = (p - c) / p

Normal demand:
Q* = mu + z(SL) * sigma

Aggregating independent daily demand:
mu_n = n * mu
sigma_n = sqrt(n) * sigma

Interpretation:
SL > 50% -> Q* above median/mean for symmetric demand.
SL < 50% -> Q* below median/mean.
SL = 50% -> Q* at median/mean for symmetric demand.
```

## Retrieval Prompts

1. What operational problem does the Newsvendor model solve?
2. Define underage cost and overage cost in plain language.
3. What is the critical fractile formula?
4. Why does higher underage cost lead to higher order quantity?
5. How do you get `Q*` from a service level?
6. Why does standard deviation not change the service level?
7. For normal demand, what is the formula for `Q*`?
8. Why is weekly standard deviation `sqrt(6) * daily sigma`, not `6 * daily sigma`?

## Practice Tasks

### Task 1: Critical Fractile

A product costs EUR 4 and sells for EUR 10. Unsold units have zero salvage value. What is the service level?

Short answer guide:

```text
SL = (10 - 4) / 10 = 0.60
```

### Task 2: Normal Demand

Demand is normal with `mu = 500`, `sigma = 80`, and `SL = 0.75`. If `z(0.75) = 0.674`, what is `Q*`?

Short answer guide:

```text
Q* = 500 + 0.674 * 80 = 553.92
```

### Task 3: Standard Deviation Intuition

If `SL > 50%`, what happens to `Q*` when demand standard deviation increases?

Short answer guide:

```text
Q* increases because the chosen quantile is above the mean/median.
```

## Connections

Previous SCM note:

- `topic-02-forecasting/topic-02-forecasting.md`: provides the demand distribution and uncertainty that Newsvendor uses.

Future SCM links:

- Inventory management and safety stock will reuse the service-level and uncertainty logic.
- Capacity and supply planning will reuse the demand-risk tradeoff.

## Weakness Flags

- Pending active-recall session.

## Open Uncertainties

- The answer key rounds the Sunday watch quantity from about 20.52 to 20. In many operational settings one would discuss integer rounding policy. Follow the course answer key unless later materials specify a different convention.


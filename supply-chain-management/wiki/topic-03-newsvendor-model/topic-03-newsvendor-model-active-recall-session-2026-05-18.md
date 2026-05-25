# Active Recall Session: Topic 03 Newsvendor Model

Course: Supply Chain Management
Wiki note: `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`
Context file: `supply-chain-management/wiki/topic-03-newsvendor-model/CONTEXT.md`
Date: 2026-05-18
Session type: `first active-recall pass; overdue repair`

## Session Focus

Build exam-ready recall for the Newsvendor model:

- model purpose and fit conditions
- underage and overage costs
- critical fractile and service level
- discrete CDF quantity selection
- uniform and normal demand quantity calculations
- difference between service level and expected profit

## User Raw Answers

### Prompt 1: Model Setup

User answer:

> 1-determines the probaility of demand to deterime the order quantity
> 2-demand is uncertain, order must be one before demand is known, there is a marginal loss for too much or few ordering in stock
> 3-underage and overage cost
> 4-you can have the ratio of trade-off for over or under demand

Feedback:

- The skeleton was correct, but the model does not determine the probability of demand.
- The demand distribution is estimated before Newsvendor.
- Newsvendor uses that distribution and the cost tradeoff to choose `Q*`.
- `c_u` and `c_o` must be defined as marginal losses, not only named.

Quality: `yellow`

### Prompt 2: Donut Cost Setup

Prompt:

```text
p = 2.00
c = 0.50
salvage value = 0
```

User answer:

> 1-2 eur
> 2-0.50 eur
> 3-3/4
> 4-Service level is around %75 which means keeping the items in stock is more feasible than ordering below the demand forecast

Feedback:

- `c_o = 0.50` and `SL = 0.75` were correct.
- `c_u` was incorrect: it is not the selling price.
- Correct setup:

```text
c_u = p - c = 2.00 - 0.50 = 1.50
c_o = c = 0.50
SL = 1.50 / (1.50 + 0.50) = 0.75
```

Quality: `yellow`

### Prompt 3: Discrete Demand Table

Prompt:

| Q | P(D <= Q) |
|---:|---:|
| 7 | 0.50 |
| 8 | 0.68 |
| 9 | 0.77 |
| 10 | 0.90 |

User answer:

> 1- 9 since its the closest integer quantity value to the service level where it equals to  P(D <= Q) 0.75
> 2-9 is closer than 8 in terms of service level value
> 3- it gets out of the expected service level which is the control limit for the order behviour, it might be costly in long term due to overbuying and continous stock overload

Feedback:

- Correct quantity: `Q = 9`.
- Reasoning needed correction: discrete Newsvendor does not use closest CDF.
- Correct rule:

```text
Choose the smallest Q such that F(Q) >= target service level.
```

Quality: `yellow`

### Prompt 4: Uniform Demand

Prompt:

```text
D ~ Uniform(2000, 5000)
p = 1.50
c = 0.50
salvage value = 0
```

User answer:

> 1- 1 and 0.5
> 2- 1 / 1.5 = 2/3
> 3- 2000 + (2/3 ) *3000 = 4000
> 4- Service level is around  %67 which means the underage cost is more than overage costs and ordering 4000 units satisfies all demand based on the probability. Order units above 4000 are not justified by the cost tradeoff and below 4000 are not justified by sell price tradeoff

Feedback:

- Calculation was correct.
- Interpretation was mostly correct.
- Best phrasing:

```text
Because underage cost is twice the overage cost, the firm targets a 66.7% service level and orders the 66.7th percentile of demand, which is 4,000 units.
```

Quality: `green`

### Prompt 5: Normal Demand

Prompt:

```text
mu = 1000
sigma = 50
c_u = 10
c_o = 5
z(0.667) approximately 0.43
```

User answer:

> 1- 10/15 = 0.667
> 2- above 0?
> 3- 1000 + (0.43 * 50) = 1021.5 -> 1022 units
> 4- because the target service level is above the %50 where the risk is taken more on overbought side rather than underage  cost

Feedback:

- Calculation was correct.
- Rounding logic should be stated if units are indivisible.
- Better wording: accept more overage risk to reduce the more expensive underage risk.

Quality: `green`

### Prompt 6: Concept Check

User answer:

> 1- no, the service level completely relies on cost tradeoff for overage and underage
> 2-increases the quantity unit
> 3- service level is the probability of the order qunatity meets with expected demand, and expected profit is calculated based on the expected demand which correlates with service level in proportional way

Feedback:

- Correct: variability does not change the target service level.
- Correction: higher `sigma` only increases `Q*` when `SL > 50%`; if `SL < 50%`, higher `sigma` can decrease `Q*`.
- Correction: service level and expected profit are different. Service level is `P(D <= Q)`. Expected profit is weighted average profit across all demand outcomes and is not always proportional to service level.

Quality: `yellow`

### Prompt 7: Exam Trap Mini-Test

User answer:

> 1-no, service level is not relevant to demand, it cares cost
> 2-yes
> 3-yes
> 4-yes

Feedback:

- 1 and 2 were correct.
- 3 was false: for discrete demand, choose the smallest `Q` with `F(Q) >= SL`, not the closest CDF.
- 4 was false: Newsvendor uses an already estimated demand distribution; it does not determine the distribution.

Quality: `yellow`

### Final One-Minute Exam Answer

User answer:

> The newsvendor model utilizes the predefined distribution obtained by forecasting and probability modelings to determine optimal order quantity that meeting all demand by utilizing the service level which is calculated based on overage and uderage costs

Refined answer:

```text
The Newsvendor model chooses the optimal order quantity Q* for a single-period decision under uncertain demand. The demand distribution is estimated first through forecasting or probability modeling. The model then compares underage cost c_u, the marginal loss from ordering one unit too few, with overage cost c_o, the marginal loss from ordering one unit too many. Their ratio gives the target service level: SL = c_u / (c_u + c_o). The optimal order quantity is the demand quantile that reaches this service level: Q* = F^-1(SL).
```

Quality: `green/yellow`

## Repaired Mental Models

- Newsvendor does not estimate demand; it uses an estimated demand distribution.
- `c_u` is lost margin or marginal loss from too few units, not the selling price.
- `c_o` is marginal loss from too many units, often `c - salvage value`.
- Service level is cost-driven: `c_u / (c_u + c_o)`.
- Quantity is distribution-driven: `Q* = F^-1(SL)`.
- For discrete demand, choose the smallest `Q` where `F(Q) >= SL`.
- For normal demand, `sigma` affects the distance from the mean through `Q* = mu + z sigma`.
- Expected profit is not the same as service level.

## Weak Spots

| Quality | Weak Spot | Correction |
|---|---|---|
| `yellow` | Model purpose | Say Newsvendor chooses `Q*`; forecasting/probability modeling estimates demand. |
| `yellow` | Underage cost | Use `c_u = p - c` in the no-salvage newspaper/donut setup. |
| `yellow` | Discrete CDF rule | Use smallest `Q` with `F(Q) >= SL`, not closest CDF. |
| `yellow` | Variability effect | Higher `sigma` increases `Q*` only when target service level is above 50%. |
| `yellow` | Service level vs expected profit | Service level is probability of covering demand; expected profit averages profit over all demand outcomes. |

## Next Recall Prompts

1. Define `c_u` and `c_o` for a product with price, cost, and salvage value.
2. Given a discrete CDF table and target service level, choose `Q*` using the smallest-quantity rule.
3. Explain why `sigma` changes `Q*` but not the target service level.
4. Compare service level, fill rate, and expected profit.
5. Write the one-minute Newsvendor exam answer without notes.

## Note References

- Source note: `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`
- Context file: `supply-chain-management/wiki/topic-03-newsvendor-model/CONTEXT.md`
- Related prior note: `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`

# Topic 10 Multi-Period Inventory Management And Order-Up-To Model - Clarification Session 2026-07-03

Source note: [topic-10-multi-period-inventory-management-order-up-to-model.md](topic-10-multi-period-inventory-management-order-up-to-model.md)

Companion context: [CONTEXT.md](CONTEXT.md)

Session type: clarification and wiki refinement

Status: clarification saved; first active recall still pending

## User Request

> I am currently studying topic 10 SCM multi period inventory management and I wanna better clarification to understand the grounding: how it relates with newswendor , random variables and also EOQ-EPQ? it seems closer to newswendor model which is used to calculate one time order uncertainty for extreme cases and we usually rely on EOQ-EPQ for constand demand replenishments but this topic goes over newswendor and makes it periodical replenishment methodology if I am not wrong?

Follow-up questions:

> for in-stock and stockout probability, why the continous demand and discrete demand have different service level convention?

> how about the expected backorders and excpected leftover inventory calculations? they impact the service level or the cumulative porbbility that demand is no larger than service level?

> I wanna see the full calculation of medtronic numerical examples with details

> so all this S values that are found means the inventory remains always at least that quantity and we schedule the ordering based on that value to avoid in-stock or stockout via cost calculations and service level?

> from service level perspective, both newsvendor and the up-to-model refers the same thing?

> so we deine the service level as a desired inventory quantity that is calculated based on expected demand with a given lead time containment

> could you rephrase me again the concepts with analogy for up-to-model and the newsvendor and also the comparison

> but where actually the difference occurs to use up-to-model and EOQ/EPQ?

> give me an example that blends EOQ/EPQ and the up-to-model

> and how do you incorporate newsvendor into this example continuation?

> ah then the up-to-model complements the newsvendor operation in terms of calculation?

## Professor Feedback

- The user's main intuition was directionally correct: Topic 10 is closer to Newsvendor than basic EOQ/EPQ because it uses random demand, service levels, and quantiles.
- The important correction is that the order-up-to model is not simply "Newsvendor repeated every period." It operationalizes Newsvendor-style service-level logic inside a recurring replenishment system with lead time, on-order inventory, and backorders.
- `S` is not a guaranteed minimum physical stock level. It is the target inventory position after placing the period order.
- Service level is not an inventory quantity. Service level is a probability target; `S` is the inventory-position quantity chosen to achieve it.
- Expected backorders and expected leftover inventory are not service levels. They are expected quantities in units, calculated after selecting or testing `S`.
- EOQ/EPQ and order-up-to solve different managerial problems. EOQ/EPQ optimizes economic batch size under stable recurring demand. Order-up-to sets a protection target under uncertain recurring demand and lead time.

## Refined Mental Models

### Model Router

```text
Newsvendor:
one uncertain selling period -> choose Q once
analogy: sandwiches for a one-day festival
```

```text
EOQ/EPQ:
stable recurring demand -> choose economic batch size Q*
analogy: efficient crate size for a warehouse replenishment cycle
```

```text
Order-up-to:
uncertain recurring demand with lead time -> choose target inventory position S
analogy: hospital pharmacy repeatedly restoring its protected system position
```

### Service Level Versus S

```text
Service level = probability target
S = inventory-position quantity that achieves that probability
```

Exam sentence:

```text
The service level is the target probability of not stocking out; the order-up-to level S is the inventory-position quantity chosen from the demand distribution over l+1 periods to achieve that probability.
```

### Inventory Position Versus Inventory Level

```text
Inventory position = on-hand + on-order - backorders
Order quantity = S - inventory position
```

Correct interpretation:

```text
After ordering, the inventory position returns to S.
Physical on-hand inventory may still be below S until orders arrive.
Stockout can still occur with probability 1 - F(S).
```

### Newsvendor Inside Order-Up-To

Newsvendor provides the cost-to-service-level chain:

```text
c_u and c_o -> SL* = c_u/(c_u+c_o) -> demand quantile
```

Order-up-to applies that chain to the protection-period demand distribution:

```text
SL* -> S = F^-1(SL*) for demand over l+1 periods
each period -> order S - inventory position
```

### EOQ/EPQ Blend

EOQ/EPQ can be layered with order-up-to when a manager wants fixed economical batches:

```text
EOQ -> Q*
Order-up-to -> S
Hybrid policy -> order Q* when inventory position reaches s = S - Q*
```

## Medtronic Calculation Refinement

The main note was expanded with full calculation ladders for:

1. Distribution center normal-demand conversion from monthly to weekly demand.
2. Protection-period aggregation over `l+1 = 4` weeks.
3. Normal z-score, in-stock probability, stockout probability, expected backorders, and expected leftover inventory for `S = 625`.
4. Sales representative Poisson demand conversion from monthly to daily demand.
5. Protection-period aggregation over `l+1 = 2` days.
6. Poisson CDF calculation for `S = 3`.
7. Expected backorders and leftover inventory for the sales-representative example.
8. Cost-based service-level calculation for the sales representative and the strict rounding nuance between `S = 3` and `S = 4`.

## Files Updated

- [topic-10-multi-period-inventory-management-order-up-to-model.md](topic-10-multi-period-inventory-management-order-up-to-model.md)
- [CONTEXT.md](CONTEXT.md)
- [topic-10-multi-period-inventory-management-order-up-to-model-clarification-session-2026-07-03.md](topic-10-multi-period-inventory-management-order-up-to-model-clarification-session-2026-07-03.md)
- `learning-system/review-dashboard.md`
- `learning-system/weekly-calendar.md`

## Weak Spots To Revisit

| Weak spot | Quality | Correction rule | Next prompt |
|---|---|---|---|
| Treating `S` as a minimum physical inventory floor | `yellow` | `S` is a target inventory position after ordering, not a guaranteed on-hand minimum. | With `S = 100`, on-hand `40`, on-order `35`, and backorders `0`, compute order quantity and explain why on-hand is not 100. |
| Treating service level as an inventory quantity | `yellow` | Service level is `P(D <= S)`; `S` is the quantity target. | Explain in one sentence the difference between `SL = 95%` and `S = 971 boxes`. |
| Blurring Newsvendor, EOQ/EPQ, and order-up-to | `yellow` | Newsvendor sets service-level logic, EOQ/EPQ sets batch size, order-up-to sets target inventory position. | Route three mini cases: festival sandwiches, stable weekly crate demand, uncertain hospital-stock demand with lead time. |
| Expected backorders versus stockout probability | `yellow` | `1-F(S)` is probability; `B(S)` is expected units short. | For a demand table, compute `F(S)`, `1-F(S)`, `B(S)`, and `I(S)`. |

## Next Recall Prompts

1. Explain the difference between Newsvendor `Q`, EOQ `Q*`, and order-up-to `S`.
2. Give the hospital-pharmacy analogy for order-up-to without looking at the note.
3. Compute inventory position and order quantity from on-hand, on-order, and backorders.
4. Explain why order-up-to uses demand over `l+1` periods.
5. Rebuild the Medtronic sales-representative Poisson CDF for `S = 3`.
6. Rebuild the Medtronic DC normal calculation for `S = 625`.
7. Explain how a hybrid `(s,Q)` policy combines EOQ with order-up-to.

## Schedule Impact

No `First Pass` or `D+n` checkpoint was advanced. This was a clarification and wiki-refinement session while the formal Topic 10 first active-recall session remains pending.

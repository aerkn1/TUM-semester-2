# Topic 10: Multi-Period Inventory Management And The Order-Up-To Model

Source files:

- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/10 Multi-Period Inventory Management/Slides Order-up-to Inventory Model.pdf`
- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/10 Multi-Period Inventory Management/Exercise Order-up-to Inventory Models.xlsx`

Course: Supply Chain Management
Processed: 2026-06-04
Wiki note: `supply-chain-management/wiki/topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md`

Course logistics checked: the SCM exam is closed-book, allows only a non-programmable calculator and one handwritten A4 cheat sheet, and may include numerical open-ended questions. Topic 10 should therefore be practiced as hand calculations: inventory position, lead-time demand, service level, quantile lookup, and expected backorder/inventory interpretation.

## 80/20 Exam Summary

The Newsvendor model chooses one order for one selling period. The order-up-to model handles repeated replenishment with lead time.

Core idea:

```text
Every period, place an order that raises inventory position back to S.
```

The exam-critical chain is:

```text
lead time l -> demand over l+1 periods -> target service level -> S = F^-1(SL)
```

High-yield formulas:

```text
Inventory level = on-hand inventory - backorders
Inventory position = on-order inventory + on-hand inventory - backorders
Order quantity = S - inventory position
End-of-period inventory level = S - demand over l+1 periods
In-stock probability = F(S)
Stockout probability = 1 - F(S)
B(S) = E[max(0, D - S)]
I(S) = E[max(0, S - D)] = S - mu + B(S)
SL* = c_u / (c_u + c_o)
```

For normally distributed lead-time-plus-one-period demand:

```text
z = (S - mu) / sigma
L(z) = phi(z) - z(1 - Phi(z))
B(S) = sigma * L(z)
I(S) = S - mu + B(S)
```

## Where This Fits In SCM

This topic connects three earlier building blocks:

- Demand uncertainty and CDFs from [Topic 04 Random Variables](../topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md).
- The service-level tradeoff from [Topic 03 Newsvendor](../topic-03-newsvendor-model/topic-03-newsvendor-model.md).
- Lead-time and inventory logic from [Topic 05 EOQ/EPQ](../topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md).

Topic 10 changes the operational decision:

```text
Not "How much do I order once?"
But "What inventory position do I restore to every period?"
```

### Model Router: Newsvendor, EOQ/EPQ, And Order-Up-To

Use this router before choosing formulas:

| Situation | Model | Main decision | Demand assumption | Output |
|---|---|---|---|---|
| One uncertain selling event | Newsvendor | How much should I commit once? | Random demand for one selling period | One-time order quantity `Q` |
| Repeated stable replenishment | EOQ/EPQ | How large should each order or production run be? | Constant or predictable demand rate | Economic batch size `Q*` |
| Repeated uncertain replenishment with lead time | Order-up-to | What inventory position should I restore to every period? | Random demand over the protection period | Target inventory position `S` |
| Probability/quantile support | Random variables | How do I translate uncertainty into probabilities and quantiles? | Distribution of demand | `F(S)`, `F^-1(SL)`, expected values |

Analogy:

```text
Newsvendor = buy sandwiches for one festival day.
EOQ/EPQ = decide the efficient crate size for steady warehouse demand.
Order-up-to = a hospital pharmacy checks stock repeatedly and restores its system position to a protective target S.
```

The order-up-to model complements the Newsvendor calculation, but it is not just "Newsvendor repeated." It takes the Newsvendor-style chain:

```text
shortage cost versus leftover cost -> target service level -> demand quantile
```

and turns it into a recurring operating policy:

```text
target service level -> S = quantile of demand over l+1 periods
each period -> order S - inventory position
```

The EOQ/EPQ connection is different. EOQ/EPQ answers how large the replenishment batch should be when demand is stable. Order-up-to answers how much inventory-position protection is needed when demand is uncertain and lead time exposes the system to stockout risk.

Exam sentence:

```text
Newsvendor chooses how much to buy once; EOQ/EPQ chooses the economic batch size; order-up-to chooses the protected inventory-position target S for repeated uncertain replenishment.
```

## Why Newsvendor Is Not Enough

The Newsvendor model is useful for one-shot uncertainty, such as one season of newspapers, fashion, or perishables. It is weak for a replenishment system because it ignores:

- repeated ordering periods
- lead times
- on-order inventory already in the pipeline
- backorders that carry across periods
- the distinction between inventory level and inventory position

In a real supply chain, the manager often orders today while earlier orders are still on the way. That is why the order-up-to model tracks inventory position, not only physical inventory on the shelf.

## Medtronic Pacemaker Case Logic

The slides use Medtronic pacemakers to show why the same product needs different inventory periods at different supply-chain levels.

Inventory locations:

- Manufacturing facilities: finished-goods inventory ignored in the deck.
- Distribution centers: planning period is about one week.
- Sales representatives: planning period is about one day.

Demand modeling examples:

| Level | Planning Period | Demand Approximation | Reason |
|---|---:|---|---|
| Distribution center | 1 week | Normal | Higher aggregate volume, monthly mean and standard deviation converted to weeks. |
| Sales representative | 1 day | Poisson | Low count demand at an individual representative. |

Demand distribution analysis step:

```text
Estimate the demand distribution for the relevant planning period.
Then aggregate demand across l+1 periods, because lead time matters.
```

## Order-Up-To Model Mechanics

Let `S` be the order-up-to level and `l` be order lead time in periods.

Sequence of events in each period:

1. Receive the order placed `l` periods ago.
2. Observe current inventory, backorders, and outstanding orders.
3. Place a new order.
4. Demand occurs during the period.

The policy is a pull system:

```text
Order just enough to replace what demand has pulled out of the system.
```

Because lead time can exceed one period, several orders can be outstanding at the same time.

## Inventory Measures

The model uses two inventory concepts that must not be mixed.

| Measure | Formula | What It Means |
|---|---|---|
| Inventory level | `on-hand inventory - backorders` | What you physically have, net of unmet demand. |
| Inventory position | `on-order inventory + on-hand inventory - backorders` | What the system will have after outstanding orders arrive, before future demand. |
| Period order quantity | `S - inventory position` | Amount needed to restore the inventory position to `S`. |

Operational caveat:

```text
If S - inventory position is negative, the formula says the position is above target. In practice, if returns/cancellations are not possible, the order quantity is usually set to 0.
```

## Why Demand Over `l+1` Periods Matters

At the end of a period:

```text
inventory level = S - demand over l+1 periods
```

Reason:

- Immediately after ordering, inventory position equals `S`.
- Outstanding orders represent demand that has occurred but has not yet been replenished.
- By the time the next usable replenishment catches up, the system is exposed to demand over the current period plus the lead-time periods.

Mental model:

```text
S is the umbrella.
Demand over l+1 periods is the rain you must survive before the system has fully recovered.
```

## In-Stock Probability And Stockout Probability

Let `D` be demand over `l+1` periods.

```text
In-stock probability = P(D <= S) = F(S)
Stockout probability = 1 - F(S)
```

For continuous demand, `< S` and `<= S` give the same probability. For discrete demand, use the course convention from random variables:

```text
service level at stock S = P(D <= S)
```

Exam trap:

```text
F(S) is not the probability that demand equals S. It is the cumulative probability that demand is no larger than S.
```

## Expected Backorders And Expected Leftover Inventory

Let `mu` be expected demand over `l+1` periods.

```text
B(S) = E[max(0, D - S)]
I(S) = E[max(0, S - D)]
```

The useful identity:

```text
I(S) = S - mu + B(S)
```

Interpretation:

- `B(S)` measures expected unmet units at the end of a period.
- `I(S)` measures expected leftover units at the end of a period.
- If you can calculate one, you can calculate the other from the identity.

For normal demand:

```text
z = (S - mu) / sigma
L(z) = phi(z) - z(1 - Phi(z))
B(S) = sigma * L(z)
I(S) = S - mu + B(S)
```

The deck frames expected sales as:

```text
E[sales] = mu - sigma * L(z)
```

So expected lost sales/backorders equal:

```text
mu - E[sales] = sigma * L(z)
```

## Choosing The Optimal Service Level

The service-level formula has the same critical-fractile structure as Newsvendor:

```text
SL* = c_u / (c_u + c_o)
```

In the order-up-to context:

- `c_u` is the underage or stockout cost of one unit short for the relevant period.
- `c_o` is the overage or holding cost of one extra unit for the relevant period.

Sales representative example from the slides:

```text
annual holding cost = 35% of product price
daily holding cost h = 35% / 360 * product price = 0.000972 * product price
stockout cost b = 75% margin * 50% lost margin = 0.375 * product price
SL* = b / (b + h) = 0.375 / (0.375 + 0.000972) = 99.74%
```

The product price cancels out. What matters is the relative cost of a stockout day versus a holding day.

For the distribution center, the deck does not provide a clean stockout cost. It suggests simulation or a rule of thumb, such as targeting around 99%, because the business consequence of a stockout is harder to price.

## Medtronic Numerical Examples

### Distribution Center

The distribution center example uses normal demand because weekly DC demand is aggregated and relatively high-volume.

Facts:

```text
Monthly mean demand = 349 pacemakers
Monthly standard deviation = 122.38 pacemakers
Planning period = 1 week
Lead time l = 3 weeks
l+1 = 4 weeks
```

Step 1: convert monthly mean demand to weekly mean demand.

```text
mean weekly demand = 349 * 12 / 52
                   = 80.54
                   = about 80.6 pacemakers/week
```

Step 2: convert monthly standard deviation to weekly standard deviation.

For standard deviation, scale with the square root of time:

```text
sigma_week = 122.38 * sqrt(12 / 52)
           = 58.81 pacemakers/week
```

Step 3: aggregate demand over the protection period `l+1 = 4` weeks.

```text
mu = 80.6 * 4
   = 322.4 pacemakers
```

```text
sigma = 58.81 * sqrt(4)
      = 58.81 * 2
      = 117.62 pacemakers
```

Demand over the protection period:

```text
D ~ Normal(mu = 322.4, sigma = 117.62)
```

Step 4: evaluate the example order-up-to level.

```text
S = 625
```

Calculate the z-value:

```text
z = (S - mu) / sigma
  = (625 - 322.4) / 117.62
  = 302.6 / 117.62
  = about 2.57
```

Step 5: calculate in-stock probability.

```text
F(S) = Phi(2.57)
     = about 0.994954
     = 99.50%
```

Stockout probability:

```text
1 - F(S) = 1 - 0.994954
         = 0.005046
         = about 0.50%
```

Step 6: calculate expected backorders.

For normal demand:

```text
B(S) = sigma * L(z)
L(z) = phi(z) - z * [1 - Phi(z)]
```

For `z = about 2.57`, the normal loss value is about:

```text
L(z) = 0.001596
```

Therefore:

```text
B(625) = 117.62 * 0.001596
       = 0.1878
       = about 0.19 pacemakers
```

Step 7: calculate expected leftover inventory.

```text
I(S) = S - mu + B(S)
```

Substitute:

```text
I(625) = 625 - 322.4 + 0.1878
       = 302.7878
       = about 302.79 pacemakers
```

Managerial interpretation:

```text
S = 625 almost eliminates backorders at the DC.
Expected backorders are only about 0.19 pacemakers.
But expected leftover inventory is about 302.79 pacemakers, so the service level is bought with a very large inventory buffer.
```

### Sales Representative

The sales representative example uses Poisson demand because an individual representative faces low-count daily demand.

Facts:

```text
Monthly mean demand = 6.25 pacemakers
Assume 5 working days per week
52 weeks per year
12 months per year
Lead time l = 1 day
l+1 = 2 days
```

Step 1: convert monthly demand to daily demand.

```text
mean daily demand = 6.25 * 12 / (52 * 5)
                  = 75 / 260
                  = 0.2885
                  = about 0.29 pacemakers/day
```

Step 2: aggregate demand over `l+1 = 2` days.

For Poisson demand, means add:

```text
lambda = 0.29 * 2
       = 0.58 pacemakers
```

Demand over the protection period:

```text
D ~ Poisson(lambda = 0.58)
```

Step 3: evaluate the example order-up-to level.

```text
S = 3
```

Step 4: calculate the in-stock probability.

```text
F(3) = P(D <= 3)
     = P(0) + P(1) + P(2) + P(3)
```

Poisson probability formula:

```text
P(D = d) = e^(-lambda) * lambda^d / d!
```

Substitute `lambda = 0.58`:

```text
P(0) = e^(-0.58)
     = 0.559898
```

```text
P(1) = e^(-0.58) * 0.58
     = 0.324741
```

```text
P(2) = e^(-0.58) * 0.58^2 / 2
     = 0.094175
```

```text
P(3) = e^(-0.58) * 0.58^3 / 6
     = 0.018207
```

Add:

```text
F(3) = 0.559898 + 0.324741 + 0.094175 + 0.018207
     = 0.997021
     = 99.70%
```

Stockout probability:

```text
1 - F(3) = 1 - 0.997021
         = 0.002979
         = about 0.30%
```

Step 5: calculate expected backorders.

```text
B(3) = E[max(D - 3, 0)]
```

Only demand above 3 creates backorders:

```text
B(3) = 1*P(D=4) + 2*P(D=5) + 3*P(D=6) + ...
```

The slide table gives:

```text
B(3) = 0.003352
     = about 0.0034 pacemakers
```

Step 6: calculate expected leftover inventory.

For Poisson demand:

```text
mu = lambda = 0.58
```

Use:

```text
I(S) = S - mu + B(S)
```

Substitute:

```text
I(3) = 3 - 0.58 + 0.003352
     = 2.423352
     = about 2.42 pacemakers
```

Managerial interpretation:

```text
S = 3 gives about 99.70% in-stock probability.
Expected backorders are almost zero.
Expected leftover inventory is about 2.42 pacemakers.
Because representative-level demand is low, a small S can still produce a very high service level.
```

Cost-based service-level nuance:

```text
annual holding cost = 35% of product price
daily holding cost h = 35% / 360 * p = 0.000972p
stockout cost b = 75% margin * 50% lost margin = 0.375p
```

```text
SL* = b / (b + h)
    = 0.375p / (0.375p + 0.000972p)
    = 0.375 / 0.375972
    = 0.9974
    = 99.74%
```

Exam nuance:

```text
F(3) = 99.7021%
Target SL* = 99.74%
```

So `S = 3` is the slide's example for calculating `F(S)`, `B(S)`, and `I(S)`. If the exam asks for the smallest integer `S` that meets the strict cost-based target, then:

```text
F(3) = 99.7021% < 99.74%
F(4) = 99.9662% >= 99.74%
```

Strict integer target:

```text
S = 4
```

## Applying The Model

Use this decision process:

1. Define the planning period and lead time `l`.
2. Estimate the demand distribution for one period.
3. Convert it into demand over `l+1` periods.
4. Compute the target service level from costs, or choose a managerial rule of thumb.
5. Set `S = F^-1(SL)`.
6. Calculate `B(S)` and `I(S)` to understand operational consequences.
7. Check whether the selected `S` is realistic for storage space, cash, and service expectations.

## Exercise Workbook Answer Guide

The workbook contains templates, not a completed solution sheet. The following guide is computed from the stated task data.

### Task 1: Speed Print Paper

Facts:

```text
Weekly demand ~ Normal(mu = 100, sigma = 65)
Lead time l = 5 weeks
S = 700
On-hand inventory = 523
On-order inventory = 180
Backorder = 0
Target in-stock probability = 99%
```

Part a:

```text
Inventory position = 523 + 180 - 0 = 703
Order quantity = S - inventory position = 700 - 703 = -3
```

Operational answer:

```text
Do not place a new positive order if negative orders are not allowed. The position is already 3 boxes above target.
```

Part b:

```text
l+1 = 6 weeks
mu_period = 100 * 6 = 600
sigma_period = 65 * sqrt(6) = 159.22
z_0.99 = 2.326
S = 600 + 2.326 * 159.22 = 970.39
```

Order-up-to level:

```text
S is about 970.4 boxes; as an integer target, use 971 boxes to meet at least 99%.
```

### Task 2: Printer Demand With Poisson Distribution

Facts:

```text
Weekly demand ~ Poisson(lambda = 25)
Backorder cost = EUR 50 per printer per week
Holding cost = EUR 20 per printer per week
Lead time l = 3 weeks
```

Part a:

```text
SL* = 50 / (50 + 20) = 71.43%
```

Part b:

```text
l+1 = 4 weeks
lambda_period = 25 * 4 = 100
```

Exact Poisson quantile logic:

```text
Choose the smallest integer S with P(D <= S) >= 0.7143.
For Poisson(lambda = 100), S = 106.
```

Normal approximation:

```text
mu = 100
sigma = sqrt(100) = 10
z_0.7143 = 0.566
S = 100 + 0.566 * 10 = 105.66 -> 106
```

### Task 3: Laptop Demand With Normal Distribution

Facts:

```text
Weekly demand ~ Normal(mu = 240, sigma = 90)
Overage cost = EUR 50
Underage cost = EUR 39.98
Lead time l = 2 weeks
Expected lost sales value L(z) = 0.1785
```

Part a:

```text
SL* = 39.98 / (39.98 + 50) = 44.43%
```

Part b:

```text
l+1 = 3 weeks
mu_period = 240 * 3 = 720
sigma_period = 90 * sqrt(3) = 155.88
z_0.4443 = -0.140
S = 720 - 0.140 * 155.88 = 698.17
```

Order-up-to level:

```text
Exact continuous target: about 698.17 laptops.
If an integer level must meet at least the target service level, use 699.
```

Part c:

```text
If S = 698.17, realized service level is 44.43%.
If rounded to S = 698, realized service level is about 44.39%.
If rounded up to S = 699, realized service level is about 44.64%.
```

Part d:

```text
B(S) = sigma * L(z) = 155.88 * 0.1785 = 27.83 laptops
I(S) = S - mu + B(S)
```

Using the exact continuous `S = 698.17`:

```text
I(S) = 698.17 - 720 + 27.83 = about 6.00 laptops
```

## Blending EOQ/EPQ, Newsvendor, And Order-Up-To

In real operations, the three models can be layered, but they answer different questions.

```text
EOQ/EPQ      -> efficient batch size
Newsvendor   -> economically justified service level
Order-up-to  -> inventory-position target S under uncertainty and lead time
```

Constructed hospital-gloves example:

```text
Annual demand D = 52,000 boxes/year
Ordering cost K = EUR 100/order
Annual holding cost h = EUR 2/box/year
Weekly demand ~ Normal(mu = 1,000, sigma = 200)
Lead time l = 1 week
Underage cost c_u = EUR 18/box short
Overage cost c_o = EUR 2/box extra
```

Step 1: EOQ decides the efficient replenishment batch.

```text
Q* = sqrt(2DK / h)
```

Substitute:

```text
Q* = sqrt((2 * 52,000 * 100) / 2)
   = sqrt(5,200,000)
   = 2,280 boxes
```

Interpretation:

```text
Ordering about 2,280 boxes balances fixed ordering cost against holding cost.
EOQ answers batch-size efficiency, not stockout protection.
```

Step 2: Newsvendor logic converts shortage and leftover costs into a service level.

```text
SL* = c_u / (c_u + c_o)
```

Substitute:

```text
SL* = 18 / (18 + 2)
    = 18 / 20
    = 0.90
    = 90%
```

Interpretation:

```text
Because a shortage is much more painful than one extra box, the system targets a 90% in-stock probability.
```

Step 3: Order-up-to converts the service level into the target inventory position `S`.

Protection period:

```text
l + 1 = 1 + 1 = 2 weeks
```

Aggregate demand:

```text
mu = 1,000 * 2
   = 2,000 boxes
```

```text
sigma = 200 * sqrt(2)
      = 282.84 boxes
```

For 90% service level:

```text
z_0.90 = 1.282
```

Order-up-to level:

```text
S = mu + z * sigma
  = 2,000 + 1.282 * 282.84
  = 2,000 + 362.60
  = about 2,363 boxes
```

Interpretation:

```text
To have about 90% probability of not stocking out over the two-week protection period, restore inventory position to about 2,363 boxes.
```

Step 4: combine batch efficiency with service protection.

A pure order-up-to policy would order:

```text
order quantity = S - inventory position
```

If the company wants EOQ-sized batches instead, a practical hybrid is an `(s, Q)` policy:

```text
Order Q* when inventory position falls to reorder point s.
```

Set the reorder point so that one EOQ batch brings the system back to `S`:

```text
s = S - Q*
```

Substitute:

```text
s = 2,363 - 2,280
  = 83 boxes
```

Hybrid policy:

```text
When inventory position falls to about 83 boxes, order 2,280 boxes.
After ordering, inventory position becomes 83 + 2,280 = 2,363 = S.
```

Managerial interpretation:

```text
Newsvendor tells the manager how protected the system should be.
Order-up-to translates that protection into S.
EOQ/EPQ decides the efficient replenishment batch used to restore the position.
```

## Order-Up-To Versus Newsvendor

| Dimension | Newsvendor | Order-Up-To Model |
|---|---|---|
| Time horizon | Single period | Repeated periods |
| Order decision | One-time `Q` | Repeated replenishment to `S` |
| Lead time | Usually absent or simplified | Explicit lead time `l` |
| State variable | Demand distribution and order quantity | Inventory position, on-order inventory, backorders |
| Leftover consequence | Often salvage/markdown/obsolete stock | Inventory carries into future periods |
| Shortage consequence | Lost margin or shortage penalty | Backorders or recurring stockout cost |
| Main exam move | Critical fractile -> quantile | Demand over `l+1` -> service level -> `S` |

## Exam Relevance

Likely exam tasks:

- Compute inventory position and period order quantity.
- Convert weekly/daily/monthly demand to demand over `l+1` periods.
- Compute a target service level from cost data.
- Find `S` using a normal z-score or Poisson CDF/approximation.
- Interpret expected backorders and expected leftover inventory.
- Compare Newsvendor, EOQ/EPQ, and order-up-to assumptions.
- Explain how Newsvendor's critical-fractile logic can feed an order-up-to service level.
- Explain why physical on-hand inventory is not enough when orders are outstanding.

Common mistakes:

- Calling service level an inventory quantity. Service level is a probability; `S` is the quantity target.
- Calling `S` a minimum inventory level. `S` is a target inventory position after ordering; physical on-hand stock can be below `S`.
- Using demand over `l` periods instead of `l+1`.
- Treating inventory level as inventory position.
- Forgetting on-order inventory.
- Treating `F(S)` as `P(D = S)` instead of `P(D <= S)`.
- Using annual holding cost directly in a daily/weekly model.
- Rounding a quantile downward when the target service level must be met.

## Practice Questions

1. A retailer has `S = 120`, 70 units on hand, 60 units on order, and 5 backorders. What is the inventory position and order quantity?
   - Answer guide: inventory position `= 60 + 70 - 5 = 125`; formula order quantity `= 120 - 125 = -5`, so no positive order if negative orders are impossible.

2. Weekly demand is normal with `mu = 40`, `sigma = 12`, and lead time is 2 weeks. What demand distribution should be used for the order-up-to decision?
   - Answer guide: demand over `l+1 = 3` weeks; `mu = 120`, `sigma = 12*sqrt(3) = 20.78`.

3. If holding cost is EUR 2 per unit per week and stockout cost is EUR 18 per unit per week, what service level should the manager target?
   - Answer guide: `SL = 18/(18+2) = 90%`.

4. In one sentence, explain why order-up-to is a pull system.
   - Answer guide: each order replaces demand that has occurred, restoring inventory position to a fixed target.

5. Why can a sales representative need a high service level but only a small `S`?
   - Answer guide: low-volume Poisson demand can make `P(D <= 3)` very high over a short lead-time horizon.

6. Explain how Newsvendor, EOQ, and order-up-to can all appear in one inventory policy.
   - Answer guide: Newsvendor-style costs choose the service level, order-up-to converts it into `S`, and EOQ chooses an economical batch `Q*`; a hybrid `(s,Q)` policy can order `Q*` when inventory position reaches `s = S - Q*`.

## Visual Knowledge Map

```mermaid
flowchart TD
    Decision[Repeated replenishment decision] --> Period[Choose planning period]
    Period --> Lead[Identify lead time l]
    Lead --> Horizon[Demand over l+1 periods]
    Horizon --> Dist[Estimate distribution F]
    Dist --> Costs{Cost data available?}
    Newsvendor[Newsvendor cost logic] --> Costs
    Costs -->|Yes| SL[SL = cu / (cu + co)]
    Costs -->|No| Rule[Managerial service-level rule]
    SL --> Quantile[S = F inverse of SL]
    Rule --> Quantile
    Quantile --> Position[Inventory position]
    Position --> Order[Order quantity = S - inventory position]
    Quantile --> Performance[Performance measures]
    Performance --> InStock[F(S)]
    Performance --> Backorders[B(S)]
    Performance --> Leftover[I(S) = S - mu + B(S)]
    EOQ[EOQ or EPQ batch Q] --> Hybrid[Hybrid s,Q policy]
    Quantile --> Hybrid
    Hybrid --> Reorder[s = S - Q]
```

## Subject Knowledge Graph

| Node | Meaning | Exam Relevance |
|---|---|---|
| Order-Up-To Model | Multi-period replenishment policy that restores inventory position to `S`. | Core Topic 10 model. |
| Order-Up-To Level `S` | Target inventory position after placing the period order. | Main decision variable. |
| Lead Time `l` | Number of periods between placing and receiving an order. | Determines demand exposure horizon. |
| Demand Over `l+1` Periods | Demand the system must cover before replenishment catches up. | Most common setup mistake. |
| Inventory Level | On-hand inventory minus backorders. | Physical/net stock state. |
| Inventory Position | On-order plus on-hand minus backorders. | Correct ordering state. |
| Period Order Quantity | `S - inventory position`. | Direct calculation task. |
| In-Stock Probability | `F(S) = P(D <= S)`. | Service-level interpretation. |
| Expected Backorders `B(S)` | Expected unmet units at period end. | Performance measure. |
| Expected Leftover Inventory `I(S)` | Expected units remaining at period end. | Holding-cost interpretation. |
| Normal Loss Function `L(z)` | `phi(z) - z(1 - Phi(z))`. | Shortcut for expected backorders under normal demand. |
| Cost-Based Service Level | `c_u/(c_u+c_o)`. | Links operational costs to `S`. |
| Newsvendor Logic | Cost-based underage/overage reasoning that can set the target service level. | Explains why Topic 10 uses the same critical-fractile idea. |
| EOQ/EPQ Batch Size `Q*` | Economical replenishment or production-run quantity under stable recurring demand. | Useful contrast and possible hybrid-policy input. |
| Hybrid `(s,Q)` Policy | Fixed-batch policy that orders `Q` when inventory position reaches `s`. | Shows how EOQ batch sizing can be combined with order-up-to protection. |
| Reorder Point `s` | Inventory-position trigger for placing a fixed batch order in a hybrid `(s,Q)` policy. | Optional extension connecting EOQ batch size and order-up-to protection. |

| From | Relationship | To |
|---|---|---|
| Lead Time `l` | expands | Demand Over `l+1` Periods |
| Demand Over `l+1` Periods | is evaluated by | CDF `F(S)` |
| CDF `F(S)` | gives | In-Stock Probability |
| Cost-Based Service Level | determines | Order-Up-To Level `S` |
| Inventory Position | determines | Period Order Quantity |
| Expected Backorders `B(S)` | helps compute | Expected Leftover Inventory `I(S)` |
| Newsvendor Critical Fractile | generalizes to | Cost-Based Service Level |
| EOQ/EPQ Batch Size `Q*` | can combine with | Order-Up-To Level `S` |
| Hybrid `(s,Q)` Policy | uses | Reorder Point `s = S - Q*` |

## Open Uncertainties

- The exercise workbook is a blank solution template. The answer guides above are computed from the task text and standard order-up-to logic, not copied from an official solution sheet.
- For discrete demand, the exact choice of integer `S` depends on whether the exam expects "nearest quantile" or "smallest integer meeting the service level." Use the safer rule: choose the smallest integer with `F(S) >= SL`.

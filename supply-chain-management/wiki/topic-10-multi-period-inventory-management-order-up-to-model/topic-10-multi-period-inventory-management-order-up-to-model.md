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

Facts:

```text
Lead time l = 3 weeks
l+1 = 4 weeks
Mean weekly demand = 80.6
Standard deviation weekly demand = 58.81
Mean demand over 4 periods = 322.4
Standard deviation over 4 periods = 117.62
```

For `S = 625`, the slide table gives:

```text
F(S) = 99.5%
B(625) = 0.19
I(625) = 625 - 322.4 + 0.19 = 302.79
```

Managerial interpretation:

```text
This level almost eliminates backorders, but it also leaves a very large expected inventory buffer at the DC.
```

### Sales Representative

Facts:

```text
Lead time l = 1 day
l+1 = 2 days
Mean demand over 2 days = 0.58
Poisson demand
```

For `S = 3`, the slide table gives:

```text
F(S) = 99.7%
B(3) = 0.0034
I(3) = 3 - 0.58 + 0.0034 = 2.42
```

Managerial interpretation:

```text
Even a stock of 3 pacemakers can be enough for a very high service level when individual-representative demand is low and Poisson-distributed.
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
- Compare Newsvendor and order-up-to assumptions.
- Explain why physical on-hand inventory is not enough when orders are outstanding.

Common mistakes:

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

## Visual Knowledge Map

```mermaid
flowchart TD
    Decision[Repeated replenishment decision] --> Period[Choose planning period]
    Period --> Lead[Identify lead time l]
    Lead --> Horizon[Demand over l+1 periods]
    Horizon --> Dist[Estimate distribution F]
    Dist --> Costs{Cost data available?}
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

| From | Relationship | To |
|---|---|---|
| Lead Time `l` | expands | Demand Over `l+1` Periods |
| Demand Over `l+1` Periods | is evaluated by | CDF `F(S)` |
| CDF `F(S)` | gives | In-Stock Probability |
| Cost-Based Service Level | determines | Order-Up-To Level `S` |
| Inventory Position | determines | Period Order Quantity |
| Expected Backorders `B(S)` | helps compute | Expected Leftover Inventory `I(S)` |
| Newsvendor Critical Fractile | generalizes to | Cost-Based Service Level |

## Open Uncertainties

- The exercise workbook is a blank solution template. The answer guides above are computed from the task text and standard order-up-to logic, not copied from an official solution sheet.
- For discrete demand, the exact choice of integer `S` depends on whether the exam expects "nearest quantile" or "smallest integer meeting the service level." Use the safer rule: choose the smallest integer with `F(S) >= SL`.

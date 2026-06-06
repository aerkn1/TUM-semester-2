# Topic 05: EOQ, Production Systems, And Batching

Source files:

- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/05 Economic Order Quantity Mod___roduction Systems and Batching/Slides EOQ.pdf`
- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/05 Economic Order Quantity Mod___roduction Systems and Batching/Slides Production systems, and Batching.pdf`
- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/05 Economic Order Quantity Mod___roduction Systems and Batching/Exercise EOQ.xlsx`
- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/05 Economic Order Quantity Mod___roduction Systems and Batching/Exercise EPQ.xlsx`
- `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/05 Economic Order Quantity Mod___roduction Systems and Batching/Exercise Answer Key EOQ.pdf`

Course: Supply Chain Management
Processed: 2026-05-14; refreshed with Moodle export on 2026-06-04
Wiki note: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

Course logistics checked: the SCM exam is closed-book except for one handwritten A4 cheat sheet and includes numerical/open-ended tasks. EOQ, finite-horizon EOQ, reorder points, and EPQ formulas are high-priority cheat-sheet candidates.

## 80/20 Exam Summary

Topic 05 is the deterministic inventory and production-lot-size block.

The decision is:

```text
How large should each order or production batch be when demand is known and constant?
```

The core tradeoff:

- larger orders or batches reduce setup/order frequency
- larger orders or batches increase average inventory
- finite production lowers peak inventory because demand continues while production is running

The basic EOQ model applies when replenishment is instantaneous:

```text
Q* = sqrt(2K lambda / h)
TC(Q) = hQ/2 + K lambda/Q
```

The EPQ model applies when the production rate is finite:

```text
Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
Imax = ((p - lambda) / p) * Q
TC(Q) = h Imax/2 + K lambda/Q
```

Where:

- `lambda`: deterministic demand rate, units per year
- `K`: fixed order/setup cost per order or batch
- `h`: holding cost per unit per year
- `Q`: order quantity or batch size
- `p`: production rate, units per year, with `p > lambda`

High-yield extensions:

- initial inventory delays the first order
- deterministic lead time changes when to order, not how much to order
- finite horizon requires an integer number of orders
- production-system choice positions inventory along the customer-order decoupling point
- batching can improve machine efficiency but increases WIP, waiting, and lead-time risk

## Where This Fits In SCM

The earlier SCM topics built the demand side:

- [Topic 02 Forecasting](../topic-02-forecasting/topic-02-forecasting.md): estimate future demand.
- [Topic 04 Random Variables](../topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md): model uncertain demand.
- [Topic 03 Newsvendor](../topic-03-newsvendor-model/topic-03-newsvendor-model.md): choose a single-period order quantity under uncertainty.

Topic 05 switches to deterministic planning:

```text
Forecasting/random variables/Newsvendor = demand uncertainty.
EOQ/EPQ = known, constant demand and recurring replenishment.
```

Do not use EOQ to solve a stockout-risk or service-level problem. Use it when the fact pattern gives constant demand, setup/order cost, and holding cost.

## Model Selection Router

| Fact Pattern | Use | Decision Output |
|---|---|---|
| Known constant demand, instant replenishment, repeated orders | Basic EOQ | `Q*`, order frequency, total annual cost |
| Known constant demand, current inventory exists | EOQ with initial inventory | `Q*`, first-order timing |
| Known constant demand, positive lead time | EOQ with reorder point | `Q*`, reorder point `lambda l` |
| Known constant demand, finite selling season | Finite-horizon EOQ | integer number of orders `m*`, order quantity `t lambda / m*` |
| Known constant demand, finite production rate | EPQ | batch size `Q*`, maximum inventory, run duration |
| Unknown or random demand | Forecasting, random variables, Newsvendor | forecast, distribution, service level, quantile |

## Basic EOQ Model

### Assumptions

The lecture's basic deterministic inventory model assumes:

- no initial inventory
- no order lead time
- infinite planning horizon
- one product
- deterministic and constant demand rate
- shortages are not permitted
- costs include fixed setup/order cost and holding cost

These assumptions are exam triggers. If the case changes one of them, the formula may need an extension.

### Inventory Pattern

EOQ inventory is a sawtooth:

1. Order `Q` units.
2. Inventory jumps to `Q`.
3. Inventory decreases at slope `-lambda`.
4. The next order arrives exactly when inventory reaches zero.

Core quantities:

```text
Average inventory = Q/2
Cycle length T = Q/lambda
Orders per year N = lambda/Q
```

### Cost Function And Optimum

Holding cost per year:

```text
H(Q) = hQ/2
```

Setup/order cost per year:

```text
k(Q) = K lambda/Q
```

Total annual cost:

```text
TC(Q) = hQ/2 + K lambda/Q
```

Optimal order quantity:

```text
Q* = sqrt(2K lambda / h)
```

Cost at optimum:

```text
TC(Q*) = sqrt(2hK lambda)
```

At the EOQ optimum:

```text
annual holding cost = annual setup/order cost
```

That equality is a useful calculation check.

### Managerial Interpretation

- Higher `K`: each order is expensive, so order less often and in larger quantities.
- Higher `lambda`: demand is larger, so the optimal lot size rises.
- Higher `h`: inventory is expensive, so order smaller quantities.
- Lead time alone does not change `Q*` under deterministic demand and no shortages.

## EOQ Extensions

### Positive Initial Inventory

If current inventory is `I0 > 0`, do not order immediately.

Without lead time, wait:

```text
I0 / lambda
```

Then order `Q*` and continue the normal EOQ cycle.

With lead time `l`, place the order early enough that it arrives when inventory reaches zero.

### Positive Order Lead Time

If it takes lead time `l` for an order to arrive, reorder when inventory reaches:

```text
reorder point = lambda l
```

Interpretation:

```text
During lead time l, deterministic demand consumes lambda*l units.
```

Under the lecture assumptions, lead time changes the reorder point but not `Q*`.

### Finite Planning Horizon

Finite-horizon EOQ applies to seasonal or limited-horizon products where the horizon is `[0, t]`, no starting inventory exists, and no leftover inventory remains at `t`.

For a fixed number of orders `m`, equally spaced intervals minimize holding cost:

```text
T1 = T2 = ... = Tm = t/m
```

Average cost per unit time:

```text
TC(m) = K m/t + h lambda t/(2m)
```

Continuous minimizer:

```text
m_hat = t * sqrt(h lambda / (2K))
```

But `m` must be an integer. Therefore:

```text
m* is floor(m_hat) or ceil(m_hat)
Q* = t lambda / m*
```

Exam procedure:

1. Compute `m_hat`.
2. Check `floor(m_hat)` and `ceil(m_hat)` in `TC(m)`.
3. Choose the lower-cost integer.
4. Compute the per-order quantity `Q* = t lambda / m*`.

Common trap: do not place `2.72` orders. The finite-horizon decision needs an integer order count.

## Production Systems

The production-systems slides position inventory relative to the customer-order decoupling point.

| System | Inventory Position | Customer Lead Time | Inventory Investment | Managerial Meaning |
|---|---|---:|---:|---|
| Make-to-stock | Finished goods exist before the customer order | low | high | Fast delivery, but inventory risk is high. |
| Assemble-to-order | Components/modules are stocked, final assembly waits for order | medium-low | medium | Good for variety with manageable delivery time. |
| Make-to-order | Production starts after order | medium-high | low | Lower finished-goods inventory, longer customer wait. |
| Engineer-to-order | Design and production start after order | high | lowest finished-goods stock | Custom projects; long lead time and high coordination needs. |

The visual logic is:

```text
Engineer-to-order -> high customer lead time, low inventory investment
Make-to-stock -> low customer lead time, high inventory investment
```

### Push Versus Pull

The customer-order decoupling point separates:

- push activity: planned from forecasts before the customer order
- pull activity: triggered by a real customer order

This connects directly to Topic 06: if upstream firms see only distorted orders, the push side can amplify demand signals.

### Batch-And-Queue Logic

Batch-and-queue tries to maximize efficiency through:

- more products per setup
- fewer setups
- specialization
- clear work-center structures

In a job-shop/work-center layout, similar machines are grouped into departments. Batches move between departments, creating setups between different batches and inventory between work centers.

Managerial tradeoff:

```text
larger batches -> fewer setups and higher local machine efficiency
larger batches -> more WIP, waiting, lead time, and coordination risk
```

This is not automatically "better operations." It can make a machine look efficient while the whole system becomes slower.

## Economic Production Quantity Model

EPQ extends EOQ to finite production rate.

Assumptions:

- one product
- deterministic and constant demand
- shortages are not permitted
- no order lead time
- setup and holding costs matter
- production rate `p` is finite and greater than `lambda`

### Inventory Pattern

During production:

```text
inventory builds at slope p - lambda
```

After production stops:

```text
inventory falls at slope -lambda
```

Production-run duration:

```text
T0 = Q/p
```

Maximum inventory:

```text
Imax = (p - lambda) T0 = ((p - lambda)/p) Q
```

Average inventory:

```text
Imax/2
```

### EPQ Cost And Optimum

Total annual cost:

```text
TC(Q) = h * ((p - lambda)/p) * Q/2 + K lambda/Q
```

Optimal production batch:

```text
Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
```

Production-run duration at optimum:

```text
T0* = Q*/p
```

Extreme cases:

- If `p -> infinity`, EPQ becomes EOQ because replenishment is effectively instantaneous.
- If `p -> lambda`, inventory builds very slowly and the formula pushes `Q*` upward.

Exam trap: EPQ is usually larger than EOQ, but maximum inventory is lower than the batch size because demand consumes units during production.

## Exercise Answer Guides

### EOQ Task 1: ABI Warehouses

Facts:

- two warehouses
- each has demand `50` units/year
- `h = EUR 20` per unit/year
- `K = EUR 50` per order

Per warehouse:

```text
Q* = sqrt(2*50*50/20) = 15.81
TC per warehouse = EUR 316.23
```

Two warehouses:

```text
TC company = EUR 632.46
```

Pooled demand:

```text
lambda = 100
Q* = 22.36
TC pooled = EUR 447.21
savings = EUR 185.24 = 29.29%
```

Interpretation: pooling reduces total safety/order-system duplication in this deterministic cost setup because setup/holding tradeoffs are optimized over aggregated demand.

### EOQ Task 2: Tek Pak Beer Crates

Facts:

- `h = EUR 0.65` per crate/year
- `K = EUR 25`
- `lambda = 130` crates/year
- initial inventory `I0 = 100`
- lead time `l = 2` weeks
- assume 52 weeks/year

Answer key:

```text
Q* = 100 crates
reorder point = 5 crates
first order should be placed after 38 weeks
```

Reasoning:

```text
demand per week = 130/52 = 2.5
lead-time demand = 2.5*2 = 5
inventory reaches 5 after (100 - 5)/2.5 = 38 weeks
```

### EOQ Task 3: Kerosene Infinite Versus Finite Horizon

Facts:

- `K = EUR 10`
- `h = EUR 2`
- `lambda = 8000` gallons/year
- finite selling season: 5 weeks

Infinite horizon:

```text
Q* = 282.84 gallons
orders/year = 28.28
orders in 5 weeks = 2.72
```

Finite horizon:

```text
m* = 3 orders
Q* = 256.41 gallons per order
```

Answer key interpretation:

```text
The finite-period average total cost is 0.48% larger because the integer order count rounds away from the continuous optimum.
```

### EPQ Task 1: Battery-Cell Line

Facts:

- `lambda = 12000` packs/year
- `p = 60000` packs/year
- `K = EUR 500`
- `h = EUR 4`

Computed from lecture EPQ formulas:

```text
EPQ Q* = 1936.49 packs
production-run duration = 1.68 weeks
maximum inventory = 1549.19 packs
EPQ total annual cost = EUR 6196.77
instantaneous EOQ total annual cost = EUR 6928.20
EPQ cost reduction = EUR 731.43, about 10.56%
```

Interpretation: finite production lowers average inventory because units are consumed during the production run.

### EPQ Task 2: Router Make-To-Stock Factory

Facts:

- `lambda = 10400` units/year
- `p = 52000` units/year
- `K = EUR 750`
- `h = EUR 6`
- initial inventory `I0 = 1300`
- preparation lead time `l = 2` weeks
- demand per week `= 200`

Computed from lecture EPQ formulas:

```text
EPQ Q* = 1802.78 units
start preparation inventory level = 400 units
start preparation after 4.5 weeks
actual first production starts after 6.5 weeks
maximum inventory = 1442.22 units
cycle time = 9.01 weeks
production-run duration = 1.80 weeks
non-production duration = 7.21 weeks
```

Interpretation: start preparation when the remaining inventory equals demand during the two-week preparation lead time.

### EPQ Task 3: Shovel Factory And Technology Adoption

Facts:

- production rate `p = 200` units/week
- maximum inventory `Imax = 150`
- current economic production quantity `Q* = 300`
- assume 52 weeks/year

Demand implied by the EPQ maximum-inventory formula:

```text
Imax = ((p - lambda)/p) Q
150 = ((200 - lambda)/200) * 300
lambda = 100 units/week = 5200 units/year
```

New technology:

- production rate increases by 50%: `p = 300` units/week = `15600` units/year
- same demand: `lambda = 5200` units/year
- `K = EUR 350`
- `h = EUR 5`
- previous total cost: `EUR 6000`

Computed from lecture EPQ formulas:

```text
new EPQ Q* = 1044.99 units
new maximum inventory = 696.66 units
new total annual cost = EUR 3483.29
maximum willingness to invest = EUR 2516.71
```

Interpretation: willingness to invest equals avoided annual cost if the decision threshold allows zero incremental value.

## Diagrams, Tables, And Visuals

### EOQ Sawtooth

The EOQ diagram is a sawtooth with peak `Q`, slope `-lambda`, and average inventory `Q/2`. It teaches why holding cost grows with `Q` and setup cost falls with `Q`.

### Finite-Horizon Diagram

The finite-horizon diagram shows separate triangles for each order interval. Equal interval lengths minimize holding cost for a fixed number of orders, but the number of orders must be rounded to an integer.

### Production-System Positioning

The production-system diagram maps customer lead time against inventory investment. Moving from make-to-stock toward engineer-to-order reduces finished-goods inventory but increases customer waiting time and customization complexity.

### EPQ Inventory Triangle

The EPQ diagram has two slopes:

```text
production phase: p - lambda
depletion phase: -lambda
```

This is the visual reason EPQ uses `Imax`, not `Q`, as the inventory peak.

## Visual Knowledge Map

```mermaid
flowchart TD
    Start[Deterministic recurring demand] --> CostTradeoff[Setup or order cost vs holding cost]
    CostTradeoff --> Instant{Replenishment instant?}
    Instant -->|Yes| EOQ[Basic EOQ]
    EOQ --> EOQQ[Q* = sqrt(2K lambda / h)]
    EOQ --> Lead{Lead time exists?}
    Lead -->|Yes| ROP[Reorder point = lambda l]
    EOQ --> Initial{Initial inventory exists?}
    Initial -->|Yes| Wait[Wait I0/lambda, adjusted for lead time]
    EOQ --> Horizon{Finite horizon?}
    Horizon -->|Yes| IntegerOrders[Compute m_hat, check floor and ceil]
    IntegerOrders --> FiniteQ[Q* = t lambda / m*]
    Instant -->|No| EPQ[EPQ finite production rate]
    EPQ --> Build[Inventory builds at p - lambda]
    EPQ --> EPQQ[Q* = EOQ * sqrt(p/(p-lambda))]
    EPQ --> Imax[Imax = ((p-lambda)/p)Q]
    CostTradeoff --> ProductionSystems[Production-system choice]
    ProductionSystems --> MTS[Make-to-stock]
    ProductionSystems --> ATO[Assemble-to-order]
    ProductionSystems --> MTO[Make-to-order]
    ProductionSystems --> ETO[Engineer-to-order]
    ProductionSystems --> BatchQueue[Batch-and-queue tradeoff]
```

## Subject Knowledge Graph

| Node | Meaning | Exam Relevance |
|---|---|---|
| Deterministic Demand | Known, constant demand rate `lambda` | Trigger for EOQ/EPQ instead of Newsvendor. |
| Setup/Order Cost | Fixed cost `K` per order or production batch | Drives larger optimal quantities when it rises. |
| Holding Cost | Cost `h` per unit per year | Drives smaller optimal quantities when it rises. |
| EOQ | Order size minimizing setup plus holding cost with instant replenishment | Core formula and calculation topic. |
| Reorder Point | Inventory level `lambda l` for ordering under deterministic lead time | Separates order timing from order quantity. |
| Finite-Horizon EOQ | EOQ variant with integer number of orders in a fixed horizon | Exam trap: round `m`, not `Q` first. |
| Customer-Order Decoupling Point | Boundary between forecast-driven and order-driven activity | Explains make-to-stock through engineer-to-order. |
| Batch-And-Queue | Large batches moving between work centers | Links efficiency to WIP and lead-time cost. |
| EPQ | EOQ extension with finite production rate | Uses `Imax`, production-run duration, and `p > lambda`. |
| Maximum Inventory | EPQ peak inventory `((p-lambda)/p)Q` | Prevents confusing batch size with inventory peak. |

| From | Relationship | To | Why It Matters |
|---|---|---|---|
| Deterministic Demand | enables | EOQ | The model assumes known constant demand. |
| Setup/Order Cost | decreases as Q rises | Order Frequency Cost | Larger orders reduce setup frequency. |
| Holding Cost | increases as Q rises | Inventory Carrying Cost | Larger orders raise average inventory. |
| EOQ | balances | Setup/Order Cost and Holding Cost | This balance creates the square-root formula. |
| Lead Time | determines | Reorder Point | Lead time changes timing, not `Q*`, under deterministic assumptions. |
| Finite-Horizon EOQ | requires | Integer Orders | The continuous optimum must be rounded and checked. |
| Production Rate | constrains | EPQ | Finite production changes inventory buildup. |
| EPQ | uses | Maximum Inventory | Holding cost is based on `Imax/2`, not `Q/2`. |
| Batch-And-Queue | reduces | Setup Frequency | Local efficiency benefit. |
| Batch-And-Queue | increases | WIP and Waiting | System-level cost. |

## Real Business Examples

- A pharmacy replenishing a stable medication SKU can use EOQ if demand is predictable and stockouts are not allowed.
- A warehouse with current inventory and a two-week supplier lead time should use the reorder point to avoid ordering too late.
- A seasonal kerosene seller should use finite-horizon EOQ because it cannot place a fractional number of orders before the season ends.
- A router factory with finite production capacity should use EPQ, because inventory builds while production and demand happen simultaneously.
- A furniture company moving from make-to-stock to make-to-order lowers finished-goods inventory but customers wait longer.

## Exam Relevance

Likely prompts:

- Compute EOQ, order frequency, total annual cost, and interpretation.
- Add initial inventory or deterministic lead time and compute first-order timing or reorder point.
- Compare finite-horizon and infinite-horizon EOQ.
- Compute EPQ, maximum inventory, production-run duration, and non-production time.
- Explain make-to-stock, assemble-to-order, make-to-order, and engineer-to-order in terms of inventory and customer lead time.
- Explain why batch-and-queue can improve local efficiency while harming flow.

Common traps:

- Using EOQ when demand is uncertain and the decision is single-period.
- Forgetting that `lambda` and `h` must use the same time unit.
- Treating lead time as a reason to change `Q*` under deterministic EOQ.
- Using `Q/2` as average inventory in EPQ instead of `Imax/2`.
- Allowing fractional finite-horizon order counts.
- Calling make-to-order "zero inventory"; it may still have raw-material or WIP inventory.

High-scoring answer structure:

1. State the operational decision.
2. Identify whether demand is deterministic or uncertain.
3. Choose EOQ, finite-horizon EOQ, EPQ, or a production-system concept.
4. Define variables and units before substitution.
5. Compute the quantity/timing/cost.
6. Interpret what the decision changes operationally.

## Retrieval Prompts

Closed-book questions:

1. What assumptions must hold before basic EOQ is appropriate?
2. Why does EOQ use `Q/2` as average inventory?
3. Why does deterministic lead time change reorder timing but not `Q*`?
4. Why does finite-horizon EOQ require checking `floor(m_hat)` and `ceil(m_hat)`?
5. Why is EPQ's maximum inventory lower than the production batch size?
6. What is the operational difference between make-to-stock and make-to-order?

Application prompts:

1. A supplier has stable demand, fixed order cost, holding cost, and a two-week lead time. What model and what outputs are needed?
2. A factory produces faster than demand but not instantaneously. Which formula changes relative to EOQ?
3. A seasonal product has a five-week selling window. Why can the finite-horizon cost be higher than infinite-horizon EOQ?
4. A manager wants larger batches to improve machine utilization. What system-level risk should you mention?

## Practice Tasks

1. Compute EOQ for `lambda = 9600` units/year, `K = 80`, `h = 6`. Then compute orders per year and average inventory.
2. With the same facts and lead time of three weeks, compute the reorder point. Assume 52 weeks/year.
3. A finite season lasts 10 weeks. Compute `m_hat`, test floor/ceil, and state why integer rounding matters.
4. For EPQ with `lambda = 12000`, `p = 60000`, `K = 500`, `h = 4`, compute `Q*`, `Imax`, and production-run duration.
5. Explain when a firm should prefer assemble-to-order over make-to-stock.

## Connections

Previous notes from this lecture:

- [Topic 01 Kristen Cookie Case](../topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md): process flow, capacity, bottleneck, and cycle-time logic.
- [Topic 02 Forecasting](../topic-02-forecasting/topic-02-forecasting.md): deterministic planning depends on demand estimates.
- [Topic 03 Newsvendor Model](../topic-03-newsvendor-model/topic-03-newsvendor-model.md): contrast uncertainty-driven service level with EOQ's deterministic cost tradeoff.
- [Topic 04 Random Variables](../topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md): distributions are needed before using stochastic inventory models.

Next related topic:

- [Topic 06 Supply Chain Coordination And Bullwhip Effect](../topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md): batching and distorted order signals can amplify upstream variability.

Cross-course links:

- Finance: cost minimization and investment in new technology should be interpreted as a cash-flow improvement, not only a lower formula result.
- Organization: production-system choice is also an organizational coordination design problem.

## Open Uncertainties

- The EPQ workbook did not include a separate answer-key PDF. The answer guides above are computed directly from the lecture formulas and workbook task wording.
- The production-system slides use visual examples for make-to-stock through engineer-to-order; the exact pictured products are less important than the inventory-positioning logic.

## Weakness Flags

- Pending active recall: the user has not yet completed a first-pass retrieval session for this topic.
- Highest-risk formulas: finite-horizon `m_hat`, EPQ `Imax`, and lead-time first-order timing.

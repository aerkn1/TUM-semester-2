# Topic 05: EOQ, Production Systems, And Batching

Source files:

- `supply-chain-management/raw/TUM_PL_2026_05_EOQ.pdf`
- `supply-chain-management/raw/3. PL- EOQ-Exercise-Task.xlsx`
- `supply-chain-management/raw/TUM_PL_2026_05_production systems, batching.pdf`

Course: Supply Chain Management
Processed: 2026-05-14
Wiki note: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

Course logistics checked: the SCM exam allows a one-page handwritten cheat sheet and includes numerical/open-ended tasks. EOQ/EPQ formulas, reorder point logic, and finite-horizon integer order logic are high-priority cheat-sheet candidates.

## 80/20 Exam Summary

EOQ answers a deterministic inventory question:

```text
How large should each order be when demand is constant and known?
```

The core tradeoff:

- larger orders reduce setup/order frequency
- larger orders increase average inventory and holding cost

Basic EOQ formula:

```text
Q* = sqrt(2K lambda / h)
```

Where:

- `lambda`: demand rate, units/year
- `K`: setup/order cost per order
- `h`: holding cost per unit per year
- `Q`: order quantity

Total annual cost:

```text
TC(Q) = h Q/2 + K lambda/Q
```

At EOQ:

```text
annual holding cost = annual setup/order cost
TC(Q*) = sqrt(2 h K lambda)
```

Main extensions:

- initial inventory: wait `I0 / lambda` before starting the EOQ cycle
- positive lead time: reorder when inventory reaches `lambda * l`
- finite horizon: choose an integer number of orders `m`
- production batching/EPQ: production is finite, so inventory builds while production and demand happen simultaneously

EPQ formula:

```text
Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
```

Where `p` is production rate and must be greater than demand rate `lambda`.

## Where This Fits In SCM

Previous topics handled uncertainty:

- Forecasting estimates future demand.
- Random variables model demand uncertainty.
- Newsvendor decides single-period order quantity under uncertainty.

EOQ is different:

```text
EOQ assumes deterministic, constant, known demand.
```

It is not about stockout risk. It is about minimizing the cost tradeoff between ordering/setup cost and holding cost.

Related notes:

- `supply-chain-management/wiki/topic-02-forecasting/topic-02-forecasting.md`
- `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`
- `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`

## Basic EOQ Model

### Assumptions

The basic EOQ model assumes:

- no initial inventory
- no order lead time
- infinite planning horizon
- one product
- deterministic and constant demand rate
- shortages are not permitted
- costs include setup/order cost and holding cost

These assumptions are restrictive. Exam questions often ask what changes when one assumption is relaxed.

### Inventory Pattern

Inventory follows a sawtooth pattern:

1. Order `Q` units.
2. Inventory jumps to `Q`.
3. Inventory decreases at constant slope `-lambda`.
4. When inventory reaches zero, the next order arrives.

Average inventory:

```text
Q / 2
```

Cycle length:

```text
T = Q / lambda
```

Number of orders per year:

```text
N = lambda / Q
```

### Cost Function

Holding cost per year:

```text
H(Q) = h * Q/2
```

Setup/order cost per year:

```text
k(Q) = K * lambda/Q
```

Total annual cost:

```text
TC(Q) = h Q/2 + K lambda/Q
```

### Optimal Order Quantity

Minimize total annual cost:

```text
Q* = sqrt(2K lambda / h)
```

Economic interpretation:

- If `K` increases, order less often but in larger quantities.
- If `lambda` increases, order quantity increases.
- If `h` increases, order smaller quantities to avoid holding inventory.

At the optimum:

```text
h Q*/2 = K lambda/Q*
```

This equality is useful for checking calculations.

## EOQ Extensions

### Positive Initial Inventory

If initial inventory is `I0 > 0`, do not order immediately.

Time until inventory reaches zero:

```text
I0 / lambda
```

Then order `Q*` and continue the EOQ cycle.

If lead time also exists, place the first order earlier so it arrives when inventory hits zero.

### Positive Order Lead Time

If order lead time is `l`, place the order when inventory reaches:

```text
reorder point = lambda * l
```

Interpretation:

```text
During lead time l, demand consumes lambda*l units. Ordering at that inventory level makes the delivery arrive exactly when inventory reaches zero.
```

Important: under deterministic demand and no shortages, lead time changes when you order, not how much you order.

```text
Q* is unchanged.
```

### Finite Planning Horizon

The infinite-horizon EOQ assumes a continuing cycle. Seasonal products may have a finite horizon `[0, t]`.

Assumptions in the lecture:

- finite horizon length `t`
- total of `m >= 1` orders
- no initial inventory
- no leftover inventory at time `t`
- deterministic demand rate `lambda`

If `m` orders are placed, equally spaced order intervals minimize holding cost:

```text
T1 = T2 = ... = Tm = t/m
```

Average cost per unit time for `m` orders:

```text
TC(m) = K m/t + h lambda t/(2m)
```

Continuous minimizer:

```text
m_hat = t * sqrt(h lambda / (2K))
```

But the number of orders must be an integer. Therefore:

```text
m* is either floor(m_hat) or ceil(m_hat)
```

Decision rule:

1. Compute `m_hat`.
2. Evaluate `TC(m)` at `floor(m_hat)` and `ceil(m_hat)`.
3. Choose the lower-cost integer.
4. Order quantity in the finite horizon:

```text
Q* = t lambda / m*
```

Common trap:

```text
Do not place 2.72 orders. You must choose an integer number of orders.
```

## Production Systems And Batching

The production systems deck connects inventory decisions to how products are made and where inventory is positioned.

### Production System Types

| System | Main logic | Inventory position | Customer lead time |
|---|---|---|---|
| Make-to-stock | Produce before customer order | Finished goods inventory | Short |
| Assemble-to-order | Keep components, assemble after order | Component inventory | Medium |
| Make-to-order | Produce after customer order | Little finished goods inventory | Longer |
| Engineer-to-order | Design/engineer after order | Minimal prebuilt inventory | Longest |

Managerial tradeoff:

```text
More inventory investment usually reduces customer lead time.
Less inventory investment usually increases customer lead time.
```

### Push Vs Pull

Push production:

```text
Production starts based on forecast or plan before customer order is known.
```

Pull production:

```text
Production starts or moves based on actual customer/order signal.
```

The customer order decoupling point separates forecast-driven stages from order-driven stages.

### Batch-And-Queue Philosophy

Batch-and-queue aims for efficiency through:

- larger batches
- fewer setups
- specialization
- clear department structures

Typical job-shop logic:

```text
Similar machines are grouped into departments -> products move in batches -> setups occur between batches -> inventory and waiting accumulate.
```

Benefit:

```text
Fewer setups and high local utilization.
```

Cost:

```text
More work-in-process inventory, longer lead times, and slower response.
```

This is why batching links directly to EOQ/EPQ: larger batches save setup cost but increase inventory and waiting.

## Economic Production Quantity Model

EOQ assumes inventory arrives instantly. EPQ relaxes this: production happens at finite rate `p` while demand simultaneously consumes units at rate `lambda`.

Assumptions:

- deterministic constant demand
- one product
- shortages not permitted
- no order lead time
- setup cost and holding cost
- finite production rate `p`
- `p > lambda`

### Inventory Dynamics

During production:

```text
inventory builds at rate p - lambda
```

After production stops:

```text
inventory decreases at rate -lambda
```

If a batch size is `Q`, production run duration is:

```text
T0 = Q / p
```

Maximum inventory is lower than `Q` because demand consumes during production:

```text
I_max = ((p - lambda) / p) * Q
```

Average inventory:

```text
I_max / 2 = ((p - lambda) / p) * Q/2
```

### EPQ Cost Function

```text
TC(Q) = h * ((p - lambda) / p) * Q/2 + K lambda/Q
```

Optimal production batch size:

```text
Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
```

Equivalent form:

```text
Q* = sqrt((2K lambda p) / (h(p - lambda)))
```

Production run duration:

```text
T0* = Q* / p
```

### EPQ Intuition

Compared with EOQ, EPQ batch size is larger because inventory does not all arrive at once. While production is happening, demand already consumes some units, so average inventory is lower for the same batch size.

Extreme cases from the lecture:

```text
p -> infinity: EPQ becomes EOQ
p -> lambda: Q* -> infinity
```

Interpretation:

- If production is extremely fast, it behaves like instant replenishment.
- If production rate barely exceeds demand rate, inventory accumulates very slowly; large batches become attractive in the formula, but this is also a warning sign that capacity is tight.

## Worked Exercise Answers

### Exercise Task 1: ABI GmbH Warehouse Pooling

Given for each warehouse:

```text
lambda = 50 units/year
h = 20 euros/unit/year
K = 50 euros/order
```

#### a. Annual Logistics Costs With Two Warehouses

EOQ per warehouse:

```text
Q* = sqrt(2K lambda / h)
   = sqrt(2 * 50 * 50 / 20)
   = sqrt(250)
   = 15.81
```

Total logistics cost per warehouse:

```text
TC = hQ/2 + K lambda/Q
   = 20 * 15.81/2 + 50 * 50/15.81
   = 158.11 + 158.11
   = 316.23
```

Two warehouses:

```text
TC_company = 2 * 316.23 = 632.46
```

#### b. Pooling Demand Into One Warehouse

Pooled demand:

```text
lambda_pooled = 100 units/year
```

EOQ pooled:

```text
Q*_pooled = sqrt(2 * 50 * 100 / 20)
          = sqrt(500)
          = 22.36
```

Pooled cost:

```text
TC_pooled = 20 * 22.36/2 + 50 * 100/22.36
          = 223.61 + 223.61
          = 447.21
```

Savings:

```text
Savings = 632.46 - 447.21 = 185.24
Savings % = 185.24 / 632.46 = 29.3%
```

Managerial interpretation:

```text
Pooling reduces total logistics cost because setup and holding tradeoffs scale sublinearly with demand under EOQ.
```

### Exercise Task 2: Tek Pak Beer Crates

Given:

```text
h = 0.65 euros/crate/year
K = 25 euros/order
lambda = 130 crates/year
I0 = 100 crates
lead time = 2 weeks
52 weeks/year
```

#### a. EOQ

```text
Q* = sqrt(2 * 25 * 130 / 0.65)
   = sqrt(10000)
   = 100 crates
```

#### b. Inventory Level To Place New Orders

Weekly demand:

```text
lambda_week = 130 / 52 = 2.5 crates/week
```

Reorder point:

```text
lambda_week * lead time = 2.5 * 2 = 5 crates
```

#### c. When To Place The First Order

Without lead time, inventory lasts:

```text
I0 / lambda_week = 100 / 2.5 = 40 weeks
```

Because lead time is 2 weeks, place the order:

```text
40 - 2 = 38 weeks from now
```

### Exercise Task 3: Kerosene Oil Infinite Vs Finite Horizon

Given:

```text
K = 10 euros/order
h = 2 euros/gallon/year
lambda = 8000 gallons/year
```

#### a. Infinite Planning Horizon

EOQ:

```text
Q* = sqrt(2 * 10 * 8000 / 2)
   = sqrt(80000)
   = 282.84 gallons
```

Orders per year:

```text
N = lambda / Q* = 8000 / 282.84 = 28.28 orders/year
```

Expected orders in 5 weeks:

```text
N_5weeks = 28.28 * 5/52 = 2.72 orders
```

This is an average under the infinite-horizon model, not an allowed finite-horizon integer order count.

#### b. Finite 5-Week Selling Season

Horizon:

```text
t = 5/52 years = 0.09615
```

Continuous optimal number of orders:

```text
m_hat = t * sqrt(h lambda / (2K))
      = 5/52 * sqrt(2 * 8000 / (2 * 10))
      = 2.72
```

Integer candidates:

```text
floor(m_hat) = 2
ceil(m_hat) = 3
```

Finite-horizon cost function:

```text
TC(m) = K m/t + h lambda t/(2m)
```

Check `m = 2`:

```text
TC(2) = 10*2/(5/52) + 2*8000*(5/52)/(2*2)
      = 208.00 + 384.62
      = 592.62
```

Check `m = 3`:

```text
TC(3) = 10*3/(5/52) + 2*8000*(5/52)/(2*3)
      = 312.00 + 256.41
      = 568.41
```

Choose:

```text
m* = 3 orders
```

Finite-horizon order quantity:

```text
Q*_finite = lambda * t / m*
          = 8000 * (5/52) / 3
          = 256.41 gallons
```

#### c. Cost Comparison

Infinite-horizon annualized cost:

```text
TC_infinite = K N + h Q*/2
            = 10 * 28.28 + 2 * 282.84/2
            = 282.84 + 282.84
            = 565.69
```

Finite-horizon annualized cost:

```text
TC_finite = 568.41
```

Difference:

```text
568.41 - 565.69 = 2.72
```

Percent difference:

```text
2.72 / 565.69 = 0.48%
```

Interpretation:

```text
The finite-horizon solution is slightly more expensive because the best continuous number of orders is 2.72, but the real system must choose an integer number of orders. Rounding creates a small inefficiency.
```

## Mermaid Visual Map

```mermaid
flowchart TD
    EOQ[EOQ problem] --> Tradeoff[Order/setup cost vs holding cost]
    Tradeoff --> Setup[Setup/order cost K lambda/Q]
    Tradeoff --> Holding[Holding cost hQ/2]
    Setup --> TC[TC(Q) = hQ/2 + K lambda/Q]
    Holding --> TC
    TC --> EOQFormula[Q* = sqrt(2K lambda / h)]
    EOQFormula --> OrderCycle[Cycle length T = Q/lambda]
    EOQFormula --> Orders[N = lambda/Q]

    EOQ --> Assumptions[Deterministic constant demand]
    Assumptions --> InitialInventory[Initial inventory I0]
    InitialInventory --> Wait[Wait I0/lambda]
    Assumptions --> LeadTime[Positive lead time l]
    LeadTime --> ReorderPoint[Reorder point = lambda*l]
    Assumptions --> FiniteHorizon[Finite horizon t]
    FiniteHorizon --> IntegerOrders[m* = floor or ceil m_hat]
    IntegerOrders --> FiniteQ[Q = t lambda / m*]

    EOQ --> ProductionSystems[Production systems]
    ProductionSystems --> MTS[Make-to-stock]
    ProductionSystems --> ATO[Assemble-to-order]
    ProductionSystems --> MTO[Make-to-order]
    ProductionSystems --> ETO[Engineer-to-order]
    ProductionSystems --> BatchQueue[Batch-and-queue]
    BatchQueue --> Setups[Fewer setups]
    BatchQueue --> WIP[More WIP and waiting]

    BatchQueue --> EPQ[EPQ finite production rate]
    EPQ --> BuildRate[Inventory builds at p-lambda]
    EPQ --> MaxInv[Imax = (p-lambda)/p * Q]
    MaxInv --> EPQCost[TC = h((p-lambda)/p)Q/2 + K lambda/Q]
    EPQCost --> EPQFormula[Q* = sqrt(2Klambda/h) * sqrt(p/(p-lambda))]
```

## Subject Knowledge Graph

### Nodes

| Node | Meaning |
|---|---|
| EOQ | Deterministic order quantity model |
| Demand Rate `lambda` | Constant known demand per year |
| Setup Cost `K` | Fixed cost per order/setup |
| Holding Cost `h` | Annual cost of holding one unit |
| Order Quantity `Q` | Units ordered per cycle |
| Average Inventory | `Q/2` in basic EOQ |
| Total Cost | Holding plus setup/order cost |
| Reorder Point | Inventory level for placing order under lead time |
| Initial Inventory | Starting stock before EOQ cycle begins |
| Finite Horizon | Inventory problem with limited selling period |
| Integer Orders `m` | Number of orders in finite horizon |
| Production System | How production is triggered and inventory positioned |
| Batch-And-Queue | Efficiency philosophy using large batches and departments |
| EPQ | EOQ extension with finite production rate |
| Production Rate `p` | Units produced per time period |
| Maximum Inventory `Imax` | Peak inventory in EPQ |

### Edges

| From | Relationship | To |
|---|---|---|
| EOQ | minimizes | Total Cost |
| Total Cost | combines | Holding Cost |
| Total Cost | combines | Setup Cost |
| Larger Order Quantity | decreases | Setup Cost per year |
| Larger Order Quantity | increases | Holding Cost |
| EOQ Formula | balances | Holding and setup costs |
| Positive Lead Time | changes | Reorder Point |
| Positive Lead Time | does not change | EOQ quantity under deterministic demand |
| Initial Inventory | delays | First order |
| Finite Horizon | requires | Integer order count |
| Batch-And-Queue | reduces | Setup frequency |
| Batch-And-Queue | increases | WIP and waiting |
| EPQ | extends | EOQ |
| Finite Production Rate | reduces | Maximum inventory vs instant replenishment |
| Production Rate approaching infinity | makes EPQ become | EOQ |

## Exam Relevance

Likely question types:

- Compute EOQ from `K`, `h`, and `lambda`.
- Compute total annual cost at EOQ.
- Compute number of annual orders and cycle time.
- Calculate reorder point with deterministic lead time.
- Handle initial inventory and first-order timing.
- Compare decentralized vs pooled inventory cost.
- Solve finite-horizon integer order problems.
- Explain why finite horizon can cost more than infinite-horizon EOQ.
- Explain production system types and the inventory/customer lead-time tradeoff.
- Calculate EPQ or interpret how finite production changes average inventory.

Common mistakes:

- Mixing annual and weekly demand units.
- Forgetting to convert lead time into years or demand into weekly units.
- Using `Q/2` average inventory in EPQ instead of `((p-lambda)/p)Q/2`.
- Treating `m_hat` as feasible when it is not an integer.
- Forgetting that lead time changes reorder point, not EOQ quantity, under deterministic demand.
- Confusing Newsvendor uncertainty with EOQ deterministic demand.

## Cheat-Sheet Candidates

```text
EOQ TC(Q) = hQ/2 + K lambda/Q
EOQ Q* = sqrt(2K lambda / h)
At EOQ: hQ*/2 = K lambda/Q*
TC(Q*) = sqrt(2hKlambda)
Orders/year: N = lambda/Q
Cycle time: T = Q/lambda
Initial inventory wait: I0/lambda
Reorder point with lead time: lambda*l
Finite horizon: TC(m) = Km/t + h lambda t/(2m)
Finite horizon: m_hat = t*sqrt(hlambda/(2K))
Finite horizon: m* = floor(m_hat) or ceil(m_hat), whichever has lower TC
Finite horizon quantity: Q = t lambda/m*
EPQ: Imax = ((p-lambda)/p)Q
EPQ TC(Q) = h((p-lambda)/p)Q/2 + K lambda/Q
EPQ Q* = sqrt(2Klambda/h) * sqrt(p/(p-lambda))
Production run time: T0 = Q/p
```

## Practice Questions

1. Why does EOQ increase when setup cost `K` increases?
2. A product has `lambda = 1000`, `K = 40`, `h = 5`. Compute EOQ.
3. If lead time is 3 weeks and weekly demand is 20 units, what is the reorder point?
4. Why does finite-horizon EOQ require checking `floor(m_hat)` and `ceil(m_hat)`?
5. In EPQ, why is average inventory lower than in EOQ for the same batch size `Q`?
6. Explain the tradeoff between make-to-stock and engineer-to-order.

## Short Answer Guide

1. Higher setup cost makes frequent ordering expensive, so larger orders reduce setup frequency.
2. `Q* = sqrt(2*40*1000/5) = sqrt(16000) = 126.49`.
3. `20*3 = 60 units`.
4. The optimal continuous number of orders may be fractional, but actual orders must be integer.
5. Demand consumes units while production is still running, so maximum inventory is only `((p-lambda)/p)Q`.
6. Make-to-stock uses more inventory to give short customer lead time; engineer-to-order uses little prebuilt inventory but creates long customer lead time.

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

Interactive companion: [EOQ and EPQ interactive tutorial](eoq-epq-interactive-tutorial.html) - editable versions of all six exercise workflows plus the saved free-practice case.

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

## Clarification Bridge: From Forecast Uncertainty To EOQ

EOQ is a continuation of inventory decision-making, but it is not the next calculation in the Newsvendor formula chain. Forecasting and Random Variables first describe the demand environment; then the decision pattern determines the inventory model.

```text
Forecasting estimates demand
        |
Random Variables describe uncertainty
        |
Model router
        |-- one-time uncertain commitment --> Newsvendor
        `-- repeated replenishment with stable demand --> EOQ
```

### Why The Cost Trade-Off Changes

Newsvendor asks how much to commit once before uncertain demand is realized. Excess units may become obsolete, discounted, or wasted, so the model balances underage and overage costs through a service-level quantile.

EOQ assumes recurring demand. Units ordered today can normally satisfy later demand, so excess stock is not automatically lost. The operating problem is instead:

```text
Large Q -> fewer orders -> lower setup cost -> higher holding cost
Small Q -> more orders -> higher setup cost -> lower holding cost
```

Basic EOQ therefore has no service-level target. When recurring demand is uncertain, use EOQ for the replenishment quantity and add a reorder point plus safety stock for timing and protection. An emergency order does not automatically create a Newsvendor problem; Newsvendor returns only when the event creates a separate one-time uncertain commitment.

### Constant Demand Is A Planning Assumption

The demand rate `lambda` is fixed only within the current decision horizon. It may originate from a forecast and should be revised when persistent forecast errors, control-limit violations, trend, seasonality, or structural change make the old estimate unreliable.

```text
Actual demand -> forecast-error monitoring -> model refit
-> updated lambda -> recalculated EOQ
```

One unusual observation should normally trigger investigation, not an automatic model replacement. Persistent instability can require shorter planning windows, safety stock, or a model beyond basic EOQ.

## EOQ Variant Analogies And Use Cases

Use one bakery consuming flour at a known constant rate:

### Basic EOQ: Supplier Delivery

The bakery buys flour from an outside mill. Each order creates one administrative and transport event: the purchasing employee contacts the supplier, a truck is scheduled, the delivery is received, and the invoice is processed. This is the real asset represented by setup or ordering cost `K`.

Once the truck arrives, the full quantity `Q` enters the flour storeroom immediately. Bakers then withdraw flour at the stable demand rate `lambda`. The stock level therefore falls from `Q` to zero as a straight line. The average amount physically occupying the storeroom is `Q/2`.

The bakery uses EOQ to choose the recurring truckload size. A larger truckload means fewer delivery events but more flour tied up in storage; a smaller truckload means less stored flour but more frequent ordering and receiving work.

### Initial Inventory: Flour Already In Storage

Suppose the bakery starts the planning period with `I0` kilograms of flour already on its shelves. This stock is a real asset available for bread production; it is not a new delivery and does not create a new ordering cost.

The bakers consume the opening stock at rate `lambda`. If replenishment is instantaneous, the first order is needed after `I0/lambda` time units. The existing flour changes the date of the first purchase, but it does not normally change the economical size `Q*` of every later delivery.

Managerial meaning: do not place a fresh order merely because the EOQ has been calculated. First ask how long the stock already owned can support operations.

### Positive Lead Time: Supplier Travel Time

Suppose the flour mill needs `l` weeks to prepare and transport a delivery. The bakery cannot wait until the storeroom is empty before ordering. It must trigger the order while enough flour remains to cover all baking during the supplier's travel time.

The reorder point is `r = lambda l`. Here, `r` is kilograms of flour physically left on the shelf when the purchasing employee sends the order. During the next `l` weeks, the bakery consumes those `r` kilograms. The truck should arrive exactly when inventory reaches zero.

Deterministic lead time changes **when** the bakery orders, not the recurring quantity `Q*`. Uncertain demand or uncertain delivery would require protection such as safety stock, which basic EOQ does not provide.

### Initial Inventory Plus Lead Time: First-Order Timing

Now combine both facts: flour is already in storage and the supplier needs time to deliver. If the bakery has `I0` kilograms, it reaches the reorder point after `(I0 - r)/lambda`, equivalently `I0/lambda - l`.

For example, if opening flour lasts four weeks and supplier travel takes two weeks, the bakery waits two weeks, places the order, consumes the remaining two weeks of flour, and receives the delivery at depletion. The first-order clock and the delivery clock are different operational events.

Exam correction rule: `I0/lambda` is the time until stockout, not automatically the time to place the order. Subtract the lead time.

### Finite Horizon: Temporary Bakery Event

Suppose the bakery operates a ten-week festival stall and closes afterward. Total flour demand is known, but the bakery cannot make `2.7` deliveries. A truck either arrives or it does not, so the number of orders `m` must be a feasible integer.

The continuous value `m_hat` identifies the neighborhood of the optimum. Management compares `floor(m_hat)` and `ceil(m_hat)`, chooses the lower-cost integer, and divides total event demand `t lambda` equally across those deliveries. Equal deliveries prevent one interval from carrying unnecessarily more flour than another.

This variant answers a temporary planning question: how many real deliveries should serve the event, and how much flour should each truck bring?

### EPQ: Flour Produced While Baking Continues

Suppose the bakery mills flour internally instead of receiving an instantaneous truckload. The mill produces at rate `p`, while the ovens continue consuming flour at rate `lambda`. During milling, flour inventory rises only at the net rate `p - lambda` because some newly produced flour goes directly into baking.

If a milling run produces batch `Q`, the storeroom never contains all `Q` kilograms at once. Its maximum is `Imax = Q(1 - lambda/p)`, and average inventory is `Imax/2`. When milling stops, baking continues, so the stored flour falls at rate `lambda` until the next run.

The setup cost `K` is now the physical and administrative effort of preparing the mill: cleaning, calibration, changeover, labor, and startup loss. EPQ selects a production batch that balances those run setups against the cost of storing flour.

### Bakery Flow Comparison

| Variant | Asset entering inventory | Asset leaving inventory | Trigger or timing decision | Quantity decision |
|---|---|---|---|---|
| Basic EOQ | Full supplier truckload arrives instantly | Flour used for baking at `lambda` | Reorder at depletion under zero lead time | Recurring delivery size `Q*` |
| Initial inventory | Opening flour already owned | Flour used for baking | First order after existing flour is consumed | Later deliveries still use `Q*` |
| Positive lead time | Supplier delivery after `l` | Flour used during supplier travel | Order when `lambda l` remains | Lead time normally leaves `Q*` unchanged |
| Initial inventory plus lead time | Opening flour, then supplier delivery | Flour used continuously | First order at `I0/lambda - l` | Recurring delivery size `Q*` |
| Finite horizon | Integer number of event deliveries | Flour used before event closes | Choose feasible delivery count `m*` | `Q = t lambda/m*` per delivery |
| EPQ | Flour output produced gradually at `p` | Flour consumed simultaneously at `lambda` | Start each milling setup before depletion | Production batch `Q*`; peak stock `Imax < Q*` |

Memory hook: EOQ is a truckload appearing in inventory at once and then being consumed; EPQ is a tap filling a tank while an open drain continues removing material.

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

#### Operating Story

ABI stocks the same maintenance component in two regional warehouses. Each warehouse serves its own local technicians and issues 50 physical components per year. Every replenishment creates a fixed purchasing and inbound-receiving event costing EUR 50, regardless of whether the truck carries 10 or 30 components. Every component left on a shelf ties up space and capital worth EUR 20 per year.

Management is comparing two operating designs: each warehouse orders independently, or one pooled location orders for the combined demand. Pooling does not reduce total customer usage; it removes one duplicated replenishment stream.

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `lambda = 50` | components withdrawn by technicians from each warehouse per year |
| `K = EUR 50` | one purchase-order, transport, receiving, and invoice-processing event |
| `h = EUR 20` | annual cost of keeping one component on a warehouse shelf |
| `Q` | components delivered in one replenishment shipment |
| `Q/2` | average physical shelf inventory under the sawtooth cycle |

#### Full Operational Workflow

1. A warehouse receives `Q` components and its stock jumps upward immediately.
2. Technicians withdraw components at the stable rate of 50 per year until stock reaches zero.
3. The warehouse repeats the order and incurs another EUR 50 ordering event.
4. Under separate operation, this entire cycle and its fixed cost occur independently at both sites.
5. Under pooling, one site serves 100 units of annual demand and places larger but less duplicated orders.

Facts:

- two warehouses
- each has demand `50` units/year
- `h = EUR 20` per unit/year
- `K = EUR 50` per order

Per warehouse:

```text
Q* = sqrt(2K lambda / h)
   = sqrt((2 * 50 * 50) / 20)
   = 15.81 units/order

Annual holding cost = hQ*/2
                    = 20 * 15.8114 / 2
                    = EUR 158.11/year

Annual ordering cost = K lambda/Q*
                     = 50 * 50 / 15.8114
                     = EUR 158.11/year

TC per warehouse = hQ*/2 + K lambda/Q*
                 = 158.1139 + 158.1139
                 = EUR 316.23/year
```

Two warehouses:

```text
TC company = 2 * TC per warehouse
           = 2 * 316.2278
           = EUR 632.46/year
```

Pooled demand:

```text
lambda_pooled = 50 + 50
              = 100 units/year

Q*_pooled = sqrt(2K lambda_pooled / h)
          = sqrt((2 * 50 * 100) / 20)
          = 22.36 units/order

TC_pooled = hQ*_pooled/2 + K lambda_pooled/Q*_pooled
          = 20 * 22.3607 / 2 + 50 * 100 / 22.3607
          = 223.6068 + 223.6068
          = EUR 447.21/year

Annual savings = TC_separate - TC_pooled
               = 632.4555 - 447.2136
               = EUR 185.24/year

Percentage savings = Annual savings / TC_separate * 100
                   = 185.2419 / 632.4555 * 100
                   = 29.29%
```

#### Physical Interpretation

Separate operation keeps about `15.81/2 = 7.91` components on average at each location, or about 15.81 components across the company. Pooling keeps about `22.36/2 = 11.18` components on average in one system. The firm still supplies 100 components per year, but it carries less average stock and processes fewer duplicated replenishment cycles.

#### Managerial Decision

Centralizing the deterministic inventory saves EUR 185.24 per year, or 29.29% of the modeled relevant cost. ABI should pool only if that saving is not outweighed by extra outbound transport, slower technician access, service risk, or other costs excluded from the EOQ comparison.

#### Exam Trap

Do not double the individual EOQ and call it the pooled EOQ. Pool demand first and recalculate because EOQ grows with the square root of demand. Also do not claim pooling automatically improves service; this calculation proves only the modeled ordering-and-holding saving.

### EOQ Task 2: Tek Pak Beer Crates

#### Operating Story

Tek Pak supplies reusable beer crates from a storage yard. The yard begins with 100 crates. Customers collect 2.5 crates per week, and a supplier needs two weeks to deliver after Tek Pak places an order. Each order creates EUR 25 of fixed purchasing and delivery work, while each crate stored for a year costs EUR 0.65.

The operating question has two parts: how many crates should arrive in each recurring shipment, and when must the first order be released so the initial 100 crates cover demand until the truck arrives?

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `I0 = 100` | reusable beer crates physically in the yard today |
| `lambda = 130/year` | crates collected by customers, equal to 2.5 per week |
| `K = EUR 25` | one supplier-order and inbound-delivery event |
| `h = EUR 0.65` | annual storage cost for one crate |
| `l = 2 weeks` | supplier preparation and transport time |
| `r` | crates that must remain when the order is sent |
| `Q` | crates arriving on each delivery truck |

#### Full Operational Workflow

1. Tek Pak starts with 100 crates and releases 2.5 crates to customers each week.
2. The economical recurring shipment is 100 crates.
3. A two-week delivery delay consumes `2.5 * 2 = 5` crates, so the order trigger is five crates.
4. Stock falls from 100 to five over 38 weeks; Tek Pak then sends the purchase order.
5. During the two-week lead time, customers collect the final five crates.
6. The truck carrying 100 crates arrives when stock reaches zero, starting the recurring EOQ cycle.

Facts:

- `h = EUR 0.65` per crate/year
- `K = EUR 25`
- `lambda = 130` crates/year
- initial inventory `I0 = 100`
- lead time `l = 2` weeks
- assume 52 weeks/year

Worked calculation:

```text
Q* = sqrt(2K lambda / h)
   = sqrt((2 * 25 * 130) / 0.65)
   = 100 crates/order

demand per week = lambda/52
                = 130/52
                = 2.5 crates/week

reorder point r = demand per week * lead time
                = 2.5 * 2
                = 5 crates

first-order placement time = (I0 - r) / demand per week
                           = (100 - 5) / 2.5
                           = 38 weeks
```

#### Physical Interpretation

`Q* = 100` is the size of a physical inbound crate shipment. `r = 5` is not extra safety stock; it is exactly the deterministic quantity customers use while the supplier is travelling. The initial inventory lasts 40 weeks in total, but the order must be placed at week 38.

#### Managerial Decision

Tek Pak should order 100 crates per replenishment and release the first order after 38 weeks, assuming demand and the two-week lead time are reliable. If either varies, the five-crate trigger needs a separate safety-stock decision.

#### Exam Trap

Do not place the order after `I0/lambda = 40` weeks. That is the stockout date. Subtract the two-week lead time, or equivalently order when five crates remain. Lead time changes the timing trigger, not the EOQ quantity in this deterministic model.

### EOQ Task 3: Kerosene Infinite Versus Finite Horizon

#### Operating Story

A temporary heating-fuel seller operates for only five weeks and expects customers to draw kerosene at a known annualized rate of 8,000 gallons. Each tanker delivery costs EUR 10 to arrange, and storing one gallon for a year costs EUR 2. Unlike a permanent depot, this seller must finish the season without planning fractional deliveries beyond the closing date.

The infinite-horizon EOQ gives a useful benchmark, but the real seasonal decision is the whole number of tanker visits during the five-week window.

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `lambda = 8000 gallons/year` | customer withdrawals expressed as an annual rate |
| `t = 5/52 year` | the five-week period in which the temporary seller operates |
| `K = EUR 10` | dispatching and receiving one tanker delivery |
| `h = EUR 2` | annual cost of storing one gallon |
| `m` | whole tanker deliveries during the season |
| `Q` | gallons unloaded by each tanker |

#### Full Operational Workflow

1. The five-week season requires total fuel of `t lambda = 769.23` gallons.
2. The perpetual EOQ benchmark suggests 282.84 gallons per delivery and 2.72 delivery cycles during the season.
3. A real dispatcher cannot book 2.72 tanker visits, so management tests two and three visits.
4. With two visits, each load is larger and more fuel waits in storage; with three, storage falls but another EUR 10 delivery setup is incurred.
5. Three equal tanker loads minimize the feasible seasonal cost, so each carries 256.41 gallons.

Facts:

- `K = EUR 10`
- `h = EUR 2`
- `lambda = 8000` gallons/year
- finite selling season: 5 weeks

Infinite horizon:

```text
Q* = sqrt(2K lambda / h)
   = sqrt((2 * 10 * 8000) / 2)
   = 282.84 gallons/order

orders per year N = lambda/Q*
                  = 8000/282.84
                  = 28.28 orders/year

selling horizon t = 5/52
                  = 0.096154 years

continuous orders in horizon = N * t
                             = 28.28 * 5/52
                             = 2.72 orders

TC_infinite = sqrt(2hK lambda)
            = sqrt(2 * 2 * 10 * 8000)
            = EUR 565.69/year
```

Finite horizon:

```text
m_hat = t * sqrt(h lambda / (2K))
      = (5/52) * sqrt((2 * 8000) / (2 * 10))
      = 2.72 orders

TC(m = 2) = Km/t + h lambda t/(2m)
          = 10 * 2/(5/52) + 2 * 8000 * (5/52)/(2 * 2)
          = 208.00 + 384.62
          = EUR 592.62/year

TC(m = 3) = Km/t + h lambda t/(2m)
          = 10 * 3/(5/52) + 2 * 8000 * (5/52)/(2 * 3)
          = 312.00 + 256.41
          = EUR 568.41/year

m* = 3 orders because TC(3) < TC(2)

Q*_finite = t lambda/m*
          = (5/52) * 8000 / 3
          = 256.41 gallons/order
```

Answer key interpretation:

```text
Finite-horizon cost increase = (TC_finite - TC_infinite) / TC_infinite * 100
                             = (568.41 - 565.69) / 565.69 * 100
                             = 0.48%
```

#### Physical Interpretation

The continuous solution's `2.72` is a mathematical location between two feasible schedules, not a deliverable operating plan. Three tankers divide the 769.23 seasonal gallons into equal 256.41-gallon loads. The feasible annualized relevant cost is slightly above the smooth infinite-horizon benchmark because delivery count is indivisible.

#### Managerial Decision

Schedule three deliveries for the five-week season. The 0.48% increase is the operational cost of respecting an integer number of tanker visits rather than pretending the continuous optimum can be executed.

#### Exam Trap

Do not round `m_hat = 2.72` automatically without evaluating both neighboring integers. Compare `TC(floor(m_hat))` and `TC(ceil(m_hat))`. Also keep units consistent: the five-week horizon must be converted to years because `lambda` and `h` are annual.

### EPQ Task 1: Battery-Cell Line

#### Operating Story

A factory makes battery packs on an internal production line and ships them continuously to assembly customers. The line can produce 60,000 packs per year, while customers consume 12,000 per year. Starting a production run costs EUR 500 for cleaning, tooling, calibration, labor preparation, and startup loss. A finished pack held for a year costs EUR 4.

This is EPQ rather than EOQ because a batch does not appear in the warehouse instantaneously. Packs enter storage gradually while customers keep removing packs during the same production run.

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `p = 60000/year` | battery packs completed by the production line per year while running |
| `lambda = 12000/year` | finished packs shipped to customers per year |
| `K = EUR 500` | one physical line setup and startup event |
| `h = EUR 4` | annual holding cost for one finished battery pack |
| `Q` | total packs manufactured during one production run |
| `Imax` | highest number of finished packs simultaneously in storage |

#### Full Operational Workflow

1. The line is set up, creating one EUR 500 setup event.
2. During the run, the line produces faster than customers withdraw: inventory builds at `60000 - 12000 = 48000` packs per year.
3. The line runs for 1.68 weeks and makes 1,936.49 packs in total.
4. Customers remove packs during those 1.68 weeks, so only 1,549.19 packs accumulate at the peak.
5. Production stops, but customer shipments continue at 12,000 packs per year until stock reaches zero.
6. The factory then starts the next setup and repeats the cycle.

Facts:

- `lambda = 12000` packs/year
- `p = 60000` packs/year
- `K = EUR 500`
- `h = EUR 4`

Computed from lecture EPQ formulas:

```text
EPQ Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
       = sqrt((2 * 500 * 12000) / 4) * sqrt(60000 / (60000 - 12000))
       = 1936.49 packs/batch

production-run duration T0* = Q*/p
                            = 1936.49/60000 years
                            = 1936.49/60000 * 52
                            = 1.68 weeks

maximum inventory Imax = ((p - lambda)/p) * Q*
                       = ((60000 - 12000)/60000) * 1936.49
                       = 1549.19 packs

EPQ annual holding cost = hImax/2
                        = 4 * 1549.19 / 2
                        = EUR 3098.39/year

EPQ annual setup cost = K lambda/Q*
                      = 500 * 12000 / 1936.49
                      = EUR 3098.39/year

TC_EPQ = hImax/2 + K lambda/Q*
       = 3098.3867 + 3098.3867
       = EUR 6196.77/year

TC_EOQ = sqrt(2hK lambda)
       = sqrt(2 * 4 * 500 * 12000)
       = EUR 6928.20/year

EPQ cost reduction = TC_EOQ - TC_EPQ
                   = 6928.20 - 6196.77
                   = EUR 731.43/year

Percentage reduction = EPQ cost reduction / TC_EOQ * 100
                     = 731.43 / 6928.20 * 100
                     = 10.56%
```

#### Physical Interpretation

`Q* = 1936.49` is total output during one run, not the warehouse peak. The peak is 1,549.19 packs because roughly 387.30 packs are shipped while the line is still producing. Average finished-goods inventory is `Imax/2 = 774.60` packs.

#### Managerial Decision

Run batches of about 1,936 packs for approximately 1.68 weeks each. Under the stated relevant costs, gradual production reduces annual modeled cost by EUR 731.43, or 10.56%, compared with treating replenishment as an instantaneous EOQ delivery.

#### Exam Trap

Do not use `Q/2` as average inventory for EPQ. Use `Imax/2`, where `Imax = Q(1 - lambda/p)`. Also do not interpret the EOQ comparison as a freely available saving unless the factory can actually choose between internal production and instantaneous external supply.

### EPQ Task 2: Router Make-To-Stock Factory

#### Operating Story

A factory produces one model of Wi-Fi router for stock. Retail and online orders remove 200 routers from the finished-goods warehouse every week. When the line is configured for this model, it can build 1,000 routers per week. Preparing the line takes two weeks, so planners must start changeover work before the current router stock is exhausted.

The factory begins with 1,300 finished routers. A production batch is the total number of routers made during one run; it is not the maximum warehouse stock because customers continue buying routers while the line is running.

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `I0 = 1300` | finished Wi-Fi routers physically available in the warehouse today |
| `lambda = 10400/year = 200/week` | routers shipped to customers each week |
| `p = 52000/year = 1000/week` | routers completed by the line each week while this model is running |
| `K = EUR 750` | one line preparation, changeover, and startup event |
| `h = EUR 6` | annual cost of storing one finished router |
| `l = 2 weeks` | time required to prepare the line before production can start |
| `Q` | total routers manufactured during one run |
| `Imax` | highest warehouse stock reached during the run |

#### Full Operational Workflow

1. The warehouse starts with 1,300 routers and ships 200 per week while this model is not being produced.
2. After 4.5 weeks, 400 routers remain. Planning starts the two-week line preparation because those 400 routers exactly cover demand during preparation.
3. At week 6.5, the final opening-stock routers are shipped and the prepared line starts producing this model.
4. The line makes 1,000 routers per week while customers still remove 200, so warehouse stock builds at the net rate of 800 routers per week.
5. The 1.80-week run produces 1,802.78 routers. Customers take about 360.56 during the run, leaving a peak warehouse stock of 1,442.22.
6. Production of this router model stops. The factory may produce another product or perform other work, but router customers continue withdrawing 200 per week.
7. Router stock depletes over 7.21 weeks. When 400 remain, preparation for the next router run begins, keeping the cycle continuous.

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
EPQ Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
       = sqrt((2 * 750 * 10400) / 6) * sqrt(52000 / (52000 - 10400))
       = 1802.78 units/batch

demand per week = lambda/52
                = 10400/52
                = 200 units/week

start-preparation inventory r = demand per week * preparation lead time
                              = 200 * 2
                              = 400 units

time until preparation starts = (I0 - r) / demand per week
                              = (1300 - 400) / 200
                              = 4.5 weeks

time until first production starts = preparation-start time + lead time
                                   = 4.5 + 2
                                   = 6.5 weeks

maximum inventory Imax = ((p - lambda)/p) * Q*
                       = ((52000 - 10400)/52000) * 1802.78
                       = 1442.22 units

cycle time T = Q*/lambda
             = 1802.78/10400 years
             = 1802.78/10400 * 52
             = 9.01 weeks

production-run duration T0* = Q*/p
                            = 1802.78/52000 years
                            = 1802.78/52000 * 52
                            = 1.80 weeks

non-production duration = T - T0*
                        = 9.01 - 1.80
                        = 7.21 weeks
```

#### Physical Interpretation

`Q* = 1802.78` means the line manufactures about 1,803 routers in a run. It does not mean the warehouse holds that many routers. Because 200 routers leave each week during production, the peak stock is only 1,442.22. “Non-production duration” means this router model is not being made for 7.21 weeks; customer shipments continue, and the shared factory may be doing other work.

At the EPQ optimum, annual setup cost and annual holding cost are each approximately EUR 4,326.66. This balance explains why management should neither run tiny, frequent router batches nor manufacture a very large stockpile.

#### Managerial Decision

Start preparing the line when finished-router inventory reaches 400 units. Start production two weeks later at depletion, run the model for about 1.80 weeks, and manufacture about 1,803 routers. This coordinates the warehouse asset, customer withdrawals, and line availability without a deterministic stockout.

#### Exam Trap

Do not confuse four different quantities: `Q` is run output, `Imax` is peak stock, `r` is the preparation trigger, and `I0` is opening stock. Also do not say production is idle for 7.21 weeks; only production of this router model is off under the modeled cycle.

### EPQ Task 3: Shovel Factory And Technology Adoption

#### Operating Story

A shovel factory currently makes 300 shovels in each production run. Its line can produce 200 shovels per week, but the highest finished-goods stock observed in a cycle is only 150 shovels. That gap reveals that dealers are collecting shovels while the production run is still active.

Management is considering technology that raises the line rate by 50% to 300 shovels per week. The commercial question is not only the new batch size; it is the maximum annual amount the firm could pay for the technology from the modeled setup-and-holding savings.

#### Asset Dictionary

| Symbol | Real asset or activity |
|---|---|
| `p = 200/week` | shovels completed per week by the current line while running |
| `Q = 300` | shovels made in one current production run |
| `Imax = 150` | greatest physical finished-shovel inventory in the current cycle |
| `lambda` | shovels collected by dealers per week or year |
| `p_new = 300/week` | output rate of the proposed faster technology |
| `K = EUR 350` | cost of preparing and starting one shovel run |
| `h = EUR 5` | annual holding cost per finished shovel |
| `TC` | annual relevant setup plus finished-goods holding cost |

#### Full Operational Workflow

1. Under the old process, the line produces 200 shovels per week while dealers withdraw an unknown quantity.
2. A 300-shovel run raises stock by only 150, so the other 150 shovels leave during production.
3. Solving the EPQ stock identity shows dealer demand is 100 shovels per week, or 5,200 per year.
4. The proposed line makes 300 per week while dealers still take 100, so stock builds faster at 200 shovels per week.
5. With the new economics, the optimal run makes 1,044.99 shovels and reaches a peak stock of 696.66.
6. The faster process reduces the number of costly setups, but its larger inventory peak creates more holding cost; EPQ balances those effects.
7. Management compares the new annual relevant cost with the old EUR 6,000 cost before valuing the investment.

Facts:

- production rate `p = 200` units/week
- maximum inventory `Imax = 150`
- current economic production quantity `Q* = 300`
- assume 52 weeks/year

Demand implied by the EPQ maximum-inventory formula:

```text
Imax = ((p - lambda)/p) Q
150 = ((200 - lambda)/200) * 300
150/300 = (200 - lambda)/200
0.5 * 200 = 200 - lambda
lambda = 200 - 100
       = 100 units/week
       = 100 * 52
       = 5200 units/year
```

New technology:

- production rate increases by 50%: `p_new = 200 * (1 + 0.50) = 300` units/week; `p_new = 300 * 52 = 15600` units/year
- same demand: `lambda = 5200` units/year
- `K = EUR 350`
- `h = EUR 5`
- previous total cost: `EUR 6000`

Computed from lecture EPQ formulas:

```text
new EPQ Q* = sqrt(2K lambda / h) * sqrt(p / (p - lambda))
           = sqrt((2 * 350 * 5200) / 5) * sqrt(15600 / (15600 - 5200))
           = 1044.99 units/batch

new maximum inventory Imax = ((p - lambda)/p) * Q*
                           = ((15600 - 5200)/15600) * 1044.99
                           = 696.66 units

new annual holding cost = hImax/2
                        = 5 * 696.66 / 2
                        = EUR 1741.65/year

new annual setup cost = K lambda/Q*
                      = 350 * 5200 / 1044.99
                      = EUR 1741.65/year

new TC = hImax/2 + K lambda/Q*
       = 1741.6467 + 1741.6467
       = EUR 3483.29/year

maximum willingness to invest = previous TC - new TC
                              = 6000.00 - 3483.29
                              = EUR 2516.71/year
```

#### Physical Interpretation

The original 150-shovel peak is evidence about demand: half of the 300-shovel batch is shipped while production is active. Under the faster technology, a run creates more shovels than before and the warehouse peak rises to 696.66, but fewer setups are needed over the year. At the new optimum, annual setup and holding costs are each about EUR 1,741.65.

#### Managerial Decision

The technology creates up to EUR 2,516.71 of annual relevant-cost saving before acquisition, installation, maintenance, financing, tax, and risk effects. Management can use that annual saving as an operating benefit in an investment appraisal, but it is not automatically the one-time purchase price to pay.

#### Exam Trap

Do not treat EUR 2,516.71 per year as a present value. A technology with multiple years of benefits requires discounting and may have additional cash flows. Also derive demand using consistent time units before inserting it into the annual EPQ formula.

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

### Practice Task 1: Medical-Glove Distributor

**Operating setting:** A hospital-supply distributor sells 9,600 boxes of medical gloves per year. Placing and receiving one supplier order costs EUR 80. Keeping one box in the warehouse for a year costs EUR 6. Replenishment is instantaneous and demand is stable.

**Asset mapping:** `lambda` is boxes shipped to hospitals per year; `K` is one purchasing and receiving event; `h` is annual shelf cost per box; `Q` is boxes arriving in one supplier shipment.

**Your task:** Compute EOQ, orders per year, cycle time, and average inventory. Write every result with its physical unit.

**Physical interpretation prompt:** Describe one complete warehouse cycle from truck arrival to depletion. Explain what becomes more frequent and what becomes larger if management chooses a quantity below or above EOQ.

**Exam-trap check:** Did you distinguish annual demand from order quantity, and did you use `Q/2` only because replenishment is instantaneous?

### Practice Task 2: Medical-Glove Reorder Timing

**Operating setting:** Use the glove-distributor facts from Task 1, but assume the supplier takes three weeks to deliver and the warehouse currently follows the calculated EOQ policy. There are 52 weeks per year and no safety stock.

**Asset mapping:** The reorder point is boxes physically remaining when the buyer sends the order; lead time is the supplier's preparation and transport time; weekly demand is boxes withdrawn while the truck is pending.

**Your task:** Compute weekly demand and the deterministic reorder point. State when the order is placed and what should happen to inventory during the three-week lead time.

**Physical interpretation prompt:** Narrate the flow from the moment the trigger is reached until the truck unloads. Explain why the lead time changes timing but does not change the EOQ quantity here.

**Exam-trap check:** Did you convert annual demand into weekly demand before multiplying by a lead time measured in weeks? Did you avoid calling the reorder point safety stock?

### Practice Task 3: Ten-Week Festival Beverage Stall

**Operating setting:** A temporary festival stall has known, constant beverage demand of 5,200 cases per year but operates for only ten weeks. Each wholesaler delivery costs EUR 60 to arrange, and holding one case costs EUR 3 per year.

**Asset mapping:** `t lambda` is total cases required during the festival; `m` is the whole number of delivery trucks; `Q = t lambda/m` is cases per truck; `m_hat` is a continuous benchmark, not a feasible truck count.

**Your task:** Convert the ten-week horizon to years, compute `m_hat`, evaluate its floor and ceiling, choose `m*`, and calculate cases per delivery.

**Physical interpretation prompt:** Draw or describe the inventory triangles for both neighboring integer schedules. Explain which plan has more delivery activity and which holds more beverage stock.

**Exam-trap check:** Did you test both neighboring integers rather than merely rounding? Are `t`, `lambda`, and `h` expressed in compatible time units?

### Practice Task 4: Battery-Pack Production Run

**Operating setting:** A battery factory ships 12,000 packs per year and can produce 60,000 packs per year while its line is running. Each startup costs EUR 500, and holding one finished pack costs EUR 4 per year.

**Asset mapping:** `p` is packs completed by the active line; `lambda` is packs shipped to customers; `Q` is total run output; `Imax` is peak warehouse stock; `K` is one line setup and startup event.

**Your task:** Compute EPQ, maximum inventory, average inventory, production-run duration, cycle time, and non-production duration.

**Physical interpretation prompt:** Quantify how many packs customers receive during the production run and use that amount to explain why `Imax` is below `Q`.

**Exam-trap check:** Did you verify `p > lambda`, use `Imax/2` for holding cost, and keep annual rates consistent when converting durations to weeks?

### Practice Task 5: Assemble-To-Order Computer Firm

**Operating setting:** A computer firm can either stock finished laptop configurations or hold common modules and assemble a customer-specific laptop after an order arrives. Finished-product demand is varied, but customers tolerate a short assembly delay.

**Asset mapping:** Finished laptops are make-to-stock inventory; common screens, batteries, and processors are component inventory; the customer-order decoupling point is where forecast-driven work changes into order-driven work.

**Your task:** Recommend make-to-stock or assemble-to-order. Identify the inventory pooled by postponement, the customer lead-time consequence, the variety benefit, and two operating capabilities required to make the choice work.

**Physical interpretation prompt:** Follow one laptop from shared components through customer configuration and delivery. Explain which assets exist before the order and which activities wait for the order.

**Exam-trap check:** Did you discuss the trade-off rather than claim one system is universally superior? Did you separate inventory-cost effects from response-time and process-capability effects?

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

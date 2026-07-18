# Sample Examination WS22/23: Thorough Solutions

Source: `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/Sample Examinations/Sample Examination from WS2223.pdf`

Generated: 2026-07-08

Important source note: this sample PDF contains unresolved Moodle-randomization placeholders in a few questions, for example `{24-30}%` and `{4-8}`. Where the exact parameter is missing, the solution gives the formula and the value range.

## Production Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 Setup cost decreases by 19% | b | EOQ changes with the square root of setup cost. `sqrt(0.81) = 0.90`, so `Q*` decreases by 10%. |
| 1.2 Non-integer number of EOQ orders | c | In a finite horizon, check neighboring integer order counts and choose the one with lower total cost. |
| 1.3 Batch-and-queue disadvantage | c | The best available answer is less variety/flexibility. Batch-and-queue often creates long queues, WIP, and poor responsiveness to variety. |
| 1.4 Normal and Poisson | d | Normal is continuous; Poisson is discrete. |
| 1.5 Little's Law relationship | c | Little's Law links average inventory, average flow rate, and average flow time: `I = R*T`. |
| 1.6 Forecast technique always worst | d | No method is always worst. Performance depends on the demand pattern and error criterion. |
| 1.7 EOQ cost balance | d | At EOQ, average annual holding cost equals annual ordering/setup cost. |
| 1.8 Exponential smoothing with alpha = 1 | d | If `alpha = 1`, the next forecast equals the last actual value, which is naive forecasting. |
| 1.9 Poisson standard deviation | c | For Poisson demand, `variance = mu`, so `sigma = sqrt(mu)`. |
| 1.10 Not true for distributions | c and d are technically false | A CDF cannot be infinity; it is bounded by 1. Also, a continuous PDF can exceed 1 because it is a density, not a probability. If forced to choose one, c is the clearest false statement. |
| 1.11 Lean transformation | b | Poka-yoke, or fool-proofing, reduces process errors. |
| 1.12 Kaizen | c | Kaizen means continuous improvement. |

### Exercise 2: Forecasting

Actual demand:

| Day | Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|---|---:|---:|---:|---:|---:|---:|---:|
| Demand | 336 | 494 | 360 | 748 | 858 | 596 | 1122 |

#### 2.1.i Exponential smoothing forecast for Thursday

Use `alpha = 0.63` and initial forecast equal to Sunday demand.

```text
F_Sunday = 336
F_Monday = 0.63*336 + 0.37*336 = 336.00
F_Tuesday = 0.63*494 + 0.37*336 = 435.54
F_Wednesday = 0.63*360 + 0.37*435.54 = 387.95
F_Thursday = 0.63*748 + 0.37*387.95 = 614.78
```

Answer:

```text
614.78
```

#### 2.1.ii Moving average forecast for Saturday

Two-day moving average:

```text
F_Saturday = (A_Thursday + A_Friday)/2
F_Saturday = (858 + 596)/2
F_Saturday = 727
```

#### 2.1.iii Linear regression

Using `t = 1` for Sunday through `t = 7` for Saturday:

```text
Demand = intercept + slope*t
intercept = 207.71
slope = 109.29
```

#### 2.1.iv Best method by MSE

Using periods Tuesday through Saturday so all three methods have comparable forecasts:

| Method | MSE |
|---|---:|
| Moving average | 79,471.20 |
| Exponential smoothing | 87,571.70 |
| Linear regression | 29,210.87 |

Answer: linear regression.

#### 2.1.v Optimal alpha by MAD

Using Excel Solver with `0 <= alpha <= 1` and minimizing MAD gives approximately:

```text
alpha = 0.40
```

The result is stable around `0.40` whether the validation window starts at Monday or Tuesday.

#### 2.2 Why forecasting is needed before supplier orders

Three arguments:

1. Supplier orders must cover future demand during procurement and transportation lead time, not just today's demand.
2. Forecasting reduces both stockout risk and excess-inventory risk by estimating expected demand and uncertainty.
3. Better forecasts improve capacity, labor, purchasing, and cash planning; poor forecasts amplify bullwhip effects upstream.

#### 2.3 Control limits

Given:

```text
SSE = 125
n = 5
MSE = 125/5 = 25
sqrt(MSE) = 5
97.725% corresponds to z = 2
```

Control limits:

```text
UCL/LCL = +/- z*sqrt(MSE)
UCL/LCL = +/- 2*5 = +/- 10
```

Correct answer: a.

### Exercise 3: Capacity Management and Process Analysis

#### 3.1.i Townhall capacity before adding workers

Resource capacities:

| Resource group | Tasks | Staff | Minutes per visitor | Capacity |
|---|---|---:|---:|---:|
| A | Check-in + pickup | 2 | `3 + 2 = 5` | `2*60/5 = 24 visitors/hour` |
| B | Document check | 2 | 5 | `2*60/5 = 24 visitors/hour` |
| C | Payment | 1 | 3 | `1*60/3 = 20 visitors/hour` |
| D | Certificate preparation | 3 | 10 | `3*60/10 = 18 visitors/hour` |

System capacity:

```text
min(24, 24, 20, 18) = 18 visitors/hour
```

#### 3.1.ii Visitors in steady state

Flow time:

```text
3 + 8 + 5 + 3 + 3 + 10 + 2 = 34 minutes
34 minutes = 34/60 = 0.5667 hours
```

Little's Law at full capacity:

```text
I = R*T = 18*0.5667 = 10.20 visitors
```

#### 3.1.iii Utilization when 14 visitors arrive per hour

```text
Utilization = flow rate / capacity
Utilization = 14/18 = 0.7778 = 77.78%
```

#### 3.1.iv Allocation after adding one Group D employee

There are now 4 Group D employees.

If workers must be assigned as whole people to one activity, the best simple allocation is:

| Group D activity | Count |
|---|---:|
| Certificate preparation | 4 |
| Check-in | 0 |
| Document check | 0 |
| Payment | 0 |
| Pickup | 0 |

Then certificate capacity becomes:

```text
4*60/10 = 24 visitors/hour
```

Payment becomes the bottleneck at:

```text
1*60/3 = 20 visitors/hour
```

If fractional/time-sharing allocation is allowed, Group D can spend a small fraction of time supporting payment while most time remains in certificate preparation:

```text
10R + (3R - 60) <= 240
13R <= 300
R <= 23.08 visitors/hour
```

That would require about `3.85` Group D workers on certificate preparation and `0.15` on payment support.

#### 3.1.v New capacity

Exam-safe answer under whole-worker allocation:

```text
20 visitors/hour
```

With fractional time-sharing:

```text
23.08 visitors/hour
```

### Exercise 4: Economic Order Quantity

#### 4.1.i EOQ in boxes from Pakistan

Inputs:

```text
Demand = 5000 footballs per 6 months = 10000 footballs/year
K = EUR 98/order
h = EUR 0.50/football/year
Box size = 5 footballs
```

EOQ in footballs:

```text
Q* = sqrt(2*K*lambda/h)
Q* = sqrt(2*98*10000/0.50)
Q* = 1979.90 footballs
```

EOQ in boxes:

```text
1979.90/5 = 395.98 boxes
```

Answer: about `396 boxes`.

#### 4.1.ii Nine-month selling season

Demand over 9 months:

```text
10000*(9/12) = 7500 footballs
```

Continuous EOQ order count:

```text
7500/1979.90 = 3.79 orders
```

Check integer order counts:

| Orders | Balls/order | Boxes/order | Relevant season cost |
|---:|---:|---:|---:|
| 3 | 2500 | 500 | 762.75 |
| 4 | 1875 | 375 | 743.56 |
| 5 | 1500 | 300 | 771.25 |

Answer:

```text
Order 4 times.
Order 375 boxes each time.
Total boxes over the season = 1500 boxes.
```

#### 4.1.iii Reorder point for new supplier

New supplier lead time:

```text
2.4 weeks
Weekly demand = 10000/52 = 192.31 footballs/week
```

Inventory needed when placing the order:

```text
ROP = demand during lead time
ROP = 192.31*2.4 = 461.54 footballs
```

With boxes of 2:

```text
461.54/2 = 230.77 boxes
```

Use at least `462 footballs`, or `231 boxes`, to cover lead-time demand.

#### 4.1.iv EOQ in boxes from the new supplier

The new supplier also costs EUR 3 per football, and the setup and holding costs remain unchanged, so EOQ in footballs remains:

```text
Q* = 1979.90 footballs
```

With 2 footballs per box:

```text
1979.90/2 = 989.95 boxes
```

Unconstrained EOQ answer: about `990 boxes`.

If the question is interpreted as using the same 9-month finite-season plan from part ii, the practical four-order quantity is:

```text
1875 footballs/order / 2 = 937.50 boxes/order
```

That would be rounded to a feasible whole-box quantity.

### Exercise 5: Kristen's Cookie Company Case

#### 5.1.i Capacity improvement MCQ

Correct answer: c.

An electric baking oven with 3 trays improves the bottleneck. Automation of order processing/payment improves administration, but not system capacity while baking is the bottleneck.

#### 5.1.ii Issue with direct delivery

Correct answer: c.

Delivery increases process complexity and risks weakening the fresh-out-of-the-oven value proposition.

#### 5.1.iii Production system

Correct answer: a, make-to-order.

Kristen produces after receiving the customer order, which supports freshness and customization.

#### 5.1.iv Why order/payment automation does not improve capacity

The current bottleneck is baking:

```text
Oven time = 10 minutes/dozen
Capacity = 60/10 = 6 dozen/hour
```

Order arrival and payment steps are not the capacity constraint. Automating them can reduce customer friction and labor effort, but the process still cannot complete more than the oven can bake.

Recommendation: increase baking capacity with a larger/second oven, then re-check whether mixing, spooning, trays, or labor become the new bottleneck.

### Exercise 6: OceanCove Restaurant Case

#### 6.1.i Pandemic restrictions

Dine-in is prohibited, so dine-in capacity falls to zero. Take-away may still operate, but the restaurant's operating window shrinks from 11:00-23:00 to 11:00-20:00 because the rule prohibits opening after 20:00.

Operational effect:

- dine-in capacity: `0`
- dine-in customer order lead time: not applicable/infinite because customers cannot dine in
- take-away lead time: governed by kitchen preparation, pickup, and delivery coordination rather than table availability

#### 6.1.ii Added value of delivery service

Two added values:

1. It creates a sales channel while dine-in is unavailable or capacity-constrained.
2. It can use idle kitchen capacity without requiring dining-room seats.

It may also reduce customer travel effort and broaden geographic reach.

#### 6.1.iii Disadvantages of multiple delivery services

Two disadvantages:

1. Operational complexity: multiple platforms create more order streams, handoff errors, sequencing issues, and monitoring effort.
2. Margin and quality risk: platform commissions reduce contribution, while delivery delays or poor handling can damage customer experience.

## Logistics Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 Pull/push decision level | c | Production-system design is a strategic operations decision. |
| 1.2 Not a bullwhip cause | b | Everyday low pricing is a bullwhip mitigation, not a cause. |
| 1.3 Knapsack objective | a | Maximize selected value under the capacity limit. |
| 1.4 Bullwhip upstream effect | a | Order volatility increases upstream from customers to suppliers. |
| 1.5 Hotelling competition | c | The model studies location equilibrium among competitors. |
| 1.6 Supermarket distribution design | c | Retailer storage with customer pickup. |
| 1.7 TSP not true | c and d are technically false | TSP is not the same as shortest path, and a valid TSP tour does not repeat nodes except returning to the start. If forced to choose one, c is the standard trap. |
| 1.8 End inventory in order-up-to model | d | End inventory is order-up-to level minus demand over `l+1` periods. |
| 1.9 Rounding countable quantities | d, with correction | The practical reason is that fractional units cannot be ordered. Exam-quality answers should compare floor/ceiling or choose the smallest integer meeting the service target, rather than blindly dropping digits. |
| 1.10 Shortage gaming category | c | Shortage gaming is categorized as individual incentives in the lecture framing. |
| 1.11 Positive salvage in Newsvendor | c | Salvage reduces overage cost, so the critical fractile/service level increases. |
| 1.12 Tactical decision | b | Production planning is tactical; network configuration and production-system design are strategic. |

### Exercise 2: Inventory Management

#### 2.1 Phones with unresolved holding-cost placeholder

The source gives annual holding cost as `{24-30}%` of phone value. Let:

```text
H = annual holding-cost percentage, between 0.24 and 0.30
b = weekly backorder cost = 0.20
h = H/52
l = 3 weeks
Exposure horizon = l + 1 = 4 weeks
Weekly demand ~ Poisson(lambda = 80)
Aggregate demand ~ Poisson(lambda = 320)
```

##### 2.1.i Optimal in-stock probability

```text
SL* = b/(b+h) = 0.20/(0.20 + H/52)
```

Range:

| H | Service level |
|---:|---:|
| 24% | 97.74% |
| 30% | 97.20% |

##### 2.1.ii Optimal order-up-to level

Find the smallest integer `S` with:

```text
P(D <= S) >= SL*, D ~ Poisson(320)
```

Range:

| H | SL* | Smallest S meeting target |
|---:|---:|---:|
| 24% | 97.74% | 356 |
| 30% | 97.20% | 355 |

Because the exact randomized `H` value is missing, the answer is in the range `355-356 phones`.

##### 2.1.iii Realized service level

Realized service level is the Poisson CDF at the chosen `S`:

```text
Realized SL = P(D <= S)
```

For the endpoint quantities:

```text
S = 355 -> P(D <= S) = 97.49%
S = 356 -> P(D <= S) = 97.79%
```

##### 2.1.iv Effect of changing the demand distribution

The optimal service level does not change because it is determined by costs:

```text
SL* = b/(b+h)
```

Changing the demand distribution changes the order-up-to level `S` required to achieve that service level.

##### 2.1.v Changing from order-up-to to Newsvendor

Correct answer: c.

The Newsvendor model focuses on a single period. It does not use future replenishment periods in the same way as an order-up-to model with lead time.

#### 2.2 Newsvendor with unresolved margin placeholder

Demand:

```text
Uniform(250, 450)
Cost = EUR 3/unit
Profit margin = m, where m is `{4-8}` EUR/unit in the source
```

##### 2.2.i Optimum service level

```text
c_u = margin = m
c_o = cost = 3
SL* = m/(m+3)
```

Range:

| Margin m | Service level |
|---:|---:|
| 4 | 57.14% |
| 8 | 72.73% |

##### 2.2.ii Optimal order quantity

Uniform quantile:

```text
Q* = 250 + SL*(450-250)
Q* = 250 + 200*m/(m+3)
```

Range:

| Margin m | Q* |
|---:|---:|
| 4 | 364.29 |
| 8 | 395.45 |

Because the exact Moodle-randomized margin is missing, the solution is parameterized by `m`.

### Exercise 3: Supply Chain Coordination

#### 3.1.i Effect of sudden demand increase

The social-media shock raises consumer demand. Retailers react with larger orders, suppliers see an amplified signal, and the manufacturer can receive orders beyond capacity. The effect is strongest upstream because each echelon reacts not only to end-customer demand but also to the order behavior of the next downstream party.

#### 3.1.ii Four potential supply-chain impacts

1. Excess inventory if the demand spike is temporary.
2. Stockouts and poor service if firms underestimate the spike.
3. Higher production, overtime, and expediting costs.
4. Capacity overload and unstable schedules upstream.

Other valid impacts: distorted forecasts, emergency transportation, supplier shortages, cancellations, and working-capital pressure.

#### 3.1.iii Mitigation strategy not suitable in this case

The least suitable listed strategy is a pure pull system with make-to-order.

Why:

- Almond milk/green tea style consumer goods are usually replenished to stock.
- Customers expect immediate shelf availability.
- A pure make-to-order pull system would create long lead times and lost sales.

VMI, EDI, and POS data are suitable because they share demand information and reduce distorted ordering.

### Exercise 4: Facility Location Problem

From the figure:

| Arc | Distance | Unit cost formula | Unit cost |
|---|---:|---|---:|
| P1 to C1 | 8 | `50 + 4*8` | 82 |
| P1 to C3 | 18 | `50 + 4*18` | 122 |
| P2 to C1 | 12 | `50 + 4*12` | 98 |
| P2 to C2 | 13 | `50 + 4*13` | 102 |
| P3 to C2 | 9 | `50 + 4*9` | 86 |
| P3 to C3 | 40 | `50 + 4*40` | 210 |

Capacities:

```text
P1 = 121/day
P2 = 87/day
P3 = 132/day
```

Demands:

```text
C1 = 104/day
C2 = 93/day
C3 = 143/day
```

#### 4.1.i Objective function

```text
min 82x_11 + 122x_13 + 98x_21 + 102x_22 + 86x_32 + 210x_33
```

#### 4.1.ii Shipment matrix

Optimal shipment plan:

| Plant to customer | C1 | C2 | C3 |
|---|---:|---:|---:|
| P1 | 17 | - | 104 |
| P2 | 87 | 0 | - |
| P3 | - | 93 | 39 |

Checks:

```text
P1 capacity: 17 + 104 = 121
P2 capacity: 87 + 0 = 87
P3 capacity: 93 + 39 = 132
C1 demand: 17 + 87 = 104
C2 demand: 0 + 93 = 93
C3 demand: 104 + 39 = 143
```

#### 4.1.iii Minimum cost

```text
Cost = 17*82 + 104*122 + 87*98 + 0*102 + 93*86 + 39*210
Cost = 1,394 + 12,688 + 8,526 + 0 + 7,998 + 8,190
Cost = EUR 38,796
```

### Exercise 5: Supply Chain Finance

#### 5.1.i Reverse factoring processes

The image labels the three parties:

```text
Buyer
Supplier(s)
Bank
```

Process interpretation:

| Label | Process |
|---|---|
| C | Supplier delivers goods and/or invoice to the buyer. |
| A | Buyer approves the invoice and sends approved payable information to the bank/platform. |
| B | Bank pays the supplier early, usually minus a financing fee. |
| D | Buyer pays the bank later at invoice maturity. |

Reverse factoring is buyer-led approved-invoice financing. The buyer's credit quality helps the supplier access earlier and cheaper liquidity.

#### 5.1.ii Correct sequence

```text
C -> A -> B -> D
```

That is:

```text
supplier invoice/delivery -> buyer approval to bank -> bank early payment to supplier -> buyer later payment to bank
```

### Exercise 6: HP Case

European demand:

```text
Annual demand = 24,500 printers
Europe share = 40%
Europe demand = 9,800 printers/year
Printer net value = 20,000
WACC = 22.5%
Capital cost per printer/year = 0.225*20,000 = 4,500
Holding cost excluding capital = 400/year
Total in-transit holding/capital rate = 4,900 per printer/year
```

#### 6.1.i Transportation mode with lower total cost

Container ship:

```text
Freight = (9,800/500)*10,000 = 196,000
In-transit carrying cost = 9,800*4,900*(11/52) = 10,158,076.92
Total ship cost = 10,354,076.92
```

Airfreight:

```text
Freight = 9,800*300 = 2,940,000
In-transit carrying cost = 9,800*4,900*(2/52) = 1,846,923.08
Total air cost = 4,786,923.08
```

Answer: airfreight has the lower total cost once in-transit capital and holding costs are included.

#### 6.1.ii Savings

```text
Savings = ship total - air total
Savings = 10,354,076.92 - 4,786,923.08
Savings = 5,567,153.85
```

If only capital cost, not the extra `400/year` holding cost, is counted during transit, air still wins by `4,888,692.31`. The decision is unchanged.

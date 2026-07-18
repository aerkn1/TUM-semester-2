# Sample Examination SS23: Thorough Solutions

Source: `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/Sample Examinations/Sample Examination from SS23.pdf`

Generated: 2026-07-08

These answers are derived from the sample PDF, rendered diagram pages, and the SCM course notes. Round numerical answers to two decimals unless an integer decision is required.

## Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 HP optimal service level | d | Weekly holding cost is `48%/52 = 0.9231%` of value. Backlog cost is `50%*22.4% = 11.2%` of value. `SL = 0.112/(0.112+0.48/52) = 92.39%`. |
| 1.2 HP maturity phase least appropriate | a | In maturity, customer expectations usually rise or standardize, margins fall, ramp-up issues disappear, and process superiority matters more. |
| 1.3 Bullwhip effect | a | Bullwhip can increase inventory, capacity, expediting, and coordination costs. |
| 1.4 Annual spend from financing cost | b | `5750 = Spend*10%*(60/360)`, so `Spend = 345,000`. |
| 1.5 Lean transformation | b | Fool-proofing/Poka-yoke reduces execution errors. |
| 1.6 Setup cost decreases by 19% | b | `Q*` changes by `sqrt(0.81) = 0.90`, so it decreases by 10%. |
| 1.7 Make-to-stock to assemble-to-order | b | A major production-system change is Kaikaku, a radical change. |
| 1.8 Least likely bullwhip cause | b | Everyday low pricing is a mitigation; inflated orders, long lead times, and seasonal discounts are causes. |
| 1.9 SCF statements | a | SCF concerns cash flows along supply chains and can enable better operations policies. |
| 1.10 EPQ extreme cases | a | As production rate approaches infinity, EPQ approaches EOQ and total relevant cost is higher than when production is closer to demand. As `p` approaches demand from above, inventory buildup shrinks and total relevant cost decreases. |

## Exercise 2: Forecasting

Actual and judgemental data:

| Day | Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|---|---:|---:|---:|---:|---:|---:|---:|
| Actual demand | 157 | 227 | 180 | 260 | 419 | 249 | 471 |
| Judgemental forecast | 177 | 252 | 165 | 225 | 499 | 224 | 551 |

### 2.1 Exponential smoothing forecast for Wednesday

Use `alpha = 0.8`, initial forecast equal to Sunday demand.

```text
F_Sunday = 157
F_Monday = 0.8*157 + 0.2*157 = 157.00
F_Tuesday = 0.8*227 + 0.2*157 = 213.00
F_Wednesday = 0.8*180 + 0.2*213 = 186.60
```

Answer:

```text
186.60
```

### 2.2 Moving average forecast for Saturday

Use the past two actual days:

```text
F_Saturday = (A_Thursday + A_Friday)/2
F_Saturday = (419 + 249)/2
F_Saturday = 334
```

### 2.3 Linear regression forecast for Thursday

Given:

```text
intercept = 105.43
slope = 43.75
Sunday corresponds to t = 1
Thursday corresponds to t = 5
```

Calculation:

```text
F_Thursday = 105.43 + 43.75*5
F_Thursday = 324.18
```

### 2.4 MAD of judgemental forecast

Errors:

| Day | Actual - Forecast | Absolute error |
|---|---:|---:|
| Sunday | -20 | 20 |
| Monday | -25 | 25 |
| Tuesday | 15 | 15 |
| Wednesday | 35 | 35 |
| Thursday | -80 | 80 |
| Friday | 25 | 25 |
| Saturday | -80 | 80 |

```text
MAD = (20+25+15+35+80+25+80)/7
MAD = 280/7
MAD = 40.00
```

### 2.5 MSE of judgemental forecast

```text
Squared errors = 400, 625, 225, 1225, 6400, 625, 6400
MSE = 15,900/7
MSE = 2,271.43
```

## Exercise 3: Inventory Management

### 3.1.1 Newsvendor order quantity for one day

Inputs:

```text
c_u = 2500
c_o = 1700
Demand ~ Normal(mu = 40, sigma = 7)
```

Critical fractile:

```text
SL* = c_u/(c_u+c_o)
SL* = 2500/(2500+1700)
SL* = 0.59524
```

Normal quantile:

```text
z_0.59524 = 0.24
Q* = mu + z*sigma
Q* = 40 + 0.24*7
Q* = 41.69
```

Integer decision:

```text
Order 42 items if the service target must be met with whole units.
```

### 3.1.2 In-stock probability for service level 63.86%

In this setting, the in-stock probability is the service level:

```text
63.86%
```

### 3.1.3 Monthly order quantity for at least 80% service

Daily demand is independent:

```text
mu_month = 30*40 = 1200
sigma_month = sqrt(30)*7 = 38.34
z_0.80 = 0.8416
```

Quantity:

```text
Q = 1200 + 0.8416*38.34
Q = 1232.27
```

At least 80% with integer units:

```text
Order 1233 units
```

### 3.2 Poisson normal approximation

For `Poisson(lambda = 25)`:

```text
mu = lambda = 25
variance = lambda = 25
sigma = sqrt(25) = 5
```

Correct answer: b.

### 3.3 Demand-distribution statement

None of the provided statements is fully correct.

Corrections:

- Normal demand realizations do not all have the same probability density.
- Poisson is not always more suitable than normal, and uniform is not a lossless replacement.
- Firms do not "order the service level"; they order the quantile corresponding to the service level.
- A normal random variable can be negative, but firms still approximate demand as normal when the mean is large relative to the standard deviation and negative probability is negligible.

Exam-safe answer: reject all options and write the corrected statement above.

### 3.4 Uniform Newsvendor for T-shirts

Inputs:

```text
Demand ~ Uniform(3500, 6000)
Cost = 6
Price = 8
Salvage = 0
```

Costs:

```text
c_u = price - cost = 8 - 6 = 2
c_o = cost - salvage = 6 - 0 = 6
SL* = 2/(2+6) = 0.25
```

Uniform quantile:

```text
Q* = 3500 + 0.25*(6000-3500)
Q* = 3500 + 625
Q* = 4125
```

## Exercise 4: Capacity Management

The rendered process flow shows:

```text
Check-in: 3 min
Wait: 10 min
Ordering: 5 min
Wait: 6 min
Payment: 4 min
Order preparation: 15 min
Pickup: 2 min
```

Assume one worker performs each staffed task unless the subquestion changes it.

### 4.1 Bottleneck activity

Activity capacities:

| Activity | Time | Capacity |
|---|---:|---:|
| Check-in | 3 min | 20 customers/hour |
| Ordering | 5 min | 12 customers/hour |
| Payment | 4 min | 15 customers/hour |
| Order preparation | 15 min | 4 customers/hour |
| Pickup | 2 min | 30 customers/hour |

Correct answer: c, order preparation.

### 4.2 Restaurant capacity

System capacity is the minimum activity capacity:

```text
capacity = min(20, 12, 15, 4, 30)
capacity = 4 customers/hour
```

### 4.3 Two payment employees

Payment capacity with two employees:

```text
2*60/4 = 30 customers/hour
```

The bottleneck remains order preparation at `4 customers/hour`, so total capacity remains the same.

Correct answer: b.

### 4.4 Manager supports order preparation

Trained worker:

```text
60/15 = 4 customers/hour
```

Manager takes 50% more time:

```text
15*1.5 = 22.5 min/customer
60/22.5 = 2.67 customers/hour
```

Combined order-preparation capacity:

```text
4 + 2.67 = 6.67 customers/hour
```

Other capacities are still higher than this except no smaller step appears, so new restaurant capacity is:

```text
6.67 customers/hour
```

### 4.5 Average customers in steady state at 11 customers/hour

Flow time:

```text
3 + 10 + 5 + 6 + 4 + 15 + 2 = 45 minutes = 0.75 hours
```

Little's Law:

```text
I = R*T = 11*0.75 = 8.25 customers
```

### 4.6 Utilization with capacity 10 and arrivals 6/hour

```text
Utilization = 6/10 = 0.60 = 60.00%
```

## Exercise 5: Facility Location Problem

### 5.1.1 Aluminum foil roll problem type

Correct answer: d, Knapsack Problem.

The firm selects product units to maximize value subject to a limited roll length.

### 5.1.2 Objective function

With binary `X_i` and values `V_i`:

```text
max sum_i V_i X_i
```

For the given products:

```text
max 1*X_chocolate + 1.5*X_plate + 2*X_food_container + 0.5*X_utility_cup
```

Subject to the roll-length capacity:

```text
0.25X_chocolate + 0.5X_plate + 0.625X_food_container + 0.10X_utility_cup <= 1
```

### 5.1.3 Maximum value with multiple units allowed

Value density:

| Product | Length | Value | Value per meter |
|---|---:|---:|---:|
| Chocolate wrap | 0.25 | 1.00 | 4.00 |
| Plate | 0.50 | 1.50 | 3.00 |
| Food container | 0.625 | 2.00 | 3.20 |
| Utility cup | 0.10 | 0.50 | 5.00 |

Utility cups have the highest value density. With 1 meter:

```text
10 utility cups * 0.10 m = 1.00 m
Total value = 10*0.50 = 5.00
```

Answer: maximum value is `5.00`, achieved by producing 10 utility cups.

### 5.2 TSP formulation labels

The rows correspond to:

| Formula row | Correct label |
|---|---|
| `min sum c_ij x_ij` | Minimizing the cost of traversing edges. |
| `sum incident x = 2` for each city | Conservation/degree constraint ensuring each city has two incident tour edges. |
| Subset cut constraint | Subtour elimination constraint. |

### 5.3.1 Set covering heuristic

Plants:

```text
P1 cost 5: serves C1, C2, C3, C4, C5
P2 cost 0: serves C1, C2, C4
P3 cost 3: serves C4, C5
P4 cost 4: serves C3, C5
```

Heuristic:

1. Choose the plant with lowest cost per newly covered customer.
2. `P2` has cost `0/3 = 0`, so choose `P2` first. Covered: C1, C2, C4.
3. Remaining: C3, C5.
4. `P4` covers both remaining customers for cost `4/2 = 2`.

Correct answer: c, open `P2` and `P4`.

### 5.3.2 Minimum total heuristic cost

```text
Cost = cost(P2) + cost(P4)
Cost = 0 + 4
Cost = 4
```

## Exercise 6: Kristen's Cookie Company

### 6.1 Second oven conclusion

Correct answer: b.

A second oven helps the former baking bottleneck, but capacity does not automatically double. Mixing, spooning, labor, and recipe variety can become new constraints. A buffer of mixed/spooned cookies can help keep the ovens fed, especially when orders have different doughs and cannot be mixed together.

### 6.2 Minimum time for two different one-dozen orders

One feasible schedule:

| Time | Activity |
|---:|---|
| 0-1 | Confirm order A |
| 1-7 | Mix A; confirm B can be done during this window if mixing is treated as mixer resource rather than worker-only |
| 7-9 | Spoon A |
| 7-13 | Mix B as soon as mixer is free |
| 9-19 | Bake A |
| 13-15 | Spoon B |
| 19-24 | Cool A; bake B starts at 19 |
| 24-27 | Pack/payment/delivery A |
| 19-29 | Bake B |
| 29-34 | Cool B |
| 34-37 | Pack/payment/delivery B |

Minimum completion time:

```text
37 minutes
```

The oven creates the main sequencing constraint for two different one-dozen orders.

### 6.3 Fill-in production-system logic

Correct sequence:

```text
make-to-order
baking process
buying a larger oven
make-to-stock
customized
```

Full sentence:

Kristen Cookies uses a make-to-order production system. The bottleneck is the baking process. If the firm wants to sell more cookies, it should primarily consider buying a larger oven. Switching to make-to-stock would be risky because the cookies would no longer be customized.

## Exercise 7: OceanCove

### 7.1 Overall capacity

Cocean Ove capacities:

| Activity | Capacity |
|---|---:|
| Fish-grilling | 100 meals/hour |
| Fish-frying | 200 meals/hour |
| French-fry frying | 400 meals/hour |
| Expediting | Plenty |
| Assembling | 180 meals/hour |
| Order-taking, delivery, billing | 120 meals/hour |
| Dining area | 270 meals/hour |

Customers order fried fish as often as grilled fish, so the mix is 50/50.

Fish capacity under equal mix:

```text
0.5Q <= 100  -> Q <= 200
0.5Q <= 200  -> Q <= 400
```

Other limits:

```text
Assembly <= 180
Order-taking/delivery/billing <= 120
Dining <= 270
```

Overall capacity:

```text
min(200, 400, 400, 180, 120, 270) = 120 meals/hour
```

### 7.2 Paper slips and lean concept

Correct answer: d, Kanban.

The paper slip is an information signal that authorizes and communicates work to the kitchen.

### 7.3 Waiting time with 38 orders waiting

Use Little's Law:

```text
I = R*T
T = I/R
```

Inputs:

```text
I = 38 orders
R = 2 orders/minute
```

Calculation:

```text
T = 38/2 = 19 minutes
```

Average waiting time:

```text
19 minutes
```

# Sample Examination SS20: Thorough Solutions

Source: `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/Sample Examinations/Sample Examination from SS20.pdf`

Generated: 2026-07-08

These solutions are derived from the SCM course notes and sample-exam source. Round numerical answers to two decimals unless the question clearly calls for an integer.

## Production Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 Process capacity | c | Process capacity is the maximum sustainable output per time unit, not the average output and not merely elapsed production time. |
| 1.2 Capacity-management tradeoff | a | With fluctuating demand, a system cannot simultaneously guarantee 100% service and 100% utilization unless it has buffers such as inventory, waiting capacity, or slack. |
| 1.3 EOQ versus in-house production | c | EPQ has finite production, so inventory builds gradually. The optimal batch is `Q_EPQ = Q_EOQ * sqrt(p/(p-lambda))`, which is larger than EOQ when `p > lambda`. |
| 1.4 Optimal batch size | c | `Q* = sqrt((2*K*lambda/h) * p/(p-lambda)) = sqrt((2*200*150/24) * 200/(200-150)) = sqrt(10000) = 100`. |
| 1.5 Production starts per year | b | Production frequency is `lambda/Q* = 150/100 = 1.5` starts per year. |
| 1.6 Tool for relationships and bottlenecks | b | A process flow diagram maps process steps and resource relationships so bottlenecks become visible. |
| 1.7 Task with smallest capacity | a | The bottleneck is the lowest-capacity task or resource and therefore limits system capacity. |
| 1.8 Reached after ramp-up | c | Steady state is the stable operating condition after transient ramp-up effects. |
| 1.9 Timing overlap tool | a | A Gantt chart shows when resources and tasks overlap over time. |
| 1.10 Simulation surely needed | a | Simulation is most useful when the system is too complex or uncertain for a clean analytical model. |
| 1.11 Inventory investment sequence | c | Increasing inventory investment: engineer-to-order, make-to-order, assemble-to-order, make-to-stock. |
| 1.12 Legit production-improvement recommendation | b | Moving from push toward pull production is a standard lean improvement candidate. |

### Exercise 2: Forecasting

Actual demand:

| Period | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| Demand | 135 | 215 | 175 | 214 | 159 |

#### 2.a Forecasts

Naive forecast:

| Forecast for period | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|
| Forecast | 135 | 215 | 175 | 214 |

Naive with trend:

Formula after two actual observations:

```text
F_t = A_(t-1) + (A_(t-1) - A_(t-2))
```

| Forecast for period | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|
| Forecast | 135 | 295 | 135 | 253 |

For period 2 there is no prior trend yet, so the practical starting value is the naive forecast.

Exponential smoothing with `alpha = 0.6`, initial forecast `F_1 = 100`:

```text
F_t = alpha*A_(t-1) + (1-alpha)*F_(t-1)
```

| Forecast for period | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|
| Forecast | 121.00 | 177.40 | 175.96 | 198.78 |

#### 2.b MAD and MSE for periods 3-5

| Method | Errors for periods 3-5 | MAD | MSE | Interpretation |
|---|---:|---:|---:|---|
| Naive | `-40, 39, -55` | 44.67 | 2048.67 | Better than naive with trend, but still misses the reversals strongly. |
| Naive with trend | `-120, 79, -94` | 97.67 | 9825.67 | Worst here because trend extrapolation amplifies short-term noise. |
| Exponential smoothing | `-2.40, 38.04, -39.78` | 26.74 | 1011.86 | Best by both MAD and MSE. |

Correct recommendation: exponential smoothing performs best because it has the lowest average absolute error and the lowest squared-error penalty on the same validation window.

#### 2.c Finding alpha in Excel

Set up the exponential smoothing recursion with `alpha` in one input cell. Then compute forecast errors, MAD, and/or MSE. Use Excel Solver with:

```text
Changing variable: alpha
Constraint: 0 <= alpha <= 1
Objective: minimize the selected error metric cell
```

If large deviations are especially costly, minimize MSE. If a typical absolute miss is the decision criterion, minimize MAD.

### Exercise 3: Process Analysis

#### 3.a Throughput time versus customer order lead time

The statement "throughput time is always strictly larger than customer order lead time" is false.

Throughput time is the time a flow unit spends inside the process. Customer order lead time is the time from the customer's order until delivery or service completion. They can be equal in a make-to-order service, customer lead time can be shorter than internal throughput time in make-to-stock settings, and customer lead time can include waiting that is not part of internal processing. "Always strictly larger" is too strong.

#### 3.b Capacity of ProfiCutZ

Resource capacities:

| Resource | Staff | Time per customer | Capacity calculation | Capacity |
|---|---:|---:|---|---:|
| Administration | 1 | `2 + 3 = 5 min` | `60/5` | 12 customers/hour |
| Hair washers | 2 | `6 min` | `2*60/6` | 20 customers/hour |
| Hairdressers | 5 | `30 min` | `5*60/30` | 10 customers/hour |

System capacity:

```text
capacity = min(12, 20, 10) = 10 customers/hour
```

#### 3.c Bottleneck

The bottleneck is the professional hairdresser group because it has the lowest capacity, `10 customers/hour`.

#### 3.d Average number of customers in steady state

Flow time:

```text
2 + 7 + 6 + 3 + 30 + 5 + 3 = 56 minutes
56 minutes = 56/60 = 0.9333 hours
```

Little's Law:

```text
I = R*T = 10 customers/hour * 0.9333 hours = 9.33 customers
```

Average inventory in the shop at full steady-state capacity: `9.33 customers`.

#### 3.e Capacity after hiring two more hairdressers

If the usual task assignment remains unchanged:

```text
Hairdresser capacity = 7*60/30 = 14 customers/hour
Administration capacity = 12 customers/hour
Hair-washing capacity = 20 customers/hour
```

Then administration becomes the bottleneck and capacity is `12 customers/hour`.

If the stated cross-training is used optimally, hairdressers can also help with check-in/check-out after the administrator is fully loaded. For rates above 12 customers/hour:

```text
Hairdresser minutes needed = 30R + 5(R - 12)
Available hairdresser minutes = 7*60 = 420
30R + 5R - 60 <= 420
35R <= 480
R <= 13.71 customers/hour
```

Exam-safe conclusion: `12 customers/hour` under the normal fixed assignment; up to `13.71 customers/hour` if hairdressers are deliberately reallocated to support administration. In either case, hiring hairdressers alone does not raise capacity to 14 because the bottleneck moves.

### Exercise 4: EOQ and Lean

#### 4.a Warehouse pooling savings

For one warehouse:

```text
Q* = sqrt(2*K*lambda/h)
Minimum relevant cost per warehouse = sqrt(2*K*lambda*h)
```

Before pooling, `n` identical warehouses cost:

```text
TC_before = n * sqrt(2*K*lambda*h)
```

After pooling, total demand is `n*lambda`:

```text
TC_after = sqrt(2*K*(n*lambda)*h)
         = sqrt(n) * sqrt(2*K*lambda*h)
```

Savings fraction:

```text
(TC_before - TC_after) / TC_before
= (n - sqrt(n)) / n
= 1 - 1/sqrt(n)
```

Answer:

```text
Savings percentage = (1 - 1/sqrt(n)) * 100%
```

#### 4.b Order frequency over 12 weeks

Known inputs:

```text
K = 12 USD/order
h = 2 USD/unit/year
weekly demand = 57 units/week
annual demand = 57*52 = 2964 units/year
season demand = 57*12 = 684 units
```

EOQ:

```text
Q* = sqrt(2*K*lambda/h)
Q* = sqrt(2*12*2964/2)
Q* = 188.59 units
```

Continuous order count:

```text
684 / 188.59 = 3.63 orders
```

Because an actual season uses whole order events, compare 3 and 4 orders:

```text
3 orders: order quantity = 684/3 = 228 units
4 orders: order quantity = 684/4 = 171 units
```

Total season cost is lower with 4 orders, so the practical answer is `4 orders during the 12 weeks`.

#### 4.c Product usually made to stock

Example: bottled water. It is usually made to stock because demand is broad and predictable enough, customers expect immediate availability, and customization is not central to the value proposition.

#### 4.d Steps to transform push into pull

Two required steps:

1. Introduce a downstream demand signal such as Kanban, point-of-sale replenishment, or supermarket pull so production is triggered by consumption.
2. Reduce setup times and batch sizes so the process can replenish frequently without building large finished-goods inventory.

Additional useful steps include WIP limits, level scheduling, standardized work, supplier synchronization, and visual controls.

### Exercise 5: Practice Problems

#### 5.a Kristen Cookies technologies and KPIs

Two suitable technologies:

1. Online ordering and payment system.
2. Demand forecasting or scheduling tool using historical order data.

Operational KPIs affected:

| KPI | Expected effect | Why |
|---|---|---|
| Customer order lead time | Decreases if ordering/payment delays are removed. | Customers spend less time in administrative steps. |
| Capacity | Only increases if the technology affects the bottleneck. | If baking remains the bottleneck, order automation alone does not raise dozen/hour capacity. |
| Labor productivity | Increases. | Less manual time is spent confirming orders and collecting payment. |
| Demand forecast accuracy | Increases. | Better order data improves staffing, ingredient planning, and promotion timing. |
| On-time delivery / reliability | Increases if scheduling is integrated. | More predictable order arrivals reduce overload and missed promises. |

The exam trap is to claim that every digital tool increases capacity. Capacity improves only when the current bottleneck or bottleneck variability is improved.

#### 5.b OceanCove benefits of FoodX

Two major operations benefits:

1. FoodX can create demand beyond the dining room constraint. If physical seats limit dine-in throughput, delivery lets the kitchen sell meals without consuming table capacity.
2. It can use idle kitchen capacity outside peak dine-in periods. This improves resource utilization and may smooth demand across time.

#### 5.c OceanCove downsides of FoodX

Two major operations downsides:

1. Delivery adds coordination complexity. Orders must be sequenced with dine-in orders, packed correctly, and handed off reliably.
2. Food quality and customer experience may degrade. Lead time, temperature, packaging, and delivery reliability are partly outside OceanCove's direct control.

Other relevant risks: commission cost, channel conflict, more volatile demand, and loss of direct customer relationship.

#### 5.d FoodX recommendation with quantitative reasoning

Use FoodX if the delivery margin loss is smaller than the contribution gained from using otherwise idle kitchen capacity.

From the OceanCove process note:

```text
Lunch dining-area flow = 120 customers/hour
Lunch assembly capacity = 144 meals/hour
Spare assembly capacity at peak lunch = 24 meals/hour
```

If FoodX orders can be handled within the spare `24 meals/hour`, delivery adds revenue without requiring more dining seats. If FoodX demand exceeds this spare capacity, it will compete with dine-in orders at assembly and may lengthen lead time.

Recommendation: yes, test FoodX with controlled order caps and priority rules. Keep dine-in lead-time promises protected, and use FoodX mainly when the kitchen has spare capacity or when the dining room is externally constrained.

## Logistics Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 Strategic forward buying in promotions | g | Forward buying under promotions is a cause of the bullwhip effect because customers buy ahead and distort demand signals. |
| 1.2 EDLP | c | Everyday low pricing reduces promotion-driven order spikes and therefore mitigates bullwhip. |
| 1.3 Drop-shipping plus single delivery | b | Manufacturer storage with direct shipping and in-transit merge combines orders from different locations into one customer delivery. |
| 1.4 Inventory at distributors, package carrier final delivery | a | This is distributor storage with package carrier delivery. |
| 1.5 Excel Solver changing cells | a | Changing cells are decision variables. Solver changes them to optimize the objective while respecting constraints. |
| 1.6 Hotelling intuition | b | Firms move toward the center to capture larger customer shares; if one moves away, a rival can move closer to the larger market side. |
| 1.7 Complement of event A | c | The complement is the set of outcomes in the sample space that are not in `A`. |
| 1.8 Incorrect comparison of normal and Poisson | b | Poisson has mean equal to variance, but normal variance is `sigma^2`, not generally equal to its mean. Option c is also too strong because Poisson can be close to symmetric for large `lambda`. |
| 1.9 Order-up-to versus Newsvendor | b | Order-up-to chooses `S`; Newsvendor chooses order quantity `Q`. |
| 1.10 On-hand and backorder after demand | c | With 50 on hand and demand 80, on-hand inventory is 0 and backorder is 30. |
| 1.11 COVID supply-chain design implication | d | The crisis affected global supply chains heavily and is likely to change supply-chain and distribution-network design. |
| 1.12 COVID and bullwhip | c | Demand spikes/drops plus supply shocks can be amplified by bullwhip dynamics. |

### Exercise 2: Inventory Management

Book shop assumptions:

```text
Order once per week
Lead time l = 2 weeks
Demand per week ~ Poisson(lambda = 3)
Exposure horizon = l + 1 = 3 weeks
Aggregate demand during exposure horizon ~ Poisson(lambda = 9)
Annual holding cost = 30% of item value
Weekly holding cost = 30%/52 of item value
Weekly backorder cost = 15% of item value
```

#### 2.a Optimal service level

```text
SL* = b / (b + h)
b = 0.15
h = 0.30/52 = 0.005769
SL* = 0.15 / (0.15 + 0.005769)
SL* = 0.96296 = 96.30%
```

#### 2.b Optimal in-stock probability

In this order-up-to model, the optimal in-stock probability is the same target service level:

```text
96.30%
```

#### 2.c Order-up-to level for a 95% service level

Aggregate weekly demand over `l+1 = 3` weeks:

```text
lambda_aggregate = 3*3 = 9
```

Find the smallest integer `S` with:

```text
P(D <= S) >= 0.95, where D ~ Poisson(9)
```

Poisson CDF check:

```text
P(D <= 14) = 95.85%
```

Thus:

```text
S = 14 books
```

#### 2.d Stockout probability for S = 15

```text
P(stockout) = P(D > 15) = 1 - P(D <= 15)
```

For `D ~ Poisson(9)`:

```text
P(D <= 15) = 97.79%
P(stockout) = 2.21%
```

#### 2.e Distributor normal order-up-to level

Inputs:

```text
l = 8 weeks
Exposure horizon = l + 1 = 9 weeks
Weekly demand ~ Normal(mu = 300, sigma = 120)
h = 35%/52 per week
b = 20% per week
```

Service level:

```text
SL* = 0.20 / (0.20 + 0.35/52)
SL* = 0.96743 = 96.74%
```

Aggregate demand:

```text
mu_9 = 9*300 = 2700
sigma_9 = sqrt(9)*120 = 360
```

Normal quantile:

```text
z_0.96743 = 1.84
S = mu_9 + z*sigma_9
S = 2700 + 1.84*360
S = 3362.40 books
```

For integer inventory, use approximately `3363 books` if the target must be met or exceeded.

#### 2.f Random variable statement

The statement is correct. A random variable is a function from outcomes in a sample space to numerical values. In SCM it is a model of uncertain reality, such as weekly demand, delivery delay, or number of returns. It is not reality itself; it is a simplified representation that allows the manager to compute probabilities, service levels, expected backorders, and inventory targets.

### Exercise 3: Supply Chain Coordination

#### 3.a Order-up-to level for 98% service

Inputs:

```text
Demand ~ Normal(mu = 1000, sigma = 30)
Required service level = 98%
z_0.98 = 2.05
```

Calculation:

```text
S = mu + z*sigma
S = 1000 + 2.05*30
S = 1061.61
```

If non-integer amounts are allowed, `S = 1061.61 units`.

#### 3.b Standard deviation of orders under optimal order-up-to decisions

With a simple order-up-to policy and no batching, the replenishment order in each period equals the previous period's demand, assuming the system is reviewed regularly and inventory position is restored to `S`.

Therefore:

```text
sigma_orders = sigma_demand = 30 units
```

The order-up-to level changes the target inventory position, but under the basic model it does not amplify order variability by itself.

#### 3.c Effect of batching orders in lots of 25

Batching increases order variability. Instead of ordering exactly what demand consumed every period, the firm waits until enough demand accumulates or rounds orders into chunks of 25. This creates periods with no order and periods with larger orders.

Operationally:

```text
Customer demand may move smoothly.
Retailer orders become lumpy.
Upstream suppliers see amplified variability.
```

Thus the standard deviation of orders increases relative to the no-batching order-up-to case.

#### 3.d Literature name

This amplification is part of the bullwhip effect.

### Exercise 4: Supply Chain Network Design

The graph shows:

```text
P1 serves C1
P2 serves C1 and C2
P3 serves C2
Opening costs: P1 = 6, P2 = 2, P3 = 3
```

#### 4.a MILP formulation

Decision variables:

```text
y_i = 1 if plant i is opened, 0 otherwise
```

Objective:

```text
min 6y_1 + 2y_2 + 3y_3
```

Coverage constraints:

```text
C1 covered: y_1 + y_2 >= 1
C2 covered: y_2 + y_3 >= 1
```

Domains:

```text
y_1, y_2, y_3 in {0,1}
```

#### 4.b Location-covering heuristic

Use cost per newly covered customer:

| Plant | Newly covered customers at start | Cost | Cost per newly covered customer |
|---|---:|---:|---:|
| P1 | 1 | 6 | 6.00 |
| P2 | 2 | 2 | 1.00 |
| P3 | 1 | 3 | 3.00 |

Choose `P2`. It covers both `C1` and `C2`.

Heuristic solution:

```text
Open P2 only.
Total cost = 2.
```

#### 4.c Does the heuristic find the optimum?

Yes.

Proof by enumeration:

```text
Open P2 only: cost 2, covers C1 and C2.
Open P1 and P3: cost 9, covers C1 and C2.
Open P1 and P2: cost 8.
Open P2 and P3: cost 5.
Open all: cost 11.
P1 only or P3 only are infeasible.
```

The lowest feasible cost is `2`, so the heuristic solution is optimal.

#### 4.d Why TSP subtour constraints only need |S| <= ceil(|V|/2)

In a symmetric TSP, every subtour on a subset `S` has a complementary subset `V \ S`. A disconnected tour separating `S` from the rest of the graph can be detected from either side of the cut.

If `|S| > |V|/2`, then:

```text
|V \ S| < |V|/2
```

The same violated separation can be represented by the smaller complement `V \ S`. Therefore it is sufficient to write subtour-elimination constraints only for subsets up to half the node set. Larger subsets duplicate the same cut logic through their complements.

#### 4.e Is there a Dijkstra-like algorithm for TSP?

No comparable efficient algorithm is known for the general TSP. Dijkstra solves shortest path because the problem has optimal substructure: once the shortest distance to a node is fixed, it does not need to be revisited.

TSP is different because the decision is a complete tour visiting all nodes exactly once. A locally short edge can later force an expensive route, and subtours must be prevented. The general TSP is combinatorial and NP-hard, so exact solution methods usually require enumeration, branch-and-bound, cutting planes, or integer programming rather than a simple polynomial-time shortest-path algorithm.

### Exercise 5: Practice Problems

#### 5.a Factoring, reverse factoring, and supply chain finance

| Concept | Meaning | Exam distinction |
|---|---|---|
| Factoring | Supplier sells its receivable to a financial provider. | Supplier-led receivables financing. |
| Reverse factoring | Buyer approves invoices and enables supplier early payment through a funder. | Buyer-led approved-invoice financing. |
| Supply chain finance | Broader coordinated approach to improve working capital and liquidity across supply-chain partners. | Practical umbrella including platforms, onboarding, data, and payment-process design. |

#### 5.b SCF as win-win-win and supplier onboarding

The statement is too optimistic.

SCF can be win-win-win when:

```text
Supplier receives cash earlier at a lower financing rate.
Buyer preserves or extends payment terms.
Bank/funder earns a financing spread on relatively low-risk approved invoices.
```

But onboarding is not a minor problem. Suppliers may mistrust the program, face platform effort, dislike fees, worry that the buyer is simply extending payment terms, or already have cheap financing. Adoption depends on efficiency benefits and legitimacy: suppliers join faster when the financing-cost reduction is real and comparable suppliers already treat SCF as normal.

#### 5.c Key problem in the HP/PH case

The key problem is matching uncertain regional printer demand with supply while controlling inventory, service levels, and lead times. The classic HP issue is product variety and regional uncertainty: printers are produced centrally, but demand differs across regions and product versions. Long replenishment lead times force high inventory or poor availability.

#### 5.d Root causes and modern technology response

Root causes:

1. Long physical lead times from central production to regional markets.
2. Demand uncertainty by region and product variant.
3. Product variety caused by localization requirements.
4. Inventory tied up before demand is known.

Modern technology responses:

| Technology | How it helps |
|---|---|
| Better demand sensing and forecasting | Uses sell-through data, retailer data, and online signals to update regional forecasts faster. |
| Postponement-enabled modular production | Keeps generic printers common for longer and localizes late, reducing wrong-region inventory. |
| Real-time inventory visibility | Shows stock and pipeline inventory across regions, reducing overreaction and emergency shipments. |
| Advanced planning/optimization | Balances service level, transportation lead time, and working capital under uncertainty. |

Exam-safe recommendation: combine postponement with demand visibility. Technology helps most when it reduces the time between true demand information and the final product-allocation decision.

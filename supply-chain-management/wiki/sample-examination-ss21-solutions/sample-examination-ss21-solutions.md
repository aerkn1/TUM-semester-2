# Sample Examination SS21: Thorough Solutions

Source: `supply-chain-management/raw/moodle-export-operations-950888956-s26-20260604/Sample Examinations/Sample Examination from SS21.pdf`

Generated: 2026-07-08

These answers are derived from the local SCM notes and the sample PDF. The PDF has a few extraction/font issues; where answer options are not recoverable from the source, this file marks the omission and gives the concept solution.

## Production Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1.1 Distributions | c | The normal distribution is continuous. Poisson is discrete, normal CDFs do have inverse quantiles, and continuous PDF values can exceed 1. |
| 1.2 EOQ cost balance | d | At `Q*`, annual inventory holding cost equals annual ordering/setup cost in the basic EOQ model. |
| 1.3 Capacity utilization | b | Utilization is used capacity divided by available capacity. |
| 1.4 Customized apparel with customer-defined material | b | Engineer-to-order fits when the customer's requirements affect product design/material characteristics before production. |
| 1.5 Order-up-to model | a | It is a multi-period inventory model with random demand and fixed lead time. |
| 1.6 Bottleneck | a | The bottleneck is the least-capacity activity and defines process capacity. |
| 1.7 Little's Law inventory | a | Flow rate `R = 160 units/hour`; flow time `T = 120 min = 2 hours`; `I = R*T = 320 units`. |
| 1.8 Forecast control limits | a | `UCL/LCL = +/- z*sqrt(MSE) = +/- 1.96*sqrt(15) = +/- 7.59`. |
| 1.9 Lean transformation | c | Poka-yoke reduces process errors and is a lean tool. |
| 1.10 EPQ batch size | a | `Q* = sqrt((2*20*250/5) * 300/(300-250)) = sqrt(12000) = 109.54`. |
| 1.11 Random variable | d | A random variable maps real-world outcomes/events into numerical values. |
| 1.12 Value in lean | a | Value is what the customer is willing to pay for. |

### Exercise 2: Forecasting

Actual demand:

| Period | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Demand | 97 | 121 | 159 | 127 | 175 | 135 | 143 |

#### 2.a Required forecast values

Naive with trend:

```text
F_t = A_(t-1) + (A_(t-1) - A_(t-2))
F_5 = A_4 + (A_4 - A_3)
F_5 = 127 + (127 - 159)
F_5 = 95
```

Exponential smoothing with `alpha = 0.7`, initial forecast `100`:

```text
F_2 = 0.7*97 + 0.3*100 = 97.90
F_3 = 0.7*121 + 0.3*97.90 = 114.07
F_4 = 0.7*159 + 0.3*114.07 = 145.52
F_5 = 0.7*127 + 0.3*145.52 = 132.56
F_6 = 0.7*175 + 0.3*132.56 = 162.27
F_7 = 0.7*135 + 0.3*162.27 = 143.18
```

Answer:

```text
Exponential smoothing forecast for period 7 = 143.18
```

Linear regression using period numbers `t = 1,...,7`:

```text
Demand = intercept + slope*t
intercept = 110.71
slope = 6.50
```

Forecast for period 3:

```text
F_3 = 110.71 + 6.50*3 = 130.21
```

#### 2.b MAD and MSE for periods 3-7

| Method | MAD | MSE | Interpretation |
|---|---:|---:|---|
| Naive with trend | 60.00 | 4308.80 | The trend method overreacts to alternating changes. |
| Exponential smoothing | 26.67 | 981.34 | Good, but still worse than regression on this sample. |
| Linear regression | 19.64 | 464.89 | Best by both MAD and MSE over periods 3-7. |

Correct best method: linear regression, because it has the lowest MAD and MSE on the same validation window.

#### 2.c Error criterion and optimal alpha

If large forecast deviations are especially costly, use MSE because squaring errors penalizes large misses more strongly than MAD.

Using Solver to minimize MSE for periods 3-7 with `0 <= alpha <= 1` gives:

```text
alpha ~= 0.56
```

The exact value depends slightly on whether the validation window starts at period 2 or period 3; both conventions give about `0.55-0.56`.

### Exercise 3: Process Analysis

Available capacity per workstation:

```text
8 hours/day = 480 minutes/day per employee
```

#### 3.a Capacity requirement for workstation 1 producing product 1

```text
Product 1 demand = 40 units/day
Workstation 1 time for product 1 = 6 min/unit
Daily requirement = 40*6 = 240 min/day
```

#### 3.b Utilization of workstation 3 if all demand is produced

Workstation 3 time requirement:

```text
Product 1: 40*2 = 80 min/day
Product 2: 45*7 = 315 min/day
Product 3: 60*3 = 180 min/day
Total = 575 min/day
```

Capacity:

```text
1 employee * 480 min/day = 480 min/day
```

Utilization:

```text
575/480 = 1.1979 = 119.79%
```

This means workstation 3 cannot meet the full demand mix with the current staffing.

#### 3.c Bottleneck workstation

Daily utilization by workstation:

| Workstation | Required minutes/day | Capacity minutes/day | Utilization |
|---:|---:|---:|---:|
| 1 | 915 | 960 | 95.31% |
| 2 | 740 | 960 | 77.08% |
| 3 | 575 | 480 | 119.79% |
| 4 | 435 | 480 | 90.63% |
| 5 | 760 | 960 | 79.17% |

The bottleneck is workstation 3. It is the only workstation above 100% utilization.

#### 3.d Employees needed to meet all demand

Employees required per workstation:

```text
required employees = ceil(required minutes / 480)
```

| Workstation | Required minutes | Required employees | Current employees | Add |
|---:|---:|---:|---:|---:|
| 1 | 915 | 2 | 2 | 0 |
| 2 | 740 | 2 | 2 | 0 |
| 3 | 575 | 2 | 1 | 1 |
| 4 | 435 | 1 | 1 | 0 |
| 5 | 760 | 2 | 2 | 0 |

Answer: add 1 employee to workstation 3.

#### 3.e Whether to add workers to resource 3 when product 2 is most valuable

The best answer is: information is not enough for a conclusive optimization recommendation.

Why:

- We know product 2 has a high margin relative to the others.
- We do not know the absolute margin, worker cost, hiring constraints, or whether unmet demand is lost/backordered.
- We can say workstation 3 is the capacity bottleneck, but the profit-optimal staffing decision needs economics, not only minutes.

#### 3.f Flow rate per hour under the fixed demand mix

Demand mix:

```text
Product 1 : Product 2 : Product 3 = 40 : 45 : 60
```

Workstation 3 is bottleneck and requires `575 min/day` to produce the full mix. It has `480 min/day`.

Scaling factor:

```text
480/575 = 0.83478
```

Daily feasible production in the same mix:

```text
Product 1 = 40*0.83478 = 33.39 units/day
Product 2 = 45*0.83478 = 37.57 units/day
Product 3 = 60*0.83478 = 50.09 units/day
```

Per hour:

```text
Product 1 = 33.39/8 = 4.17 units/hour
Product 2 = 37.57/8 = 4.70 units/hour
Product 3 = 50.09/8 = 6.26 units/hour
Total = 15.13 units/hour
```

### Exercise 4: EOQ and Lean

Karl operates 4 warehouses.

Known inputs per warehouse:

```text
Demand = 1800 e-axles/year
Order cost K = EUR 300/order
Holding excluding capital = EUR 150/unit/year
Capital cost = 10% * EUR 1750 = EUR 175/unit/year
Total h = 150 + 175 = EUR 325/unit/year
```

#### 4.a Total logistics cost before pooling

Minimum EOQ relevant cost per warehouse:

```text
TC_warehouse = sqrt(2*K*lambda*h)
TC_warehouse = sqrt(2*300*1800*325)
TC_warehouse = EUR 18,734.99
```

Four warehouses:

```text
TC_total = 4*18,734.99 = EUR 74,939.98
```

Rounded to zero decimals:

```text
EUR 74,940
```

#### 4.b Cost savings from pooling

For `n = 4` identical warehouses:

```text
Savings = 1 - 1/sqrt(n)
Savings = 1 - 1/sqrt(4)
Savings = 50.00%
```

#### 4.c Savings if demand at each warehouse rises by 50%

The percentage saving from pooling identical EOQ systems depends on the number of warehouses, not the absolute demand level:

```text
Savings = 1 - 1/sqrt(4) = 50.00%
```

The euro amount of savings changes, but the percentage remains `50.00%`.

#### 4.d EOQ cost-balance statement

The statement is correct under the basic EOQ assumptions. At `Q*`, annual ordering/setup cost equals annual inventory holding cost.

#### 4.e Effect of in-house production on annual setup cost

With finite production rate `p`, the EPQ optimum is:

```text
Q_EPQ = Q_EOQ * sqrt(p/(p-lambda))
```

Since `p/(p-lambda) > 1`, EPQ uses a larger batch size than EOQ. Larger batches mean fewer setups per year:

```text
annual setup cost = K*lambda/Q
```

Therefore, annual setup cost decreases compared with the basic EOQ ordering case, assuming `K` and demand stay the same.

#### 4.f Production system for mobile phones

Choose assemble-to-order.

Reason:

- 90% of parts are standardized.
- Only 10% are brand-specific.
- Total manufacturing and assembly takes 3 weeks, but the customer expects delivery within 4 days.
- Demand is random, so making all brand-specific finished phones to stock risks wrong inventory.

Operational interpretation: manufacture or stock common modules in advance, then complete the brand-specific final assembly after the customer order. This is postponement.

### Exercise 5: Practice Problems

#### 5.a Kristen Cookies: capacity improvement

Improve the oven/baking step, for example by buying a larger oven or adding a second oven. The oven is the bottleneck at 6 dozen/hour, so improving non-bottleneck activities such as payment does not increase system capacity unless the bottleneck moves.

#### 5.b Kristen Cookies: demand improvement

Use online ordering, targeted promotions, or partnerships to smooth and increase demand. The recommendation must not overload the oven bottleneck. A good demand improvement should either fill idle periods or help forecast demand, not simply create a peak the process cannot serve.

#### 5.c Comment on MTO and one-hour lead time

The statement is false. Kristen Cookies is make-to-order, but that does not imply lead time must be at least one hour.

The one-dozen process takes about 27 minutes for the first order, and steady-state cycle time is 10 minutes per dozen when the oven is bottleneck. Lead time can be reduced by redesigning the process, improving the bottleneck, preparing some generic inputs, or better scheduling. The risk is that too much preproduction would weaken freshness and customization.

#### 5.d OceanCove customer values and pandemic effect

Core customer values:

- good food
- low prices
- fast and reliable service
- convenience
- casual dining experience

A 30% capacity restriction harms customer value by reducing seating availability, increasing waiting risk, weakening the dine-in atmosphere, and lowering revenue per hour. The kitchen may still have capacity, but the dining-room constraint prevents using it for dine-in customers.

#### 5.e Seating expansion versus delivery partnership

Normal lunch dining capacity with 120 seats:

```text
120 seats / 0.75 hours = 160 seat-turns/hour
```

Under a 30% restriction:

```text
Available seats = 120*30% = 36
Dine-in capacity = 36/0.75 = 48 customers/hour
```

If seating is increased to 160:

```text
Available seats = 160*30% = 48
Dine-in capacity = 48/0.75 = 64 customers/hour
Increment = 16 customers/hour
```

Delivery can use spare kitchen capacity beyond dine-in. Since OceanCove's assembly capacity is about `144 meals/hour`, a 48 customers/hour dine-in restriction leaves substantial potential kitchen capacity. Even with a 10% margin loss, delivery is operationally attractive if it fills otherwise idle kitchen capacity and does not damage food quality or dine-in service.

Recommendation: partner with a delivery service, with order caps and quality controls. Seating expansion alone gives only `+16 customers/hour` under the 30% rule.

## Logistics Module

### Exercise 1: Multiple Choice

| Question | Correct answer | Explanation |
|---|---|---|
| 1 Bullwhip mitigation not true | a | Information sharing is useful but not easy; trust, incentives, systems, and data definitions make it hard. |
| 2 EDLP not true | c | EDLP reduces strategic buying and volatility; it does not increase strategic buying. |
| 3 Knapsack objective | a | The objective is to maximize the total value selected subject to the weight/capacity constraint. |
| 4 Newsvendor, EOQ, order-up-to values | c | They combine physical units with monetary tradeoffs. |
| 5 Corona and SCF | a | COVID increased interest in SCF because supplier liquidity and payment timing became more critical. |
| 6 Operations strategy | a | Strategic decisions must align with operational decisions. |
| 7 Shortage gaming category | c | In the lecture framing, shortage gaming is tied to individual incentives. |
| 8 Yeezy preorder example | b | This is shortage gaming due to individual incentives: customers inflate orders because they expect scarcity. |
| 9 Same in Newsvendor and order-up-to | d | Both explicitly consider random demand. |
| 10 `P(D <= Q)` | d | It is the in-stock probability and, in these models, the achieved service level. |
| 11 Newsvendor not true | b | Newsvendor is single-period; leftover inventory is generally not carried to the next selling season. Option c is also imprecise because the model uses monetary underage/overage costs. |
| 12 Poisson normal approximation | c | Use `mu = lambda` and `sigma^2 = lambda`. |

### Exercise 2: Inventory Management

Inputs:

```text
Weekly review
Lead time l = 3 weeks
Exposure horizon = l + 1 = 4 weeks
Weekly demand ~ Poisson(lambda = 16)
Aggregate demand ~ Poisson(lambda = 64)
Annual holding cost = 30% of desk value
Weekly holding cost h = 30%/52
Weekly backorder cost b = 20%
```

#### 2.a Optimal service level

```text
SL* = b/(b+h)
SL* = 0.20 / (0.20 + 0.30/52)
SL* = 0.97196 = 97.20%
```

#### 2.b Optimal order-up-to level under Poisson demand

Find the smallest integer `S` with:

```text
P(D <= S) >= 0.97196, D ~ Poisson(64)
```

CDF check:

```text
P(D <= 80) = 97.74%
```

Answer:

```text
S = 80 desks
```

#### 2.c Optimal service level after normal approximation

The cost-based service level does not change when the demand distribution changes:

```text
SL* = 97.20%
```

The distribution affects the quantity `S`, not the service-level formula.

#### 2.d Normal order-up-to level

Weekly approximation:

```text
D_week ~ Normal(mu = 16, sigma^2 = 16)
sigma_week = 4
```

Four-week aggregate demand:

```text
mu_4 = 4*16 = 64
sigma_4 = sqrt(4)*4 = 8
```

Quantile:

```text
z_0.97196 = 1.91
S = 64 + 1.91*8 = 79.28 desks
```

If an integer level must meet or exceed the target, use `80 desks`.

#### 2.e Expected backorder, leftover inventory, and sales

Given expected lost sales/backorder quantity:

```text
B(S) = 0.02 desks
```

Using the normal `S = 79.28` and aggregate mean `mu = 64`:

Expected backorder quantity:

```text
B(S) = 0.02 desks
```

Expected leftover inventory:

```text
I(S) = S - mu + B(S)
I(S) = 79.28 - 64 + 0.02
I(S) = 15.30 desks
```

Expected sales:

```text
Expected sales = mu - B(S)
Expected sales = 64 - 0.02
Expected sales = 63.98 desks
```

#### 2.f Newsvendor with uniform demand

Inputs:

```text
Demand ~ Uniform(150, 300)
Cost = EUR 2/unit
Profit margin = EUR 3/unit
```

Underage and overage:

```text
c_u = 3
c_o = 2
SL* = c_u/(c_u+c_o) = 3/(3+2) = 0.60
```

Uniform quantile:

```text
Q* = 150 + 0.60*(300-150)
Q* = 240 units
```

### Exercise 3: Supply Chain Coordination

#### 3.a Demand increase

Retailer orders increased from 200 to 350 packs:

```text
Increase = (350 - 200)/200 = 0.75 = 75%
```

#### 3.b Stage affected most

The most upstream stages are affected most. The retailer sees the consumer change first; the manufacturer and raw-material supplier often see an amplified signal because each stage orders protectively, updates forecasts, and may batch or overreact.

#### 3.c Source omission: missing MC statements

The PDF text and rendered page do not expose the listed answer statements for this subquestion. The correct concept is:

- Distorted demand can cause excess inventory if the spike fades.
- It can cause stockouts and capacity overload if the spike is real and supply is constrained.
- It can cause poor production planning, overtime, emergency purchasing, and higher logistics cost.
- It can create later order cancellations and demand drops upstream.

Any answer choice that claims the manufacturer now sees true end-customer demand would be incorrect.

#### 3.d Cause and category

Cause: reactive or overreactive ordering based on a sudden demand signal.

Category: behavioral factors and information distortion. If the retailer intentionally orders more than needed because of scarcity allocation rules, it becomes shortage gaming under individual incentives. In this almond milk story, the core cause is overreaction to a social-media demand shock.

Example:

```text
Consumers buy 75% more almond milk for one week.
Retailer orders 75% more or even more to avoid stockouts.
Manufacturer interprets the order spike as a persistent demand increase.
Supplier sees an even larger raw-material order.
```

That is the bullwhip effect.

### Exercise 4: Supply Chain Network Design

The graph shows:

```text
P1 serves C1
P2 serves C1 and C2
P3 serves C2
Opening costs: P1 = 4, P2 = 5, P3 = 7
```

#### 4.a MILP formulation

Decision variables:

```text
y_i = 1 if plant i is opened, 0 otherwise
```

Objective:

```text
min 4y_1 + 5y_2 + 7y_3
```

Coverage:

```text
C1: y_1 + y_2 >= 1
C2: y_2 + y_3 >= 1
```

Domain:

```text
y_1, y_2, y_3 in {0,1}
```

#### 4.b Location-covering heuristic

Initial cost per newly covered customer:

| Plant | Covers | Cost | Cost/new customer |
|---|---|---:|---:|
| P1 | C1 | 4 | 4.00 |
| P2 | C1, C2 | 5 | 2.50 |
| P3 | C2 | 7 | 7.00 |

Choose `P2`, which covers both customers.

Heuristic solution:

```text
Open P2 only.
Total cost = 5.
```

#### 4.c Optimality proof

Feasible alternatives:

```text
P2 only: cost 5
P1 + P3: cost 11
P1 + P2: cost 9
P2 + P3: cost 12
All plants: cost 16
```

`P1 only` and `P3 only` are infeasible. Therefore `P2 only` is optimal.

#### 4.d Knapsack

Capacity:

```text
12 kg
```

Items:

| Item | Weight | Value |
|---|---:|---:|
| Sleeping bag | 8 | 12 |
| Torch | 1 | 5 |
| Water bottle | 2 | 8 |
| Rope | 3 | 2 |
| Laptop | 6 | 6 |

Best feasible set:

```text
Sleeping bag + torch + water bottle
Weight = 8 + 1 + 2 = 11 kg
Value = 12 + 5 + 8 = 25
```

Answer: pack the sleeping bag, torch, and water bottle.

### Exercise 5: Practice Problems

#### 5.a SCF solution for buyer and suppliers

Potential solution: reverse factoring / supply chain finance.

The buyer can keep later payment terms, while suppliers can receive early payment from a bank or SCF provider after the buyer approves the invoice.

#### 5.b Parties involved

The core parties are:

1. Buyer.
2. Supplier(s).
3. Bank or SCF provider/platform.

#### 5.c Benefits for all parties

| Party | Benefit |
|---|---|
| Supplier | Gets cash earlier and may finance at a lower rate based on the buyer's credit quality. |
| Buyer | Can preserve or extend DPO while keeping suppliers liquid and stable. |
| Bank/provider | Earns financing fees on approved invoices with relatively transparent credit risk. |

#### 5.d Implementation difficulties for buyers

Common difficulties:

- Supplier onboarding is slow and requires trust.
- Smaller suppliers may lack platform capability.
- Suppliers may suspect the buyer is using SCF to force longer payment terms.
- Legal, accounting, data, and process integration can be complex.
- Benefits depend on the financing-rate gap between supplier and buyer/provider.

#### 5.e HP KPIs

Three relevant HP KPIs:

| KPI | Why it matters |
|---|---|
| Service level / product availability | Measures whether regional demand is met without stockouts. |
| Inventory value / days of inventory | Captures working capital tied up in printers and localized stock. |
| Order lead time / replenishment lead time | Drives how much inventory is needed and how fast HP can react to regional demand changes. |

Other acceptable KPIs: forecast error, obsolescence cost, transportation cost, localization delay, and in-transit inventory value.

#### 5.f Main HP issues

Main issues:

- regional demand uncertainty
- product localization and variety
- long transportation lead times from centralized production
- high inventory and working-capital cost
- service-level pressure in each market

The core tradeoff is service level versus inventory risk.

#### 5.g Two modern technologies for HP

1. Real-time demand sensing and advanced forecasting.
   - Helps HP distinguish true regional demand from noise and allocate inventory earlier.
2. Digital postponement/localization planning with modular product design.
   - Keeps printers generic longer and localizes later, reducing wrong-market stock.

Other valid technologies: IoT inventory tracking, supply-chain control towers, integrated planning systems, and faster regional 3D/late-stage configuration tools. The best answer links technology to the key issue: reducing uncertainty before the final localization/allocation decision.

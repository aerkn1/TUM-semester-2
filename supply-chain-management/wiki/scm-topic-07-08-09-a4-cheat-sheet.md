# SCM Topics 07-09 A4 Formula Cheat Sheet

Local check: no `topic-07` wiki note or raw folder exists in this workspace. Do not invent Topic 07; verify the Moodle title if it appears in an exam prompt.

```text
Exam move: decision layer -> formula/model -> units -> result -> operational meaning
```

## 08 Process Analysis / Capacity

Core formulas:

```text
Little's Law: I=R*T; R=I/T; T=I/R
Capacity = parallel resources / processing time per unit
Utilization = actual flow / capacity
System capacity = min required-step capacities
Lead time = queue/wait + processing
Queue waiting time = avg waiting inventory / avg flow rate
```

OceanCove anchors:

```text
Peak lunch: I=30 tables*3=90 customers; T=45/60=0.75 h
R=90/0.75=120 customers/h = 2 orders/min

Assembly: 25 sec/meal = 25/3600 h -> 144 meals/h
Waiters: 6/(6/60 h/table)=60 tables/h -> *3 = 180 customers/h
Lunch seats: 120/(45/60)=160 seat-turns/h; *3/4 occupancy = 120 customers/h
Dinner seats: 120/(82.5/60)=87.27 seat-turns/h; *3/4 = about 65 customers/h
```

Fish mix capacity:

```text
2:1 grilled:fried. Let fried=x, grilled=2x, total=3x.
Fried: x<=90; grilled: 2x<=300 -> x<=150
Binding x=90 -> total fish capacity=90+180=270 fish meals/h
```

Bottlenecks / lead time:

```text
Lunch capacity = min(270 fish, 400 fries, 144 assembly, 180 waiters, 160 seats)
= 144 meals/h -> assembly bottleneck.
Dinner bottleneck = dining area because stay time is longer.

Fast grilled meal = order 3 + grill 4 + assembly 25 sec + deliver 3 = 10m25s
Peak queue wait = 26 orders / 2 orders/min = 13 min
Peak non-rushed lead time = 13 + 10m25s = 23m25s
```

Expansion / revenue:

```text
160 seats lunch: 160/(45/60)=213.33 seat-turns/h; *3/4=160 customers/h
Lunch after expansion = min(160 dining flow, 144 assembly)=144 meals/h
Revenue = price * flow * duration
Contribution = full-capacity revenue * utilization * net margin
```

Other exercise anchors:

```text
ProfiCutZ: flow time = process+waiting = 60 min = 1 h.
Before hiring: admin 12/h, washing 12/h, hairdressing 10/h -> bottleneck 10/h.
I=R*T=10 customers/h*1h=10 customers.
After flexible hiring: test required worker-minutes <= available worker-minutes.

Circored: time = quantity / flow rate.
Demand flow = 657000/(365*24)=75 tons/h.
25000 tons / 75 tons/h = 333.33 h.
Bottleneck cap = 100 tons/h -> overall utilization = 75/100 = 75%.

Gantt: schedule earliest feasible start respecting predecessors + qualified worker availability.
Project duration = calendar span, not sum of task durations.
```

Traps: do not add sequential capacities; convert min/sec to hours; demand/seats are not system capacity; after any improvement, recompute bottleneck; mix coefficients are required load, not extra capacity; lead time includes waiting.

## 09 Facility Location / Transportation / Shipping

Model router:

```text
Fixed facilities, ship quantities -> Transportation LP, x_ij continuous
Open facilities + ship -> CPLP, x_ij + binary y_i
Two tiers -> x_ijk + y_1j + y_2k
Cover demand points -> covering model, y_i + a_ij
One origin-destination route -> Dijkstra
Closed tour visiting all customers -> TSP
Select items under capacity -> knapsack
Competitive customer capture -> Hotelling
```

Transportation LP:

```text
min sum_i sum_j c_ij x_ij
Demand:   sum_i x_ij >= D_j or = d_j        [customer side]
Capacity: sum_j x_ij <= K_i                 [plant side]
x_ij >= 0
Graphical LP axes = decision variables, not map locations.
```

CPLP:

```text
min sum_i sum_j c_ij x_ij + sum_i f_i y_i
Demand: sum_i x_ij = d_j
Capacity activation: sum_j x_ij <= q_i*y_i
x_ij >= 0; y_i in {0,1}
y_i=0 -> plant ships 0; y_i=1 -> plant ships up to q_i.
```

Present-value route coefficient:

```text
PV factor = sum_{n=1}^N 1/(1+r)^n
Daily route cost = production cost + logistics cost/km * distance
PV route coefficient = daily route cost * 365 * PV factor
Total PV = variable PV + fixed opening costs
```

Two-echelon:

```text
x_ijk = flow to customer i through tier-1 j and tier-2 k
min sum_i sum_j sum_k c_ijk x_ijk + sum_j f_1j y_1j + sum_k f_2k y_2k
Demand: sum_j sum_k x_ijk = d_i
Tier 1 cap: sum_i sum_k x_ijk <= q_1j y_1j
Tier 2 cap: sum_i sum_j x_ijk <= q_2k y_2k
Positive x_ijk consumes capacity at both tiers.
```

Covering:

```text
min sum_i f_i y_i
sum_i a_ij y_i >= 1 for each customer j
y_i in {0,1}; a_ij=1 if facility i covers customer j under service standard.
Heuristic: open zero-cost facilities, then choose lowest f_i/n_i for remaining uncovered constraints.
Heuristic is not guaranteed optimal unless checked.
```

Routing models:

```text
Dijkstra: start=0, others=infinity. New label = current distance + edge cost.
Visit unvisited node with smallest total tentative distance; recover path via predecessors.
Not local cheapest-edge choice.

TSP: min sum c_ij x_ij; each node degree=2; one closed tour visits each node once.
Degree 2 is necessary, not sufficient -> eliminate subtours.
Tour length includes return edge.

Knapsack: max sum v_i x_i; sum w_i x_i <= W; x_i binary.
Value density v_i/w_i is intuition, not proof.

Hotelling equal-price line: boundary=(location A + location B)/2.
Market share = captured line length.
```

Traps: `x_ij` continuous in transportation but binary edge in TSP; do not omit fixed costs; closed facilities cannot ship; covering means reachable, not shipped quantity; Dijkstra is not TSP; interpret Solver variables/constraints.

## Last Line

```text
T08 = physical feasibility/capacity. T09 = network/location/routing. Identify scope before calculating.
```

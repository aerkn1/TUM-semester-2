# Topic 09 Facility Location, Transportation, And Shipping - Clarification Session 2026-07-02

Source note: [topic-09-facility-location-transportation-shipping.md](topic-09-facility-location-transportation-shipping.md)

Context companion: [CONTEXT.md](CONTEXT.md)

## Session Trigger

User asked:

> what actually is the graphical solution logic? I did not get the example with x11-x21 etc.?

Follow-up:

> also how about CLPLP? I need more detailed exercise solutions as in other topic wiki contents for topic-09

Interpretation:

- `CLPLP` was treated as `CPLP`, the local course term for **Capacitated Plant Location Problem**.
- The user needed EOQ-style worked ladders: formula -> substitution -> result -> unit -> interpretation.

## Clarification 1: Graphical LP Logic

Prompt/question:

> What do `x11` and `x21` represent in the graphical solution?

Refined answer:

```text
x11 = amount shipped from plant 1 to customer 1
x21 = amount shipped from plant 2 to customer 1
```

Corrected mental model:

```text
The graph is not a map of plants and customers.
It is a graph of possible shipping decisions.

horizontal axis = x11
vertical axis   = x21
```

Example:

```text
(30, 0) means ship 30 units from plant 1 and 0 units from plant 2.
(10, 20) means ship 10 units from plant 1 and 20 units from plant 2.
```

Key rule:

```text
x11 + x21 >= 30 means customer demand must be met.
```

Optimal logic:

```text
Plant 1 route cost = 80
Plant 2 route cost = 120

Since 80 < 120, use plant 1 first.
Optimal: x11 = 30, x21 = 0.
Cost: 80*30 + 120*0 = 2400.
```

Weak spot label: `yellow`

Reason: The user understood the general graph after clarification, but `xij` notation and axis interpretation need one recall pass.

## Clarification 2: CPLP Logic

Prompt/question:

> How about CLPLP / CPLP?

Refined answer:

```text
Transportation LP = choose shipment quantities xij from already-available plants.
CPLP = choose which plants open yi and how much they ship xij.
```

Key distinction:

```text
xij = shipment amount
yi  = binary open/closed facility decision
```

Capacity activation:

```text
sum_j xij <= qi yi
```

If `yi = 0`:

```text
sum_j xij <= qi*0 = 0
```

so the closed plant cannot ship.

If `yi = 1`:

```text
sum_j xij <= qi
```

so the open plant can ship up to capacity.

Weak spot label: `yellow`

Reason: The main confusion was not the objective formula itself, but why the binary `yi` is needed and how it switches capacity on/off.

## Clarification 3: Workbook Exercise Expansion

Files updated:

- Main note expanded under `Graphical Solution Logic`.
- Main note expanded under `Exercise 1b: Two-Plant CPLP`.
- Main note expanded under `Constructed Two-Echelon Worked Example`.
- Main note expanded under `Constructed Location Covering Worked Example`.
- Main note expanded under `Transportation And Shipping` with an exam routing guide and constructed Dijkstra worked example.
- Main note expanded under `Traveling Salesman Problem`, `Knapsack Problem`, and `Hotelling Competition` with exam vision guides and constructed examples.
- Main note expanded under `Workbook Covering Exercise`.
- `CONTEXT.md` updated with graphical LP, feasible point, route PV coefficient, daily shipment unit, two-echelon path language, and extra exam traps.

Important solved results:

```text
CPLP best plan:
y1 = 1, y2 = 1
x11 = 10, x12 = 0, x21 = 30, x22 = 50
total PV = EUR 6,507,961.66
```

```text
Covering workbook best/heuristic plan:
y1 = 1, y2 = 1, y3 = 0, y4 = 0
z = 2
```

## Clarification 4: Two-Echelon Model Depth

Follow-up:

> also not much depth for two-echelon model, maybe better to give a example use case with detailed calculations?

Refined answer:

```text
A two-echelon model is not only "which plant serves which customer".
It chooses a complete path:

customer i <- tier-1 facility j <- tier-2 supplier k

That is why the flow variable has three indices: x_ijk.
```

Constructed study example added to the main note:

```text
Tier 2 suppliers: S1, S2
Tier 1 distribution centers: A, B
Tier 0 retailers: R1, R2

Demand:
R1 = 30 units/day
R2 = 20 units/day
```

Best enumerated plan:

```text
y11 = 1  open DC A
y12 = 1  open DC B
y21 = 1  open supplier S1
y22 = 1  open supplier S2

x111 = 30  serve R1 through A and S1
x222 = 20  serve R2 through B and S2
all other x_ijk = 0
```

Cost ladder:

```text
Variable cost = 6*30 + 5*20 = 180 + 100 = 280
Fixed cost = 70 + 50 + 40 + 40 = 200
Total cost = 280 + 200 = 480
```

Tradeoff interpretation:

```text
Compared with opening only A and S1:
extra fixed cost = 90
variable-cost saving = 100
net saving = 10
```

The main note also includes an exhaustive open-set table for all feasible combinations of A/B and S1/S2, so the `480` result is not only an illustrative candidate.

Weak spot label: `yellow`

Reason: The notation `x_ijk` becomes intuitive only when the user sees that one shipped unit consumes capacity at both an intermediate facility and an upstream supplier.

## Clarification 5: Location Covering Difference And Example

Follow-up:

> how about the location covering problem ? where it differs and also provide an example for it too.

Refined answer:

```text
Transportation/CPLP/two-echelon models move quantities.
Location covering models select sites so every demand point is reachable.
```

Core distinction:

| Model | Decision | Meaning of service |
|---|---|---|
| Transportation LP | choose `x_ij` | ship units from existing plants |
| CPLP | choose `y_i` and `x_ij` | open plants and ship units |
| Two-echelon | choose `y_1j`, `y_2k`, `x_ijk` | open two tiers and assign full paths |
| Location covering | choose `y_i` only | every demand point is covered at least once |

Constructed emergency-station example added to the main note:

```text
Candidate stations:
A cost 5
B cost 4
C cost 6
D cost 3

Neighborhoods:
C1, C2, C3, C4, C5
```

Covering constraints:

```text
C1: y1 + y4 >= 1
C2: y1 + y2 >= 1
C3: y2 >= 1
C4: y2 + y3 >= 1
C5: y3 + y4 >= 1
```

Solving logic:

```text
C3 forces y2 = 1.
Station B covers C2, C3, and C4.
Remaining uncovered: C1 and C5.
Station D covers both C1 and C5 at cost 3.
```

Solution:

```text
y1 = 0
y2 = 1
y3 = 0
y4 = 1

z = 5*0 + 4*1 + 6*0 + 3*1
z = 7
```

Weak spot label: `yellow`

Reason: The main exam risk is treating `y_i` like a shipment quantity. In covering, `y_i = 1` means "site opened"; coverage is yes/no reachability through `a_ij`.

## Clarification 6: Transportation And Shipping Exam Vision

Follow-up:

> also I need clearer vision on transportation and shipping if it will require calculation ? or is it just a interpreation? or applying this Dijkstra's algorithm will require?

Refined answer:

```text
Transportation and shipping can be calculation or interpretation.
The question wording decides the method.
```

Decision rule:

| Trigger in question | Method | Calculation? |
|---|---|---|
| demands, capacities, route costs | transportation LP / CPLP | yes, calculate shipment costs or formulate model |
| "formulate" or "set up Solver" | write variables, objective, constraints | mostly setup |
| Solver output | interpret routes, binding constraints, objective | mostly interpretation |
| weighted network + shortest path from one node to another | Dijkstra | yes, algorithm table |
| visit every customer once and return | TSP | route/tour logic and subtour check |
| container/items/value/capacity | knapsack | selection calculation |

Correct mental model:

```text
Transportation = flow allocation.
Shipping/routing = path or tour selection.
```

Constructed Dijkstra example added:

```text
Edges:
A-B = 2
A-C = 5
B-C = 1
B-D = 7
C-D = 3

Shortest path from A to D:
A -> B -> C -> D
Total distance = 2 + 1 + 3 = 6
```

Key Dijkstra correction:

```text
Dijkstra does not simply choose the cheapest next edge.
It chooses the unvisited node with the smallest total tentative distance from the start.
```

Weak spot label: `yellow`

Reason: The user needed a higher-level exam router for deciding whether to formulate, calculate, interpret, or run Dijkstra.

## Clarification 7: TSP, Knapsack, And Hotelling Exam Vision

Follow-up:

> better to have the same for salesman, knapsack, hotelling competition

Refined answer:

```text
TSP, knapsack, and Hotelling can each be calculation or interpretation.
The exam trigger determines the routine.
```

Decision rule:

| Trigger in question | Method | Calculation? |
|---|---|---|
| visit all customers exactly once and return | TSP | yes, add full tour lengths |
| explain invalid route with cycles | TSP subtour check | mostly interpretation |
| choose items under capacity | knapsack | yes, compare feasible combinations |
| explain greedy/value density risk | knapsack | interpretation plus small comparison |
| firms compete on a line | Hotelling | maybe, compute market boundary if positions are given |
| explain why firms move toward the center | Hotelling | mostly interpretation |

Constructed TSP example added:

```text
Depot A, customers B, C, D.

Best checked tour:
A -> B -> D -> C -> A

Total distance:
2 + 4 + 3 + 9 = 18
```

Constructed knapsack example added:

```text
Capacity W = 10.
Best feasible selection:
x1 = 1, x2 = 1, x3 = 0, x4 = 0

capacity = 6 + 4 = 10
value = 30 + 24 = 54
```

Knapsack trap:

```text
Greedy by value density picks item 2 + item 3:
capacity = 4 + 5 = 9
value = 24 + 28 = 52

But item 1 + item 2 gives value 54.
```

Constructed Hotelling example added:

```text
Market line from 0 to 10.
Shop A at 3, Shop B at 7.

Boundary = (3 + 7) / 2 = 5.
Market split = 5 and 5.

If A moves to 4:
Boundary = (4 + 7) / 2 = 5.5.
A captures 5.5, B captures 4.5.
```

Weak spot label: `yellow`

Reason: The user needed the same exam-router clarity for the remaining Topic 09 models: TSP is full-tour calculation, knapsack is feasible-combination selection, and Hotelling is competitive customer-boundary logic.

## Corrected Mental Models

- **Graphical LP**: graph of decisions, not a geographic network.
- **Transportation LP**: choose only `xij`, because facilities are assumed available.
- **CPLP**: choose `yi` and `xij`, because opening a plant creates fixed cost and usable capacity.
- **Two-echelon model**: choose a full `i-j-k` path; every positive `x_ijk` consumes both tier-1 and tier-2 capacity.
- **Location covering model**: choose `yi` only; a customer is covered if at least one selected facility has `a_ij = 1`.
- **Transportation and shipping exam router**: first decide whether the task is flow allocation, site selection, one shortest path, full tour, or item selection.
- **TSP**: calculate full closed-tour length and check subtours.
- **Knapsack**: compare feasible selections; density is intuition, not proof.
- **Hotelling**: compute market boundary only if line positions are given; otherwise explain competitive location logic.
- **Route PV coefficient**: daily route cost becomes a multi-year present-value coefficient before comparing against opening cost.
- **Covering model**: choose facilities so every constraint/customer node is covered at least once; the selected facilities are not shipment quantities.

## Next Recall Prompts

1. In the graphical example, what does the point `(10,20)` mean operationally?
2. Why is `(10,10)` infeasible when demand is 30?
3. In the CPLP workbook exercise, why is plant 2 not enough by itself?
4. Why does plant 2 serve all of customer 2 before serving the remaining customer 1 demand?
5. Write the capacity activation constraint for plant 2 and explain what happens when `y2 = 0`.
6. In the two-echelon example, why does `x111 = 30` consume capacity at both DC A and supplier S1?
7. Write the demand constraint for retailer R1 in the constructed two-echelon example.
8. Write the tier-1 capacity constraint for DC B in the constructed two-echelon example.
9. Why does the all-open two-echelon plan beat the A+S1-only plan even though it has more fixed cost?
10. In the constructed covering example, why is `y2 = 1` mandatory?
11. In the constructed covering example, why does station D solve both remaining uncovered neighborhoods?
12. In the covering problem, why does `y2 = 1` happen first under the workbook heuristic?
13. Why is `y1 + y2` optimal in the workbook covering instance?
14. If an exam question gives demands, plant capacities, and route costs, is it a transportation calculation or Dijkstra?
15. If an exam question gives a weighted network and asks for one shortest path, which algorithm do you apply?
16. In the constructed Dijkstra example, why is the path `A -> B -> C -> D` better than `A -> C -> D`?
17. In the constructed TSP example, why must the edge returning to A be included?
18. In the constructed knapsack example, why is item 2 plus item 3 not the best feasible answer?
19. In the constructed Hotelling example, what happens to A's market share when it moves from 3 to 4?

## Remaining Weak Spots

| Weak Spot | Label | Corrective Drill |
|---|---|---|
| Interpreting `xij` as a physical coordinate instead of a shipment quantity | yellow | Translate three graph points into shipment plans. |
| Distinguishing transportation LP from CPLP | yellow | State whether `yi` is needed before writing the objective. |
| Interpreting `x_ijk` as only a customer-to-DC shipment | yellow | For one positive `x_ijk`, name the customer, tier-1 facility, tier-2 supplier, and both capacity constraints it affects. |
| Treating location covering as shipment allocation | yellow | State that `y_i` opens a site and `a_ij` is yes/no reachability; no `x_ij` quantity is chosen in the basic model. |
| Unclear whether transportation/shipping requires calculation or interpretation | yellow | Use the exam router: flow allocation -> transportation/CPLP; one shortest path -> Dijkstra; full tour -> TSP; Solver output -> interpretation plus checks. |
| Confusing TSP, knapsack, and Hotelling with transportation flow | yellow | TSP = closed tour; knapsack = item selection under capacity; Hotelling = competitive market boundary. |
| Comparing daily route cost without fixed/opening cost and PV conversion | yellow | Recompute one route PV coefficient from daily cost. |
| Treating covering variables as shipment quantities | yellow | Draw the bipartite facility-to-constraint coverage graph. |

## Schedule Impact

No `First Pass` or `D+n` checkpoint was advanced. This was a clarification and wiki-refinement session only. Topic 09 remains pending first pass.

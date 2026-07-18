# SCM Topics 10, 12, 13 A4 Cheat Sheet

Handwrite as 3 compact columns. Always show time base and units.

```text
Exam move: model -> formula -> substitution -> unit -> managerial meaning.
T10 = inventory target S. T12 = cash timing/resilience. T13 = waste/flow/pull.
```

## 10 Multi-Period Inventory / Order-Up-To

Model router:

```text
EOQ/EPQ -> efficient batch Q*
Newsvendor -> one-shot uncertain quantity q
Order-up-to -> target inventory position S over l+1 periods
(s,Q): order Q* when IP reaches s = S - Q*
```

State and service:

```text
Inventory level = on-hand - backorders
Inventory position IP = on-hand + on-order - backorders
Order quantity = S - IP              (if negative: order 0)
End inventory = S - D_(l+1)
SL(S)=F(S)=P(D<=S); stockout prob = 1-F(S)
B(S)=E[max(0,D-S)]      expected shortage
I(S)=E[max(0,S-D)] = S - mu + B(S)
SL* = c_u/(c_u+c_o)     choose smallest integer S with F(S)>=SL*
```

Demand aggregation:

```text
Protection period = review period + lead time = l+1 periods.
Normal: mu=mu_1*(l+1); sigma=sigma_1*sqrt(l+1)
Poisson: lambda=lambda_1*(l+1)
```

Normal formulas:

```text
z=(S-mu)/sigma
S=mu+z(SL)*sigma
B(S)=sigma*L(z)
L(z)=phi(z)-z[1-Phi(z)]
I(S)=S-mu+B(S)
```

Poisson formulas:

```text
F(S)=sum_{k=0}^S e^-lambda * lambda^k/k!
B(S)=sum_{k=S+1}^infty (k-S)P(D=k)
I(S)=S-lambda+B(S)
```

Exam anchors:

```text
Medtronic DC: monthly mu=349, sigma=122.38 -> weekly mu=80.54,
weekly sigma=58.81. With l=3: mu=322.4, sigma=117.62.
S=625 -> z=2.57, SL approx 99.50%, B approx 0.19, I approx 302.79.

Medtronic sales rep: monthly lambda=6.25, l=1 day.
daily lambda=6.25*12/(52*5)=0.2885; protection lambda=0.58.
S=3 -> F approx 99.70%, B approx 0.00335, I approx 2.42.
Cost target: h_day=0.35/360*p, b=0.75*0.50p -> SL* approx 99.74% -> S=4.

Speed Print: IP=523+180=703; S=700 -> no positive order.
99% target, weekly Normal 100/65, l=5:
mu=600, sigma=159.22, S=600+2.326*159.22=970.39 -> 971.

Printer Poisson: b=50, h=20 -> SL*=71.43%; l=3, lambda=100 -> S=106.
Laptop: c_o=50, c_u=39.98 -> SL*=44.43%; l=2:
mu=720, sigma=155.88, z approx -0.14 -> S approx 698.17 -> 699.
```

Traps: `S` is inventory position, not on-hand. Aggregate over `l+1`. For discrete demand choose smallest integer meeting target. Do not confuse EOQ `Q*` with order-up-to `S`.

## 12 Supply Chain Finance / Resilience

Working capital:

```text
AR = revenue * DSO/360
AP = COGS * DPO/360
NWC = AR + inventory - AP       if inventory=0: NWC=AR-AP
One DSO day = revenue/360
One DPO day = COGS/360
Cash conversion cycle = DIO + DSO - DPO
```

Reverse factoring / SCF:

```text
Flow: supplier delivers -> buyer approves invoice -> provider pays supplier
early net fee -> buyer pays provider later.
Supplier: lower DSO + cheaper financing.
Buyer: higher effective DPO without starving supplier liquidity.
Fee = invoice * annual SCF rate * days early/360
Supplier cash = invoice - fee
100000*5%*80/360 = 1111 fee -> supplier receives 98889.
```

500k invoice anchor:

```text
Without SCF: supplier cost 500000*10%*60/360=8333;
buyer benefit 500000*4.5%*60/360=3750.
With SCF: supplier cost 500000*5%*90/360=6250;
buyer benefit 500000*4.5%*90/360=5625.
Improvements: supplier 2083, buyer 1875, total approx 3958.
```

Superb Flowers:

```text
DSO=60, DPO=30, COGS=90%R, inventory=0, NWC=2.5M.
2.5M = R*60/360 - .90R*30/360 = .09167R -> R approx 27.27M.
COGS approx 24.55M; 1 DSO day approx 75,758; 1 DPO day approx 68,182.
10% NWC cut = 250k; 50% cut = 1.25M.
50% cut by DSO only: 1.25M/75,758 = 16.5 days faster.
50% cut by DPO only: 1.25M/68,182 = 18.3 days later.
DPO 30 -> 60 raises AP by approx 2.05M; NWC falls to approx 0.46M.
5% customer discount costs .05*27.27M=1.36M: too expensive unless strategic.
```

Resilience and adoption:

```text
Efficiency motive: smaller/high-financing-cost suppliers gain most from SCF.
Legitimacy motive: mimetic/normative adoption; coercive not supported.
Resilience = absorb, respond, recover, adapt after disruption.
Redundancy = extra buffer/capacity/supplier; costly immediate protection.
Flexibility = switch/reconfigure/reroute; capability and coordination cost.
Triple-P: process complexity -> standardize; partnership complexity -> visibility;
product complexity -> footprint diversification.
```

Traps: SCF rate is financing cost, not a bonus. Buyer DPO changes only if buyer pays provider later. Supplier DSO falls when paid early. NWC cuts can hurt resilience or margin.

## 13 Lean Management / Lean Simulation

Lean chain:

```text
Value -> value stream -> muda diagnosis -> flow -> pull/Kanban -> perfection
Five elements: value, value stream, flow, pull, perfection.
Flow concepts: standardization, takt time, no rework, JIT, transparency.
Takt time = available production time / customer demand.
```

Seven muda:

```text
Overproduction, transport, over-processing, excess inventory, motion, defects, waiting.
Exam move: name waste -> point to symptom -> propose countermeasure.
```

Push, pull, Kanban:

```text
Push = forecast/plan-driven upstream production -> overproduction, inventory, bullwhip.
Pull = downstream demand signal triggers replenishment -> lower WIP, better fit to demand.
Pull is not "no forecast"; forecasts still support capacity/S&OP.
Kanban = visual demand/replenishment signal + WIP limiter.
No card/signal/space -> upstream should not produce.
Kanban reduces overproduction/WIP and exposes bottlenecks; it does not fix capacity,
layout, skills, or defect causes by itself.
```

Simulation iterations:

```text
I1 conventional batch/queue functional layout:
sorted bricks -> sets -> axes/chassis/final assembly.
Wastes: handoffs, transport, waiting, WIP, over-processing, defects.

I2 pull with Kanban:
same broad process, but demand signal limits WIP. Overproduction falls;
bottlenecks and layout problems become visible.

I3 manufacturing cells:
product-flow mini systems. Fewer handoffs/transport/WIP/waiting,
closer order signal, faster feedback.
```

Improvement words:

```text
Kaikaku = radical redesign, e.g. functional layout -> cells.
Kaizen = continuous incremental improvement.
Poka-yoke = mistake-proofing to prevent defects at source.
Postponement = delay differentiation until demand is clearer.
```

Traps: lean is value-flow design, not only cost cutting. Muda is the diagnosis lens; WIP/waiting/output/defects/lead time are observable measures. Kanban may expose bottlenecks before output improves.

## Last Line

```text
T10: protect l+1 demand with S. T12: cash timing changes liquidity and risk.
T13: remove muda by redesigning flow and using pull signals.
```

# SCM Topic 14 HP DeskJet Case A4 Cheat Sheet

```text
Case move: symptom -> SKU demand -> SL/LIFR -> order-up-to S -> scenario costs -> recommendation.
Core issue: high inventory + stockouts = localized SKU mismatch, not simply "too little stock".
```

## Situation / Life Cycle / KPIs

```text
HP early 1990s: sales rising, inventory rising similarly, stockouts despite full warehouses.
EOQ intuition: Q*=sqrt(2Klambda/h); if lambda doubles, Q* rises by sqrt(2), not 2x.
DeskJet life cycle: maturity/late growth -> lower margins, higher service expectations,
less ramp-up uncertainty, process efficiency becomes key.
```

KPIs:

```text
Inventory turns = annual sales / average inventory
On-hand inventory = average inventory / annual sales * 52
Service level = % periods without stockout = P(D<=S)
LIFR = expected filled units / expected demand
OFR = % complete orders filled
Trap: service level != LIFR. A stockout period can still fill most units.
```

## Demand / Normal Setup

```text
Options: A, AA, AB, AQ, AU, AY. AB dominates volume.
No aggregate trend: F=2.224, p=0.166>0.1.
Weekly mean = monthly mean * 12/52
Weekly variance = monthly variance * 12/52
Protection mean = weekly mean * weeks
Protection sigma = sqrt(weekly variance * weeks)
Pooling: add means and variances, not standard deviations.
```

Weekly anchors:

```text
A 9.8 / var 242.4; AA 97.0 / 9596.8; AB 3653.1 / 7300588.7;
AQ 531.0 / 315086.9; AU 971.1 / 1121581.6; AY 70.8 / 2454.1;
TOTAL 5332.8 / 8997008.9.
```

## Service Level / LIFR

```text
Annual holding cost = 48% of V. One period = 1 week.
c_o = 0.48V/52 = 0.0092V
Margin = 22.4%V; lost backlog margin = 50%
c_u = 0.224*0.5V = 0.112V
SL* = c_u/(c_u+c_o) = 0.112/(0.112+0.0092) = 92.4%
z_92.4% approx 1.43
L(z)=phi(z)-z[1-Phi(z)] approx 0.034
LIFR = 1 - sigma*L(z)/mu approx 1 - 0.034*sigma/mu
```

Order-up-to:

```text
S = mu + z*sigma
Expected backorders B = sigma*L(z)
Expected leftover/safety inventory I = S - mu + B
Order each period = S - inventory position
```

## Scenarios

Baseline ship:

```text
Lead time 5w + cycle 1w = 6w protection.
Total mean=31996.5; total S=47723.0.
Cycle inv=2666.4; in-transit=26663.8; B=375.8; leftover=16102.3.
At V=$400: total inv cost=$9.598M; 8.65% revenue; cost/printer=$34.61.
AB example: mu=21918.6, sigma=6618.4, S=31392.0, LIFR=98.97%, I=9699.9.
```

Air:

```text
Lead time 1w + cycle 1w = 2w protection.
Total mean=10665.5; total S=19745.2.
Cycle inv=2666.4; in-transit=5332.8; B=217; leftover=9059.7.
At V=$400: total inv cost=$3.826M; 3.45% revenue; saving/printer=$20.80.
Rule: use air only if extra freight cost < about $20.80/printer.
```

Pooling + ship:

```text
Aggregate demand, still 6w protection.
Pooled mean=31996.5; sigma=7347.2; S=42513.2; LIFR=99.21%.
Slide nuance: 251.3 = expected backorders; 10768.0 = expected leftover/safety inventory.
At V=$400: total inv cost=$8.284M; 7.47% revenue; saving/printer=$4.74.
Improves LIFR from about 98.8% to 99.21%.
```

## Recommendation

```text
Air gives biggest inventory saving but adds recurring freight cost.
European integration/pooling improves SKU fit but can add labor, skills, handoffs, defects.
Best structural answer: postponement/product redesign if feasible:
one standard printer per box + all languages/manuals + all European plugs.
Slide anchor: possible added cost about $0.50, possible saving about $5.00.
Final sentence: choose redesign/postponement because it reduces mismatch while keeping processes lean;
use air only when freight premium is below the quantified inventory saving.
```

## Traps

```text
Do not use monthly sigma directly; convert variance first.
Do not forget +1 review/cycle period.
Do not call LIFR a service level.
Do not add standard deviations under pooling.
Do not recommend local integration without process-complexity discussion.
Do not recommend air without freight-cost comparison.
```

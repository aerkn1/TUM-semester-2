# SCM Topics 04-06 A4 Formula Cheat Sheet

Handwrite this as three tight columns. Keep units/time bases visible.

```text
Exam move: identify model -> write formula -> substitute -> unit -> operational meaning
```

## 04 Random Variables / Demand Modeling

```text
D = demand random variable; realization = observed value after uncertainty resolves
Service level for stock/capacity q: SL(q)=P(D<=q)=F(q)
Discrete: P(D=k) can be >0; P(D<=q)=sum P(D=k)
Continuous: P(D=x)=0; P(a<=D<=b)=F(b)-F(a)
```

Probability basics:

```text
P(Omega)=1; P(empty)=0; P(A)>=0
P(A union B)=P(A)+P(B)-P(A intersection B)
If disjoint: P(A union B)=P(A)+P(B)
```

Poisson count demand:

```text
D ~ Poisson(lambda)
P(D=k)=lambda^k * e^(-lambda) / k!
E[D]=lambda; Var(D)=lambda; sigma=sqrt(lambda)
P(D<=q)=sum from k=0 to q P(D=k)
Use for integer arrivals/orders in fixed time interval.
Large lambda: approx Normal(mu=lambda, sigma=sqrt(lambda)).
```

Uniform rough interval demand:

```text
D ~ Uniform[A,B]
P(a<=D<=b)=(b-a)/(B-A)
F(q)=0 if q<=A; F(q)=(q-A)/(B-A) if A<=q<=B; F(q)=1 if q>=B
E[D]=(A+B)/2
Inverse CDF / quantile: Q=A+SL(B-A)
```

Normal demand:

```text
D ~ Normal(mu,sigma)
z=(x-mu)/sigma
P(D<=x)=Phi(z)
Q=mu+z(SL)*sigma
95% interval approx mu +/- 1.96*sigma
Anchors: Phi(0)=0.5; Phi(1.96)=0.975; Phi(-1.96)=0.025; Phi(2.32) approx 0.99
Use normal when high-volume demand / many small drivers / negative-demand risk negligible.
```

Traps: service level is cumulative `P(D<=q)`, not `P(D=q)`; density height is not probability; variance is `sigma^2`, not `sigma`; z-score is not a probability; uniform exact-point probability is zero.

## 05 EOQ / EPQ / Batching

Model router:

```text
One-time uncertain demand -> Newsvendor
Recurring known constant demand + instant replenishment -> EOQ
Recurring known constant demand + finite production rate -> EPQ
Lead time under deterministic demand -> timing/reorder point, not Q*
Finite horizon -> integer number of orders m*
```

Basic EOQ:

```text
lambda = deterministic demand rate [units/time]
K = fixed order/setup cost [EUR/order]
h = holding cost [EUR/unit/time]
Q* = sqrt(2Klambda/h)
TC(Q)=hQ/2 + Klambda/Q
At Q*: annual holding cost = annual setup/order cost
Avg inventory=Q/2; orders/time=lambda/Q; cycle length=Q/lambda
TC(Q*)=sqrt(2hKlambda)
```

Initial inventory and lead time:

```text
I0 = opening inventory; l = lead time
No lead time: first order after I0/lambda
Reorder point r=lambda*l
First order with I0 and lead time: (I0-r)/lambda = I0/lambda - l
If inventory already <= r, order immediately.
```

Finite-horizon EOQ:

```text
t = finite horizon length, same time unit as lambda and h
Total demand=t*lambda
TC(m)=Km/t + h*lambda*t/(2m)
m_hat=t*sqrt(hlambda/(2K))
Test floor(m_hat) and ceil(m_hat); choose lower TC.
Q*=t*lambda/m*
```

EPQ finite production:

```text
p = production rate, requires p>lambda
Production run T0=Q/p
Inventory builds at p-lambda, depletes at -lambda
Imax=((p-lambda)/p)Q
Avg inventory=Imax/2
TC(Q)=h*((p-lambda)/p)*Q/2 + Klambda/Q
Q*=sqrt(2Klambda/h)*sqrt(p/(p-lambda))
```

Production systems:

```text
MTS: finished goods before order -> low customer lead time, high inventory.
ATO: components stocked, final assembly after order.
MTO: production after order -> lower FG inventory, longer wait.
ETO: design after order -> highest customization, longest lead time.
Push = forecast-driven before order; Pull = real-order triggered.
```

Batching trap: larger batches reduce setup frequency/local cost but increase WIP, waiting, lead time, and bullwhip risk. EPQ uses `Imax/2`, not `Q/2`. Do not mix time units.

## 06 Coordination / Bullwhip

```text
Bullwhip = upstream amplification of order/demand variability, not average demand growth.
CV = standard deviation / mean
Bullwhip signal: CV upstream > CV downstream/final demand.
```

Cause -> mechanism:

```text
Order synchronization -> many retailers order same time -> upstream spikes.
Order batching -> lumpy orders/zeros -> variability amplification.
Trade promotion -> forward buying -> big order now, low orders later.
Shortage gaming -> buyers inflate orders during scarcity to improve allocation.
Reactive ordering + long lead time -> stale info -> overcorrection.
Information distortion -> upstream sees orders, not real POS demand.
Pathological incentives -> local rational behavior damages chain signal.
```

Consequences:

```text
Wrong capacity decisions, low utilization, higher safety stock, stockouts,
supplier stockouts, emergency logistics, higher purchasing/logistics cost.
```

Mitigation levers:

```text
Information: POS data, EDI, CPFR -> upstream sees real demand signal.
Flow smoothing: VMI, EDLP, Lean -> fewer artificial order lumps.
Incentives: coordinate promotions, restructure returns, turn-and-earn -> stop rewarding inflated orders.
Lean words: value, value stream, flow, pull, perfection.
```

MCQ traps:

```text
EDLP is mitigation, not cause.
Beer Game illustrates bullwhip; it is not the only setting.
Retailer orders are not automatically true demand.
"Better forecasting" is vague; name POS/EDI/CPFR/VMI/incentive alignment.
EOQ-style batching can be locally efficient and system-wide harmful.
```

## Last Line

```text
T04: CDF turns q into SL. T05: EOQ balances setup vs holding. T06: bullwhip is upstream variability amplification.
```

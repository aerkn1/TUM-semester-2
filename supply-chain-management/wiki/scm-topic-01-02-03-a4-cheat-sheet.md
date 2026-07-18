# SCM Topics 01-03 A4 Formula Cheat Sheet

Handwrite this as three tight columns. Prioritize formulas, units, and traps.

```text
Exam move: decision -> constraint/uncertainty -> formula -> units -> interpretation
```

## 01 Kristen Cookies / Process Flow

```text
Flow rate = min{demand rate, process capacity, supply rate}
Capacity_i = 60 / processing time_i          [units/hour]
System capacity = bottleneck capacity = min capacity_i
Cycle time = time between completed units in steady state
Throughput time = elapsed time for one order from start to finish
```

Kristen one-dozen base case:

```text
Order 1 + mix 6 + spoon 2 + bake 10 + cool 5 + pack 2 + deliver 1 = 27 min
Baking bottleneck = 10 min/dozen -> 6 dozen/hour
Steady-state cycle time = 10 min/dozen
```

Labor:

```text
You = mix+spoon = 8 min/tray; roommate = order+pack+deliver = 4 min/tray
Direct labor = 12 min/tray; $12/hour = $0.20/min -> $2.40/tray
Incl. idle at bottleneck cycle = 2 workers * 10 min * $0.20 = $4/tray
```

Improvement logic:

```text
Extra oven: baking capacity 6 -> 12 dozen/hour, then re-check bottleneck.
If mixing binds: 6 min -> 10 dozen/hour.
If one person still does mix+spoon: 8 min -> 7.5 dozen/hour.
```

Traps: first-order throughput time is not steady-state cycle time; improving a non-bottleneck does not increase system capacity; after any improvement, find the new bottleneck; keep demand, capacity, and supply separate.

## 02 Forecasting

```text
e_t = A_t - F_t
ME = avg(e_t)          bias
MAD = avg(|e_t|)       typical absolute miss, original units
MSE = avg(e_t^2)       large-error penalty, squared units
RMSE = sqrt(MSE)       error scale in original units
```

```text
ME > 0 -> actuals > forecasts -> underforecasting
ME < 0 -> forecasts > actuals -> overforecasting
ME near 0 can still hide large errors because signs cancel
```

Forecast methods:

```text
Naive:              F_t = A_{t-1}
Naive + trend:      F_t = A_{t-1} + (A_{t-1} - A_{t-2})
Seasonal naive:     F_t = A_{t-n}                         [n = season length]
Moving average:     F_t = (A_{t-1}+...+A_{t-n})/n
Exp. smoothing:     F_t = F_{t-1} + alpha(A_{t-1}-F_{t-1})
                    = alpha A_{t-1} + (1-alpha)F_{t-1}
```

```text
High alpha -> fast reaction/noisy; low alpha -> smooth/slow.
Trend-adjusted: TAF_t=S_{t-1}+T_{t-1};
S_t=TAF_t+alpha(A_t-TAF_t);
T_t=T_{t-1}+beta(TAF_t-TAF_{t-1}-T_{t-1})
Regression: Y_t = beta_0 + beta_1*t + seasonal dummy effects
95% control limits = mean error +/- 1.96*error SD, approx. +/- 1.96*RMSE
```

Traps: compare MAD/MSE only on the same window; MAD is not MSE; MSE means squared errors, not exponential errors; inside control limits means normal noise; outside limits or repeated pattern means investigate; best method is empirical, not automatically most complex.

## 03 Newsvendor

```text
c_u = marginal loss from ordering 1 unit too few       [underage]
c_o = marginal loss from ordering 1 unit too many      [overage]
SL = c_u / (c_u + c_o)                                 [critical fractile]
Q* = F^{-1}(SL)
Service level = P(D <= Q) = probability all demand is covered
```

Cost setup:

```text
No salvage: c_u=p-c; c_o=c; SL=(p-c)/p
With salvage v: c_u=p-c; c_o=c-v; SL=(p-c)/(p-v)
```

Distribution rules:

```text
Discrete demand: choose smallest Q with F(Q) >= SL, not closest Q.
Uniform [a,b]: Q* = a + SL(b-a)
Normal: Q* = mu + z(SL)*sigma
n independent periods: mu_n=n*mu; sigma_n=sqrt(n)*sigma
```

Interpretation/traps:

```text
High c_u -> order more -> higher SL; high c_o -> order less -> lower SL.
SL > 50% -> Q* above median/mean; SL < 50% -> below median/mean.
sigma does not change SL; sigma changes Q* for a given SL.
Newsvendor uses a forecast distribution; it does not create the forecast.
SL is not forecast accuracy, fill rate, or expected profit.
Show unrounded Q*, then follow exam rounding/answer options.
```

## Last Line

```text
Kristen: bottleneck limits capacity. Forecasting: e=A-F, ME/MAD/MSE. Newsvendor: cost ratio -> SL -> quantile -> Q*.
```

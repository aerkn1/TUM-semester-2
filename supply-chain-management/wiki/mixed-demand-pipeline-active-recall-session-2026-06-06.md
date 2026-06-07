# Active Recall Session: SCM Mixed Demand Pipeline

Course: Supply Chain Management
Date: 2026-06-06
Session type: `D+3 mixed repair`

Source notes:

- `supply-chain-management/wiki/topic-02-forecasting/topic-02-forecasting.md`
- `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`
- `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`

## Session Focus

Repair the chain:

```text
forecasting -> random variable -> Newsvendor order quantity
```

The user explicitly replaced the planned German blocks on 2026-06-06 with this SCM mixed repair.

## Prompts, User Answers, Feedback

### Prompt 1: Forecast Errors, Metrics, Random Variable, Newsvendor Setup

Prompt:

> A bakery must decide tomorrow morning how many fresh muffins to bake. Unsold muffins are discounted at the end of the day.
>
> Forecast/actual data: Day 1 `F=100`, `A=110`; Day 2 `F=120`, `A=100`; Day 3 `F=130`, `A=150`; Day 4 `F=150`, `A=140`.
>
> Tomorrow's demand is normally distributed with `mu = 130`, `sigma = 20`. Each muffin costs `c = 1.20`, sells for `p = 3.00`, and has salvage value `s = 0.60`.
>
> Compute forecast errors, `ME`, `MAD`, `MSE`; explain why tomorrow's demand is a random variable; set up Newsvendor with `c_u`, `c_o`, and critical ratio.

User raw answer:

> 1- 10 -20 + 20 -10 = 0
> 2- all becomes 0, it means there is no bias or concrete average demand regarding the forecast.
> 3-we have mean unit and the standart deviation as sigma
> 4- c+s/p gives the service level, which is 0.60. since its over 0.50 better to target high service level for order quantity

Feedback and corrections:

- Quality: `yellow`
- Error signs were correct: `10, -20, 20, -10`.
- `ME = 0` was correct, but it means no average signed bias, not no errors.
- Correct metrics:

```text
ME = 0
MAD = (10 + 20 + 20 + 10) / 4 = 15
MSE = (100 + 400 + 400 + 100) / 4 = 250
```

- `D` is a random variable because tomorrow's actual demand is uncertain before it happens, but each possible outcome can be represented as a numerical muffin quantity.
- `mu = 130` and `sigma = 20` describe the assumed distribution of `D`.
- Correct Newsvendor setup with salvage:

```text
c_u = p - c = 3.00 - 1.20 = 1.80
c_o = c - s = 1.20 - 0.60 = 0.60
SL = c_u / (c_u + c_o) = 1.80 / 2.40 = 0.75
```

### Prompt 2: Normal Demand Quantile

Prompt:

> Use `D ~ N(130, 20)`, `SL = 0.75`, and `z(0.75) approximately 0.67`.
>
> Compute `Q* = mu + z(SL) * sigma`.

User raw answer:

> 130 + 0.67 * 20 = 143,4

Feedback and corrections:

- Quality: `green`
- Correct setup and arithmetic:

```text
Q* = 130 + 0.67 * 20 = 143.4
```

- Exam-safe conclusion: order about `143-144` muffins; use `144` if rounding up to meet at least the target service level.

### Prompt 3: Sigma Effect

Prompt:

> Why did the bakery order above mean demand of `130`? What happens to `Q*` if `sigma` increases from `20` to `40`, while `mu` and the critical ratio stay the same?

User raw answer:

> this increases the probability and risk interval as the stdandard deviation for forecast increases which reduces service level as impacts the quantity order reduce

Feedback and corrections:

- Quality: `yellow-red`
- Correct intuition: higher `sigma` means wider uncertainty.
- Correction: `sigma` does not reduce the service level in this setup. The service level stays fixed at `0.75` because it comes from the cost tradeoff.
- Higher `sigma` changes the order quantity needed to reach the same service level:

```text
Q* = 130 + 0.67 * 40 = 156.8
```

- Refined mental model:

```text
Higher sigma spreads demand out. If the target service level stays 75%, the bakery must order farther above the mean, so Q* increases.
```

### Prompt 4: Discrete Demand CDF

Prompt:

> Demand table: `D=100,120,140,160,180` with probabilities `0.10, 0.25, 0.40, 0.20, 0.05`. Use `SL = 0.75`.
>
> Build `F(Q) = P(D <= Q)`, choose the optimal quantity using the smallest `Q` where `F(Q) >= SL`, and explain why we do not choose the closest probability.

User raw answer:

> 1- cumultaive sum of probablities must equal to the SL
> 2- it is 140 where the cumultaive sum reaches to 0.75 exact 010 + 0.25 + 0.40
> 3-it has to be the sum of all possible demand probabilites to meet the expected quantity that needs to cover all the possible omega values and assumes the best cumultaive value for quantity

Feedback and corrections:

- Quality: `green-yellow`
- Correct result: `Q* = 140`.
- Correct CDF:

```text
F(100) = 0.10
F(120) = 0.35
F(140) = 0.75
F(160) = 0.95
F(180) = 1.00
```

- Correction: cumulative probability does not need to equal the service level exactly. It must reach or exceed the service level.

### Prompt 5: Same Table, New Critical Ratio

Prompt:

> With the same discrete demand table, assume `SL = 0.80`. What order quantity do we choose, and why?

User raw answer:

> 160 to be able to meet the probability of expected demand without cost tradeoff at service level

Feedback and corrections:

- Quality: `green-yellow`
- Correct quantity: `160`.
- Correction: the service level is not without cost tradeoff; it comes from the cost tradeoff.

```text
F(140) = 0.75 -> too low
F(160) = 0.95 -> first value >= 0.80
```

Exam-safe sentence:

```text
Because 140 only covers 75% of demand outcomes, it does not meet the 80% target; 160 is the smallest quantity whose cumulative probability reaches or exceeds the service level.
```

### Prompt 6: Full Pipeline

Prompt:

> In 3-5 sentences, explain the full chain: forecasting -> random variable -> Newsvendor order quantity. Use the muffin/bakery example.

User raw answer:

> based on the past order data for certain period of time, we can calculate the probability dsitribution of the next incoming days of demand. First we need to find out the best fit forecasting model with the most moderate ME, MAD, and MSE and then we define the control limits that the forecasts for the following periods remains inside those control limits. After control limits are defined for the demand, we have to incorporate the cost tradeoffs for the quantity order accordingly. We need to find the service level to figure out the optimal order quantity probability that meets the target demand with the least over or underage costs.

Feedback and corrections:

- Quality: `yellow-green`
- Forecasting gives a demand estimate and forecast uncertainty; it does not by itself directly calculate the probability distribution.
- Use `ME` to check bias; use low `MAD`/`MSE` to compare accuracy.
- Control limits monitor whether forecast errors are abnormal; they do not define demand itself.

Exam-safe version:

```text
The bakery uses past demand to choose a forecasting model and estimate tomorrow's expected demand. Forecast errors help measure uncertainty, so tomorrow's demand can be modeled as a random variable D with a probability distribution. The Newsvendor model then adds the cost tradeoff: underage cost if demand exceeds the order quantity, and overage cost if muffins remain unsold. This cost tradeoff gives the target service level, and the bakery chooses the smallest quantity or quantile that reaches that service level.
```

### Prompt 7: Control Limits And Probability Distribution

Prompt:

> Suppose forecast errors are usually around `MAD = 15`. Tomorrow, forecast is `130`, actual demand is `190`, so `e = 60`. Should the manager immediately change the forecasting model after this one large error? Explain using control-limit logic.

User clarification question:

> I am losing connection for how those defined control limits and measured uncertanities with forecasting then used in probaility distribution and when it is actually the warning that the forecast model needs to change accordingly?

Feedback and correction:

- Quality: `clarification needed, then green`
- Key distinction:

```text
Forecast distribution = decision tool before demand happens.
Control limits = warning system after demand happens.
```

- Forecast uncertainty feeds the demand distribution, for example `D ~ Normal(mu = 130, sigma = 20)`.
- Control limits monitor later forecast errors and signal when the forecasting model may be unreliable.
- One large error should trigger investigation, not automatic model replacement.
- Repeated abnormal errors, repeated positive/negative bias, new trend/seasonality, or a permanent demand shift can justify refitting the model.

User follow-up:

> and then if the error rate is excedding the control limit like MAD 15 but error 60 for a certain period of time, it means that the forecast model and control limits needs to be redefined right? so it changes the probability demand formula

Feedback:

- Corrected model:

```text
Repeated abnormal errors
-> model may be misspecified or demand pattern changed
-> refit or change forecasting model
-> new forecast and new error estimate
-> updated probability distribution
-> updated Newsvendor order quantity
```

- The formula usually stays the same; the distribution and inputs change.

Example:

```text
Old: D ~ Normal(mu = 130, sigma = 20)
New after refit: D ~ Normal(mu = 170, sigma = 25)
Q* = mu + z(SL) * sigma
```

### Final Checkpoint

Prompt:

> Mark each statement true or false and correct false ones.
>
> 1. `ME = 0` means the forecast has no errors.
> 2. `MAD` measures the typical absolute forecast miss.
> 3. A random variable `D` represents uncertain future demand as numbers.
> 4. In Newsvendor, `sigma` determines the service level.
> 5. If `SL = 0.80`, choose the smallest `Q` where `F(Q) >= 0.80`.
> 6. Repeated errors outside control limits may mean the forecast model or demand pattern needs updating.

User raw answer:

> 1- no, the bias towards positive and negative forecasting is zero
> 2-yes
> 3-yes
> 4-no, its the standart deviation that represents control limit interval from mean
> 5-yes
> 6-yes

Feedback:

- Quality: `green-yellow`
- Items 1, 2, 3, 5, and 6 were correct.
- Item 4 was correctly marked false, but the correction needs precision:

```text
Sigma is the standard deviation of demand or forecast error uncertainty. It affects the distance between the mean and the quantity needed for a target service level. The service level itself comes from the Newsvendor cost ratio, not from sigma.
```

## Weak Spots

| Quality | Weak Spot | Correction Rule |
|---|---|---|
| yellow | `ME = 0` treated as no forecast error | `ME = 0` means no signed bias; use `MAD`/`MSE` to measure error size. |
| yellow | Missed `MAD`/`MSE` after correct errors | Compute absolute errors and squared errors separately. |
| yellow | Critical ratio with salvage value | Use `c_u = p - c`; `c_o = c - s`; `SL = c_u / (c_u + c_o)`. |
| yellow-red | Sigma confused with service level | Costs set `SL`; sigma changes the quantile distance and therefore `Q*`. |
| yellow | Discrete CDF described as exact equality | Choose the smallest `Q` where `F(Q) >= SL`; exact equality is not required. |
| yellow-green | Control limits confused with demand distribution | Distribution supports pre-demand ordering; control limits monitor post-demand forecast errors. |

## Refined Mental Models

```text
Forecasting estimates demand and error.
Random variable D turns uncertain future demand into a probability model.
Newsvendor turns the cost tradeoff into a service level and order quantity.
Control limits are a monitoring alarm, not the order-quantity formula.
```

```text
Repeated abnormal forecast errors can change the forecast model and the distribution inputs, but the Newsvendor formula usually stays the same.
```

## Next Recall Prompts

1. Given a forecast-error table, compute `ME`, `MAD`, and `MSE`, then interpret each.
2. Given `p`, `c`, and salvage value `s`, compute `c_u`, `c_o`, `SL`, and explain the managerial tradeoff.
3. Given a discrete CDF, choose the smallest `Q` where `F(Q) >= SL`.
4. Explain why higher `sigma` increases `Q*` when `SL > 0.5`.
5. Distinguish forecast uncertainty from control limits in one sentence.

## References

- Forecasting note: `supply-chain-management/wiki/topic-02-forecasting/topic-02-forecasting.md`
- Random Variables note: `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`
- Newsvendor note: `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`

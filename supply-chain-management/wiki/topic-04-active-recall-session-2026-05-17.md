# Active Recall Session: Topic 04 Modeling Uncertain Demand With Random Variables

Course: Supply Chain Management  
Wiki note: `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables.md`  
Date: 2026-05-17  
Session type: `first active-recall pass; overdue repair`

## Session Focus

Build the bridge from forecasting to probabilistic demand modeling:

- random variable intuition
- discrete vs continuous demand
- service level as `P(D <= q)`
- Poisson count demand
- uniform bounded uncertainty
- normal demand and z-scores
- link to Newsvendor critical ratio

## User Raw Answers And Feedback

### Round 1: Core Intuition

1. What does it mean to model demand as a random variable `D`?

User answer:

> it is a changing dynamic value over time

Feedback:

- Quality: `yellow`
- Correction: `D` is a numerical representation of uncertain demand before it is realized, not just something changing over time.
- Refined model: tomorrow's demand is unknown today, so we model it as a random variable.

2. Difference between `P(D = 5)` and `P(D <= 5)`?

User answer:

> probability of constant and less demand than 5

Feedback:

- Quality: `yellow-green`
- `P(D = 5)` means demand is exactly 5.
- `P(D <= 5)` means demand is at most 5.

3. Why is `P(D <= 10)` the service level if stocking 10 units?

User answer:

> because ordering high or low than 10 units has marginal cost, we do the forecast without knowing the actual unit of demand

Feedback:

- Quality: `yellow`
- Correction: service level is the probability of no stockout: demand does not exceed inventory.
- Costs matter in Newsvendor, but service level itself is a probability.

4. Customer arrivals: discrete or continuous?

User answer:

> continuous?

Feedback:

- Quality: `red-yellow`
- Correct answer: `discrete`, because customers are countable: 0, 1, 2, 3, ...

5. Liters of oil or kilograms of flour: discrete or continuous?

User answer:

> continuous?

Feedback:

- Quality: `green`
- Correct: measurable quantities over intervals are usually modeled as continuous.

### Round 2: Poisson

Example: `D ~ Poisson(lambda = 4)` for muffin customers per hour.

1. Why is Poisson reasonable?

User answer:

> because demand is countable and discrete?

Feedback:

- Quality: `green-yellow`
- Correct: countable/discrete.
- Add: Poisson is especially for arrivals/counts over a fixed time interval with roughly independent arrivals.

2. What is `E[D]`?

User answer:

> expected value

Feedback:

- Quality: `yellow`
- Correct concept, missing value.
- For Poisson, `E[D] = lambda = 4`.

3. What is `Var(D)`?

User answer:

> expected value

Feedback:

- Quality: `yellow`
- For Poisson, `Var(D) = lambda = 4`.

4. What is `sigma`?

User answer:

> variablity interval around expected value

Feedback:

- Quality: `yellow`
- Correct intuition: standard deviation measures spread.
- Formula: `sigma = sqrt(lambda) = sqrt(4) = 2`.

5. Service level at `q = 2`?

User answer:

> no idea

Feedback:

- Quality: `red-yellow`
- Correct expression: `P(D <= 2) = P(D=0) + P(D=1) + P(D=2)`.
- For Poisson: `e^-4 * 4^0/0! + e^-4 * 4^1/1! + e^-4 * 4^2/2!`.

### Round 3: Uniform

Example: `D ~ Uniform[150, 450]`.

1. Meaning of uniform:

User answer:

> boundary of the estimated demand based on historical data that expected for next time interval

Feedback:

- Quality: `yellow-green`
- Refined model: demand can take any value between 150 and 450, and equal-length intervals are equally likely.
- It can be historical-data based or managerial-estimate based.

2. Expected demand:

User answer:

> 300

Feedback:

- Quality: `green`
- Correct: `(150 + 450) / 2 = 300`.

3. `P(D = 200)`:

User answer:

> 0 , because the single point estimatiion probabiltiies are quite low to happen

Feedback:

- Quality: `green-yellow`
- Correct answer: 0.
- Correction: not just low; exactly zero for a continuous distribution at a single point.

4. `P(D <= 300)`:

User answer:

> 300-150 / 450-150 = 2 / 3 = 0.667

Feedback:

- Quality: `yellow`
- Setup is correct but arithmetic is wrong.
- Correct: `(300 - 150) / (450 - 150) = 150 / 300 = 0.5`.

5. Service level at `q = 420`:

User answer:

> 420 -150 / 450-150 =  270/300 = 0.9

Feedback:

- Quality: `green`
- Correct: `P(D <= 420) = 0.9`.

### Round 4: Normal

Example: `D ~ Normal(mu = 320, sigma = 45)`.

1. Meaning of `mu` and `sigma`:

User answer:

> mu = average unit and sigma is the expected variability towards both side

Feedback:

- Quality: `green`
- Correct: `mu` is mean/expected demand; `sigma` is standard deviation/spread.

2. z-score for `q = 350`:

User answer:

> 30/45 = 2/3

Feedback:

- Quality: `green`
- Correct: `z = (350 - 320) / 45 = 0.667`.

3. Meaning of `P(D <= 350)`:

User answer:

> probability of demand quantity below or equal to 350

Feedback:

- Quality: `green`
- Correct: operationally, this is the service level if stocking 350 units.

4. 95% interval:

User answer:

> 320 + 1.96 * 45 , 320 + 1.96 *45

Feedback:

- Quality: `yellow`
- Correction: use both sides: `mu - 1.96sigma` to `mu + 1.96sigma`.
- Correct interval: `[231.8, 408.2]`.

5. Demand much higher than `mu + 1.96sigma`:

User answer:

> rearrange the methodology to calculate the demand forecast

Feedback:

- Quality: `yellow-green`
- Correct instinct: the model may need revision.
- Refinement: first investigate root cause. It may be one-time shock, seasonality, promotion, structural change, or wrong model. Change method only after evidence.

### Round 5: Bridge To Newsvendor

Given:

```text
cu = 20
co = 10
D ~ Uniform[150, 450]
```

1. Meaning of `cu`:

User answer:

> marginal loss from ordering one unit less

Feedback:

- Quality: `green`
- Correct: underage cost is the opportunity cost/loss of being short one unit.

2. Meaning of `co`:

User answer:

> marginal loss from ordering one unit more

Feedback:

- Quality: `green`
- Correct: overage cost is the loss from leftover/excess one unit.

3. Critical ratio / target service level:

User answer:

> probabiltiy of meeting all demand

Feedback:

- Quality: `yellow`
- Correct interpretation but missing formula.
- Formula: `cu / (cu + co) = 20 / (20 + 10) = 2/3`.

4. Uniform order quantity:

User answer:

> 20/30 = 2/3 * 300 + 150 = 350

Feedback:

- Quality: `green`
- Correct: target quantile is `150 + (2/3) * 300 = 350`.

5. Why this topic is needed before Newsvendor:

User answer:

> to determine the correct order quantity with reliable probability

Feedback:

- Quality: `green`
- Correct: Newsvendor converts cost tradeoff into a target service level, then uses the demand distribution to choose the matching quantile.

## Repaired Mental Models

```text
Forecasting gives an expected demand or pattern.
Random variables describe the uncertainty around demand.
A distribution lets us calculate service levels and quantiles.
Service level at q = P(D <= q) = probability of no stockout.
Discrete demand = countable units or arrivals.
Continuous demand = measurable quantities over intervals.
Newsvendor uses costs to determine a target service level, then chooses the matching demand quantile.
```

## Weak Spots

| Concept | Quality | Fix |
|---|---|---|
| Random variable definition | `yellow` | Define `D` as uncertain demand represented numerically before realization. |
| Discrete vs continuous | `yellow` | Customer arrivals and unit counts are discrete; measurements like kg/liters are continuous. |
| Poisson service level | `red-yellow` | For `q`, sum probabilities from `0` to `q`: `P(D <= q)`. |
| Uniform CDF arithmetic | `yellow` | Use `(q-A)/(B-A)` and check numerator carefully. |
| Normal 95% interval | `yellow` | Use both bounds: `mu - 1.96sigma`, `mu + 1.96sigma`. |
| Critical ratio formula | `yellow` | `SL* = cu / (cu + co)`. |

## Next Recall Prompts

1. If `D ~ Poisson(9)`, what are `E[D]`, `Var(D)`, and `sigma`?
2. If `D ~ Uniform[80, 200]`, calculate `P(D <= 140)`.
3. If `D ~ Normal(100, 20)`, calculate the z-score for `q = 130`.
4. For `cu = 6` and `co = 3`, what is the critical ratio?
5. Explain in one sentence why Newsvendor needs a probability distribution.

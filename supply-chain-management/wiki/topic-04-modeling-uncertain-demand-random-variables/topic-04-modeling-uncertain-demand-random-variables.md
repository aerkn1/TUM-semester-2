# Topic 04: Modeling Uncertain Demand With Random Variables

Source files:

- `supply-chain-management/raw/TUM_PL_2024_03_Modeling_Demand_Random_Variables.pdf`
- `supply-chain-management/raw/PL- Random Variables-Exercise-Task.xlsx`

Course: Supply Chain Management
Processed: 2026-05-14
Wiki note: `supply-chain-management/wiki/topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`

Course logistics checked: the SCM exam is closed-book, numerical/open-ended questions are possible, and one handwritten A4 cheat sheet is allowed. This topic is a high-priority formula topic because it supports Newsvendor, inventory decisions, service levels, and demand modeling.

## 80/20 Exam Summary

This topic teaches how to turn uncertain real-life demand into a probability model that can be used in inventory decisions.

High-yield points:

- A random variable maps real-life uncertain outcomes to numbers.
- Demand is usually modeled as a random variable `D`.
- A probability distribution tells how likely different demand outcomes are.
- Discrete demand uses probabilities for exact values and cumulative sums.
- Continuous demand uses intervals, CDFs, PDFs, and probabilities from areas under curves.
- The CDF `F(q) = P(D <= q)` is the service level if you stock/order `q` units.
- Poisson is useful for count demand or arrivals with mean `lambda`.
- Uniform is useful for rough one-shot uncertainty over an interval `[A, B]`.
- Normal is useful for high-volume demand or when demand aggregates many effects.
- Normal z-standardization is essential:

```text
z = (x - mu) / sigma
P(D <= x) = Phi(z)
```

- Approximate 95% of a normal distribution lies in:

```text
[mu - 1.96 sigma, mu + 1.96 sigma]
```

- Poisson with large `lambda` can often be approximated by a normal distribution with:

```text
mu = lambda
sigma = sqrt(lambda)
```

## Why This Matters In SCM

Operations managers rarely know exact future demand. They need a model that answers questions like:

- How likely is demand below 100 units?
- How much should we stock to satisfy 95% of demand?
- Is demand better modeled as count arrivals, a broad launch range, or a bell-shaped forecast error?
- Can we approximate a discrete problem with a normal distribution to calculate faster?

The key bridge to inventory management is:

```text
Order q units -> service level = P(D <= q) = F(q)
```

That same logic drives the Newsvendor model: once the optimal service level is known, choose the demand quantile that reaches it.

Related note:

- `supply-chain-management/wiki/topic-03-newsvendor-model/topic-03-newsvendor-model.md`

## Core Concepts

### Random Variable

A random variable is a function that assigns a number to an uncertain real-life outcome.

Example:

```text
Real event: customers arrive and buy apples during the day
Random variable D: total apple demand for that day
Realization: D = 3
```

The model intentionally simplifies reality. It ignores who bought, exact arrival times, and individual motives. It keeps the number needed for the operational decision.

### Sample Space And Events

The sample space `Omega` is the set of all possible realizations.

Examples:

```text
Dice roll: Omega = {1, 2, 3, 4, 5, 6}
Demand count: Omega = {0, 1, 2, 3, ...}
Water amount: Omega = [0, 1]
```

An event is a subset of the sample space.

Example:

```text
Event: odd dice result = {1, 3, 5}
Event: demand does not exceed 5 = {0, 1, 2, 3, 4, 5}
```

### Probability Distribution

A probability distribution assigns probabilities to events.

Exam-safe properties:

```text
P(Omega) = 1
P(empty set) = 0
P(A) >= 0
P(A union B) = P(A) + P(B) - P(A intersection B)
```

If events do not overlap:

```text
P(A union B) = P(A) + P(B)
```

## Discrete Vs Continuous Demand

### Discrete Demand

Discrete means countable.

Examples:

- number of customers arriving
- number of espresso orders per hour
- number of spare parts requested
- number of units sold if units are indivisible

For discrete demand:

```text
P(D = k) can be positive
P(D <= q) = sum from k = 0 to q of P(D = k)
```

Service level if stocking `q` units:

```text
SL(q) = P(D <= q)
```

### Continuous Demand

Continuous means uncountable, usually represented by an interval.

Examples:

- liters of oil demanded
- kilograms of raw material used
- total energy consumption
- approximate high-volume demand modeled continuously

For continuous demand:

```text
P(D = exact value) = 0
P(a <= D <= b) = F(b) - F(a)
```

This is a common exam trap. In a continuous uniform distribution, `P(D = 200) = 0`, even if 200 is inside the interval.

## Poisson Distribution

### When To Use

Use Poisson for count demand over a fixed time interval when arrivals are roughly independent.

Examples:

- customers entering a store per hour
- espresso orders per hour
- spare-part failures per week
- support tickets per day

### Formula

If `D` follows a Poisson distribution with parameter `lambda`:

```text
P(D = k) = (lambda^k * e^(-lambda)) / k!
```

Where:

- `k` is a nonnegative integer
- `lambda > 0`
- `lambda` is both the expected value and the variance of Poisson demand

```text
E[D] = lambda
Var(D) = lambda
sigma = sqrt(lambda)
```

### Cumulative Probability

To calculate service level for stock `q`:

```text
P(D <= q) = sum from k = 0 to q of (lambda^k * e^(-lambda)) / k!
```

Example from the slides:

If `lambda = 3`, then:

```text
P(D <= 5) = P(0) + P(1) + P(2) + P(3) + P(4) + P(5)
          approximately 0.916
```

### Managerial Intuition

Poisson is a count model. It says demand comes in integer counts and is centered around `lambda`.

If the cafe expects 4 espresso orders per hour, `lambda = 4`. The exact number can be 0, 1, 2, 3, ... but values near 4 are more likely than very high values.

## Uniform Distribution

### When To Use

Use continuous uniform when demand is only roughly bounded and all values inside the range are treated as equally plausible.

Examples:

- one-day product launch with very uncertain demand
- early-stage market experiment
- rough scenario planning when there is little data

### Probability Formula

If `D` is uniformly distributed on `[A, B]`:

```text
P(a <= D <= b) = (b - a) / (B - A)
```

for `A <= a <= b <= B`.

CDF:

```text
F(q) = 0                    if q <= A
F(q) = (q - A) / (B - A)    if A <= q <= B
F(q) = 1                    if q >= B
```

Expected value:

```text
E[D] = (A + B) / 2
```

Inverse CDF:

```text
Q = A + SL * (B - A)
```

This inverse CDF is very useful for Newsvendor with uniformly distributed demand.

## CDF And PDF

### CDF

The cumulative distribution function is:

```text
F(q) = P(D <= q)
```

Operational meaning:

```text
If you stock q units, F(q) is the probability demand will be fully satisfied.
```

### PDF

For continuous random variables, the probability density function describes the shape of the distribution.

Key properties:

- `f(x) >= 0`
- `F(x)` is between 0 and 1
- `F(x)` is weakly increasing
- `f(x)` can exceed 1; density is not itself probability
- probability is area under the density curve

Interval probability:

```text
P(a <= D <= b) = F(b) - F(a)
```

## Normal Distribution

### When To Use

Use normal demand when:

- demand is high-volume
- demand is affected by many small independent factors
- rounding to integer units is not important
- negative demand probability is negligible
- the mean-to-standard-deviation ratio is sufficiently high

The slide rule of thumb:

```text
mu / sigma should be high enough, e.g. above 4
```

The slides also note that normal can be suitable when `sigma^2` is not approximately equal to `mu`, meaning Poisson may be unsuitable.

### Parameters

Normal demand is written as:

```text
D ~ Normal(mu, sigma)
```

Where:

- `mu` is the mean
- `sigma` is the standard deviation

### Standardization

To use a z-table or standard normal CDF:

```text
z = (x - mu) / sigma
P(D <= x) = Phi(z)
```

Example from the slides:

```text
mu = 2
sigma = 6
x = 4
z = (4 - 2) / 6 = 0.33
P(D <= 4) = Phi(0.33) approximately 0.6293
```

### Useful z-Table Anchors

```text
Phi(0) = 0.5
Phi(1.96) = 0.975
Phi(-1.96) = 0.025
P(-1.96 <= Z <= 1.96) = 0.95
Phi(2.32) approximately 0.99
```

For general normal demand:

```text
P(mu - 1.96 sigma <= D <= mu + 1.96 sigma) = 0.95
```

### Normal Approximation To Poisson

For large Poisson `lambda`, Poisson demand can be approximated by a normal distribution:

```text
D ~ Poisson(lambda)
approximate with Normal(mu = lambda, sigma = sqrt(lambda))
```

Why useful:

- Poisson cumulative probabilities require summing many terms.
- Normal approximation lets you use z-scores.

Caveat:

- Normal can produce negative values.
- This is not acceptable if negative-demand probability is meaningful.
- It becomes less problematic when `mu` is large relative to `sigma`.

## Distribution Selection Decision Rule

```text
Count arrivals, low/medium integer demand -> Poisson
Broad one-shot interval with rough bounds -> Uniform
High-volume aggregate demand -> Normal
Poisson with large lambda -> Normal approximation may be acceptable
Need service level/order quantity -> use CDF or inverse CDF
```

## Worked Exercise Answers

### Exercise Task 1: Campus Cafe Espresso Demand

Given:

```text
D ~ Poisson(lambda = 4)
e approximately 2.718
```

#### a. Discrete Or Continuous

`D` is discrete because espresso orders are countable.

```text
Omega = {0, 1, 2, 3, ...}
```

#### b. Expected Value And No-Order Probability

```text
E[D] = lambda = 4
```

Probability no student orders espresso:

```text
P(D = 0) = (4^0 * e^-4) / 0! = e^-4 approximately 0.0183
```

#### c. Service Level With Capacity 2

If the cafe can serve at most 2 cups:

```text
SL = P(D <= 2)
   = P(0) + P(1) + P(2)
   = e^-4 * (1 + 4 + 8)
   = 13e^-4
   approximately 0.238
```

Interpretation:

```text
There is only about a 23.8% chance that capacity of 2 cups satisfies all final-hour demand.
```

### Exercise Task 2: Limited-Edition T-Shirt

Given:

```text
D ~ Uniform(150, 450)
Price p = 50
Cost c = 30
Unsold units sold internally at 60% discount from regular price
Salvage value s = 50 * (1 - 0.60) = 20
```

#### a. Expected Value And Point Probability

```text
E[D] = (150 + 450) / 2 = 300
P(D = 200) = 0
```

Because continuous variables have zero probability at one exact point.

#### b. Probability Demand Exceeds 420

```text
1 - F(420) = (450 - 420) / (450 - 150)
           = 30 / 300
           = 0.10
```

#### c. Optimal Service Level And Production Quantity

Underage cost:

```text
c_u = p - c = 50 - 30 = 20
```

Overage cost:

```text
c_o = c - s = 30 - 20 = 10
```

Optimal service level:

```text
SL = c_u / (c_u + c_o)
   = 20 / (20 + 10)
   = 0.6667
```

Uniform inverse CDF:

```text
Q* = A + SL * (B - A)
   = 150 + 0.6667 * 300
   = 350
```

### Exercise Task 3: Vitamin C Normal Demand

Given:

```text
D ~ Normal(mu = 320, sigma = 45)
```

#### a. Probability Demand Is At Most 350

```text
z = (350 - 320) / 45 = 0.667
P(D <= 350) = Phi(0.667) approximately 0.7475
```

#### b. Probability Inside `[mu - 0.23 sigma, mu + 0.23 sigma]`

Standardize both bounds:

```text
z_low = -0.23
z_high = 0.23
```

Therefore:

```text
P(mu - 0.23sigma <= D <= mu + 0.23sigma)
= Phi(0.23) - Phi(-0.23)
approximately 0.5910 - 0.4090
approximately 0.182
```

Interpretation:

```text
Only about 18.2% of demand lies within this narrow band around the mean.
```

### Exercise Task 4: Furniture Shop Poisson Demand And Normal Approximation

Given:

```text
D ~ Poisson(lambda = 200)
c_o = 3
c_u = 5
```

#### a. Optimal Service Level

```text
SL = c_u / (c_u + c_o)
   = 5 / (5 + 3)
   = 0.625
```

#### b. Normal Approximation

Yes, normal approximation is reasonable because expected demand is high.

For Poisson:

```text
mu = lambda = 200
sigma = sqrt(lambda) = sqrt(200) = 14.14
```

The mean is far above zero relative to the standard deviation, so negative-demand probability is negligible.

#### c. Optimal Quantity With Normal Approximation

Find z such that:

```text
Phi(z) = 0.625
z approximately 0.319
```

Then:

```text
Q* = mu + z sigma
   = 200 + 0.319 * 14.14
   approximately 204.5
```

Rounding for discrete units:

```text
Q* approximately 205 units
```

## Mermaid Visual Map

```mermaid
flowchart TD
    RealLife[Uncertain real-life demand] --> RV[Random variable D]
    RV --> Omega[Sample space Omega]
    RV --> Distribution[Probability distribution]
    Distribution --> Discrete{Discrete or continuous?}

    Discrete -->|countable units| Poisson[Poisson demand]
    Poisson --> Lambda[lambda = expected demand]
    Poisson --> SumCDF[P(D <= q) = sum P(D=k)]
    SumCDF --> ServiceLevel[Service level if stocking q]

    Discrete -->|continuous interval| Continuous[Continuous demand]
    Continuous --> Uniform[Uniform distribution]
    Continuous --> Normal[Normal distribution]

    Uniform --> IntervalProb[P(a <= D <= b) = (b-a)/(B-A)]
    Uniform --> UniformInv[Q = A + SL(B-A)]

    Normal --> ZScore[z = (x-mu)/sigma]
    ZScore --> Phi[P(D <= x) = Phi(z)]
    Normal --> NormalInv[Q = mu + z(SL)sigma]

    ServiceLevel --> Newsvendor[Newsvendor order quantity]
    UniformInv --> Newsvendor
    NormalInv --> Newsvendor
```

## Subject Knowledge Graph

### Nodes

| Node | Meaning |
|---|---|
| Random Variable | Function mapping uncertain outcomes to numbers |
| Demand `D` | Random variable representing operational demand |
| Sample Space | All possible realizations of a random variable |
| Probability Distribution | Assigns probabilities to events/outcomes |
| Discrete Demand | Countable demand outcomes |
| Continuous Demand | Demand over an interval, exact point probability zero |
| Poisson Distribution | Count-demand model with parameter `lambda` |
| Uniform Distribution | Equal-density model over interval `[A, B]` |
| Normal Distribution | Bell-shaped model with `mu` and `sigma` |
| CDF | `F(q) = P(D <= q)` |
| PDF | Density whose area gives probability |
| z-score | Standardized normal value `(x - mu) / sigma` |
| Service Level | Probability demand is fully satisfied |
| Normal Approximation | Replacing high-lambda Poisson with normal |
| Newsvendor Model | Uses distribution quantiles to choose order quantity |

### Edges

| From | Relationship | To |
|---|---|---|
| Real-life demand | is modeled as | Random Variable |
| Random Variable | has | Sample Space |
| Probability Distribution | assigns likelihood to | Events |
| Discrete Demand | uses | Probability mass and cumulative sums |
| Continuous Demand | uses | CDF and PDF |
| Poisson Distribution | models | Count arrivals/demand |
| Poisson `lambda` | equals | Expected demand |
| Uniform Distribution | models | Rough bounded uncertainty |
| Normal Distribution | models | High-volume aggregate demand |
| z-score | converts | General normal to standard normal |
| CDF | gives | Service Level |
| Service Level | feeds | Newsvendor Model |
| Normal Approximation | simplifies | Large Poisson calculations |

## Exam Relevance

Likely question types:

- Identify whether demand is discrete or continuous.
- Define the sample space for a demand model.
- Compute Poisson point probabilities or cumulative service levels.
- Compute uniform expected value, interval probability, or inverse CDF quantity.
- Explain why `P(D = x) = 0` for continuous demand.
- Convert normal demand to z-score and use a z-table probability.
- Approximate Poisson demand with a normal distribution.
- Connect CDF/service level to Newsvendor order quantity.

Common mistakes:

- Treating a continuous exact point probability as positive.
- Forgetting to sum Poisson probabilities for `P(D <= q)`.
- Confusing `sigma` and `sigma^2`.
- Using normal approximation when mean is too close to zero.
- Forgetting that `F(q)` means `P(D <= q)`, not `P(D = q)`.
- Rounding order quantity before completing the formula.

## Cheat-Sheet Candidates

```text
Poisson: P(D=k) = lambda^k e^-lambda / k!
Poisson: E[D] = lambda, Var(D) = lambda, sigma = sqrt(lambda)
Uniform: E[D] = (A+B)/2
Uniform: F(q) = (q-A)/(B-A)
Uniform inverse: Q = A + SL(B-A)
Normal z: z = (x-mu)/sigma
Normal: P(D <= x) = Phi(z)
Normal inverse: Q = mu + z(SL)sigma
95% normal interval: mu +/- 1.96 sigma
Service level: SL(q) = P(D <= q) = F(q)
```

## Practice Questions

1. A product has Poisson demand with `lambda = 5`. What is `P(D = 0)` and how would you compute `P(D <= 3)`?
2. Demand is uniformly distributed between 80 and 140. What is `E[D]` and `P(D > 120)`?
3. Demand is normal with `mu = 500`, `sigma = 60`. What z-score corresponds to demand 620?
4. Why is `P(D = 200) = 0` for continuous uniform demand?
5. If `SL = 0.80` and demand is uniform on `[100, 300]`, what quantity should be ordered?
6. When is it reasonable to approximate Poisson demand by normal demand?

## Short Answer Guide

1. `P(D=0)=e^-5`; `P(D<=3)=P(0)+P(1)+P(2)+P(3)`.
2. `E[D]=110`; `P(D>120)=20/60=0.333`.
3. `z=(620-500)/60=2`.
4. Continuous probability is area over an interval; a single point has zero width.
5. `Q=100+0.80*(200)=260`.
6. When `lambda` is large enough that discreteness and negative-demand probability are not operationally important.

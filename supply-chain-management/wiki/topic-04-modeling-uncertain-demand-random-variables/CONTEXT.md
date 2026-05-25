# Ubiquitous Language: Topic 04 Modeling Uncertain Demand With Random Variables

Source note: `topic-04-modeling-uncertain-demand-random-variables.md`
Course: Supply Chain Management
Purpose: shared terminology for discussing uncertain demand, probability distributions, service levels, and the bridge into inventory decisions.

This file follows Matt Pocock's ubiquitous-language pattern: canonical terms, aliases to avoid, relationships, example dialogue, and flagged ambiguities. It is enriched for study use with SCM examples, formula intuition, visual memory aids, and exam traps.

## Demand Modeling Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Random Variable** | A numerical representation of an uncertain real-life outcome. | random number, variable, result |
| **Demand Random Variable** | The random variable, usually written as `D`, that represents uncertain customer demand. | sales amount, realized demand before realization |
| **Realization** | The value a random variable takes after uncertainty is resolved. | forecast, expected demand |
| **Sample Space** | The set of all possible outcomes for a random experiment or demand process. | option list, demand range when outcomes are countable |
| **Event** | A subset of the sample space whose probability can be calculated. | scenario, case |
| **Probability Distribution** | A rule assigning probabilities to outcomes or intervals of a random variable. | forecast method, histogram only |
| **CDF** | The cumulative distribution function `F(q) = P(D <= q)`. | exact probability, density |
| **Service Level** | The probability that stock or capacity `q` covers demand, equal to `P(D <= q)`. | fill rate, probability of selling out |
| **Quantile** | The demand value `q` that reaches a target cumulative probability. | average demand, mode |

## Demand Type Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Discrete Demand** | Demand with countable outcomes such as `0, 1, 2, ...`. | integer-ish demand, lumpy demand |
| **Continuous Demand** | Demand modeled over an interval where exact point probabilities are zero. | decimal demand, smooth demand |
| **Probability Mass** | Probability attached to an exact value in a discrete distribution. | density, height of the bar |
| **Probability Density** | A curve height for continuous demand whose area over an interval gives probability. | probability at a point |
| **Interval Probability** | The probability that continuous demand lies between two bounds. | point probability |

## Distribution Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Poisson Distribution** | A discrete distribution for count demand or arrivals over a fixed interval with mean `lambda`. | normal for counts, arrival curve |
| **Lambda** | The Poisson parameter that equals both expected demand and variance. | rate only, average only |
| **Uniform Distribution** | A continuous distribution where all values inside `[A, B]` have equal density. | equal probability for every exact point |
| **Lower Bound** | The smallest possible value `A` in a uniform demand interval. | minimum forecast |
| **Upper Bound** | The largest possible value `B` in a uniform demand interval. | maximum forecast |
| **Normal Distribution** | A continuous bell-shaped distribution with mean `mu` and standard deviation `sigma`. | Gaussian without parameters, high-demand distribution |
| **Mean** | The expected central value of demand. | most likely value, guaranteed demand |
| **Variance** | The expected squared deviation from the mean. | standard deviation |
| **Standard Deviation** | The typical scale of demand uncertainty, written as `sigma`. | variance, average error |
| **Standard Normal** | A normal distribution with mean `0` and standard deviation `1`. | z-table distribution only |
| **z-score** | The number of standard deviations a value is above or below the mean. | probability, percentile |

## Formula Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Poisson Point Probability** | The probability of exactly `k` arrivals: `P(D=k)=lambda^k e^-lambda / k!`. | service level |
| **Poisson Cumulative Probability** | The sum of point probabilities up to `q`: `P(D<=q)=sum P(D=k)`. | point probability |
| **Uniform CDF** | For `A <= q <= B`, the cumulative probability `(q-A)/(B-A)`. | density |
| **Uniform Inverse CDF** | The quantity formula `Q=A+SL(B-A)` for a target service level. | expected value |
| **Normal Standardization** | The conversion `z=(x-mu)/sigma` from normal demand to standard normal units. | normalization in general |
| **Normal Approximation** | Replacing high-`lambda` Poisson demand with `Normal(mu=lambda, sigma=sqrt(lambda))`. | exact Poisson solution |
| **Critical Ratio** | The Newsvendor target service level `c_u/(c_u+c_o)`. | cost ratio, margin |

## Visual Memory Aids

### Discrete vs Continuous Demand

```text
Discrete demand: count bars

P(D=k)
  ^
  |        |
  |    |   |   |
  | |  |   |   |  |
  +----------------> k
    0  1   2   3  4

Exact value can have positive probability:
P(D = 2) > 0
```

```text
Continuous demand: probability area

f(x)
 ^
 |          /\
 |         /  \
 |        /    \
 |_______/______\_______> x
         a      b

Exact point has zero probability:
P(D = 200) = 0

Interval has probability:
P(a <= D <= b) = area under curve
```

### Distribution Selection Map

```mermaid
flowchart TD
    D[Uncertain demand D] --> Count{Is demand countable?}
    Count -->|Yes, arrivals or units| Poisson[Poisson]
    Count -->|No, measured over interval| Continuous{What information do we have?}
    Continuous -->|Only rough lower and upper bounds| Uniform[Uniform]
    Continuous -->|Many small drivers, high volume| Normal[Normal]
    Poisson --> Large{lambda large?}
    Large -->|Yes| Approx[Normal approximation]
    Large -->|No| Sum[Sum Poisson probabilities]
    Uniform --> CDF[Use CDF or inverse CDF]
    Normal --> Z[Use z-score and Phi]
    Approx --> Z
    CDF --> SL[Service level P(D <= q)]
    Z --> SL
    Sum --> SL
```

### z-score Intuition

```text
z = (x - mu) / sigma

        mu-sigma     mu      mu+sigma
           |         |          |
Normal: ___|______/^^^^\________|_____
                   mean

If x = mu, z = 0.
If x = mu + sigma, z = 1.
If x = mu - 2sigma, z = -2.
```

## Distribution Examples In SCM

| Situation | Use | Why |
|---|---|---|
| A cafe counts espresso orders in the final hour. | **Poisson Distribution** | Orders arrive as nonnegative counts over a fixed time window. |
| A product launch may sell anywhere from 150 to 450 shirts, with little data. | **Uniform Distribution** | The manager only trusts a rough demand interval. |
| A vitamin product has high-volume daily demand affected by many small factors. | **Normal Distribution** | Aggregated demand often becomes bell-shaped. |
| A furniture shop has Poisson demand with `lambda = 200`. | **Normal Approximation** | Summing many Poisson terms is inefficient and negative-demand risk is negligible. |

## Relationships

- A **Demand Random Variable** is a kind of **Random Variable**.
- A **Random Variable** has exactly one **Sample Space** in the model.
- An **Event** is a subset of a **Sample Space**.
- A **Probability Distribution** assigns probability to **Events**.
- **Discrete Demand** uses **Probability Mass**.
- **Continuous Demand** uses **Probability Density** and **Interval Probability**.
- A **CDF** converts a quantity `q` into a **Service Level**.
- A **Quantile** converts a target **Service Level** into a quantity `q`.
- A **Poisson Distribution** uses **Lambda** as mean and variance.
- A **Normal Distribution** uses **Mean** and **Standard Deviation**.
- A **z-score** converts a **Normal Distribution** value into **Standard Normal** units.
- A **Critical Ratio** becomes a target **Service Level** in the Newsvendor model.

## Example Dialogue

> **Student:** "If demand is Poisson with `lambda = 4`, can I say the service level for capacity 2 is `P(D=2)`?"
>
> **Professor:** "No. `P(D=2)` is the probability of exactly two orders. The **Service Level** for capacity 2 is `P(D <= 2)`, so you must add `P(0)+P(1)+P(2)`."
>
> **Student:** "For uniform demand between 150 and 450, why is `P(D=200)` zero if 200 is possible?"
>
> **Professor:** "Because it is **Continuous Demand**. Probability is area over an interval. A single point has no width, so its area is zero."
>
> **Student:** "Then what does a z-score actually tell me?"
>
> **Professor:** "A **z-score** tells how many standard deviations `x` sits from the mean. It turns `D ~ Normal(mu, sigma)` into standard normal language so the z-table can give `P(D <= x)`."

## Flagged Ambiguities

- "Demand" can mean **Demand Random Variable**, **Realization**, or **Mean**. Use `D` for the random variable, `D = x` for a realization, and `E[D]` or `mu` for expected demand.
- "Probability of demand 200" is ambiguous. For **Discrete Demand**, `P(D=200)` may be positive. For **Continuous Demand**, `P(D=200)=0`; ask for an interval or CDF instead.
- "Service level" is not the same as "selling all units." In this topic, **Service Level** means `P(D <= q)`, the probability demand is fully covered by stock or capacity.
- "Variance" and **Standard Deviation** are not interchangeable. Variance is `sigma^2`; standard deviation is `sigma`.
- "z-score" is not a probability. The **z-score** is an input to the standard normal CDF `Phi(z)`, which returns a probability.
- "Uniform means every demand is equally likely" is imprecise. In a continuous uniform distribution, equal-length intervals have equal probability; exact points have zero probability.

## Exam Traps And Corrections

| Trap | Correction |
|---|---|
| Use `P(D=q)` when asked for service level. | Use `P(D <= q)`. |
| Treat continuous exact point probability as positive. | For continuous demand, `P(D=x)=0`. |
| Confuse Poisson `lambda` with only the mean. | For Poisson, `E[D]=lambda` and `Var(D)=lambda`. |
| Use normal approximation when demand can be near or below zero. | Check that `mu` is large relative to `sigma`. |
| Read density height as probability. | Probability is area under the density curve. |
| Round a Newsvendor quantity before finishing the formula. | Calculate first, then round according to indivisible-unit logic. |

## Cheat-Sheet Language

```text
Discrete -> exact values can have probability.
Continuous -> intervals have probability; exact values have probability 0.

Poisson:
P(D=k) = lambda^k e^-lambda / k!
E[D] = lambda
Var(D) = lambda
sigma = sqrt(lambda)
P(D<=q) = sum from k=0 to q of P(D=k)

Uniform:
E[D] = (A+B)/2
F(q) = (q-A)/(B-A)
Q = A + SL(B-A)

Normal:
z = (x-mu)/sigma
P(D<=x) = Phi(z)
Q = mu + z(SL)sigma
95 percent interval = mu +/- 1.96sigma
```

# Exercise 12: Options

Source files:

- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260709/CW 28  07.07. _ 08.07./Exercise 12.pdf`
- `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260709/CW 28  07.07. _ 08.07./Exercise 12 - Solutions.pdf`

Lecture folder: `finance-and-investment-management/`
Processed: 2026-07-09

## High-Yield 80/20 Summary

Options are rights, not obligations. The exam route is first payoff logic, then valuation relations, then binomial pricing.

High-yield moves:

1. Call buyer benefits when the underlying price is above strike.
2. Put buyer benefits when the underlying price is below strike.
3. Profit equals payoff minus premium for long positions and premium minus payoff for short positions.
4. Put-call parity links stock, put, call, and risk-free bond.
5. Binomial valuation uses risk-neutral probabilities, not the real-world expected return.
6. American puts may be worth more than European puts because early exercise can be valuable.

## Core Terms

| Term | Meaning |
|---|---|
| Call option | Right to buy the underlying at strike price `K`. |
| Put option | Right to sell the underlying at strike price `K`. |
| European option | Exercisable only at maturity. |
| American option | Exercisable any time until maturity. |
| Intrinsic value | Immediate exercise value, floored at zero. |
| Time value | Option price minus intrinsic value. |
| Long option | Buyer position; pays premium, owns right. |
| Short option | Seller/writer position; receives premium, has obligation if exercised. |

## Payoff And Profit Logic

```text
Long call payoff = max(S_T - K, 0)
Long call profit = max(S_T - K, 0) - call premium

Short call profit = call premium - max(S_T - K, 0)

Long put payoff = max(K - S_T, 0)
Long put profit = max(K - S_T, 0) - put premium

Short put profit = put premium - max(K - S_T, 0)
```

## Worked Exercise Routes

### A.1: Long European Put

Known inputs:

```text
Put premium = 3 EUR
Strike K = 40 EUR
Initial share price = 42 EUR
```

Exercise condition:

```text
Exercise if S_T < K
Exercise if S_T < 40
```

Profit condition:

```text
Profit = max(40 - S_T, 0) - 3
Profit > 0 when 40 - S_T > 3
S_T < 37
```

Interpretation: the buyer exercises below 40 but only profits below 37 because the 3 EUR premium must be recovered.

### A.2: Short European Call

Known inputs:

```text
Call premium received = 4 EUR
Strike K = 50 EUR
Initial share price = 47 EUR
```

Exercise by buyer:

```text
Buyer exercises if S_T > 50
```

Seller profit:

```text
Profit = 4 - max(S_T - 50, 0)
Profit > 0 when S_T < 54
```

Interpretation:

- If `S_T < 50`, call expires unexercised and seller keeps 4.
- If `50 < S_T < 54`, seller still profits but less than 4.
- If `S_T > 54`, seller loses money.

### A.3: Long Strangle

Position:

```text
Long call with K = 45, premium = 3
Long put with K = 40, premium = 4
Total premium = 7
```

Profit:

```text
Profit = max(S_T - 45, 0) + max(40 - S_T, 0) - 7
```

Break-even points:

```text
Upper break-even = 45 + 7 = 52
Lower break-even = 40 - 7 = 33
```

Interpretation: the trader bets on a strong price movement in either direction.

### Put-Call Parity

For a dividend-free underlying and same strike/maturity:

```text
S_0 + P_0 - C_0 = K / (1+r_f)^T
```

Interpretation: stock plus put minus call replicates a risk-free payoff equal to the strike at maturity.

Exam trap: parity is about portfolios with same maturity and strike. Do not mix American/European assumptions carelessly.

### A.4: Two-Step Binomial BMW Option

Known inputs:

```text
S_0 = 72
K = 70
Term = 6 months = two 3-month steps
Three-month risk-free growth factor = 1.003
u = 1.053
d = 0.953
No dividend expected
```

Risk-neutral probability:

```text
p = (1.003 - 0.953) / (1.053 - 0.953)
p = 0.050 / 0.100
p = 0.5
```

Terminal stock prices:

```text
S_uu = 72 x 1.053^2 = 79.8342
S_ud = 72 x 1.053 x 0.953 = 72.2526
S_dd = 72 x 0.953^2 = 65.3910
```

European call payoffs:

```text
C_uu = max(79.8342 - 70, 0) = 9.8342
C_ud = max(72.2526 - 70, 0) = 2.2526
C_dd = 0
```

European call value:

```text
C_0 = [9.8342 x 0.5^2 + 2.2526 x 2 x 0.5^2] / 1.003^2
C_0 = 3.5634
```

European put payoffs:

```text
P_uu = 0
P_ud = 0
P_dd = max(70 - 65.3910, 0) = 4.6090
```

European put value:

```text
P_0 = 4.6090 x 0.5^2 / 1.003^2
P_0 = 1.1454
```

Put-call parity check:

```text
S_0 + P_0 - C_0 = 72 + 1.1454 - 3.5634 = 69.5820
K / 1.003^2 = 70 / 1.003^2 = 69.5820
```

Hedge ratio:

```text
C_u = (9.8342 x 0.5 + 2.2526 x 0.5) / 1.003 = 6.0253
C_d = (2.2526 x 0.5) / 1.003 = 1.1229
m = (uS_0 - dS_0) / (C_u - C_d)
m = (1.053 x 72 - 0.953 x 72) / (6.0253 - 1.1229)
m = 1.4687
```

The hedge portfolio consists of one share and `1.4687` short calls. Its value at `t=1` is effectively risk-free:

```text
Up state: 1.053 x 72 - 1.4687 x 6.0253 = 66.9666
Down state: 0.953 x 72 - 1.4687 x 1.1229 = 66.9667
```

### A.5: American Put From The Same Binomial Tree

At the down node:

```text
Immediate exercise value = 70 - 72 x 0.953 = 1.384
Continuation value = 4.6090 x 0.5 / 1.003 = 2.2976
Choose max = 2.2976
```

Value at `t=0`:

```text
P_0 = 2.2976 x 0.5 / 1.003 = 1.1454
```

Interpretation: early exercise is not optimal here, so the American and European put values are equal in this example.

## Visual Knowledge Map

```mermaid
flowchart TD
    Options[Options] --> Call[Call right to buy]
    Options --> Put[Put right to sell]
    Call --> LongCall[Long call payoff max(S-K,0)]
    Put --> LongPut[Long put payoff max(K-S,0)]
    Options --> Parity[Put-call parity]
    Options --> Binomial[Binomial valuation]
    Binomial --> RN[Risk-neutral probability]
    Binomial --> Terminal[Terminal payoffs]
    Binomial --> Backward[Backward induction]
    Binomial --> American[American early exercise check]
```

## Subject Knowledge Graph

| Node | Type | Description |
|---|---|---|
| Call option | derivative | Right to buy underlying at strike. |
| Put option | derivative | Right to sell underlying at strike. |
| Premium | price | Amount paid by option buyer to seller. |
| Intrinsic value | payoff component | Immediate exercise value floored at zero. |
| Put-call parity | valuation relation | Replication relation among stock, put, call, and risk-free bond. |
| Binomial model | valuation model | Option pricing through up/down states and backward induction. |
| Risk-neutral probability | pricing input | Probability used for arbitrage-free valuation, not real-world belief. |
| Hedge ratio | replication input | Number of options/shares needed for a risk-free hedge. |

| From | Relationship | To |
|---|---|---|
| Long call | profits from | Large price increase |
| Long put | profits from | Large price decrease |
| Short call | loses from | Price above strike plus premium |
| Put-call parity | replicates | Risk-free payoff |
| Binomial model | discounts | Expected risk-neutral payoff |
| American option | requires | Early exercise check |

## Retrieval Prompts

1. What is the difference between exercise condition and profit condition?
2. Why does a long put in A.1 exercise below 40 but profit below 37?
3. Why does the short call seller in A.2 profit below 54?
4. What does put-call parity replicate?
5. Why does binomial valuation use risk-neutral probability instead of the physical probability?
6. When can an American put be worth more than a European put?

## Practice Tasks

1. Draw the profit line for a long put with `K=40`, premium `3`.
2. Compute the upper and lower break-even points for the strangle in A.3.
3. Recompute the risk-neutral probability in A.4.
4. Check put-call parity with the A.4 option values.

## Open Uncertainties

- The source provides official solutions for Exercise 12. Graphical payoff diagrams are not reproduced; the note preserves payoff/profit rules and calculation routes.

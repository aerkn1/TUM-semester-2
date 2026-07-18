# Ubiquitous Language: Exercise 12 Options

Source note: `exercise-12-options.md`
Course: Finance and Investment Management
Processed: 2026-07-09

## Option Position Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Call Option** | Right, not obligation, to buy the underlying at strike `K`. | stock purchase |
| **Put Option** | Right, not obligation, to sell the underlying at strike `K`. | short sale |
| **Long Option** | Buyer of the option; pays premium and owns the right. | seller |
| **Short Option** | Seller/writer of the option; receives premium and may have to perform. | buyer |
| **Strike Price** | Fixed exercise price `K`. | option price |
| **Premium** | Price paid for the option. | payoff |
| **European Option** | Exercisable only at maturity. | EU-listed option |
| **American Option** | Exercisable any time until maturity. | US-listed option |

## Payoff And Valuation Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Intrinsic Value** | Immediate exercise value floored at zero. | total option value |
| **Time Value** | Option value above intrinsic value. | waiting cost |
| **Break-Even Price** | Underlying price where option profit equals zero after premium. | strike |
| **Put-Call Parity** | Arbitrage relation linking stock, put, call, and discounted strike. | rule of thumb |
| **Binomial Model** | Option valuation model with up/down underlying states. | decision tree only |
| **Risk-Neutral Probability** | Pricing probability that makes expected payoff discountable at risk-free rate. | physical probability |
| **Backward Induction** | Value final payoffs first, then discount back through the tree. | forward compounding |
| **Early Exercise Check** | For American options, compare immediate exercise value with continuation value. | automatic exercise |

## Core Formulas

| Formula | Meaning | Use |
|---|---|---|
| `Long call payoff = max(S_T-K,0)` | Call buyer payoff | Price increase exposure. |
| `Long put payoff = max(K-S_T,0)` | Put buyer payoff | Price decrease exposure. |
| `Long option profit = payoff - premium` | Buyer profit | Separate exercise from profit. |
| `Short option profit = premium - payoff` | Seller profit | Identify loss region. |
| `S_0 + P_0 - C_0 = K/(1+r_f)^T` | Put-call parity | European-style no-dividend parity. |
| `p = (q-d)/(u-d)` | Risk-neutral up probability | Binomial valuation. |
| `Option value = discounted risk-neutral expected payoff` | Binomial pricing | Backward induction. |

## Relationships

- **Premium** shifts **Break-Even Price** away from **Strike Price**.
- **Put-Call Parity** creates an arbitrage-free relation between **Call Option** and **Put Option**.
- **Risk-Neutral Probability** belongs to valuation, not forecasting.
- **American Option** value is at least **European Option** value with the same payoff terms.
- **Early Exercise Check** matters especially for puts.

## Example Dialogue

Student: "The put buyer exercises below 40, so the profit starts below 40."

Professor: "Exercise and profit are different. The buyer paid a 3 EUR premium, so profit starts only below 37."

Student: "The binomial model says the stock has a 50% chance of going up?"

Professor: "No. That is the risk-neutral probability for pricing. It is not necessarily the physical probability."

## Flagged Ambiguities

| Ambiguity | Canonical recommendation |
|---|---|
| `p` | Say risk-neutral probability in binomial valuation. |
| `q` | In some slides, `q` may denote physical probability; do not mix with risk-neutral `p`. |
| Option price | Say premium or value, not payoff. |
| Exercise | Separate exercise decision from profit decision. |
| American | Means early exercise allowed, not country of trading. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Confusing payoff and profit. | Subtract premium for long positions and add premium for short positions. |
| Saying a long put profits whenever exercised. | It profits only below `K - premium`. |
| Using real-world expected return in binomial pricing. | Use risk-neutral probability and risk-free discounting. |
| Forgetting early exercise for American puts. | Compare immediate exercise with continuation value. |
| Applying put-call parity with mismatched maturities or strikes. | Same underlying, strike, and maturity are required. |

## Cheat-Sheet Language

```text
Payoff first, premium second.
Long call: upside above K; break-even K + premium.
Long put: downside below K; break-even K - premium.
Binomial: terminal payoffs -> risk-neutral probabilities -> discount backward.
American option: each node value = max(exercise now, continue).
```

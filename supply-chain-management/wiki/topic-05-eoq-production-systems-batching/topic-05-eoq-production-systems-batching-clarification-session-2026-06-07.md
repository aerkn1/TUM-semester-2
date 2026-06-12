# Topic 05 EOQ Clarification Session - 2026-06-07

Source note: `topic-05-eoq-production-systems-batching.md`
Context companion: `CONTEXT.md`
Course: Supply Chain Management
Session type: clarification-first conceptual bridge
Status: clarification completed; first active recall pending

Continuation instruction added 2026-06-08: every worked EOQ/EPQ calculation must show the symbolic formula, substituted values, numerical result, and units. Do not record result-only answer lines.

## Session Goal

Connect EOQ to Forecasting, Random Variables, and Newsvendor before beginning calculations, then distinguish the main EOQ variants through analogies and use cases.

## Clarification Questions And Outcomes

| User Question Or Statement | Clarification Saved |
|---|---|
| "How is EOQ linked with the previous random variables and Newsvendor? Is it a continuation?" | It continues inventory decision-making but follows the deterministic recurring-replenishment branch. Forecasting estimates demand; Random Variables represent uncertainty; model selection then separates one-time uncertain demand into Newsvendor and recurring stable demand into EOQ. |
| Demand and the forecast model can change when control limits are exceeded. Can assumed constant EOQ demand also change drastically? | Yes. Constant demand is a planning assumption for the current decision horizon. Repeated forecast-control violations can trigger model refitting, a new demand-rate estimate `lambda`, and recalculation of EOQ. |
| How do Newsvendor and EOQ actually diverge? | Newsvendor balances underage and overage costs for one commitment before uncertain demand. EOQ balances ordering/setup and holding costs across repeated cycles. Newsvendor leftovers can lose value; EOQ stock normally carries forward to later recurring demand. |
| Is Newsvendor used inside EOQ when exceptional demand creates an urgent order? | Normally no. Recurring uncertainty is handled by EOQ for `Q`, plus reorder point and safety stock for timing and protection. Newsvendor is appropriate only if the exception creates a separate one-time uncertain commitment. |
| Do all EOQ variants still revolve around constant demand? | Yes. Existing inventory changes the first-order time; lead time changes the reorder point; a finite horizon requires an integer order count; finite production changes the inventory pattern and leads to EPQ. |
| "I also need to understand all those concept differences with analogy and example use cases again." | One bakery/flour example was used across every variant so each formula change was tied to an operational condition. |
| "Understood. Let's save this for now and will continue later." | Clarification closed. First-pass recall and calculations remain pending. |

## Refined Mental Models

### Inventory-Model Router

```text
Forecasting estimates future demand
        |
Random variables describe uncertainty
        |
Choose the inventory decision
        |-- one order + uncertain demand --> Newsvendor
        `-- repeated orders + stable demand --> EOQ
```

### Dynamic Planning Loop

```text
Actual demand
-> forecast errors
-> control-limit monitoring
-> model refit if instability persists
-> updated expected demand rate lambda
-> recalculated EOQ
```

EOQ is therefore not permanently fixed. It is optimal only for the current values of `lambda`, ordering cost `K`, and holding cost `h`.

### EOQ Versus Newsvendor

| Dimension | Newsvendor | EOQ |
|---|---|---|
| Decision pattern | One-time commitment | Recurring replenishment |
| Demand treatment | Probability distribution | Known constant rate `lambda` |
| Cost trade-off | Underage versus overage | Ordering/setup versus holding |
| Excess inventory | May become obsolete, discounted, or wasted | Usually remains for later recurring demand but incurs holding cost |
| Main output | Service-level quantile and one-time `Q*` | Recurring batch size, frequency, and cycle cost |

### Bakery Flour Analogies

| Variant | Bakery use case | What changes? | Decision |
|---|---|---|---|
| Basic EOQ | Flour is consumed steadily and delivered immediately. | Recurring setup-versus-storage trade-off. | How much flour per delivery? |
| Initial inventory | The bakery already has 400 kg. | Existing stock delays the first delivery. | How long should it wait before the first order? |
| Positive lead time | The supplier needs two weeks. | Order before inventory reaches zero. | At which inventory level should it order? |
| Initial inventory plus lead time | Stock lasts four weeks, delivery takes two. | Place the first order two weeks before depletion. | When should the first order be placed? |
| Finite horizon | A temporary bakery operates for ten weeks. | Only a whole number of deliveries is feasible. | How many deliveries and how much per delivery? |
| EPQ | Flour is produced gradually while also being consumed. | Inventory builds at `p - lambda`, not instantaneously. | What production batch minimizes setup and holding cost? |

Memory analogies:

- Existing inventory: groceries already at home change the next shopping date, not the ideal future trip size.
- Lead time: reorder medicine before the current supply is exhausted.
- Finite horizon: a holiday allows only a whole number of shopping trips.
- EPQ: a bathtub fills while the drain remains open, so the level rises by inflow minus outflow.

## Quality And Weak Spots

| Area | Quality | Next Action |
|---|---|---|
| EOQ versus Newsvendor purpose | green after clarification | Retrieve the distinction without the table. |
| Dynamic forecast-to-EOQ link | green after clarification | Explain when `lambda` should be updated and EOQ recalculated. |
| EOQ variants | yellow-green | Classify cases before selecting formulas. |
| Calculations | unassessed | Begin with basic EOQ, order frequency, average inventory, and annual cost. |

## Exact Continuation Point

Start the first active-recall session with:

> A firm has repeated replenishment, stable expected demand, fixed ordering cost, and holding cost. Explain why this is EOQ rather than Newsvendor. Then state what changes if the firm has initial inventory, positive lead time, a finite selling horizon, or a finite production rate.

After the model router is correct, calculate the basic practice case:

```text
lambda = 9,600 units/year
K = EUR 80/order
h = EUR 6/unit/year
```

Compute `Q*`, orders per year, average inventory, and verify that annual ordering cost equals annual holding cost at the optimum.

Use this recall sequence for each requested value:

```text
symbolic formula
= substituted values
= numerical result with units
```

The user should recall and place the variables before calculating; the coach should correct the formula setup before checking arithmetic.

## References

- `topic-05-eoq-production-systems-batching.md`
- `CONTEXT.md`
- `../topic-02-forecasting/topic-02-forecasting.md`
- `../topic-03-newsvendor-model/topic-03-newsvendor-model.md`
- `../topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md`

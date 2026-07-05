# Topic 06 Bullwhip Effect — Clarification And Active-Recall Session

Date completed: 2026-06-21
Course: Supply Chain Management
Source note: [Topic 06: Supply Chain Coordination And The Bullwhip Effect](topic-06-supply-chain-coordination-bullwhip-effect.md)
Context companion: [CONTEXT.md](CONTEXT.md)
Outcome: first active-recall pass completed

## Session Focus

The session used detailed retail and manufacturing cases to distinguish:

- actual customer demand from downstream orders
- information visibility from replenishment decision rights
- communication infrastructure from decision mechanisms
- locally rational batching from system-wide variability
- direct mitigation of a cause from supporting coordination mechanisms

## Clarification Frame

The core distinction established during the session was:

```text
POS = what customers actually bought
VMI = who decides replenishment
EDI = how business information and documents are transmitted
CPFR = how partners jointly plan forecast and replenishment
EDLP = how stable pricing removes promotion-driven forward buying
```

## Recall Evidence

### 1. Forward Buying, EDI, CPFR, And EDLP

**Coach prompt**

> A supermarket sells 100 detergent cases per week. The supplier offers a 25% discount in week 1. The supermarket orders 500 cases in week 1 and then zero in weeks 2–5, although POS remains 100. Identify the phenomenon, explain why EDI alone does not solve it, and select the best mitigation.

**User raw answer**

> 1-forward buying
> 2-EDI works for fixed inventory setup configured based on demand-order quantity. This incident is more about one time batch purchase due to the discount that might not be within the boundary of reorder/repurchase trigger interval of the retailer
> 3-maybe CPFR can solve it by informing the supplier regarding the reason why such spike in order occurs

**Professor feedback**

- `green`: correctly identified forward buying.
- `yellow`: correctly concluded that EDI alone does not solve the behavior, but EDI is a standardized information/document channel, not an inventory policy.
- `yellow-green`: CPFR can explain the temporary spike, but EDLP is the direct mitigation because it removes the temporary price incentive.

**Refined model**

```text
EDLP removes the cause.
CPFR explains and jointly plans around the event.
EDI can transmit either a good or a distorted order efficiently.
```

### 2. POS, VMI, And EDI

**Coach prompt**

> A supermarket lets a beverage manufacturer see daily POS and inventory. The manufacturer—not the supermarket—decides when and how much to replenish. Explain the distinct role of POS, VMI, and EDI.

**User raw answer**

> 1-explicitly shares the actual demand from customers and their respective orders with the supplier for better observability.
> 2-besides POS, vendor decides on when to order and the quantity rather than retailer
> 3-only allow the transfer of order command to the suppllier once the stocks are replenished

**Professor feedback**

- `yellow-green`: POS reveals actual checkout purchases; it does not necessarily report customer orders.
- `green`: VMI correctly identified as vendor control over replenishment timing and quantity.
- `red-yellow`: EDI is not limited to an order after replenishment; it can carry POS/inventory reports, purchase orders, confirmations, advance shipping notices, and invoices throughout the cycle.

### 3. Order Batching

**Coach prompt**

> A retailer sells 50 coffee machines per week but orders 200 every four weeks to obtain full-truck shipping. Identify the mechanism, explain why it is locally rational, state what the manufacturer observes, and give two coordination methods.

**User raw answer**

> 1-order batching?
> 2-to reduce the logistic costs?
> 3-large spike in demand
> 4-POS,EDI

**Professor feedback**

- `green`: order batching and logistics-cost motivation were correct.
- `yellow`: the manufacturer observes an **order spike**, not necessarily a customer-demand spike.
- `yellow`: POS reveals stable sell-through; EDI alone transmits the batch efficiently. CPFR, VMI, order consolidation, staggered ordering, or transport-pricing changes alter planning or incentives.

**Refined model**

```text
Customer demand: 50, 50, 50, 50
Retailer orders: 200, 0, 0, 0

Batching can be locally rational but systemically risky.
```

### 4. Order Synchronization

**Coach prompt**

> Ten retailers sell 20 units each per week. Because deliveries occur every Monday, all submit weekly orders on Friday. Is this order batching, order synchronization, or both? What would staggering order days change?

**User raw answer**

> 1-seems order syncronization, but also batching could be possible across retailers to reduce costs and the logistic roundtrips
> 2-not a single day piling for the delivery, more homogeneous distribution across weekdays?

**Professor feedback**

- `green`: primary cause correctly identified as synchronization; batching may coexist if each retailer accumulates demand into a weekly order.
- `green`: staggering smooths distributor workload without changing total weekly customer demand.

### 5. Shortage Gaming

**Coach prompt**

> A chip supplier can fulfil only 50% of requested quantities. A manufacturer needs 1,000 chips but orders 2,000. Identify the mechanism, explain the capacity mistake and later collapse, and propose an allocation rule.

**User raw answer**

> 1-shortage gaming
> 2-due to the locally rational decision of retailers, manufacturer will see higher orders with spike therefore tend to increase production capacity
> 3-on retailer side to avoid the overpurchasing after the shortage, they bring the order quantities back to normal
> 4-CPFR for joint planning?

**Professor feedback**

- `green`: shortage gaming and the false capacity signal were correctly identified.
- `green`: the apparent collapse follows normalization and cancellation of inflated orders.
- `yellow-green`: CPFR improves transparency, but allocation based on historical consumption or verified sell-through more directly removes the incentive to exaggerate.

**Terminology correction**

The raw slides list turn-and-earn under elimination of pathological incentives. They do not explicitly identify it as the primary shortage-gaming remedy. Historical-sales allocation is the more precise shortage-gaming answer; turn-and-earn follows the related principle of tying access to demonstrated sell-through.

### 6. Reactive And Over-Reactive Ordering

**Coach prompt**

> A retailer normally orders 100 units weekly. One delivery is delayed, so the manager orders 200 from the original supplier and 100 from a backup supplier. All shipments arrive together. Name the mechanism, describe following orders, and explain how shorter lead times and shipment visibility help.

**User raw answer**

> 1-over-reactive ordering
> 2-due to the excess quantity in inventory by over-reacted order, which is higher quantity then the normal, the new ordering date might diverge as the retailer will tend to consume the ordered product first
> 3-no idea

**Professor feedback**

- `green`: over-reactive ordering correctly identified.
- `green`: excess inventory delays subsequent orders, producing a spike followed by zeros.
- `yellow`: shorter lead times reduce the interval of uncertainty; shipment-status information reveals inventory already in transit and prevents duplicate emergency orders.

### 7. POS Versus Shipment Status

**Coach prompt**

> In one sentence, why does shipment-status information solve a different problem from POS data?

**User raw answer**

> POS more focused on customer demand information, not on orders

**Professor feedback**

- `green`: POS was correctly assigned to customer-demand visibility.
- Shipment status complements it by reporting what replenishment has already been ordered, dispatched, or remains in transit.

### 8. Integrated Bullwhip Diagnosis

**Coach prompt**

> Customer sales remain stable. A retailer places one large order during a supplier discount and then no orders for several weeks. The supplier interprets the spike as market growth and increases production. Identify the cause, information distortion, direct mitigation, and one supporting mechanism.

**User raw answer**

> 1-forward buying
> 2-manufacturer only sees the spike in order, not the actual demand
> 3-POS, EDLP

**Professor feedback**

- `green`: forward buying correctly identified.
- `green`: correctly separated the upstream order spike from stable final demand.
- `green`: EDLP is the direct mitigation; POS is the supporting information mechanism.

## Quality Summary

| Area | Quality | Evidence |
|---|---|---|
| Cause recognition | `green` | Correctly identified forward buying, batching, synchronization, shortage gaming, and over-reactive ordering. |
| Demand versus orders | `green` after correction | Final integration answer clearly separated manufacturer orders from actual customer demand. |
| Direct versus supporting mitigation | `yellow-green` | Initially selected CPFR/POS where EDLP or incentive redesign was more direct; corrected during the session. |
| POS/VMI/EDI distinction | `yellow-green` | POS and VMI became clear; EDI initially treated as an order trigger rather than a communication standard. |
| Lead-time and pipeline visibility | `yellow` | Required explanation; needs D+1 retrieval. |

## Weak Spots For D+1

1. State `POS = demand evidence`, `VMI = replenishment decision rights`, and `EDI = transmission mechanism` without mixing their roles.
2. Select the direct lever before supporting tools: EDLP for promotion-driven forward buying; historical-sales allocation for shortage gaming; shipment visibility and shorter lead times for duplicate reactive orders.
3. Use **order spike** rather than **demand spike** unless final customer consumption actually changed.

## Next Recall Prompts

1. Classify five short cases without seeing the mechanism names.
2. For each case, give one direct mitigation and one supporting information mechanism.
3. Explain why EDI can accelerate both good coordination and distorted ordering.
4. Reconstruct the reactive-ordering pipeline: on-hand stock, on-order stock, delayed shipment, emergency order, and subsequent order drought.

## Scheduling Outcome

- First Pass completed: `2026-06-21`
- Canonical D+1: `2026-06-22`
- D+1 focus: terminology roles, direct-versus-supporting mitigation, and lead-time visibility

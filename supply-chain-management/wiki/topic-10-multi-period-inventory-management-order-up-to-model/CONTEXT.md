# Ubiquitous Language: Topic 10 Multi-Period Inventory Management And Order-Up-To Model

Source note: `topic-10-multi-period-inventory-management-order-up-to-model.md`
Course: Supply Chain Management
Definition sources: Topic 10 slides and exercise workbook; enriched with standard operations-management terminology where needed.

This file is a standalone terminology and formula companion for the order-up-to model, inventory position, service levels, demand over lead time, and expected backorders.

## Policy And Inventory State Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Order-Up-To Model** | Multi-period replenishment policy where each period's order restores inventory position to a fixed target `S`. | Newsvendor, EOQ |
| **Order-Up-To Level (`S`)** | Target inventory position immediately after placing the replenishment order. | order quantity, safety stock |
| **Inventory Level** | On-hand inventory minus backorders; physical inventory net of unmet demand. | inventory position |
| **Inventory Position** | On-order inventory plus on-hand inventory minus backorders; the state variable used to decide how much to order. | inventory level |
| **On-Hand Inventory** | Units physically available now. | on-order inventory |
| **On-Order Inventory** | Units already ordered but not yet received. | pipeline ignored |
| **Backorder** | Demand that occurred but has not yet been satisfied. | lost sale, negative inventory only |
| **Period Order Quantity** | `S - inventory position`; amount ordered in the current period to restore the position to `S`. | fixed lot size |
| **Pull System** | Replenishment system where orders replace realized demand rather than pushing a fixed production quantity. | push forecast system |

## Lead-Time And Demand Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Lead Time (`l`)** | Number of periods between placing and receiving an order. | throughput time |
| **Planning Period** | Time unit used for the model, such as one week at a DC or one day for a sales representative. | calendar horizon |
| **Demand Over `l+1` Periods** | Demand exposure used in the order-up-to model: the current period plus the lead-time periods. | demand over `l` periods |
| **Demand Distribution (`F`)** | Cumulative distribution of demand over the relevant `l+1` period horizon. | point forecast |
| **Normal Demand** | Continuous bell-shaped demand model described by `mu` and `sigma`; useful for aggregate demand. | Poisson |
| **Poisson Demand** | Discrete count-demand model described by mean `lambda`; useful for low-volume counts. | normal by default |
| **Quantile `F^-1(SL)`** | Smallest demand value/order-up-to level that reaches the target service level. | average demand |

## Service And Performance Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **In-Stock Probability** | `F(S) = P(D <= S)` for demand `D` over `l+1` periods. | fill rate, exact-demand probability |
| **Stockout Probability** | `1 - F(S)`; probability that demand exceeds the order-up-to level. | backorder quantity |
| **Expected Backorders (`B(S)`)** | `E[max(0, D - S)]`; expected units short at period end. | stockout probability |
| **Expected Leftover Inventory (`I(S)`)** | `E[max(0, S - D)]`; expected units left at period end. | service level |
| **Expected Demand (`mu`)** | Mean of demand over `l+1` periods. | one-period mean unless stated |
| **Standard Deviation (`sigma`)** | Standard deviation of demand over `l+1` periods. | variance |
| **Normal Loss Function (`L(z)`)** | For standard normal `z`, `L(z) = phi(z) - z(1 - Phi(z))`; used to compute expected backorders. | CDF |
| **Expected Sales** | Expected satisfied demand; under normal demand in the deck, `mu - sigma*L(z)`. | revenue |

## Cost And Service-Level Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Underage Cost (`c_u`)** | Cost of being one unit short for the relevant period; in this topic often a stockout/backorder cost. | purchase cost |
| **Overage Cost (`c_o`)** | Cost of carrying one extra unit for the relevant period; in this topic often holding cost. | stockout cost |
| **Cost-Based Service Level** | `SL* = c_u/(c_u+c_o)`; target in-stock probability implied by shortage versus holding costs. | arbitrary service level |
| **Holding Cost (`h`)** | Cost of carrying one extra unit for one model period. Convert annual percentages into daily/weekly costs before use. | annual price |
| **Stockout Cost (`b`)** | Economic penalty of one unit short for one model period, such as lost margin or customer-service damage. | holding cost |
| **Rule-of-Thumb Service Level** | Managerial target used when stockout costs are too hard to estimate. | optimal service level |

## Relationships Between Canonical Terms

- **Order-up-to level `S`** targets **inventory position**, not **inventory level**.
- **Lead time `l`** determines **demand over `l+1` periods**.
- **Demand over `l+1` periods** feeds the **demand distribution `F`** used for **in-stock probability**.
- **Cost-based service level** determines the target quantile **`F^-1(SL)`**.
- **Expected backorders `B(S)`** and **expected leftover inventory `I(S)`** are quantity expectations, not probabilities.
- **Normal loss function `L(z)`** helps convert a normal quantile into **expected backorders**.

## Visual Memory Aid

```mermaid
flowchart TD
    State[Inventory state] --> Position[Inventory position = on-order + on-hand - backorders]
    Position --> Order[Order quantity = S - inventory position]
    Lead[Lead time l] --> Exposure[Demand over l+1 periods]
    Exposure --> Distribution[Distribution F]
    Costs[cu and co] --> SL[SL = cu / (cu + co)]
    SL --> SLevel[S = F inverse of SL]
    Distribution --> SLevel
    SLevel --> Service[F(S)]
    SLevel --> Backorder[B(S)]
    Backorder --> Leftover[I(S) = S - mu + B(S)]
```

## Formula Cheat Sheet

```text
Inventory level = on-hand - backorders
Inventory position = on-order + on-hand - backorders
Order quantity = S - inventory position

Demand horizon = l + 1 periods
Normal aggregation:
mu_period = mu_one_period * (l+1)
sigma_period = sigma_one_period * sqrt(l+1)

In-stock probability = F(S)
Stockout probability = 1 - F(S)
B(S) = E[max(0, D-S)]
I(S) = E[max(0, S-D)] = S - mu + B(S)

z = (S - mu) / sigma
L(z) = phi(z) - z(1 - Phi(z))
B(S) = sigma * L(z)

SL* = cu / (cu + co)
S = F^-1(SL*)
```

## Example Dialogue

> **Student:** "There are 523 boxes on hand and the target is 700, so we order 177."
>
> **Professor:** "That ignores the 180 boxes already on order. The order-up-to model uses **inventory position**: `523 + 180 - 0 = 703`. The position is above `S`, so the formula gives `-3`; operationally, place no positive order."
>
> **Student:** "So the shelf count is not the ordering state?"
>
> **Professor:** "Correct. Use **inventory level** to describe physical stock, but use **inventory position** to decide the order."

## Flagged Ambiguities

| Ambiguous Phrase | Canonical Recommendation |
|---|---|
| "Inventory" | Specify **inventory level**, **on-hand inventory**, or **inventory position**. |
| "Lead-time demand" | In this topic, use **demand over `l+1` periods** unless the problem explicitly says otherwise. |
| "Service level" | State whether it means **in-stock probability** `F(S)` or a cost-based target `SL*`. |
| "Expected shortage" | Use **expected backorders `B(S)`** for units, not **stockout probability**. |
| "Optimal quantity" | In this topic, call it **order-up-to level `S`**, not one-time order quantity `Q`. |
| "Rounding S" | Use the smallest integer with `F(S) >= SL` when a target service level must be met. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Ordering to fill on-hand inventory up to `S`. | Order to fill **inventory position** up to `S`. |
| Forgetting outstanding orders. | Include **on-order inventory** in inventory position. |
| Using demand over `l` periods. | Use **demand over `l+1` periods** in the deck's order-up-to model. |
| Treating `B(S)` as a probability. | `B(S)` is expected units backordered; `1-F(S)` is probability. |
| Using annual holding cost with daily demand. | Convert cost to the model period first. |
| Choosing the nearest Poisson CDF value below target. | Choose the smallest `S` with `F(S) >= SL`. |

## Compact Answer Language

```text
This is a multi-period replenishment problem, so I use an order-up-to policy.
I first compute inventory position, not just on-hand inventory.
Because lead time is l periods, demand exposure is over l+1 periods.
The target service level is cu/(cu+co), unless the case gives a managerial target.
Then S is the corresponding demand quantile.
Finally, I interpret F(S), B(S), and I(S) as service and inventory consequences.
```

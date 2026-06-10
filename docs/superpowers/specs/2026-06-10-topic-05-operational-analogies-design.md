# Topic 05 Operational Analogies Design

## Objective

Expand the Supply Chain Management Topic 05 wiki note so EOQ and EPQ examples describe the complete real operation behind every value. The note must connect symbols and formulas to physical products, inventory, production assets, setup work, customer demand, elapsed time, costs, and managerial decisions.

Target file:

`supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

## Scope

Expand:

- the bakery analogy table and memory hooks;
- all six worked exercise examples;
- all five practice tasks.

Preserve:

- existing formulas;
- existing substituted values;
- existing numerical results;
- Topic 05 terminology and model boundaries;
- the current note structure outside the expanded learning sections.

Do not change spaced-repetition completion status because this is clarification and note refinement, not a completed recall session.

## Standard Example Structure

Each worked example will use the same learning sequence:

1. **Operating story**: identify the company, physical product, customer or consumption process, warehouse or production asset, and decision being made.
2. **Asset dictionary**: map each symbol and numeric value to a real asset, rate, cost, stock level, or time event.
3. **Full workflow**: explain the chronological operation from current state through ordering, production, consumption, depletion, and repetition.
4. **Formula ladder**: retain symbolic formula, substituted values, numerical result, and units.
5. **Physical interpretation**: distinguish what is ordered or produced from what is stored, consumed, saved, or timed.
6. **Managerial decision**: state the action management should take from the result.
7. **Exam trap**: state the most likely conceptual or variable-placement error.

## Worked Example Mapping

### ABI Warehouses

- Product: one standardized spare part stored at two warehouses.
- Demand: 50 spare parts leave each warehouse per year.
- `K`: administrative and transport setup cost for one replenishment order.
- `h`: annual cost of keeping one spare part in stock.
- Operational comparison: two independent replenishment systems versus one pooled inventory system.
- Core distinction: pooled `Q*` is the order size for the combined system, not an order sent independently to each original warehouse.

### Tek Pak Beer Crates

- Product: reusable beer crates consumed or dispatched steadily from storage.
- `I0`: physical crates currently in the warehouse.
- Reorder point: crates required to cover customer demand while the supplier shipment is in transit.
- Core distinction: `Q*` answers how many crates arrive per order; the reorder point and first-order date answer when to place that order.

### Kerosene Finite Horizon

- Product: gallons of kerosene sold during a five-week seasonal window.
- Infinite-horizon EOQ: recurring benchmark that ignores the season ending.
- `m_hat`: mathematically ideal but infeasible fractional number of deliveries.
- `m*`: actual whole number of deliveries management can schedule.
- Core distinction: finite-horizon quantity divides the season's known demand across a feasible integer number of deliveries.

### Battery-Cell Line

- Product: battery-cell packs manufactured in production runs and withdrawn by downstream customers or assembly.
- `p`: gross output of the production line while it runs.
- `lambda`: simultaneous downstream consumption.
- `p - lambda`: net rate at which finished packs accumulate in storage.
- Core distinction: `Q*` is total produced during the run; `Imax` is the smaller warehouse peak because demand continues during production.

### Router Make-To-Stock Factory

- Product: finished Wi-Fi routers produced for warehouse stock.
- `I0`: routers currently available to customers.
- preparation lead time: line scheduling, component staging, calibration, software configuration, and setup before production begins.
- start-preparation inventory: physical alarm level covering demand during preparation.
- Core distinction: the non-production duration means this router model is not being produced, not necessarily that the entire factory is idle.

### Shovel Factory Technology Adoption

- Product: finished shovels produced in batches.
- Current `p`, `Q`, and `Imax`: observed production and warehouse behavior used to infer demand.
- New technology: equipment that increases production rate.
- Maximum willingness to invest: one-year relevant-cost saving, not automatically a full capital-investment NPV.
- Core distinction: infer the hidden demand rate before calculating the new EPQ.

## Bakery Variant Expansion

The bakery section will become a compact operational progression using flour as the physical inventory item:

- basic EOQ: supplier truck delivers flour instantly;
- initial inventory: flour already in the storeroom delays the first order;
- lead time: order while enough flour remains for supplier travel time;
- initial inventory plus lead time: translate stock into weeks of coverage and subtract lead time;
- finite horizon: temporary bakery divides total event demand among whole deliveries;
- EPQ: bakery or mill produces flour gradually while baking consumes it.

Each variant will explicitly identify what changes and what remains unchanged.

## Practice Task Expansion

Each practice task will include:

- a realistic operating setting;
- symbol-to-asset prompts;
- a requested timeline or physical interpretation;
- the original calculation requirement;
- one exam-trap check.

The tasks remain unsolved retrieval prompts. They must not reveal full final answers beyond values already supplied in the question.

## Visual And Formatting Rules

- Use compact Markdown tables for asset dictionaries.
- Use short ASCII timelines for lead-time, finite-horizon, and EPQ cycles.
- Keep formulas in fenced `text` blocks.
- Use explicit units on every operational quantity.
- Avoid decorative detail that does not improve model selection, variable placement, or interpretation.
- Keep vocabulary consistent with `CONTEXT.md`: **order quantity**, **production batch**, **maximum inventory**, **reorder point**, **production-run duration**, and **non-production duration**.

## Verification

Verification will include:

- independent recalculation of all six worked examples;
- confirmation that every worked example contains an operating story, asset dictionary, workflow, formula, interpretation, decision, and exam trap;
- confirmation that bakery variants and all five practice tasks are expanded;
- balanced Markdown fences;
- `git diff --check`;
- no changes to dashboard completion dates or Topic 05 first-pass status.

## Acceptance Criteria

The refinement is complete when a student can answer, for every example:

1. What real product is flowing?
2. What physical or financial item does each variable represent?
3. What happens chronologically in the operation?
4. Why is the selected EOQ or EPQ formula appropriate?
5. What does the calculated quantity physically mean?
6. What action should the manager take?
7. What similar-looking quantity must not be confused with it?


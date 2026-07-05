# Topic 08 OceanCove Process Analysis And Capacity Management Clarification Session - 2026-06-27

Source note: [Topic 08 OceanCove Process Analysis And Capacity Management](topic-08-oceancove-process-analysis-capacity-management.md)

Companion context: [CONTEXT.md](CONTEXT.md)

Session type: wiki refinement and calculation-ladder clarification

Status: clarification saved; first active recall still pending

## User Request

> I am now reading the oceancove analysis capacity for SCM, I see that some examples are not containing the full calculations of the example answers. Please provide them as detialed as possible as we applied in EOQ study session

## Professor Feedback

- Correct diagnosis: several OceanCove and Capacity Management answer-guide sections showed final numbers without the full calculation ladder.
- The Topic 05 EOQ/EPQ standard should also apply here: symbolic formula, substituted values, arithmetic result, unit, and interpretation.
- Capacity problems are especially risky because the final number can hide a unit conversion, a bottleneck shift, a mix constraint, or a distinction between demand flow and maximum capacity.

## Refinements Saved

The main note was expanded with full worked calculations for:

1. Peak lunch flow via Little's Law.
2. OceanCove step capacities and lunch utilization.
3. Effective fish-menu capacity under the 2:1 grilled-to-fried mix.
4. Lunch and dinner bottleneck identification.
5. Fastest grilled-fish lead time and peak non-rushed lead time.
6. Seat expansion from 120 to 160 seats, including revenue and contribution arithmetic.
7. ProfiCutZ capacity, bottleneck, steady-state customers, and the 13 customers/hour hiring result.
8. Circored process capacities, demand-flow conversion, 25,000-ton production time, and individual resource utilization.
9. Renovation Gantt scheduling logic, project duration, and no-hold conclusion.

The `CONTEXT.md` file was updated with:

- a `Worked-Calculation Recall Standard`;
- additional language for occupancy adjustment, bottleneck utilization, and whole-customer capacity;
- trap corrections for result-only answers and Circored utilization ambiguity.

## Refined Mental Model

```text
For every process/capacity calculation:
flow unit -> formula -> time conversion -> substitution -> result with unit -> bottleneck or decision interpretation.
```

For OceanCove specifically:

```text
Little's Law gives peak flow.
Step capacities identify resource limits.
The minimum required capacity gives the bottleneck.
Utilization compares actual flow to each capacity.
Lead time equals waiting plus processing.
Expansion only helps if it relaxes the active bottleneck or increases profitable flow.
```

## Weak Spots To Revisit

| Weak spot | Quality | Correction rule | Next prompt |
|---|---|---|---|
| Result-only capacity answers | `yellow` | Always write formula -> substitution -> result -> unit -> interpretation. | Rebuild the OceanCove lunch bottleneck calculation from scratch. |
| Capacity versus demand flow | `yellow` | Capacity is the maximum sustainable rate; demand flow is the actual or required rate. | Explain why Circored uses 75 tons/hour for the 333.33-hour answer. |
| Bottleneck shifts | `yellow` | After improving one resource, recompute every required resource. | Explain why ProfiCutZ does not automatically become 14 customers/hour. |
| Seat capacity versus customer flow | `yellow` | Apply stay time and occupancy assumptions before revenue. | Recompute the 160-seat lunch flow and explain why assembly still binds. |

## Next Recall Prompts

1. Use Little's Law to derive OceanCove's 120 customers/hour peak lunch flow.
2. Recompute fish-menu capacity under the 2:1 grilled-to-fried mix.
3. Build the lunch utilization table for fried fish, grilled fish, assembly, waiters, and dining area.
4. Derive the 23 minutes 25 seconds peak lead time.
5. Explain the difference between Circored's 100 tons/hour capacity and 75 tons/hour demand flow.
6. Rebuild the ProfiCutZ 13 customers/hour result after hiring two flexible bottleneck-capable employees.

## Schedule Impact

No `First Pass` or `D+n` checkpoint was advanced. This was a wiki refinement while the formal Topic 08 first active-recall session remains pending.

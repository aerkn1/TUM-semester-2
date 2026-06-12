# Topic 05 EOQ/EPQ Active Recall Session - 2026-06-12

Source note: [Topic 05 EOQ, Production Systems, and Batching](topic-05-eoq-production-systems-batching.md)

Context companion: [CONTEXT.md](CONTEXT.md)

Prior clarification: [Clarification session 2026-06-07](topic-05-eoq-production-systems-batching-clarification-session-2026-06-07.md)

Course: Supply Chain Management

Session type: first active recall

Status: completed 2026-06-12 by user report

## Completion Evidence

| Item | Record |
|---|---|
| User report | "I just completed the active recall of the eoq-epq for SCM." |
| Recorded scope | Topic 05 EOQ and EPQ concepts, formulas, variants, and operational examples |
| Answer evidence | The recall occurred outside this chat, so individual prompts, calculations, and raw answers were not captured. |
| Scheduling consequence | `First Pass = 2026-06-12`; canonical `D+1 = 2026-06-13`, displaced to a repair block on 2026-06-16 because older overdue reviews occupy the earlier queue. |

## User Raw Answer

The only answer-level evidence available in this interaction is the completion statement above. No detailed response is reconstructed or inferred.

## Professor Feedback

Completion is accepted for spaced-repetition scheduling. Formula placement, arithmetic accuracy, units, model selection, and operational interpretation remain ungraded in this record because no worked answers were captured.

## Refined Mental Model To Preserve

```text
Recurring stable demand + instant replenishment -> EOQ
Recurring stable demand + gradual production -> EPQ

EOQ: full batch enters inventory at once
EPQ: production adds units while demand removes units

Always answer:
operating condition -> model -> formula -> substitution -> result + unit
-> physical meaning -> managerial decision
```

## Quality And Weak Spots

| Area | Quality | Evidence And Next Action |
|---|---|---|
| Session completion | green | Confirmed directly by the user. |
| EOQ versus Newsvendor routing | unassessed | Retrieve the decision pattern and uncertainty distinction at `D+1`. |
| Basic EOQ formula and cost balance | unassessed | Calculate one case using the full formula ladder and verify annual ordering cost equals annual holding cost. |
| Lead time and finite horizon | unassessed | Distinguish reorder timing from quantity and test both integer neighbors for finite-horizon order count. |
| EPQ asset flow | unassessed | Explain why `Imax < Q`, calculate run duration, and distinguish production output from peak inventory. |

## Next Recall Prompts

1. Route four cases without notes: one-time uncertain demand, recurring instant replenishment, recurring positive lead time, and gradual internal production.
2. For `lambda = 9,600 units/year`, `K = EUR 80/order`, and `h = EUR 6/unit/year`, calculate `Q*`, orders per year, average inventory, annual ordering cost, and annual holding cost.
3. Explain the Router make-to-stock cycle using only real assets: routers in storage, customer withdrawals, line preparation, production output, peak inventory, and non-production time.
4. State what initial inventory, deterministic lead time, a finite horizon, and finite production each change in the decision.
5. Use the required sequence: `formula -> substitution -> result -> unit/interpretation`.

## References

- [Exercise Answer Guides](topic-05-eoq-production-systems-batching.md#exercise-answer-guides)
- [EOQ Variant Analogies And Use Cases](topic-05-eoq-production-systems-batching.md#eoq-variant-analogies-and-use-cases)
- [Practice Tasks](topic-05-eoq-production-systems-batching.md#practice-tasks)
- [Interactive EOQ/EPQ tutorial](eoq-epq-interactive-tutorial.html)

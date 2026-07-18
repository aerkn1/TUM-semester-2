# Week 09 Warranty Rights II - Clarification Session 2026-07-12

Source note: [week-09-warranty-rights-ii.md](week-09-warranty-rights-ii.md)

Session type: clarification and wiki refinement, not active recall completion.

Schedule consequence: no `First Pass` or `D+n` checkpoint advanced. Warranty Rights II remains pending first pass.

## Clarification Questions

### Prompt 1

User question:

> I need also clarification for warranty rights II: I understood that it is the extension of warranty rights I when the cure doees not work or agreed between both parties and revocation/reduction is the case. It discusses the details of revocation or reduction is applied under damage or reimbursement circumstances?

Professor clarification:

Warranty Rights II is the money-claim extension of Warranty Rights I. It is not mainly the details of revocation or reduction under damages.

Correct map:

```text
defect at transfer of risk
-> Section 437 BGB gateway
-> cure / revocation / reduction / damages / reimbursement
```

Revocation, reduction, damages, and reimbursement are separate remedy branches. Warranty Rights II mainly asks what kind of money claim the buyer has:

- damages in addition to performance;
- damages instead of performance;
- reimbursement of futile expenses under Section 284 BGB.

Core router:

```text
Would the loss still exist even if the seller later performed correctly?
```

- Yes: damages in addition to performance.
- No: damages instead of performance.
- Voluntary reliance expense wasted by failed performance: Section 284 reimbursement.

### Prompt 2

User question:

> Give examples for all case types with issue/solution/sentences applies

Professor clarification:

The saved answer now treats each case type as an exam template:

- damages in addition to performance: defective good burns other property;
- small damages instead of performance: buyer keeps defective item and claims value gap;
- reduction: buyer keeps defective item and adjusts price under Section 441 BGB;
- big damages instead of performance: buyer gives up performance and claims substitute-purchase loss;
- revocation: buyer unwinds the contract and returns performances;
- impossibility damages: Section 283 or Section 311a route;
- secondary-duty damages: Section 282 route;
- reimbursement of futile expenses: Section 284 route;
- mixed defective-fuel case: split engine damage from defective fuel value.

### Prompt 3

User question:

> For big and small damages instead of cases, how they actually distingusihed with revocation and reduction?

Professor clarification:

They are distinguished by legal route, not only by economic result.

```text
Small damages look like reduction.
Big damages look like revocation.
But they are damages claims, so they need the damages route.
```

#### Small Damages Versus Reduction

Example:

```text
agreed price = EUR 10,000
defect-free value = EUR 10,000
defective value = EUR 7,000
value deficit = EUR 3,000
```

Small damages:

- buyer keeps the machine;
- buyer claims compensation for the EUR 3,000 performance deficit;
- legal route: Sections 437 No. 3, 280 I, III, 281 BGB;
- seller responsibility is required.

Reduction:

- buyer keeps the machine;
- buyer adjusts the purchase price because the item is worth less;
- legal route: Sections 437 No. 2, 441 BGB;
- no seller fault/responsibility requirement.

Reusable sentence:

```text
Although the economic result resembles reduction, the buyer is claiming compensation for the value deficit. This is small damages instead of performance under Sections 437 No. 3, 280 I, III, and 281 BGB, so responsibility and the damages requirements must be checked.
```

Reduction sentence:

```text
The buyer does not claim damages but adjusts the purchase price because the defective item is worth less. This is reduction under Sections 437 No. 2 and 441 BGB, which does not require seller responsibility.
```

#### Big Damages Versus Revocation

Example:

```text
original price = EUR 10,000
seller fails to cure
buyer buys substitute machine = EUR 12,000
extra cost = EUR 2,000
```

Big damages:

- buyer gives up the defective performance;
- buyer claims non-fulfilment loss, such as substitute-purchase extra cost;
- legal route: Sections 437 No. 3, 280 I, III, 281 BGB;
- seller responsibility is required.

Revocation:

- buyer wants to undo the contract;
- buyer returns defective item and gets purchase price back;
- legal route: Sections 437 No. 2, 323, 346 ff. BGB;
- no seller fault/responsibility requirement.

Reusable sentence:

```text
The buyer does not merely want to unwind the contract; she claims the loss caused by having to obtain substitute performance. This is big damages instead of performance under Sections 437 No. 3, 280 I, III, and 281 BGB.
```

Revocation sentence:

```text
The buyer wants to undo the contract and return the defective item against repayment of the purchase price. This is revocation under Sections 437 No. 2 and 323 BGB, with restitution under Sections 346 ff. BGB.
```

## Refined Mental Models

- **Economic result is not enough**; identify the legal route.
- **Reduction** adjusts the contract price; **small damages** compensate a value deficit.
- **Revocation** unwinds the contract; **big damages** compensate non-fulfilment loss.
- **Damages require responsibility** under Section 280 I 2 BGB; reduction and revocation do not require seller fault.
- **Small/big damages are damages instead of performance**, so Section 280 III and a Section 281/283/311a route must be considered.

## Weak Spots To Target In First Pass

| Weak Spot | Quality | Correction Rule |
|---|---|---|
| Treating Warranty Rights II as revocation/reduction details only | yellow | Say Week 09 mainly routes money claims: damages in addition, damages instead, and Section 284 reimbursement. |
| Confusing small damages with reduction | yellow | Ask whether the buyer claims compensation requiring responsibility or price adjustment without fault. |
| Confusing big damages with revocation | yellow | Ask whether the buyer wants non-fulfilment loss compensation or only unwinding/restitution. |
| Ignoring seller responsibility for damages | red/yellow | Damages require Section 280 I responsibility; reduction/revocation do not require fault. |

## Next Recall Prompts

1. Buyer keeps a defective EUR 10,000 machine worth EUR 7,000 and claims EUR 3,000. Route it once as reduction and once as small damages.
2. Buyer buys a EUR 12,000 substitute after seller fails to cure a EUR 10,000 machine. Why is this big damages rather than revocation?
3. State the one-sentence difference between revocation and big damages.
4. State the one-sentence difference between reduction and small damages.

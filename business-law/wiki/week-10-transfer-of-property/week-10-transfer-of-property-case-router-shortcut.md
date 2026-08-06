# Week 10 Transfer Of Property - Case Router Shortcut

Source note: [week-10-transfer-of-property.md](week-10-transfer-of-property.md)
Companions: [CONTEXT.md](CONTEXT.md), [week-10-transfer-of-property-cheatsheet-and-tricks.md](week-10-transfer-of-property-cheatsheet-and-tricks.md), [week-10-transfer-of-property-practice-questions-and-model-answers.md](week-10-transfer-of-property-practice-questions-and-model-answers.md)
Created: 2026-07-25
Status effect: no `First Pass` or `D+n` checkpoint advanced. This is a shortcut/refinement aid; a checkpoint closes only after closed-book recall.

## One-Sentence Core

Do not ask "who bought it?" first. Ask "what kind of right or object moved, and did a separate disposition transaction transfer it?"

```text
Contract = who must do what.
Property law = who owns what.
```

## Mixed-Case Reading Order

In a larger Business Law case, use Week 10 only when the legal question is ownership, possession, transfer of a thing, transfer of a claim, double sale, stolen/lost goods, retention of title, or replacement goods.

```text
1. Actor status first if relevant: consumer / entrepreneur / merchant.
2. Contract formation next: was there a valid obligation contract?
3. Agency/SBT overlay if the contract or clause depends on it.
4. Warranty if the issue is a defective sold good.
5. Property only when the question becomes: who owns this now?
```

## Cross-Topic Correlation Map

Week 10 is the ownership layer. Other topics usually decide whether there is a valid obligation, who is bound, whether a clause controls the deal, or what remedy follows.

| Related topic | Aspect it decides | How it connects to Transfer of Property | Exam shortcut |
|---|---|---|---|
| Contract Law I | Whether a valid purchase contract exists | A valid contract under Section 433 BGB creates the duty to transfer ownership, but it does not transfer ownership itself. | If the question is "must S deliver?", use contract law. If the question is "is B owner?", use Section 929. |
| Contract Law II | Whether a declaration can be rescinded | Rescission may attack the purchase contract only, or both purchase and transfer if the same flaw taints both. | After rescission, ask: did ownership ever pass, or is the remedy restitution/vindication? |
| Contract Law III | Revocation/cancellation and restitution | Revocation unwinds a valid contract after performance failure, but property movements still have to be reversed through return duties and ownership analysis. | Exit route first, ownership consequence second. |
| Standard Business Terms | Whether clauses such as retention of title or exclusions are incorporated/effective | A retention-of-title clause can make ownership transfer conditional on full payment. | SBT controls the clause; property law controls whether ownership passed under the condition. |
| Agency | Who made the transfer agreement for whom | The property-law agreement is a declaration of intent, so representation can matter for that agreement; physical delivery itself is a real act. | Agency can bind the principal to the agreement; delivery still needs possession/handover facts. |
| Warranty Rights I | Defect at transfer of risk and cure priority | Warranty asks whether the sold item was defective at handover; property asks who owns the item before/after delivery or replacement. | Handover can matter for both risk and ownership, but test them separately. |
| Warranty Rights II | Damages, replacement, reimbursement | Replacement cure creates duties to exchange goods, but each new ownership movement still needs a separate Section 929 transfer. | No automatic ownership switch just because replacement was demanded. |
| Trade Law | Merchant overlays, especially Section 377 HGB | In a merchant sale, late inspection/notice can kill warranty rights, while ownership may already have passed under Section 929. | For B2B goods: merchant status -> Section 377 for warranty -> Section 929 for ownership. |
| Company Law | Which legal entity owns assets and who represents it | Company assets belong to the legal entity, not personally to shareholders/directors; directors/Prokuristen may represent the company in transfers. | Separate shareholder ownership of shares from company ownership of business assets. |
| Finance/security intuition | Collateral and chattel mortgage | A lender can own a machine as security while the borrower keeps possession; this creates good-faith resale risk. | Owner and possessor can split; voluntary possession risk is the reason Section 932 can protect B. |
| Unjust enrichment / vindication | How to reverse failed or unjustified transfers | If ownership passed despite an invalid obligation, reversal often runs through Section 812. If ownership never passed, the owner may claim return under Section 985. | Ask: owner still owner? Use 985. Ownership shifted without legal ground? Use 812. |

## Multi-Layer Sale Case Sequence

For a full sales case, run this stack:

```text
1. Who are the actors?
   consumer / entrepreneur / merchant / company

2. Was a contract formed?
   offer + acceptance + validity limits

3. Who is bound?
   direct party or represented party through agency/company authority

4. Do standard terms change the deal?
   retention of title, warranty exclusions, liability limits

5. Did ownership pass?
   movable / land / claim router, then Section 929 or alternative

6. If the thing is defective, did warranty law open?
   defect + transfer of risk + no exclusion + Section 437 remedy

7. If both parties are merchants, did HGB modify the result?
   especially Section 377 inspection/notice

8. What is the final consequence?
   claim to delivery / owner / no owner / cure / damages / restitution
```

## Master Object Router

| Trigger in facts | Route | Do not use |
|---|---|---|
| Movable physical object: laptop, watch, machine, car, goods | Section 929 BGB family | Section 398 |
| Land, house, plot | Sections 311b, 873, 925 BGB | Section 929 |
| Claim/right: invoice claim, salary claim, factoring | Section 398 BGB assignment | Delivery / handover |
| Ownerless/stolen/processed/mixed goods | Statutory acquisition or Section 935 block | Ordinary sale intuition |

## Movable Ownership: Default Sequence

For a movable, write the same four checks every time:

```text
Section 929 sentence 1 BGB:
1. agreement that ownership shall pass
2. delivery or valid delivery replacement
3. agreement still exists at delivery
4. authorization: transferor is owner or otherwise authorized
```

If all four are met, ownership passes. If authorization fails, continue to good-faith acquisition; do not stop too early.

## Delivery Replacement Picker

| Possession structure | Correct shortcut | Consequence |
|---|---|---|
| Buyer already has the thing before transfer | Section 929 sentence 2 | Agreement alone can complete transfer. |
| Seller/transferor keeps direct possession, now for buyer/lender | Section 930 | Constructive delivery; classic chattel mortgage/security transfer. |
| Third party holds the thing, such as warehouse operator | Section 931 | Transferor assigns claim to surrender the thing. |

Memory rule:

```text
already with buyer = 929 II
still with seller = 930
with third party = 931
```

## Non-Owner Fork

When the transferor is not owner:

```text
1. Was the non-owner authorized by the owner or by law?
   yes -> Section 929 can still work, often with Section 185 BGB logic.
   no -> continue.

2. Did the acquirer act in good faith?
   no knowledge and no gross negligence -> continue.

3. Did possession create legal appearance?
   possessor looks like owner -> continue.

4. Did the true owner lose possession involuntarily?
   stolen / lost / otherwise involuntary -> Section 935 blocks.
   voluntarily left with transferor -> Section 935 does not block.
```

Result:

```text
Voluntary possession risk -> good-faith acquisition can succeed.
Involuntary possession loss -> Section 935 blocks even an honest buyer.
```

## All High-Yield Combinations

| Facts | Route | Conclusion sentence |
|---|---|---|
| S owns laptop, sells and hands it to B | Section 929 sentence 1 | B becomes owner because agreement, delivery, continuing agreement, and authorization are met. |
| Contract signed today, delivery Friday | Section 433 only so far | B has a contractual claim, not ownership yet. |
| B already borrowed camera, S now sells it to B | Section 929 sentence 2 | B becomes owner by agreement because B already possesses the camera. |
| S transfers machine to L as collateral but keeps using it | Sections 929, 930 | L becomes owner; S remains direct possessor. |
| S then resells that machine to innocent B | Sections 929, 932, 935 | S lacks authorization, but B can acquire in good faith because L voluntarily left possession with S. |
| T steals O's watch and sells to innocent B | Sections 929, 932, 935 | B does not become owner; Section 935 blocks because O lost possession involuntarily. |
| Auction house sells owner's painting with owner's consent | Sections 929, 185 | Non-owner is authorized; no need to rescue with good faith. |
| S sells goods stored at W's warehouse | Sections 929, 931 | B becomes owner through assignment of S's claim against W. |
| S orally sells house and B moves in | Sections 311b, 873, 925 | B is not owner; land needs notarial/conveyance/register route. |
| M assigns EUR 50,000 invoice claim to bank | Section 398 | Bank becomes new creditor; debtor consent normally not required. |
| Seller uses valid retention-of-title clause and buyer has not paid | Sections 305, 158, 929 | Ownership stays with seller until the payment condition occurs. |
| Purchase contract invalid, transfer agreement clean | Separation/abstraction, Section 812 | Ownership may stay transferred; reversal runs through restitution. |
| Deceit/incapacity taints purchase and transfer | Sections 123/105, 142, 985 | Identity of flaw can void both; owner may reclaim via vindication. |
| Buyer demands warranty replacement | Sections 439, 929 | Replacement creates duties; each ownership transfer still needs its own Section 929 act. |
| Raw planks processed into a new table | Section 950 | Processing can create statutory ownership without ordinary transfer. |

## Exam Answer Skeleton

Use this when writing a legal-opinion paragraph:

```text
B became owner if [route] is fulfilled.
First, the object is [movable / land / claim], so the applicable route is [section].
For a movable, Section 929 sentence 1 requires agreement, delivery or replacement, continuing agreement at delivery, and authorization.
Here, [apply each element].
Because authorization [is / is not] met, [ownership passes / I must test good-faith acquisition].
For good faith, [good faith + legal appearance + no Section 935 block].
Therefore, [final ownership consequence].
```

## 12-Minute Retention Drill

Do this closed-book. Say only the route and conclusion first; check the model answers only after.

1. S owns a laptop, sells it, hands it over. Which four elements?
2. S and B sign today, delivery next week. Who owns today?
3. B already borrowed the camera. Which delivery rule?
4. S keeps the machine but transfers it to L as collateral. Which delivery replacement?
5. S resells L's collateral machine to good-faith B. Why can L lose ownership?
6. T sells O's stolen watch to good-faith B. Why does B still fail?
7. Warehouse W holds S's goods. S sells to B without moving them. Which rule?
8. S sells land orally and B moves in. Why is B not owner?
9. M transfers an invoice claim to Bank F. Why is Section 929 wrong?
10. Buyer has unpaid goods under retention of title. Who owns?
11. Seller lied about the object and buyer rescinds. Which flaw question matters?
12. Buyer receives replacement cure. Does ownership move automatically or through new Section 929 transfers?

Target: 10/12 clean route choices before reading the full Week 10 note.

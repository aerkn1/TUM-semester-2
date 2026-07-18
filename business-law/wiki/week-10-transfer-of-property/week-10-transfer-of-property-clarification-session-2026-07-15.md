# Week 10 Transfer Of Property - Clarification Session 2026-07-15

Source note: [week-10-transfer-of-property.md](week-10-transfer-of-property.md)
Context companion: [CONTEXT.md](CONTEXT.md)
Session type: targeted understanding repair

## User Confusion

Prompt:

> I need clarification for transfer-of-property business law: in good-faith purchase case, how come the L loses the ownership without its consent?

User follow-up:

> I could not map it clearly the transfer of property in general in my mind, give me example use cases that can takes me through the steps that needs to be checked based on requirements and conclusion

## Professor Feedback

The missing mental model was that transfer-of-property law is a router, not one single sale rule.

The main split:

```text
Contract answers: who must do what?
Property law answers: who owns what?
```

A purchase contract under Section 433 BGB creates duties. It does not itself transfer ownership. For movable ownership, the exam route is Section 929 BGB: transfer agreement, delivery or delivery replacement, agreement at delivery, and authorization.

If authorization is missing because the transferor is not owner, the analysis does not stop. The next step is good-faith acquisition under Sections 932 and 935 BGB.

## Corrected Mental Models

### 1. General Property Router

```text
1. Identify the object:
   movable thing / land / claim?

2. Separate the legal layers:
   obligation contract or disposition transaction?

3. If movable:
   Section 929 route:
   agreement
   delivery or replacement
   agreement at delivery
   authorization

4. If no authorization:
   Sections 932 and 935:
   good faith
   possession-based legal appearance
   no lost/stolen/involuntary-loss block
   legal transaction between distinct parties

5. Conclude:
   ownership passed / ownership did not pass / acquirer acquired in good faith.
```

### 2. Why L Can Lose Ownership Without Consent

In the chattel mortgage case, L becomes owner of the machine as collateral, but L voluntarily lets S keep direct possession. To third parties, S still looks like the owner. Possession creates legal appearance, supported by Section 1006 BGB.

When S later sells and hands over the machine to B:

```text
S is not authorized.
B is in good faith.
S possesses the machine.
The machine was not lost or stolen from L because L voluntarily left it with S.
Section 935 BGB does not block acquisition.
```

Conclusion:

```text
B acquires ownership in good faith under Sections 929 and 932 BGB.
L loses ownership even without consenting to S's sale.
```

The policy idea:

```text
If the owner voluntarily creates the appearance that another person controls the thing,
the owner bears the risk that an innocent buyer relies on that appearance.
```

### 3. Stolen-Thing Contrast

If T steals O's watch and sells it to B, B may be honest, but Section 935 BGB blocks good-faith acquisition because O involuntarily lost possession.

Conclusion:

```text
B does not become owner. O remains owner.
```

## Use-Case Map

| Case | Route | Key Requirement | Conclusion |
|---|---|---|---|
| S owns laptop and hands it to B | Section 929 sentence 1 BGB | Agreement, delivery, authorization | B becomes owner |
| S and B sign purchase contract, delivery later | Section 433 only so far | No delivery/property transfer yet | B has a claim, not ownership |
| B already borrowed camera, then buys it | Section 929 sentence 2 BGB | B already possesses the thing | B becomes owner without new handover |
| S transfers machine to L as collateral but keeps it | Sections 929, 930 BGB | Constructive delivery through possession relationship | L becomes owner; S remains possessor |
| S then sells same machine to good-faith B | Sections 929, 932 BGB | Missing authorization replaced by good-faith acquisition; no Section 935 block | B becomes owner; L loses ownership |
| T sells stolen watch to good-faith B | Sections 929, 932 checked, then Section 935 blocks | Owner involuntarily lost possession | O remains owner |
| S sells land to B | Sections 311b, 873, 925 BGB | Notarial contract, conveyance, land-register entry | B becomes owner only after real-property transfer |
| A transfers EUR 5,000 claim against D to C | Section 398 BGB | Assignment agreement and transferable claim | C becomes new creditor |

## Exam-Ready Sentences

```text
The purchase agreement creates only the obligation to transfer ownership; it does not itself transfer ownership.
```

```text
For movable ownership, I test agreement, delivery or delivery replacement, agreement at delivery, and authorization under Section 929 BGB.
```

```text
Because S was not owner and not authorized, I must test good-faith acquisition under Sections 932 and 935 BGB.
```

```text
Section 935 BGB blocks good-faith acquisition if the owner lost possession involuntarily, for example through theft or loss.
```

```text
Here, Section 935 BGB does not block acquisition because L voluntarily left possession with S under the security arrangement.
```

## Weak Spots

| Area | Quality | Corrective Rule |
|---|---|---|
| General transfer-of-property map | yellow | Start with object type, then choose movable/land/claim route. |
| Consent intuition in good-faith purchase | yellow | Good-faith acquisition is a statutory exception; L's consent is not required if Sections 932 and 935 are satisfied. |
| Contract versus ownership | yellow | Contract creates a duty; disposition changes ownership. |
| Section 935 limit | green/yellow | Voluntary possession loss can allow good-faith acquisition; involuntary loss blocks it. |

## Next Recall Prompts

1. S owns a laptop and hands it to B after sale. Build the Section 929 sentence 1 BGB test.
2. S signs a sale contract with B today, but handover is Friday. Is B owner today?
3. S gives L ownership of a machine as collateral but keeps using it. Which delivery replacement applies?
4. S then sells that machine to good-faith B. Why can L lose ownership without consenting?
5. T steals O's watch and sells it to good-faith B. Why does B not acquire ownership?
6. A assigns a claim against D to C. Why is Section 929 BGB the wrong route?

## Schedule Impact

No `First Pass` or `D+n` checkpoint was advanced. This was a clarification and mapping session, not a completed closed-book active-recall session. Use these weak spots during the Transfer of Property first pass after the Warranty Rights gateway and older legal repairs.

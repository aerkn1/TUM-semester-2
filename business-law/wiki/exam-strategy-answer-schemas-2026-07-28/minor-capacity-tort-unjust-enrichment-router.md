# Minor Capacity, Tort, And Unjust Enrichment Router

Course: Business Law
Exam date: 2026-07-28
Companion to: `exam-strategy-answer-schemas-2026-07-28.md`, `additional-mock-exams-and-external-cheatsheet.md`

Source status: this covers a flagged coverage gap (`additional-mock-exams-and-external-cheatsheet.md` marks minors, tort damages, and unjust enrichment as "light"/coverage-gap-radar topics based on the SS22 historical exam). Treat this as insurance, not core doctrine — study it after Warranty/Property/Trade/Company are stable, per the six-day plan.

## When To Reach For This Page

```text
A party is under 18 -> Minor Capacity Route
Someone was physically or property-harmed outside any contract -> Tort Route
A transfer happened with no valid legal basis (void contract, failed condition, mistaken payment) -> Unjust Enrichment Route
```

## Minor Capacity Route (Sections 104-113 BGB)

```text
1. Age check:
   - under 7: Section 104 No. 1, no capacity, declaration is void.
   - 7 to under 18: Section 106 ff., limited capacity.
   - 18+: full capacity, skip this route.

2. For a 7-17 year old, classify the transaction:
   - purely legally beneficial (only rights, no duties) -> Section 107, valid without consent.
   - anything else -> needs consent of the legal representative(s).

3. No prior consent given? Check ratification paths:
   - legal representative can ratify after the fact, Section 108 I.
   - pocket-money rule, Section 110: valid without prior consent if the minor performs with funds given for that purpose or given for free disposal — the minor must have actually performed, not merely have access to enough money.

4. If the minor acted as an agent for someone else (not for themselves):
   - the minor can still validly represent the principal, because the legal effects land on the principal, not the minor (limited capacity does not block agency).
   - separate issue: if the minor acted without authority, Section 179 III sentence 2 protects the minor from personal liability to the third party, unless the legal representative had consented.

5. Consequence if invalid:
   - the contract is "pending" (schwebend unwirksam) until ratified or refused, not automatically void, unless it falls outside Sections 107/110/108 entirely with no ratification possible.
```

Trap: do not treat "the minor had money in a savings account" as satisfying Section 110 — the section requires actual performance with the specific funds, not mere solvency.

## Tort Route (Section 823 BGB And Neighbors)

```text
1. Protected right or interest infringed:
   - Section 823 I: life, body, health, freedom, property, or another absolute right.
   - Section 823 II: violation of a protective statute (Schutzgesetz) intended to protect the claimant.
   - Section 826: intentional harm contrary to public policy (rare, high bar).

2. Act or omission causing the infringement.

3. Causation between the act and the infringement, and between the infringement and the damage (two-step causation in the fuller version).

4. Unlawfulness — usually indicated once a protected right under 823 I is infringed, unless a justification applies (self-defense, consent, necessity).

5. Fault — intent or negligence, Section 276.

6. Damage, compensated under Sections 249 ff. (restitution in kind first, money if restitution is impossible or insufficient, Section 251).
```

Exam sentence:

```text
M could have a claim against K for compensation of the EUR [amount] medical costs under Section 823 I BGB in conjunction with Section 249 BGB if K unlawfully and culpably injured M's body or health.
```

Trap: tort claims run parallel to contract claims, not instead of them — a case can raise both a Section 280 contractual claim and a Section 823 tort claim on the same facts (e.g., a defective product that also injures someone), and they do not cancel each other out.

## Unjust Enrichment Route (Section 812 ff. BGB)

```text
1. One party obtained something (an asset, a benefit, a service) -> "etwas erlangt."

2. Through the other party's performance (Leistungskondiktion) or in another way, e.g. intervention (Nichtleistungskondiktion).

3. Without legal basis ("ohne rechtlichen Grund") -> most common exam trigger: the underlying contract is void, was rescinded (Section 142 I reaches back to the start), or a condition failed.

4. No exclusion applies:
   - Section 814: performer knew there was no obligation and paid anyway.
   - Section 817 sentence 2: performer itself violated a statutory or moral prohibition.

5. Consequence:
   - return the object/benefit, or its value if return is impossible (Section 818 II).
   - watch Section 818 III "Entreicherung" (loss of enrichment) as a defense, and Section 819 which removes that defense once the recipient knew the basis was missing.
```

Trap: after a successful rescission (Anfechtung) or a void SBT-tainted contract, the return of already-exchanged performance runs through unjust enrichment (812 ff.), not through the revocation restitution rules (346 ff.) — those two restitution regimes look similar but sit on different statutory bases. Use 346 ff. only where a valid contract existed and was later revoked; use 812 ff. where the contract was void or avoided from the start.

## Combined Case Pattern (Historical SS22 Style)

```text
minor capacity -> contract formation -> Section 110 validation check
  -> if invalid: no valid contract
  -> return of any exchanged goods via unjust enrichment (812 ff.), not contract law
  -> if a separate injury occurred in the same fact pattern: run the tort route independently
```

## Section Definitions

Working definitions for every section cited in the three routes above, so the page is usable without flipping to another file. Paraphrased for exam use, not verbatim statute text.

| Section | Definition |
|---|---|
| Section 104 No. 1 BGB | A person under 7 has no legal capacity to act; their declarations of intent are void. |
| Section 106 BGB | Minors who have reached 7 have limited legal capacity, governed by Sections 107-113. |
| Section 107 BGB | A minor does not need the legal representative's consent for a declaration of intent that brings them only a legal benefit, with no corresponding legal burden. |
| Section 108 I BGB | If a minor concludes a contract without the required consent, its validity depends on the legal representative's ratification. |
| Section 110 BGB | A contract concluded by a minor without prior consent is valid from the start if the minor renders the agreed performance using funds given to them by the representative (or a third party with the representative's consent) for that purpose or for free disposal. |
| Section 113 BGB | If the legal representative authorizes the minor to enter an employment or trade relationship, the minor gains capacity for the legal transactions that relationship typically involves. |
| Section 142 I BGB | A successfully rescinded (voidable) transaction is deemed void from the beginning — retroactive. |
| Section 179 III sentence 2 BGB | A minor who acted as an agent without authority is not personally liable to the third party under Section 179, unless their legal representative had consented to the agency. |
| Section 249 ff. BGB | Damages are compensated primarily through restitution in kind (restoring the position that would exist without the damaging event); Section 251 allows monetary compensation instead where restitution is impossible or insufficient. |
| Section 276 BGB | The debtor (or tortfeasor, by extension) is responsible for intent and negligence unless a stricter or milder standard applies. |
| Section 346 ff. BGB | Effects of revoking a valid contract: both parties return what they received (and any benefits derived from it), or compensate its value where return is impossible — applies only where a valid contract existed and was later revoked. |
| Section 812 BGB | A person who obtains something at another's expense through that person's performance, or in another way, without legal basis, is obliged to return it (unjust enrichment / Bereicherungsrecht). |
| Section 814 BGB | Return of a performance cannot be demanded if the performer knew, at the time of performing, that they were not obliged to perform. |
| Section 817 sentence 2 BGB | Return of a performance is barred if the performer themselves violated a statutory prohibition or public policy by performing. |
| Section 818 II-III BGB | If return of the enriched object itself is impossible, its value must be compensated (818 II); the obligation to return or compensate is excluded to the extent the recipient is no longer enriched (818 III, "Entreicherung"). |
| Section 819 BGB | The Section 818 III loss-of-enrichment defense is removed once the recipient knew (or later learns) that there was no legal basis for what they received. |
| Section 823 I BGB | A person who unlawfully and culpably injures another's life, body, health, freedom, property, or another absolute right is liable to compensate the resulting damage. |
| Section 823 II BGB | A person who culpably violates a statute intended to protect another (a Schutzgesetz) is liable to that other person for the resulting damage. |
| Section 826 BGB | A person who intentionally causes damage to another in a manner contrary to public policy is liable to compensate that damage. |

## Quick Recall Drill

```text
104 = under 7, void
106-113 = limited capacity, 7-17
107 = purely beneficial, no consent needed
110 = pocket-money, must actually perform
179 III 2 = minor agent shielded from liability
823 I = life/body/health/freedom/property/absolute right
823 II = protective statute violation
826 = intentional public-policy harm
812 = no legal basis, return the enrichment
814 / 817 s.2 = enrichment claim exclusions
818 III = loss of enrichment defense
819 = removes 818 III defense once recipient knew
```

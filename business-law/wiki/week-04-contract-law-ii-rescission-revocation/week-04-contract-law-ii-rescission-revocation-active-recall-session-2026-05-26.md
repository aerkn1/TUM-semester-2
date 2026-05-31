# Contract Law II Active Recall Session - 2026-05-26

Primary source note: `week-04-contract-law-ii-rescission-revocation.md`
Context file: `CONTEXT.md`
Related clarification session: `week-04-contract-law-ii-rescission-revocation-clarification-session-2026-05-25.md`
Course: Business Law
Session mode: use-case-driven active recall

## Outcome

Status: active recall completed 2026-05-27
Quality: green-yellow

The user correctly routed the first case to Contract Law II rescission and understood the broad idea that rescission concerns a problem after apparent contract formation. The main correction was distinguishing **error of declaration** from **error of content** and using the legal consequence **void ex tunc** instead of vague "revocation of declaration" language. In Case 2, the user correctly identified rescission for an error about an essential characteristic and excluded Section 123 BGB because there was no intentional deception or threat. In the revocation cases, the user correctly separated primary-duty breach under **Section 323 BGB**, ancillary-duty breach under **Section 324 BGB**, and impossibility/excluded performance under **Section 326 V BGB** after feedback. The final mixed routing sprint was accurate. Remaining upgrade: consistently separate exercise declarations under **Section 143/349 BGB** from effects under **Section 142 I/346-348 BGB**.

## Recall Prompts And Raw Answers

### Case 1: Typo In The Order

Prompt: A restaurant wants to order **100 bottles of wine** from a supplier. In the online order form, the owner accidentally types **1,000 bottles**. The supplier receives the order and confirms: "Accepted: 1,000 bottles at EUR 8 each." The next morning, the restaurant owner notices the mistake and immediately writes: "I made a typo. I only wanted 100 bottles. I do not want to be bound by the 1,000-bottle order."

Questions:

1. Is this Contract Law I formation, Contract Law I validity, Contract Law II rescission, or Contract Law II revocation?
2. Which section is the best anchor for the mistake?
3. What kind of mistake is it?
4. What additional steps must the restaurant owner satisfy?
5. What is the legal consequence if successful?

User answer: "1- I think its contract law II rescission since it occurs after contract is formed. Section 119 with error of content? 2-Section 119? 3-error of content 4-apply for rescission timely? 5-revocation of declarartion?"

Professor feedback:

- Correct routing: Contract Law II **rescission**, because the problem is a defective declaration, not later performance.
- Correct anchor: **Section 119 I Alt. 2 BGB**, not only general Section 119.
- Correction: this is **error of declaration**, not error of content. The owner intended 100 bottles but typed a different sign/number, 1,000.
- Required structure:

```text
Ground for rescission: Section 119 I Alt. 2 BGB
Causality: typo caused the 1,000-bottle declaration
Declaration of rescission: Section 143 I BGB
Time limit: without undue delay, Section 121 I BGB
No exclusion: especially no confirmation, Section 144 BGB
```

- Consequence: if rescission is effective, the declaration is **void from the beginning** under **Section 142 I BGB**. In an error-based case, **Section 122 BGB** reliance damages may also be considered.

Quality: yellow-green. Routing was correct; section precision and legal consequence language need repetition.

### Clarification: Meaning Of Ex Tunc

User question: "what is actually ex tunc"

Professor explanation:

**Ex tunc** means "from the beginning" or "retroactively." In rescission, Section 142 I BGB treats the flawed declaration as void from the original moment it was made.

Compact distinction:

| Concept | Meaning | Typical route | Image |
|---|---|---|---|
| **Ex tunc** | From the beginning | Rescission, Section 142 I BGB | Retroactive eraser |
| **Ex nunc** | From now on | Cancellation/termination of continuing obligations | Stop button |
| **Revocation** | Return received performances | Sections 323, 346-348 BGB | Return desk |

Example:

- If a person accidentally orders EUR 9,000 instead of EUR 900 and validly rescinds, the flawed EUR 9,000 declaration is void **ex tunc**.
- If a continuing rental relationship is cancelled, it usually ends **ex nunc**, meaning for the future.
- If a buyer revokes after defective machine delivery, the valid contract is unwound through restitution: buyer returns the machine, seller returns the price.

## Refined Mental Models

- **Rescission** = defective declaration route.
- **Revocation** = valid reciprocal contract plus performance problem route.
- **Error of content** = declaror says what they wanted but misunderstands the meaning.
- **Error of declaration** = declaror uses the wrong sign, word, number, click, or typed value.
- **Ex tunc** = retroactive eraser under Section 142 I BGB.
- **Revocation effects** = return desk under Sections 346-348 BGB, not ex tunc voidness.

## Weak Spots

| Weak Spot | Quality | Correction |
|---|---|---|
| Error of content vs error of declaration | yellow | Typing 1,000 instead of 100 is Section 119 I Alt. 2 BGB: error of declaration. |
| Legal consequence language | yellow | Say "void ex tunc under Section 142 I BGB"; do not call rescission "revocation of declaration." |
| Full rescission structure | yellow | Ground + causality + declaration under Section 143 + time under Section 121/124 + no exclusion under Section 144 + effect under Section 142. |
| Section 323 vs Section 324 routing | yellow | Defective primary performance uses Section 323 BGB; ancillary/protective duty breach uses Section 324 BGB. |
| Revocation declaration vs effects | yellow | Declare revocation under Section 349 BGB; then restitution follows under Sections 346-348 BGB. |

### Case 2: Wrong Painting

Prompt:

Buyer purchases a painting from Seller for EUR 20,000. Both believe it is an original Picasso. Later, an expert proves it was painted by Picasso's student. Seller did not know this and did not lie.

Questions:

1. Contract Law I formation/validity, Contract Law II rescission, or revocation?
2. Which rescission ground is most plausible?
3. Why is Section 123 BGB not the best route?
4. What must Buyer do to exercise the right?
5. What is the legal consequence if successful?

User answer: "1- it happens after contract is made and valid. So it is contract law II and recission due to mistake. 2-error about essential characteristic 3-this is not an intenional deceive or threatening by seller so closer to section 119 4-buyer must declare a recission 5-contract becomes void from the beginning"

Professor feedback:

- Correct routing: Contract Law II **rescission**, not Contract Law I and not revocation. The problem is a mistaken assumption at formation about the purchased object's essential quality.
- Correct ground: **Section 119 II BGB**, error about essential characteristics. Authorship/authenticity of a high-value artwork is an essential characteristic, not a mere motive or later disappointment.
- Correct exclusion: **Section 123 BGB** is not the best route because Seller did not intentionally deceive Buyer and did not threaten Buyer.
- Required exercise steps:

```text
Ground: Section 119 II BGB
Causality: Buyer would not have bought at EUR 20,000 if the painting were known to be by a student
Declaration: Buyer must declare rescission under Section 143 I BGB
Time limit: without undue delay after discovery, Section 121 I BGB
No exclusion: no confirmation under Section 144 BGB
Effect: void from the beginning under Section 142 I BGB
Possible effect: Section 122 BGB reliance damages may need discussion in error-based rescission
```

Quality: green-yellow. The concept and route were correct; improve by naming **Section 119 II BGB** and adding the full exercise structure.

### Case 3: Defective Espresso Machine

Prompt:

Cafe buys an espresso machine from Seller for EUR 8,000. The machine is delivered, but it repeatedly fails to heat water properly. Seller promises repair but misses the repair deadline. The cafe now wants to undo the transaction and get the money back.

Questions:

1. Is this Contract Law II rescission or revocation?
2. What fact tells you it is not a Section 119 mistake case?
3. Which revocation ground is most plausible?
4. What must the cafe usually do before revoking?
5. What is the legal consequence if successful?

User answer: "1-revocation, its related to the performance after contract and shipping is made 2-this is not a error or deceit over an agreement, its performance related 3-its secdtion 324 BGB 4-declare for revocation to void the contract 5-void from now on"

Professor feedback:

- Correct routing: Contract Law II **revocation**. The espresso machine was delivered under a valid contract, but the performance is defective.
- Correct reason it is not Section 119: there is no flawed declaration or mistaken agreement at formation; the problem appears after performance.
- Correction: the best anchor is **Section 323 I BGB**, not Section 324 BGB. A machine that fails to heat water properly is improper performance of the primary duty to deliver a conforming usable machine. Section 324 BGB is for ancillary/protective duty breaches, such as serious trust or safety breaches that make holding the contract unreasonable.
- Required exercise steps:

```text
Ground: Section 323 I BGB
Contract: reciprocal purchase contract
Breach: improper performance / defective machine
Additional period: repair deadline or cure period was set and missed
Declaration: revocation must be declared under Section 349 BGB
Effect: restitution under Sections 346-348 BGB
Possible addition: damages may remain under Section 325 BGB, no double compensation
```

- Correction to consequence: do not say "void from now on." Revocation does not create Section 142 I BGB ex tunc voidness. It transforms the contract into a restitution relationship: Seller returns the EUR 8,000, Cafe returns the machine, generally concurrently under Section 348 BGB.

Quality: yellow. Routing was correct, but the statutory ground and consequence need correction.

### Case 4: Damaged Customer Property

Prompt:

A catering company hires a repair technician to service its industrial oven. The technician completes the repair, but during the visit he carelessly destroys several expensive customer-owned serving trays stored beside the oven. The catering company says trust is gone and it no longer wants to continue the contract.

Questions:

1. Is this Contract Law II rescission or revocation?
2. Is Section 323 BGB or Section 324 BGB more plausible?
3. What makes this different from the defective espresso machine case?
4. What must the catering company declare?
5. What are the legal consequences if successful?

User answer: "1- this is revocation 2-more section 324 BGB 3-its not an issue regarding the primary duty or perfromance, the mistake causes out of scope company assets to be destroyed. 4-if upholding the contract is not sensible, declaration for revocation 5-returning everyting under 346-348 with damages can remain under 325"

Professor feedback:

- Correct routing: Contract Law II **revocation**, because the contract exists and the issue arises during performance.
- Correct anchor: **Section 324 BGB** is more plausible than Section 323 BGB. The technician completed the repair, so the issue is not failed primary performance of the oven repair itself. The damage to customer-owned serving trays is a breach of ancillary/protective duties under Section 241 II BGB.
- Correct distinction from Case 3: Case 3 involved defective primary performance; Case 4 involves collateral damage to protected interests during performance.
- Required exercise steps:

```text
Ground: Section 324 BGB
Duty breached: ancillary/protective duty under Section 241 II BGB
Threshold: upholding the contract must be unreasonable for the obligee
Declaration: revocation must be declared under Section 349 BGB
Effect: restitution under Sections 346-348 BGB
Damages: damages may remain under Section 325 BGB
```

Quality: green. The route, statutory distinction, and consequence were correct. Improve wording by saying "ancillary/protective duty under Section 241 II BGB" instead of "out of scope company assets."

### Case 5: Unique Sculpture Destroyed Before Delivery

Prompt:

Collector buys a unique sculpture from Seller for EUR 12,000. Before delivery, the sculpture is accidentally destroyed in a warehouse fire. The sculpture cannot be replaced because it was one of a kind. Collector wants to unwind the transaction.

Questions:

1. Is this rescission or revocation?
2. Is Section 323, Section 324, or Section 326 V BGB the best route?
3. Why is an additional repair/performance deadline usually unnecessary here?
4. What must Collector declare?
5. What are the legal consequences if successful?

User answer: "1- revocation 2-it seems like section 326 BGB due to impossiblity of the duty 3-delivery is impossible regardless 4-declaration of revocation via restitutio under section 346-348 5-Received performances must be returned"

Professor feedback:

- Correct routing: Contract Law II **revocation**, not rescission. There is no mistaken declaration; the problem is that the promised performance can no longer be rendered.
- Correct anchor: **Section 326 V BGB**, because the duty to deliver the unique sculpture is excluded due to impossibility, especially under Section 275 BGB.
- Correct deadline reasoning: an additional period for performance is unnecessary because delivery is objectively impossible; a cure period cannot make a one-of-a-kind destroyed sculpture deliverable.
- Correction: Collector must **declare revocation under Section 349 BGB**. Sections 346-348 BGB govern the effects after revocation; they are not the declaration route.
- Consequence: received performances are returned under Sections 346-348 BGB. If Collector already paid EUR 12,000, Seller returns the price. If Collector received nothing, there may be little physical restitution from Collector's side. Damages may be tested separately if fault or risk allocation matters.

Quality: green-yellow. The route and impossibility logic were correct; improve by separating **declaration under Section 349 BGB** from **effects under Sections 346-348 BGB**.

### Case 6: Mixed Routing Sprint

Prompt:

Classify each mini-case with the best route and best section anchor. Keep each answer to one line:

1. Buyer types EUR 90,000 instead of EUR 9,000 in an online offer.
2. Seller lies that a car has never had an accident.
3. Seller delivers the correct machine, but it does not work and repair deadline passes.
4. Contractor completes the work but insults and threatens the client during performance, making continuation unreasonable.
5. Unique purchased painting is destroyed before delivery and cannot be replaced.

User answer: "1- recission - Section 119 2 BGB error of declaraion 2-recission - Section 123 BGB deceit or duress 3-revocation - Section 323 BGB primary perf breach 4-revocation - Section 324 BGB Ancillary duty breach 5-revocation - section 326 BGB Impossibility/excluded performance"

Professor feedback:

- 1 correct: **rescission**, Section 119 I Alt. 2 BGB, error of declaration. Improve notation: write Section 119 I Alt. 2, not "119 2."
- 2 correct route and anchor: **rescission**, Section 123 I Alt. 1 BGB for deceit. Do not say "deceit or duress" when the facts specify a lie; duress would require unlawful threat or pressure.
- 3 correct: **revocation**, Section 323 I BGB, primary-duty non-performance or improper performance after cure deadline.
- 4 correct: **revocation**, Section 324 BGB, ancillary/protective duty breach under Section 241 II BGB.
- 5 correct: **revocation**, Section 326 V BGB, excluded performance/impossibility.

Quality: green. The final routing sprint shows the main exit-route map is now usable under exam pressure.

## Final Mental Models

- **Rescission**: defective declaration route. Anchors: Sections 119, 120, 123 BGB. Exercise under Section 143 BGB. Effect under Section 142 I BGB.
- **Revocation**: valid reciprocal contract plus performance problem. Anchors: Sections 323, 324, 326 V BGB. Exercise under Section 349 BGB. Effects under Sections 346-348 BGB.
- **Section 323 BGB**: primary duty fails or is improper.
- **Section 324 BGB**: ancillary/protective duty breach makes continuation unreasonable.
- **Section 326 V BGB**: performance duty is excluded, especially impossibility.

## Next Recall Prompts

1. In one sentence, distinguish Section 119 I Alt. 1, Section 119 I Alt. 2, and Section 119 II BGB.
2. Give one fact pattern each for Section 323, Section 324, and Section 326 V BGB.
3. Explain why revocation does not make the contract void ex tunc.
4. In a case answer, where do Section 349 and Sections 346-348 BGB appear?

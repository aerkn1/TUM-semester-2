# Active Recall Session: Week 01-02 Introduction To Business Law

Course: Business Law
Wiki note: `business-law/wiki/week-01-02-introduction-to-business-law.md`
Date: 2026-05-14
Session type: `first-pass`

## Session Focus

Build the first mental model from scratch:

- law vs morality
- private law vs public law
- state as sovereign authority vs state as equal market actor
- lex specialis
- beginning transition into civil-law method

## User Raw Answers

### Prompt 1

Friend promises to help you move, then cancels. Is that immoral, illegal, both, or neither?

User answer:

> neither for me, it does not violate any rights on me, it is just a matter of friendship and collaboration for me.

Feedback:

- Quality: `green`
- Correct intuition: ordinary friendship favors usually lack intention to be legally bound.
- Refinement: it may be socially disappointing or morally questionable, but law usually does not enforce it.

Refined model:

```text
Law = binding and enforceable.
Morality/friendship norms = may matter socially, but not automatically legally enforceable.
```

### Prompt 2

Buyer lies in negotiation and says they have a better offer elsewhere. Should that automatically be illegal?

User answer:

> it does not rely on any legal agreement, just verbal communication and decision making maybe not illegal but conventionally immoral.

Feedback:

- Quality: `yellow`
- Correct intuition: immoral does not automatically mean illegal.
- Correction: verbal communication can still be legally relevant. Law does not require everything to be written.
- Refinement: if the lie legally induces a declaration of intent, it may later matter as deceit, especially for rescission under Section 123 BGB.

Refined model:

```text
Do not ask only: "Was it morally wrong?"
Ask: "Did a legal rule attach a consequence to this behavior?"
```

### Prompt 3

A company sells a machine to another company, but the buyer does not pay. Public law or private law?

User answer:

> private law, its not about the society and based on contractual agreement between both parties and contains legal obligations to be fulfilled.

Feedback:

- Quality: `green`
- Correct: this is private law because private actors face each other as equals under a contract.

Refined model:

```text
Equal private actors + contractual obligation = private law.
```

### Prompt 4

A city authority refuses to give a company a building permit. Public law or private law?

User answer:

> not sure, both this is an issue between a governmental and private authority.

Feedback:

- Quality: `yellow`
- Correction: this is public law because the city acts with sovereign public authority.
- Important nuance: a public body being involved is not enough by itself. The question is whether it acts as a sovereign authority or as an equal market participant.

Refined model:

```text
State acting with sovereign authority = public law.
State acting like a normal buyer/seller = private law.
```

### Prompt 5

If two legal rules seem relevant, one general and one very specific, which one usually controls?

User answer:

> specific one complements the general one?

Feedback:

- Quality: `yellow`
- Correct direction: the specific rule matters more.
- Correction: if the two rules overlap and conflict, the specific rule usually takes priority.

Keyword:

```text
lex specialis = the more specific rule prevails over the more general rule.
```

## Mini-Test Results

### Municipality buys laptops from Dell and refuses to pay

User answer:

> private law, the public authority acts as a consumer actor that becoming a client of the dell to buy laptop as other private actors and conducts some agreements with dell as a legal binding like billing against payment etc.?

Feedback:

- Quality: `green`
- Correct: municipality acts as a market participant, not sovereign authority.
- Refined wording: say "private actor" or "market participant," not "private authority."

### Tax office demands additional tax from company

User answer:

> taxation I think about the public law since the tax office operates as a public authority as its own operations.

Feedback:

- Quality: `green`
- Correct: tax office uses state authority.

### Police orders shop to close because of safety rules

User answer:

> public law, the shop is operating out of the public rules that police takes action upon?

Feedback:

- Quality: `green`
- Correct classification.
- Refinement: the key is the police order as an exercise of sovereign power, not necessarily whether the shop has already violated rules.

## Current Mental Models

```text
Private law:
Legal relationships between private actors who face each other as legal equals.
Example: two companies in a sales contract.

Public law:
Legal relationships where the state or public body acts with sovereign authority.
Example: building permit, tax office, police order.

Public body test:
Is the state acting as a sovereign authority or as an equal market participant?

Lex specialis:
If a specific rule and general rule overlap, the specific rule usually takes priority.
```

## Weak Spots

| Concept | Quality | Fix |
|---|---|---|
| Verbal communication and legal relevance | `yellow` | Remember that legal declarations can be oral, written, or implied. |
| Public body involvement | `yellow` | Ask whether the public body acts with sovereign authority. |
| Lex specialis | `yellow` | Specific rule can override the general rule in case of overlap/conflict. |

## Next Recall Prompts

1. In a civil-law system like Germany, do we start from statutes, court cases, or fairness intuition?
2. If a court decision is important, does it replace the statute?
3. Why do court decisions still matter in a statute-based system?
4. What is the difference between EU regulations and EU directives?
5. What does the BGB bracketing technique mean?

## Civil-Law System Follow-Up

### Prompt 1

If you are solving a German law problem, why is starting from the written statute important?

User answer:

> its the written decisions and rules for governance across the germany. Its a guidance for a starting point to decide over a case or a incident based on the law and the enforcement that applie according to the rules that matching with that incident.

Feedback:

- Quality: `green`
- Correct: German law is statute-centered, so the written norm is the starting point for deciding which legal consequence applies to a fact pattern.
- Refinement: statutes are not "written decisions" in the court sense; they are written legal rules enacted by the competent lawmaker.

Refined model:

```text
Civil-law reasoning starts from the statutory rule:
facts -> relevant statute -> conditions -> legal consequence.
```

### Prompt 2

If a court decision does not replace the statute, why might court decisions still matter?

User answer:

> it is a good reference to take a look at but may not enforce the decision making all the time ?

Feedback:

- Quality: `yellow`
- Correct direction: court decisions are references and guides.
- Refinement: in German civil law, higher-court decisions are not precedent in the strict common-law sense, but they strongly influence interpretation because lower courts and lawyers expect similar reasoning to be followed.

Refined model:

```text
Statute is the source.
Court decisions clarify how the statute is understood in real cases.
```

### Prompt 3

Why might courts need to explain a statutory word like "deceit"?

User answer:

> because its a very broad definition and can be mapped by situations and consequences.

Feedback:

- Quality: `green`
- Correct: broad legal terms must be concretized through interpretation.
- Refinement: courts translate broad words into workable legal tests, for example whether someone intentionally created or maintained an error about facts.

Refined model:

```text
Broad statutory word -> interpretation -> legal test -> application to facts.
```

## Statutory Application Attempt: Section 123 BGB

Case:

> A seller tells a buyer, "This painting is by Picasso." The seller knows it is not. The buyer believes the seller and buys it.

Prompt:

Break the rule into conditions, legal consequence, and word needing interpretation.

User answer:

> 1- deceit and immortailty over commercial trade between two private actor.
> 2-overpayment for a product that not actually reflects the actual worthiness.
> 3- deceit ?

Feedback:

- Quality: `yellow`
- Correct: "deceit" is the key legal word needing interpretation.
- Correction: "immorality" and "overpayment" may describe the business unfairness, but the legal structure must track the statute.
- The legal consequence is not "overpayment"; it is the right to avoid/rescind the declaration of intent.

Refined rule structure:

```text
Conditions:
1. Buyer made a declaration of intent, e.g. acceptance/purchase.
2. Seller deceived the buyer.
3. The deceit induced the buyer's declaration of intent.
4. The deceit was intentional.

Legal consequence:
Buyer may avoid/rescind the declaration of intent.

Word needing interpretation:
"Deceit" = intentional creation or maintenance of an error about facts.
```

Mental model:

```text
Business harm explains why the case matters.
Legal consequence explains what the law allows.
```

### Revised User Sentence

Prompt:

> Because ___, ___, and ___, the buyer may ___.

User answer:

> because of factual lies, intention of deception and silence despite duty to inform, the buyer may avoid the declaration of intent

Feedback:

- Quality: `yellow-green`
- Correct: factual lie, intentional deception, and avoidance of the declaration of intent are the right structure.
- Correction: "silence despite duty to inform" is an important subtype of deceit, but the given facts involve active false statement, not silence.

Refined sentence:

```text
Because the seller intentionally made a false factual statement about the painting's authorship and this induced the buyer to buy it, the buyer may avoid the declaration of intent.
```

## Hierarchy Of Norms Attempt

### Prompt 1

If German federal law and Bavarian state law conflict, which one should usually win?

User answer:

> bavarain law is more specific apparently. goes with bavarian law?

Feedback:

- Quality: `red-yellow`
- Correction: federal law usually prevails over state law under Art. 31 GG.
- Reason: hierarchy of norms is different from lex specialis. Bavarian law may be geographically narrower, but it does not beat federal law if there is a true conflict and federal law is competent.

Refined model:

```text
Hierarchy question: higher-ranking law wins.
Specificity question: more specific rule wins within the relevant legal level/system.
```

### Prompt 2

If EU law applies and conflicts with German national law, which one usually has priority?

User answer:

> german national law is more specific

Feedback:

- Quality: `red-yellow`
- Correction: EU law usually has primacy where it applies.
- Reason: EU law is an independent supranational legal order with priority over conflicting national law within its field of application.

Refined model:

```text
EU law applicable + conflict with national law -> EU law usually has priority.
```

### Prompt 3

Why would business managers care about EU law, even when operating in Germany?

User answer:

> its a international operation complement for the legal boundries for maybe import/export purposes if they also have clients or agreements across european countries ?

Feedback:

- Quality: `green`
- Correct: EU law matters strongly for cross-border commerce, trade, import/export, and agreements across European countries.
- Expansion: EU law can also matter domestically because EU rules affect consumer protection, competition/cartel law, product regulation, digital markets, employment mobility, and freedom of establishment.

Refined model:

```text
EU law is not only "foreign business law." It can shape the rules German businesses must follow inside Germany whenever an EU rule governs the field.
```

### Hierarchy Mini-Test

Prompt:

1. Federal German product safety law conflicts with Bavarian product safety rule. Which likely wins?
2. EU consumer protection regulation conflicts with German national consumer rule. Which likely wins?
3. General BGB rule and specific HGB merchant rule both apply to a merchant transaction. Which principle matters?

User answer:

> 1-federal one
> 2-eu consumer
> 3-general BGB rule

Feedback:

- Q1 quality: `green`; federal law wins under hierarchy.
- Q2 quality: `green`; EU regulation wins where applicable.
- Q3 quality: `red-yellow`; the specific HGB merchant rule usually matters under lex specialis if it overlaps with the general BGB rule.

Correction:

```text
Hierarchy decides conflicts between legal levels.
Lex specialis decides conflicts between general and specific rules.
Specific HGB merchant rule can override/general-modify general BGB rule in a merchant transaction.
```

### Lex Specialis Repetition

Prompt:

> A general BGB rule says "X." A specific HGB rule for merchants says "Y." Both apply to a transaction between merchants. Which one do you check first for the final answer, and what is the keyword?

User answer:

> general BGB rule

Feedback:

- Quality: `red`
- Correction: the specific HGB merchant rule is decisive if it overlaps/conflicts with the general BGB rule.
- Keyword: `lex specialis`.

Updated weakness:

```text
The user still tends to choose the general rule when asked about BGB vs specific HGB rules. Repeat with concrete examples before moving on.
```

### Corrected Hierarchy vs Specificity Rule

Prompt:

> If federal law conflicts with Bavarian state law, ___ wins because ___.
> If EU law applies and conflicts with German law, ___ wins because ___.
> If general BGB and specific HGB rules conflict in a merchant case, ___ wins because ___.

User answer:

> 1-federal, hierarchical supression
> 2-EU law, hierarchical supression
> 3-HGB , speficiality to merchant

Feedback:

- Quality: `green-yellow`
- Correct concepts: federal wins over Bavarian state law; EU law wins where applicable; HGB can win over BGB in merchant cases because it is more specific.
- Wording refinement: say "hierarchy of norms" or "primacy/supremacy," not "hierarchical suppression."

Refined version:

```text
Federal law wins over Bavarian state law because of hierarchy of norms, especially Art. 31 GG.
EU law wins over German law where applicable because of primacy of EU law.
Specific HGB merchant rules can prevail over general BGB rules because of lex specialis.
```

## EU Regulation vs Directive Attempt

Prompt:

1. Which one creates uniform rules directly across EU Member States: regulation or directive?
2. Which one sets a goal but needs Member States to implement it into national law?
3. Why might businesses prefer a regulation when operating across many EU countries?

User answer:

> 1-regulation?
> 2-EU court?
> 3-common set of rules to comly with standards and the rules?

Feedback:

- Q1 quality: `green`; regulation is correct.
- Q2 quality: `red-yellow`; the correct answer is directive. The EU court may interpret EU law, but directives are the legal instrument that set goals for Member States to implement.
- Q3 quality: `green`; businesses may prefer regulations because uniform rules reduce compliance fragmentation across Member States.

Refined model:

```text
Regulation = directly applicable, binding in entirety, uniform rules.
Directive = EU goal/standard, Member States transpose into national law, harmonisation rather than full uniformity.
```

### EU Law Mini-Test

Prompt:

1. A rule says: "This EU packaging standard applies directly in all Member States from July 1." Regulation or directive?
2. A rule says: "Member States must ensure consumers have a 14-day withdrawal right, and each state must implement this in national law." Regulation or directive?

User answer:

> 1-directive
> 2-regulation

Feedback:

- Q1 quality: `red`; "applies directly in all Member States" signals regulation.
- Q2 quality: `red`; "Member States must implement this in national law" signals directive.

Correction:

```text
Directly applies everywhere -> regulation.
Member States must implement/transposes -> directive.
```

### Corrected EU Law Mini-Test

Prompt:

1. "This EU rule is binding in its entirety and directly applicable in Germany, France, and Italy."
2. "Germany must change the BGB to achieve an EU consumer-protection goal."

User answer:

> 1-regulation
> 2-directive

Feedback:

- Quality: `green`
- Correct. The memory hook worked:

```text
Direct = regulation.
Implement = directive.
```

## BGB Bracketing Technique Attempt

Prompt:

> Why might a contract-law case require looking at both Book 1 and Book 2 of the BGB?

User answer:

> they might have some complementary or primacy impact?

Feedback:

- Quality: `yellow`
- Correct direction: Book 1 and Book 2 can interact.
- Refinement: Book 1 contains general rules that apply across later books, including Book 2, unless a more specific rule modifies them.
- "Primacy" is less precise here than "general rule applies unless displaced by a specific rule."

Refined model:

```text
Book 1 gives general legal tools.
Book 2 gives contract/obligation-specific rules.
A contract case may need both: Book 2 for the contract obligation and Book 1 for general concepts like declaration of intent.
```

### Corrected BGB Bracketing Answer

Prompt:

> Why does Book 1 "bracket" Book 2?

User answer:

> because it contains more generic rules

Feedback:

- Quality: `green`
- Correct. More precise wording:

```text
Book 1 brackets Book 2 because Book 1 contains general rules that can apply to contract-law issues in Book 2 unless a more specific rule modifies them.
```

## End-Of-Session Concept Status

| Concept | Status | Note |
|---|---|---|
| Law vs morality | `green` | Correctly separates social/moral norms from enforceable law. |
| Public vs private law | `green` | Correctly uses sovereign authority vs equal private actors. |
| Civil-law method | `green-yellow` | Correctly starts from statutes; remember courts guide interpretation. |
| Statutory if-then analysis | `green-yellow` | Improved; keep separating economic harm from legal consequence. |
| Hierarchy of norms | `green-yellow` | Correct after repetition; use "hierarchy/primacy," not "specificity." |
| Lex specialis | `yellow` | Corrected but needs another future retrieval pass. |
| Regulation vs directive | `green` | Correct after direct/implement memory hook. |
| BGB bracketing technique | `green` | Correct core idea: general rules wrap around specific contract rules. |

## Note References

- Main note: `business-law/wiki/week-01-02-introduction-to-business-law.md`
- Relevant sections:
  - `Law, Morality, And Sources Of Law`
  - `Public Law vs Private Law`
  - `Working With German Law`
  - `Exam Relevance`

## D+1 Repair Pass: 2026-05-16

Session type: `spaced-repetition-repair`
Reason: D+1 checkpoint from 2026-05-15 was missed; repaired on 2026-05-16.

### User Raw Answers

1. Private law vs public law:

> private law applies to the agreements or the relations across private boundaries and merchants whereas the public law applies to the public authorities and also the public vs private authorities.

Feedback:

- Quality: `yellow`
- Correct direction: private law concerns equal legal actors; public law involves public authority.
- Correction: public law is not simply any case with a public body. The decisive test is whether the state acts with sovereign authority.

2. City of Munich buys laptops from Dell:

> private law, because it is between public and private boundaries

Feedback:

- Quality: `green-yellow`
- Correct classification: private law.
- Correction: it is private law because the city acts as an equal market participant/customer, not because one side is public and one side is private.

3. Lex specialis:

> lex specialis is a decision on the rule precedence to be applied in cases. If the specification of the rules applied to the cases comes from higher primacy like EU vs german federal state, EU law wins. However, if the same dilemma occurs between two different book within the same state law, the more specified one wins.

Feedback:

- Quality: `green`
- Correct: hierarchy/primacy and specificity are different conflict-resolution ideas.
- Refined exam wording: hierarchy decides between different legal ranks; lex specialis decides between overlapping general and specific rules.

4. EU regulation vs directive:

> regulation is the definition of rules , directive is the navigative boundary to make it applied across the EU member countries

Feedback:

- Quality: `yellow`
- Correction: regulation is directly applicable in all member states. Directive binds member states as to the result, but requires national transposition.

5. Law vs morality:

> morality does not depend on set of rules or regulations defined by authorities. They are ethical complementaries

Feedback:

- Quality: `green-yellow`
- Correct: morality and law differ.
- Refined exam wording: law is an institutionalized and enforceable system of rules; morality is ethical/social judgment and does not automatically create legal consequences.

### Repaired Mental Models

```text
Private law = equal legal actors, including the state if it acts as market participant.
Public law = public authority acts with sovereign power.
Lex specialis = specific rule prevails over general rule at the same/overlapping level.
Hierarchy/primacy = higher-ranking law prevails.
EU regulation = directly applicable.
EU directive = binding goal; member states transpose into national law.
Law != morality; legal enforceability requires a legal rule and legal consequence.
```

### Remaining Weak Spots

| Concept | Quality | Fix |
|---|---|---|
| Public body involvement | `yellow` | Always ask whether the state acts as sovereign or market participant. |
| EU regulation vs directive | `yellow` | Regulation applies directly; directive requires national implementation. |
| Law vs morality wording | `green-yellow` | Use enforceability/legal consequence as the exam anchor. |

### Next Recall Prompts

1. Give one example where the state is involved but private law applies.
2. Give one example where a moral wrong has no legal consequence.
3. Explain regulation vs directive in one sentence each.
4. Decide a conflict between EU law and German law.
5. Decide a conflict between a general BGB rule and a specific HGB rule.

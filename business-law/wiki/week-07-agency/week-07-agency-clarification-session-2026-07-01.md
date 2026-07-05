# Week 07 Agency - Clarification Session 2026-07-01

Source note: `business-law/wiki/week-07-agency/week-07-agency.md`
Context companion: `business-law/wiki/week-07-agency/CONTEXT.md`
Session type: targeted clarification, not completed first-pass active recall

## Session Focus

The session clarified the Agency triangle and the boundaries between:

- principal, agent, third party, and power of representation;
- internal permission (`may do`) versus external authority (`can do`);
- publicity versus authority;
- legal entities acting through organs or agents;
- regular authorization versus reliance-based authority;
- agency by estoppel versus ostensible agency;
- contracting with oneself under Section 181 BGB.

## Clarification Questions And Answers

### Prompt 1

User asked:

> what actually principal, agent and the authority represents with example analogy? how it differs as internal and external boundary declaration of intent

Professor clarification:

Agency is a legal remote-control mechanism. The agent presses the button by making an own declaration of intent, but the principal's legal position moves if Section 164 I BGB is satisfied.

```text
Principal = person whose legal position changes.
Agent = person making the declaration externally.
Third party = outside contract partner.
Power of representation = external legal authority that lets the declaration bind the principal.
```

The central distinction:

```text
External relationship = can do = can bind the principal toward the third party.
Internal relationship = may do = permission or duty inside the principal-agent relationship.
```

### Prompt 2

User answer:

> violation of internal instruction and causes wrong declaration of intent in terms of offer and accpetance between customer and the principal externally

Professor feedback:

Partly correct, but the phrase "wrong declaration of intent externally" is risky. The better wording is:

```text
The declaration may be externally effective, but internally forbidden.
```

If the agent has external power of representation, the principal may still be bound to the customer even though the agent violated an internal instruction.

### Prompt 3

User asked:

> so even if there is a violation of the internal instruction by agent against principal for the declaration of intent that made externally and accepted by customer, it may still proceed? I understand that the principal becomes bounding with customer over the agreement that agent made but it does not actually reflect its intention internally right? in that case the principal can claim ?

Professor clarification:

Yes. If the agent had external power of representation and the third party was protected, the agreement may proceed externally:

```text
P is bound to T.
A violated the internal relationship with P.
P may have internal recourse against A.
```

The principal's precise internal intention does not have to match the exact deal if the agent's external authority covers the transaction. Section 179 BGB is not the right route where the agent actually had external authority; it is for lack of authority plus refused ratification.

### Prompt 4

User asked:

> regarding no publicity, it basically means that the customer needs to reconginze the agent officialy as a authorized boundary of principal before agreement?

Professor clarification:

This confused publicity with authority.

```text
Publicity = T can recognize that A acts for P.
Authority = A can legally bind P.
```

Publicity does not require formal verification of authority. It only requires that the transaction is externally recognizable as being in the principal's name.

### Prompt 5

User asked:

> "legal entities cannot act physically. They need organs or agents to make declarations." can we elaborate on that?

Professor clarification:

A legal entity, such as a GmbH, can own property, enter contracts, owe money, sue, and be sued. It cannot physically speak, sign, negotiate, or send a human declaration by itself.

Therefore, a human act must be attributed to it:

```text
Organ = human office/body that acts for the entity by law.
Agent = authorized human representative.
```

Example:

```text
Alpha GmbH cannot speak.
Its managing director signs in Alpha GmbH's name.
The declaration is attributed to Alpha GmbH.
```

### Prompt 6

User asked:

> I did not get the reliance-based authroity , what actually distinction between agency by estoppel and ostensible? when it occurs and what is the difference against the regular authorization

Professor clarification:

Regular authorization is based on intentional authority:

```text
P intentionally says: A may represent me.
```

Reliance-based authority is based on an appearance attributable to P:

```text
P did not clearly authorize A, but P created or tolerated the appearance that A was authorized, and T reasonably relied on it.
```

Distinction:

| Type | P's state | Core distinction |
|---|---|---|
| Agency by estoppel | P knows and tolerates A acting like an agent. | Conscious tolerance. |
| Ostensible agency | P does not know, but negligently should have known and prevented the appearance. | Negligent failure to control. |

### Prompt 7

User asked:

> how about the contracting with oneself? what it is actually and how it occurs and what are the legal boundaries?

Professor clarification:

Contracting with oneself occurs when the agent is effectively on both sides of the transaction.

Two forms:

```text
Self-contracting:
A represents P and personally buys from P.

Multiple representation:
A represents both seller P and buyer T.
```

Section 181 BGB restricts this because of structural conflict of interest. It can be allowed if the principal permitted it in advance, ratified it later, the act merely performs an existing obligation, or the act is legally advantageous only for the principal.

## Refined Mental Models

### Remote-Control Model

```text
Agent presses the legal button.
Principal's legal position moves.
Third party receives the contractual effect.
```

### Boundary Model

```text
Can do = external power of representation.
May do = internal permission.
```

If A violates `may do` but still has `can do`, P may be bound externally and claim internally against A.

### Publicity Model

```text
Publicity asks: whose contract is this meant to be?
Authority asks: can A bind that person?
```

### Appearance Model For Reliance-Based Authority

```text
Regular authorization = P's declared will.
Reliance-based authority = P-created appearance plus T's good-faith reliance.
```

## Weak Spots

| Weak Spot | Quality | Corrective Rule |
|---|---|---|
| Internal-instruction breach described as "wrong declaration externally" | yellow | Say "externally effective but internally forbidden" if external authority exists. |
| Publicity confused with authority verification | yellow | Publicity identifies the principal; authority tests power to bind the principal. |
| Regular authorization versus reliance-based authority | yellow | Regular = declaration; estoppel = knowledge and tolerance; ostensible = negligent lack of knowledge. |
| Contracting with oneself | yellow | Check whether A is personally counterparty or represents both sides; then apply Section 181 exceptions. |

## Next Recall Prompts

1. P tells A internally not to sell below EUR 10,000. P publicly presents A as sales manager. A sells to T for EUR 8,000. T does not know the limit. Who is bound, and what can P claim?
2. A says "I buy this machine" while secretly intending to buy for P. T thinks A buys personally. Which Section 164 element fails?
3. P knows A repeatedly sells in P's name without express authority and tolerates it. Which reliance authority category is this?
4. P does not know A is using P's email and forms to sell, but proper controls would have revealed it. Which reliance authority category is this?
5. A is authorized to sell P's machine and sells it to herself. Which Section 181 issue appears, and what exceptions must be checked?

## Study-Control Impact

This file records the clarification portion only. It did not itself complete Agency first-pass active recall. Later on 2026-07-01, the separate file `week-07-agency-active-recall-session-2026-07-01.md` completed the first active-recall pass, so the dashboard should now show `First Pass = 2026-07-01` and `D+1 due 2026-07-02`.

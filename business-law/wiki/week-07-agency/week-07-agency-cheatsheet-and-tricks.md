# Week 07 Agency Cheatsheet And Tricks

Course: Business Law
Exam date: 2026-07-28
Source: week-07-agency.md, active-recall-session-2026-07-01.md, clarification-session-2026-07-01.md

## Must-Know (exam-critical)

| Rule | Anchor | Core content |
|---|---|---|
| Effective agency, three cumulative elements | Section 164 I BGB | Own declaration of intent, publicity (acting in the principal's name), power of representation. All three must be met. |
| Legal effect if all three are met | Section 164 I BGB | Principal and third party become the contract parties directly; the agent normally drops out of the contract. |
| Agent vs. messenger | No fixed section, tested through Section 164 I | Agent forms their own legal declaration; a messenger only transmits someone else's already-fixed declaration. No own declaration means no agency analysis — check transmission instead. |
| No publicity consequence | Section 164 II BGB | If T cannot recognize A is acting for P, A's hidden intent is irrelevant; A is likely bound personally, not P. |
| No authority consequence | Sections 177 I, 179 BGB | Contract is pending until P ratifies. If P refuses, the third party may claim against the unauthorized agent under Section 179 BGB — this is agent liability, not an ordinary Section 433 claim. |
| Internal vs. external boundary | No fixed section, framed as "can do" vs. "may do" | External power of representation = can do = binds P toward T. Internal relationship (employment/mandate/service) = may do = what A is permitted internally. Violating "may do" while keeping "can do" still binds P externally. |
| Sources of power of representation | Sections 35 GmbHG (statutory), 167 I BGB (declaration), reliance (Section 242 BGB background) | Statutory (organ representation), declared (internal or external authorization), or reliance-based (estoppel/ostensible). |
| Reliance-based authority, two forms | No fixed section, course labels: agency by estoppel, ostensible agency | Estoppel: P knows and tolerates the appearance. Ostensible: P doesn't know but should have known with due care. Both give A real power of representation if T relied in good faith. |
| Termination of authority | Section 168 BGB, third-party protection via Sections 170, 173 BGB | Authority usually ends with the underlying relationship and is freely revocable. If withdrawal is only told to the agent, a good-faith third party may still be protected unless they knew or should have known. |
| Self-dealing / contracting with oneself | Section 181 BGB | Two forms: self-contracting (A is personally the counterparty) and multiple representation (A represents both sides). Transaction is provisionally invalid unless: prior permission, later ratification, mere performance of an existing obligation, or legally advantageous only for the principal. |

## Nice-to-Have (depth/edge cases)

- Legal entities (GmbH, AG) cannot physically act — a human act must be attributed to them through an organ (statutory, e.g. Section 35 GmbHG director) or an agent (authorized representative); both routes exist side by side.
- Section 56 HGB (store/shop authority) can supply publicity and authority for customary retail-style sales made by staff, without needing an explicit declaration each time.
- With multiple GmbH directors, joint representation is the statutory default unless the articles say otherwise — one director acting alone can fail the authority element even with clear organ status.
- Collusion between agent and third party can void the transaction under Section 138 BGB even where the agent had formal external authority.
- If the third party actually knows the agent is exceeding internal limits, the third party's protection weakens even though the "can do / may do" split normally favors the third party.
- The "transaction for whom it concerns" exception can substitute for publicity in immediate, low-stakes cash transactions (e.g., paying for fuel or a small purchase) where the buyer's identity is economically irrelevant — but this is fact-sensitive and arguable, not automatic.
- Advantages/risks framing (division of labor, capacity, expertise vs. loss of control, information gaps) and the principal-agent problem (hidden characteristics/action/information/intention, and the agency-cost responses: signaling, incentives, surveillance, authority limits) are the bridge from the legal rules to the "why does business design authority this way" theory question.

## Nuances And Traps

| Nuance/Trap | Why it's easy to get wrong | Correct handling |
|---|---|---|
| No-publicity consequence | It feels intuitive that having authority should still protect the principal, so students conclude P is bound even when A never showed the transaction was for P. | Authority cannot rescue missing publicity. If A does not act recognizably in P's name, P is not bound under Section 164 I regardless of whether A had power of representation; A is likely treated as the contracting party under Section 164 II. |
| Section 166 BGB misrouting | When an agent breaches an internal instruction (e.g., sells below the minimum price), it is tempting to reach for Section 166 BGB because it "sounds like" the general agency-attribution section. | Section 166 BGB governs attribution of knowledge or defects of intent through the representative — it is not the anchor for ordinary internal recourse after a breached instruction. The correct route is: P is bound externally (can do intact), and P's remedy against A is based on the internal relationship (employment, mandate, service duties), not Section 166. |
| "Wrong declaration of intent" mislabeling | Describing an internal-instruction breach as a "wrong declaration of intent" externally sounds plausible but imports a Section 119-style mistake analysis that does not apply here. | The correct phrasing is that the declaration is externally effective but internally forbidden — this stays inside the agency can-do/may-do frame instead of drifting into rescission doctrine. |
| Section 181 exceptions, incomplete list | Students often recall only "prior permission" and "later ratification" and stop there. | There are four exceptions: prior permission, later ratification (Section 177 BGB), mere performance of an existing obligation, and a transaction that is legally advantageous only for the principal. |
| Section 181 vs. an ordinary internal-instruction violation | Both look like an agent overstepping bounds, so it is tempting to treat self-dealing as just another "may do" breach that still binds P externally. | Self-dealing is stronger than an ordinary internal-instruction violation: because there is no independent counterparty bargain, Section 181 can actually restrict A's external power, not just create internal liability. |
| Lack of authority vs. abuse of existing authority | Any bad agent action can get lumped together as "the agent had no authority." | Distinguish the two: lack of authority triggers the Section 177/179 pending-ratification route; abuse of existing authority (internal-limit violation) keeps the principal bound externally and only creates internal recourse. |
| Reliance-based authority requires a pattern, not one incident | A single unauthorized sale can look enough like "the principal should have noticed." | The exam facts should show a pattern or appearance attributable to P (repeated conduct, use of company materials/records) plus the third party's reasonable good-faith reliance — one isolated unauthorized act is usually not enough. |
| Distinguishing agency by estoppel from ostensible agency | Both protect a third party who relied on an apparent agency, so the two get merged. | Estoppel = P actually knew and tolerated the appearance (conscious tolerance). Ostensible = P did not know, but a careful principal would have noticed and prevented it (negligent failure to control). State which mental state the facts show. |

## One-Line Recall Drill

```text
164 I = own declaration + publicity + power of representation
164 II = no publicity, hidden intent irrelevant, agent likely bound personally
177 I = pending, principal ratifies
179 I = unauthorized agent liability if ratification refused
167 I = authority by declaration (internal or external)
35 GmbHG = statutory organ representation
168 = authority ends with underlying relationship, freely revocable
170, 173 = third-party protection if withdrawal only told to agent
181 = self-contracting / multiple representation, four exceptions
can do = external, binds principal
may do = internal, breach creates internal recourse only
estoppel = P knows and tolerates
ostensible = P should have known, negligent
166 =/= internal recourse; it is knowledge/defect-of-intent attribution
```

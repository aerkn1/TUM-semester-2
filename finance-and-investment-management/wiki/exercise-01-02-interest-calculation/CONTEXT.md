# Ubiquitous Language: Exercise 01-02: Interest Calculation

Source note: `exercise-01-02-interest-calculation.md`
Course: Finance and Investment Management
Definition sources: local topic note and raw material for term discovery; enriched with standard domain knowledge where the local note names a term without fully defining it.

This file is a standalone terminology and formula companion. It follows Matt Pocock style: canonical terms, aliases to avoid, relationships, example dialogue, and flagged ambiguities.

## Finance Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Cash Flow** | A dated inflow or outflow of money used for valuation and investment decisions. | profit, accounting earnings |
| **Present Value** | The value today of a future cash flow discounted at an appropriate rate. | current price always |
| **Future Value** | The amount a current cash flow grows to after earning interest over time. | forecast value |
| **Discount Rate** | The rate used to convert future cash flows into present value, reflecting time value and risk. | interest rate always |
| **Compounding** | Interest earning interest over multiple periods. | simple interest |
| **Net Present Value** | The sum of discounted cash inflows and outflows; positive NPV means value creation under the chosen discount rate. | profit, payoff |
| **Internal Rate of Return** | The discount rate that sets NPV equal to zero for a cash-flow stream. | project return always |

## Exam Setup Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Timeline** | A dated layout of cash flows and rates that prevents mixing values from different points in time. | list of numbers |
| **Nominal Rate** | A quoted annual rate before adjusting for compounding frequency. | effective rate |
| **Effective Rate** | The actual rate earned or paid over a period after compounding is considered. | nominal rate |

## Interest Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Simple Interest** | Interest calculated only on the original principal. | compound interest |
| **Compound Interest** | Interest calculated on principal plus accumulated interest. | simple interest |
| **Intra-Year Compounding** | Compounding more frequently than once per year, such as monthly or quarterly. | annual rate |
| **Continuous Compounding** | The limiting case where compounding occurs continuously, using exponential growth. | very frequent simple interest |
| **Present Value Factor** | The multiplier used to discount one future cash flow to today. | interest rate |
| **Effective Annual Rate** | The actual annual rate after considering compounding frequency. | nominal annual rate |

## Relationships

- **Cash Flow** should be distinguished from **Present Value** when writing exam answers.
- **Present Value** should be distinguished from **Future Value** when writing exam answers.
- **Future Value** should be distinguished from **Discount Rate** when writing exam answers.
- **Discount Rate** should be distinguished from **Compounding** when writing exam answers.
- **Compounding** should be distinguished from **Net Present Value** when writing exam answers.
- **Net Present Value** should be distinguished from **Internal Rate of Return** when writing exam answers.
- A strong answer defines the canonical term, applies the rule or formula, and states the managerial, legal, or analytical implication.

## Visual Memory Aid

```mermaid
flowchart TD
    N1[Cash Flow]
    N2[Present Value]
    N1 --> N2
    N3[Future Value]
    N2 --> N3
    N4[Discount Rate]
    N3 --> N4
    N5[Compounding]
    N4 --> N5
    N6[Net Present Value]
    N5 --> N6
    N7[Internal Rate of Return]
    N6 --> N7
```

## Example Dialogue

> **Student:** "I see **Cash Flow** and **Present Value** in the note. Are they interchangeable?"
>
> **Professor:** "No. Use **Cash Flow** for its precise technical meaning, and use **Present Value** only when the facts match that definition."
>
> **Student:** "So in an exam answer I should name the exact term first?"
>
> **Professor:** "Yes. Name the canonical term, apply the decision rule or mechanism, then state the implication."

## Flagged Ambiguities

- Do not use broad labels like "concept", "factor", or "thing" when a canonical term above fits.
- Do not use aliases listed in the tables unless you are explicitly explaining why they are misleading.
- If a formula symbol appears, define its unit, timing, and decision role before calculating.
- If a legal, theoretical, or framework term has a common everyday meaning, use the technical course meaning in exam answers.

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Naming a term without applying it. | Define it briefly, then apply it to the facts, formula, or decision. |
| Treating examples as definitions. | Use examples only after the canonical definition is clear. |
| Mixing related terms. | State the boundary between the terms before comparing them. |
| Copying a formula without variable meaning. | Define each variable and unit before substitution. |

## Cheat-Sheet Language

```text
Draw the timeline, identify cash flows, choose the rate convention, compute at one date, then interpret the decision rule.
For every technical term: define it, identify when it applies, and state the common confusion to avoid.
```

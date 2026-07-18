# Ubiquitous Language: Exercise 13 Mock Exam

Source note: `exercise-13-mock-exam.md`
Source file: `finance-and-investment-management/raw/moodle-export-investment-and-financial-management-950881761-s26-20260709/CW 29  14.07. _ 15.07./Exercise 13 Mock Exam.pdf`
Course: Finance and Investment Management
Processed: 2026-07-09

The source contains a mock exam but no official answer key. The source note therefore uses inferred answer routes.

## Mock-Exam Terms

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Lecture Section** | Mock-exam part covering financial analysis, investment analysis, capital budgeting, cost of capital, and capital structure. | exercise section |
| **Exercise Section** | Mock-exam part covering interest, annuities, redemptions, bonds, stocks, and options. | lecture section |
| **Single-Correct MCQ** | Multiple-choice item where exactly one option is correct. | multiple correct |
| **No Negative Points** | Wrong answers do not subtract points, so unanswered questions are costly. | penalty exam |
| **No Intermediate Rounding** | Keep full precision until the final matching step. | round every step |
| **Inferred Answer Route** | Answer derived from processed course notes and formulas, not from an official solution key. | official answer |

## Calculation Routers

| Router | Formula / Test | Mock questions |
|---|---|---|
| Net income and coverage | `net income = margin x sales`; `coverage = EBIT / interest` | Q2 |
| NPV rule | Discount cash flows and compare value creation | Q3 |
| FCF | `EBIT(1-tax) + depreciation - CapEx - Delta NWC` for annual FCF setup | Q5 |
| Asset beta | `beta_A = E/V beta_E + D/V beta_D` | Q6, Q9 |
| Doubling time | `N = ln(2)/ln(1+r)` | Q11 |
| Continuous compounding | `FV = PV x exp(rN)` | Q12 |
| Annuity due | Ordinary annuity factor times `(1+i)` | Q13, Q14 |
| Redemption duration | Solve annuity repayment years from repayment base | Q15 |
| Modified duration | `Delta B/B approx -D_mod Delta r` | Q18 |
| Gordon growth | `P_0 = D_1/(r_e-g)` and `r_e = D_1/P_0 + g` | Q19 |
| Short call profit | `premium - max(S_T-K,0)` | Q21 |

## Relationships

- **No Intermediate Rounding** affects all calculation routers.
- **Single-Correct MCQ** means multiple plausible statements must be ranked by exact wording.
- **Inferred Answer Route** should be updated if an official solution appears.
- **Lecture Section** and **Exercise Section** should be practiced separately first, then combined under timing.

## Example Dialogue

Student: "Q15 says the degree lasts three years, so I compound the loan for three years."

Professor: "Read the timing anchor: the loan starts at the beginning of the second year. The remaining study period after borrowing is two years."

Student: "Q21 is a call, so profit starts above 50."

Professor: "That is the buyer's exercise threshold. The seller received a 2.50 premium, so the seller profits as long as the stock stays below 52.50."

## Flagged Ambiguities

| Ambiguity | Canonical recommendation |
|---|---|
| Mock answer key | Treat current answers as inferred until official solutions are supplied. |
| "Correct without limitations" | Reject statements with words like always, never, or mechanically true if assumptions are missing. |
| "Beginning of second year" | Count remaining study years after loan receipt, not full degree length. |
| "Interest rate risk" in zero bonds | For this MCQ route, emphasize reinvestment risk avoidance; default risk remains. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Rounding early to match an option. | Keep exact intermediate results and round only at the end. |
| Choosing highest IRR for mutually exclusive projects. | Use NPV as the master rule. |
| Confusing EBIT with net income. | Add interest back to net income if no tax information is involved in coverage setup. |
| Forgetting annuity-due timing. | Multiply ordinary annuity factor by `(1+i)`. |
| Treating option exercise threshold as profit threshold. | Include premium in break-even. |

## Cheat-Sheet Language

```text
Mock exam route:
1. Identify topic.
2. Write the one formula or concept test.
3. Keep full precision.
4. Match the option only after the calculation.
5. If wording says always/never, test assumptions before choosing it.
```

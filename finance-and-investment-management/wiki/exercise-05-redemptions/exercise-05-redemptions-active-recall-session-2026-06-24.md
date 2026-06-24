# Exercise 05 Redemptions: Clarification Session 2026-06-24

Linked source notes:

- [Exercise 05: Redemptions](exercise-05-redemptions.md)
- [Redemptions To Capital Budgeting Bridge](redemptions-to-capital-budgeting-bridge.md)
- [Exercise 03-04: Annuities](../exercise-03-04-annuities/exercise-03-04-annuities.md)
- [Session 05-06: Capital Budgeting](../session-05-06-capital-budgeting/session-05-06-capital-budgeting.md)

Status: clarification saved 2026-06-24; first active recall remains pending.

## Clarification Prompts And User Wording

### Prompt 1

User asked whether WACC is mainly driven by the redemption process, because financing repayment and loan planning affect project attractiveness and NPV.

Feedback:

- Corrected the direction: redemption is not the main driver of WACC.
- WACC is driven by debt/equity weights, cost of debt, cost of equity, tax effects, and risk.
- Redemption models the proposed loan schedule after a financing structure is chosen.

Refined mental model:

```text
WACC affects project NPV.
Redemption affects financing feasibility.
Redemption does not normally feed directly into project FCF under WACC.
```

### Prompt 2

User asked why the financing mechanism does not affect NPV if a high-NPV project cannot proceed without a promising financing plan.

Feedback:

- Clarified that project NPV is the operating value test, not the implementation-feasibility test.
- A positive-NPV project can be economically attractive but infeasible under a specific debt schedule.
- The correct response is often to redesign financing before rejecting the project itself.

Refined mental model:

```text
Positive NPV + feasible financing = proceed.
Positive NPV + infeasible financing = restructure, delay, scale down, or reject because of constraints.
Negative NPV + easy financing = still reject economically.
```

### Prompt 3

User asked how grace periods or payment-free periods occur in real financing and identified two variants: interest paid during grace, or interest compounded on top of the base loan.

Feedback:

- Confirmed the two main commercial variants.
- Interest-paid grace keeps the debt balance constant.
- Capitalized-interest grace adds unpaid interest to the balance.

Refined mental model:

```text
Interest-only grace:
cash payment during grace = interest
loan balance after grace = original debt

Capitalized-interest grace:
cash payment during grace = 0
loan balance after grace = original debt x q^g
```

### Prompt 4

User asked whether the grace-period treatment impacts the annuity payment and requested a triangular flow among Capital Budgeting, Redemptions, and Annuities.

Feedback:

- Confirmed that the grace period directly affects the later annuity if repayment is structured as annuity repayment.
- Grace changes the repayment base.
- Annuity formulas calculate the equal payment based on that repayment base.

Refined triangle:

```text
Capital Budgeting = operating FCF + WACC -> project NPV.
Redemptions       = loan amount + rate + grace + maturity -> debt-service schedule.
Annuities         = formula tool inside Redemptions -> equal payment or PV of payments.
```

### Prompt 5

User asked how "If interest is capitalized, later annuity payments become higher" actually occurs.

Feedback:

- The annuity formula is unchanged.
- The input debt balance is higher because unpaid interest was added to principal.

Worked example:

```text
D0 = 70,000
r = 6%
g = 5 years
N = 10 payments

Interest paid during grace:
repayment base = 70,000
A = 9,510.76

Interest capitalized during grace:
repayment base = 70,000 x 1.06^5 = 93,675.79
A = 12,727.54
```

### Prompt 6

User asked whether annuity-due and annuity-immediate also have an impact.

Feedback:

- Yes. They define payment timing.
- Annuity-immediate pays at period end.
- Annuity-due pays at period beginning.
- For the same loan balance, annuity-due has a lower equal payment, but the first payment occurs earlier.

Refined mental model:

```text
Grace period changes the repayment base.
Annuity-due/immediate changes the timing factor.
```

### Prompt 7

User asked whether annuity-due or annuity-immediate affects PV or NPV.

Feedback:

- Timing affects PV whenever that annuity stream is being valued.
- For the same payment amount, annuity-due has higher PV than annuity-immediate.
- Under WACC project NPV, loan annuity payments stay outside operating FCF and are tested separately in Redemptions.

Refined mental model:

```text
Same payment:
PV_due = PV_immediate x (1 + r)

Same loan balance:
A_due = A_immediate / (1 + r)
```

### Prompt 8

User asked for the difference between PV and NPV.

Feedback:

- PV values future cash flows today.
- NPV measures value created after subtracting the investment or outflows.

Refined mental model:

```text
PV  = price tag of future benefits today.
NPV = value left after paying the investment ticket.
```

## Quality Labels

| Area | Label | Evidence |
|---|---|---|
| WACC versus redemption role | yellow -> improving | User initially connected redemption as WACC driver; corrected to WACC as valuation rate and redemption as feasibility schedule. |
| Financing feasibility versus project value | yellow -> improving | User correctly saw that implementation can block a project; needed boundary that this does not make operating NPV wrong. |
| Grace-period mechanics | green/yellow | User identified the two main variants; needed formula link to repayment base. |
| Annuity-due/immediate timing | yellow | User asked whether timing matters; needs one retrieval drill to lock same-payment vs same-loan distinction. |
| PV versus NPV | yellow | Definition now clear; needs application in mixed loan/project cases. |

## Next Recall Prompts

1. Explain why redemption is not the main driver of WACC.
2. A project has positive NPV but early debt payments exceed early FCF. What should management analyze before rejecting the project?
3. A EUR 70,000 loan has five grace years at 6%. Calculate the repayment base if interest is paid during grace and if interest is capitalized.
4. For the same loan balance, why is annuity-due lower than annuity-immediate?
5. State the difference between PV and NPV using one loan example and one project example.

## File Updates Made

- Expanded the Redemptions note with grace-period repayment-base logic, annuity-due/immediate impact, and PV versus NPV bridge.
- Updated the Redemptions `CONTEXT.md` with canonical terms and traps.
- Updated the Redemptions-to-Capital-Budgeting bridge with the triangular flow.
- Updated the Annuities `CONTEXT.md` with the redemption bridge.
- Updated the Capital Budgeting `CONTEXT.md` with the PV/NPV boundary.

# Finance 01-02 Active Recall Session - 2026-05-24

Primary source note: `session-01-02-financial-analysis.md`
Related source notes:

- `../session-01-02-excursus-fundamental-analysis-german-stock-market/session-01-02-excursus-fundamental-analysis-german-stock-market.md`
- `../exercise-01-02-interest-calculation/exercise-01-02-interest-calculation.md`

Course: Finance and Investment Management
Session mode: case-driven active recall
Scope boundary: Session 01-02 Financial Analysis, Session 01-02 Fundamental Analysis excursus, and Exercise 01-02 Interest Calculation only. Session 03-04 Investment Analysis topics such as NPV, IRR, payback, profitability index, and mutually exclusive projects were explicitly excluded for this session.

## Outcome

Status: completed
Quality: yellow-green

The user can distinguish valuation signals from financial-health signals, map basic financial statement information to the correct statement, select core ratios, apply DuPont logic, calculate market value and enterprise value, and solve basic interest problems. Remaining weak spots are arithmetic accuracy, formula notation, distinguishing growth factor from interest rate, and choosing the correct compounding convention.

## Recall Prompts And Raw Answers

### Case 1: Cheap Stock Or Value Trap

Prompt: Company A has market value of equity EUR 200m, book value of equity EUR 400m, F-Score 2, and unexplained borrowing. Company B has market value of equity EUR 600m, book value of equity EUR 400m, F-Score 8, and improving operating cash flow/profitability. Questions: calculate M/B for A and B; identify the value stock; explain why A may be a value trap; explain what F-Score adds; choose which company to investigate.

User answer: "A : 0.5, B: 0.667. A, due to lower M/B. It has a f score of 2, which means low financial health, better to check the fundamentals carefully before decision. financial health of the company. B, due to higher f score rate compared to the M/B difference"

Feedback: A was correct at 0.5. B should be 600/400 = 1.5, not 0.667. Interpretation was correct: low M/B plus low F-Score and unexplained borrowing can indicate a value trap; F-Score adds financial health beyond valuation.

### Case 2: Low M/B With Contradictory Signals

Prompt: Company C and Company D both have market value EUR 300m and book value EUR 600m. C has F-Score 8, positive operating cash flow, lower leverage, and improving profitability. D has F-Score 1, negative operating cash flow, rising leverage, and deteriorating margins. Questions: calculate M/B; classify by M/B alone; explain why F-Score changes interpretation; identify value opportunity and value trap.

User answer: "C: 0.5, B : 0.5. They are equal in terms of valuation. even though the valuations are equal, the financial health takes the importance of potenital growth and condition of the firms that will impact their valuation in long term. C with higher f score. D"

Feedback: Correct, except the second label should be D, not B. Both are equally cheap by M/B, but C looks like the value opportunity and D like the value trap because F-Score separates financial strength from distress.

### Case 3: Financial Statement Diagnosis

Prompt: A company reports strong revenue growth, positive net income, negative cash from operations, large increases in inventory and accounts receivable, and higher short-term debt due within one year. Questions: which statement shows revenue/net income; which statement shows cash from operations; why can a profitable company still face liquidity pressure; which balance-sheet items explain why profit did not become cash; is short-term debt automatically financial distress?

User answer: "income statement. cash flow statement. cash from operations are negative and the short term debt increase. inventorry and receivables increased? for the short term solvecny, better to check the liquidity ratios, the quick ratio becomes higher as the cash and receivables are increased compared to current liabilities"

Feedback: Correct statement mapping and correct inventory/receivables identification. Correction: negative cash flow and short-term debt are symptoms; the mechanism is that profit is accrual-based while cash is affected by collection and payment timing. Do not assume quick ratio rises; current liabilities also rose, so calculate liquidity ratios before concluding.

### Case 4: Ratio Selection

Prompt: Match CFO questions to ratios: A. "How much of each euro of sales becomes net income?" B. "Can we cover short-term liabilities with liquid assets?" C. "How many times can operating income cover interest expense?" D. "Are we using debt heavily relative to equity?" Ratios: net profit margin, quick ratio, EBIT interest coverage, debt-equity ratio.

User answer: "A, part of financial ratios to measure the net income per sales. B, part of liquidity ratio to measure short term inflows rate over current libailities. c, measures how safe is the investments coverage based on interests paid. D, measures the ratio of debts over equities"

Feedback: Correct matches. Correction: EBIT interest coverage measures how many times operating income covers interest expense, not investment coverage.

### Case 5: DuPont Decomposition

Prompt: Two firms have the same ROE of 15%. Firm X has high net profit margin, low asset turnover, low equity multiplier. Firm Y has low net profit margin, high asset turnover, high equity multiplier. Questions: write DuPont identity; explain net profit margin, asset turnover, equity multiplier; explain why same ROE can hide different business models or risk profiles.

User answer: "Firm x have profit driven ROE whereas the company Y have broader sales and asset coverage and less profitability. gives how much profit per sales. how much sales per assets. shows leverage. they might belong to different industries that have different oerational and financial dynamics"

Feedback: Interpretation was good, but the formula was missing. DuPont identity is `ROE = Net Profit Margin x Asset Turnover x Equity Multiplier = (Net Income/Sales) x (Sales/Total Assets) x (Total Assets/Book Equity)`.

### Case 6: Market Value Vs Enterprise Value

Prompt: Share price EUR 20, shares outstanding 10m, total debt EUR 80m, cash EUR 30m, EBIT EUR 25m. Questions: calculate market value of equity, net debt, enterprise value, EV/EBIT, and conceptual difference between market value of equity and enterprise value.

User answer: "20 * 10 million = 200 million. 80 - 30 = 50 million. 200 + 50 = 250 million. (200 + 80 - 30) / 25 = 10. enterpirse value ads the debt and excludes the cash from market value of equity"

Feedback: Correct. Refinement: market value of equity belongs to shareholders; enterprise value measures operating business value available to debt and equity providers.

### Case 7: Present Value With Monthly Interest

Prompt: You need EUR 1,000 in 18 months. Bank pays monthly interest of 0.35%. Questions: present or future value; monthly growth factor; number of periods; setup for amount to invest today; should answer be less or greater than EUR 1,000?

User answer: "present value. intrest rate ? 18. 1000/(1 + 0.0035)^ 18 =939 eur. less, because it asks for the present value of the money for the 18 months later to be 1000 eur"

Feedback: Correct after restart. Monthly growth factor is `1.0035`, not just the interest rate. Setup and interpretation were correct.

### Case 8: Nominal Vs Effective Annual Rate

Prompt: A bank advertises 12% nominal annual interest compounded monthly. Questions: monthly rate; effective annual rate formula; compare effective rate to 12%; why monthly compounding changes effective rate.

User answer: "%1. (1 + 12/12)^12. must be higher than 12 since compounding. due to reinvestment continously of the interest gains"

Feedback: Correct concept. Formula notation needed correction: use `r_eff = (1 + 0.12/12)^12 - 1 = 12.68%`. Monthly compounding is not continuous compounding.

### Case 9: Simple Vs Compound Interest

Prompt: Invest EUR 3,000 for 12 years and receive EUR 5,000 at the end under simple interest. Questions: formula; setup; annual simple interest rate; why compound answer differs.

User answer: "(5000/3000 -1) / 12 - simple interest rate formula. (5000/3000 -1) / 12. 13,90. compound makes the euqtion exponential therefore less rate is sufficient for compounding."

Feedback: Formula and intuition were right; arithmetic was wrong. Correct result: `(5000/3000 - 1)/12 = 5.56%`.

### Case 10: Continuous Compounding

Prompt: Invest EUR 3,000 for two years at a continuously compounded annual rate of 4%. Questions: formula; setup; compare to ordinary annual compounding; explain why.

User answer: "C_n = C_0 x (1 + r)^n = C_0 x q^n. 3000 * (1+ 0.04) ^2 = 3024. for simple rate it makes 3002 compound pprevails. compound interest adds the gains to the value every year"

Feedback: The annual compound formula was used instead of continuous compounding. Correct formula: `C_n = C_0 x e^(r x n)`. Correct setup: `3000 x e^(0.04 x 2) = 3249.86`. Annual compounding is `3000 x 1.04^2 = 3244.80`, not 3024.

### Final Mixed Mini-Case

Prompt: A firm has sales EUR 1,000, net income EUR 80, total assets EUR 500, book equity EUR 250, cash EUR 40, accounts receivable EUR 60, inventory EUR 100, current liabilities EUR 120. Questions: calculate net profit margin, asset turnover, equity multiplier, ROE using DuPont, quick ratio, and explain the difference between DuPont logic and quick-ratio logic.

User answer: "80 / 1000 = 0.08. 1000/ 500 = 2. 500/250 = 2. 0.08 * 2 * 2 = 0.32. (40 + 60) / 120 = 0.8. quick ratio is used to mesaure the liquidity strength whereas the dupont logic demonstrates the operational returns"

Feedback: Correct. Add units: net profit margin = 8%, asset turnover = 2.0x, equity multiplier = 2.0x, ROE = 32%, quick ratio = 0.83x. DuPont explains profitability/efficiency/leverage drivers of ROE; quick ratio explains short-term liquidity.

## Refined Mental Models

- M/B says how cheap or expensive equity looks relative to book equity; F-Score checks whether the firm is financially healthy or a value trap.
- Profit is not cash. Receivables, inventory, capex, and debt timing can create liquidity pressure even with positive net income.
- Ratio selection starts from the question: profitability, liquidity, interest coverage, leverage, valuation, or operating return.
- DuPont decomposes ROE into margin, asset efficiency, and leverage; same ROE can hide very different risk profiles.
- Interest exercises start with timing: future value moves money forward; present value moves money backward.
- Nominal, effective, intra-year, annual compound, simple, and continuous compounding are different conventions; choose the formula before calculating.

## Weak Spots

| Weak Spot | Quality | Correction |
|---|---|---|
| M/B denominator direction | yellow | Use `Market Value of Equity / Book Value of Equity`; do not invert it. |
| Quick-ratio interpretation | yellow | Calculate before concluding; rising receivables can help quick assets, but rising current liabilities can offset it. |
| DuPont formula recall | yellow | State formula before interpretation: margin x turnover x equity multiplier. |
| Growth factor vs interest rate | yellow | Growth factor is `1 + r`; the rate alone is not the multiplier. |
| Effective annual rate notation | yellow | Use decimal rates and subtract 1: `(1 + r/m)^m - 1`. |
| Simple-interest arithmetic | yellow | Formula was correct; recompute carefully before stating percentage. |
| Continuous compounding formula | red-yellow | Use `e^(r x n)`, not `(1+r)^n`; annual compounding and continuous compounding are separate cases. |

## Next Recall Prompts

1. Recalculate M/B for three companies and classify value stock vs growth stock vs value trap using F-Score.
2. Given a short financial-statement story, identify income statement, balance sheet, and cash-flow-statement signals.
3. Rebuild DuPont from memory and explain whether ROE is margin-driven, efficiency-driven, or leverage-driven.
4. Solve one simple interest, one monthly compounding, and one continuous compounding problem without mixing formulas.

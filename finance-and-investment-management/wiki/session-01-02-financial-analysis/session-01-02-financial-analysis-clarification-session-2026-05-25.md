# Finance 01-02 Clarification Session - 2026-05-25

Primary source note: `session-01-02-financial-analysis.md`
Related source notes:

- `../session-01-02-excursus-fundamental-analysis-german-stock-market/session-01-02-excursus-fundamental-analysis-german-stock-market.md`
- `../session-01-02-excursus-fundamental-analysis-german-stock-market/CONTEXT.md`
- `../exercise-01-02-interest-calculation/exercise-01-02-interest-calculation.md`

Course: Finance and Investment Management
Session mode: clarification and understanding repair
Scope boundary: Session 01-02 Financial Analysis and the valuation/F-Score logic from the Session 01-02 Fundamental Analysis excursus. Exercise 01-02 interest calculation was not reworked in this clarification session and remains for the next session.

## Outcome

Status: completed
Quality: green

The user reported greater confidence with Session 01-02 Financial Analysis after clarifying how statements, ratios, return measures, valuation multiples, and F-Score connect to real decision-making. The main improvement was moving from "calculate the metric" to "explain what decision the metric supports and what it cannot prove alone."

## Clarification Questions And Answers

### Question 1: Financial Statements And Decision Flow

User question: "where under which conditions we check balance sheet, income statement and cash flow statements and how the decision making process actually emerges out of them"

Professor explanation:

- Use the **income statement** when the question is about sales, costs, margins, EBIT, net income, and earning power over a period.
- Use the **balance sheet** when the question is about assets, liabilities, cash, receivables, inventory, debt, equity, liquidity position, and capital structure at one date.
- Use the **cash flow statement** when the question is about real cash movement, cash from operations, investment spending, borrowing, repayment, and whether accounting profit becomes cash.

Refined mental model:

```text
Income statement = performance engine
Balance sheet = financial position
Cash flow statement = cash reality check
```

Decision rule: start from the decision question, then choose the statement. A profitable company can still face liquidity pressure if receivables, inventory, capex, or debt timing prevent profit from turning into cash.

### Question 2: Ratio Evaluation By Perspective

User question: "lets dive into the details of ratios, how they impact the evaluation of the comapny form different perspectives like investor or manager or CFO etc."

Professor explanation:

- **Profitability ratios** answer whether the business model produces profit from sales.
- **Liquidity ratios** answer whether the firm can meet short-term obligations.
- **Leverage ratios** answer how much financial risk comes from debt.
- **Interest coverage** answers whether operating income can pay the interest bill.
- **Asset turnover** answers whether assets are used efficiently to generate sales.
- **Return ratios** answer whether capital or equity produces adequate return.
- **Valuation ratios** answer whether the market price is cheap or expensive relative to fundamentals.

Refined mental model:

```text
Investor: buy, hold, or sell?
CFO: finance, survive, and create value?
Manager: which operating lever should improve?
Bank/lender: can the firm repay debt?
```

Correction rule: never calculate a ratio and stop. State what it measures, who uses it, what decision it supports, and what extra information is needed.

### Question 3: Comprehensive Company Use Cases

User question: "given that, give me some comprehensive company use cases that evaluates all the ratios based on the conditions from same and different sectors with given values"

Professor explanation:

Same-sector comparison is stronger for ranking operating quality because the business models are similar. Example: two apparel retailers can be compared on margins, liquidity, asset turnover, debt, ROE, P/E, and M/B more directly.

Different-sector comparison is useful for understanding business-model structure but dangerous for simple ranking. Example: software naturally has high margins and high M/B because intangibles and growth matter; supermarkets naturally have low margins and high asset turnover because they sell high volume at low margin.

Refined mental model:

```text
Same sector: which firm performs better?
Different sector: how do business models differ?
```

Exam trap: do not call a supermarket weak only because its margin is lower than a software firm's. Compare ratios against sector economics.

### Question 4: ROIC Versus ROE

User question: "I also want a distinction to use ROIC and ROE how they actually differ for diffferent authorities for decision making?"

Professor explanation:

```text
ROIC = EBIT x (1 - Tax Rate) / (Book Equity + Net Debt)
ROE = Net Income / Book Equity
```

- **ROIC** asks whether the operating business creates value from capital invested by both debt and equity providers.
- **ROE** asks how much profit shareholders earn on accounting equity.

Decision use:

- CFO and management use **ROIC** to judge operating capital productivity and project/business-unit quality.
- Investors use **ROIC** to detect high-quality operating economics.
- Shareholders and equity analysts use **ROE** to judge return on book equity.
- CFOs use **ROE** with DuPont to see whether shareholder return is operating-driven or leverage-driven.

Refined mental model: ROIC asks whether the restaurant itself is good at turning kitchen, equipment, rent, staff, and capital into operating profit. ROE asks what return the owner earns on the owner's book equity. Debt can amplify ROE without improving the restaurant's operating quality.

### Question 5: P/E Versus M/B

User question: "and also the difference of P/E and M/B for valuation interpretetion"

Professor explanation:

```text
P/E = Market Capitalization / Net Income
M/B = Market Value of Equity / Book Value of Equity
```

- **P/E** prices current earnings. It asks how much investors pay for one euro of net income.
- **M/B** prices accounting equity. It asks how market value compares with book equity.

Decision use:

- Use **P/E** for profitable firms with meaningful recurring earnings.
- Use **M/B** for value/growth classification and asset-heavy or financial firms.
- Low P/E or low M/B can mean cheapness, but also risk, distress, declining expectations, or a value trap.

Refined mental model:

```text
P/E = market price relative to earnings power
M/B = market price relative to accounting equity
```

### Question 6: Wiring F-Score Into Valuation

User question: "how do you wire the f score within this context to strengthening the evaluation interpretation and direction?"

Professor explanation:

F-Score is a quality filter, not a valuation ratio.

```text
P/E and M/B ask: Is the market price cheap or expensive?
F-Score asks: Is the company financially healthy enough for cheapness to be believable?
```

Interpretation matrix:

| Valuation | F-Score | Interpretation |
|---|---:|---|
| Low M/B or low P/E | High | Possible value opportunity. |
| Low M/B or low P/E | Low | Possible value trap. |
| High M/B or high P/E | High | Quality/growth candidate, but check overvaluation. |
| High M/B or high P/E | Low | Expensive and weak; dangerous without turnaround evidence. |

Refined mental model: M/B or P/E is the price tag on a used car. F-Score is the inspection report. A low price is attractive only if the financial engine is healthy.

## Weak Spots And Current Status

| Weak Spot | Quality | Correction |
|---|---|---|
| Linking statements to decisions | green | Start from the question: profit -> income statement; position/liquidity -> balance sheet; cash quality -> cash flow statement. |
| Ratio interpretation by user perspective | green | Explain the decision-maker: investor, CFO, manager, lender, or analyst. |
| ROIC versus ROE | green-yellow | ROIC = operating-quality lens; ROE = shareholder-return lens affected by leverage. |
| P/E versus M/B | green-yellow | P/E prices earnings; M/B prices accounting equity. Neither proves attractiveness alone. |
| F-Score wiring | green | Use it after valuation as a quality filter for value opportunity versus value trap. |

## Wiki Updates Made

- Added decision-use statement logic to `session-01-02-financial-analysis.md`.
- Added ratio interpretation by investor, CFO, manager, lender, and analyst perspective.
- Added ROIC versus ROE distinction and P/E versus M/B interpretation.
- Added same-sector and different-sector mini-cases.
- Refreshed `CONTEXT.md` for financial analysis with decision-use terminology and exam-trap corrections.
- Added F-Score quality-filter logic to the excursus note and context file.

## Next Recall Prompts

1. Given a company story with profit, rising receivables, and negative operating cash flow, identify which statement reveals each signal and state the decision implication.
2. Explain ROIC versus ROE using one leveraged-company example.
3. Given low M/B, low P/E, and F-Score data, classify value opportunity versus value trap.
4. Compare a software company and supermarket using margins, asset turnover, P/E, and M/B without making a cross-sector ranking error.

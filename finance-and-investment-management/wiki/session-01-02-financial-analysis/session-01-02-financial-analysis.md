# Session 01-02: Financial Analysis

Source file: `finance-and-investment-management/raw/IuF_0102_SS2026_Introduction_Financial_Analysis.pdf`  
Lecture folder: `finance-and-investment-management/`  
Date processed: 2026-05-16

## High-Yield 80/20 Summary

Financial analysis turns accounting reports into economic signals about a firm's profitability, liquidity, leverage, valuation, and operating performance. The exam is likely to test whether you can identify which statement contains which information, calculate ratios, interpret them, and avoid confusing book values with market values.

The core logic is:

1. Balance sheet = financial position at one point in time.
2. Income statement = performance over a period.
3. Cash flow statement = sources and uses of cash over a period.
4. Ratios = standardized measures that make firms comparable over time and against peers.
5. DuPont identity = ROE decomposition into profit margin, asset turnover, and leverage.

## Core Statements

### Financial Statements

Financial statements are firm-issued accounting reports about past performance. They inform shareholders and stakeholders and are prepared under accounting rules such as GAAP or IFRS.

Main statements:

- Balance sheet / statement of financial position.
- Income statement.
- Statement of cash flows.
- Statement of changes in shareholders' equity.

### Balance Sheet

The balance sheet is a snapshot of assets, liabilities, and shareholders' equity at a specific date.

```text
Assets = Liabilities + Shareholders' Equity
```

Interpretation:

- Assets = what the company owns.
- Liabilities = what the company owes.
- Shareholders' equity = accounting residual claim.

Current assets are expected to become cash within one year. Examples: cash, marketable securities, accounts receivable, inventories, prepaid expenses.

Non-current assets support long-term operations. Examples: PPE, goodwill, intangible assets, other long-term assets.

Current liabilities are due within one year. Examples: accounts payable, short-term debt, current maturities of long-term debt, taxes payable, wages payable.

Non-current liabilities are due after one year. Examples: long-term debt, leases, deferred taxes.

```text
Net Working Capital = Current Assets - Current Liabilities
```

### Book Equity vs Market Equity

```text
Book Value of Equity = Book Value of Assets - Book Value of Liabilities
Market Value of Equity = Share Price x Shares Outstanding
Market-to-Book Ratio = Market Value of Equity / Book Value of Equity
```

Book equity can be negative; market equity cannot be negative. Market value usually differs from book value because accounting does not fully capture intangible assets, growth expectations, brand, technology, network effects, or future profitability.

Exam trap: do not use book equity when the question asks for market capitalization.

### Enterprise Value

Enterprise value measures the value of the operating business, independent of cash/debt financing mix.

```text
Enterprise Value = Market Value of Equity + Debt - Cash
Enterprise Value = Market Value of Equity + Net Debt
Net Debt = Total Debt - Cash and Short-Term Investments
```

Exam trap: equity value belongs to shareholders; enterprise value belongs to all capital providers and captures operating assets.

### Income Statement

The income statement records revenues, expenses, and profit over a period.

Typical structure:

```text
Revenue / Sales
- COGS
= Gross Profit
- SG&A
- Depreciation and Amortization
= Operating Income
+/- Other Income / Expenses
= EBIT
+/- Interest Income / Expense
= Pre-Tax Income
- Taxes
= Net Income
```

```text
EPS = Net Income / Shares Outstanding
```

Diluted EPS adjusts for possible future dilution from in-the-money stock options, convertible bonds, or warrants.

### Statement Of Cash Flows

The cash flow statement records sources and uses of cash over a period. It is derived from the income statement and balance-sheet changes.

Three sections:

- Operating activities.
- Investing activities.
- Financing activities.

Exam trap: profit is not cash. A profitable firm can have liquidity pressure if cash collection, inventory, capex, or debt maturity timing is unfavorable.

## Financial Ratios

### Profitability Ratios

```text
Gross Margin = Gross Profit / Sales
Operating Margin = Operating Income / Sales
EBIT Margin = EBIT / Sales
Net Profit Margin = Net Income / Sales
```

Use: measure how much of sales remains after different cost layers.

### Liquidity Ratios

```text
Current Ratio = Current Assets / Current Liabilities
Quick Ratio = (Cash + Short-Term Investments + Accounts Receivable) / Current Liabilities
Cash Ratio = Cash / Current Liabilities
```

Use: short-term solvency. Quick ratio excludes inventory because inventory may not convert into cash quickly or reliably.

### Interest Coverage

```text
EBIT Interest Coverage = EBIT / Interest Expense
EBITDA Interest Coverage = EBITDA / Interest Expense
```

Interpretation: higher coverage means more ability to meet interest obligations. The slides flag high-quality borrowers as above about 5x EBIT coverage and low-quality borrowers as below about 1.5x.

### Leverage / Gearing

```text
Debt-Equity Ratio = Total Debt / Total Equity
Debt-to-Capital Ratio = Total Debt / (Total Equity + Total Debt)
Debt-to-EV Ratio = Net Debt / (Market Value + Net Debt)
Equity Multiplier = Total Assets / Book Value of Equity
```

Exam trap: leverage can be measured using book or market values. Read the denominator carefully.

### Valuation Ratios

```text
P/E Ratio = Market Capitalization / Net Income = Share Price / EPS
EV/EBIT = (Market Value of Equity + Debt - Cash) / EBIT
EV/Sales = (Market Value of Equity + Debt - Cash) / Sales
```

Use: compare firm valuations within the same industry. Cross-industry comparison can mislead because margins, growth, asset intensity, and risk differ.

### Operating Return Ratios

```text
ROE = Net Income / Book Value of Equity
ROA = (Net Income + Interest Expense) / Total Assets
ROIC = EBIT x (1 - Tax Rate) / (Book Value of Equity + Net Debt)
Asset Turnover = Sales / Total Assets
```

ROIC is central because it evaluates returns on capital invested in operations, not only returns to equity holders.

## DuPont Identity

```text
ROE = (Net Income / Sales) x (Sales / Total Assets) x (Total Assets / Book Value of Equity)
ROE = Net Profit Margin x Asset Turnover x Equity Multiplier
```

Interpretation:

- Profitability: how much profit per euro of sales.
- Asset efficiency: how much sales per euro of assets.
- Leverage: how much assets are financed per euro of equity.

Example from slides:

| Firm | Net Profit Margin | Asset Turnover | Equity Multiplier | ROE |
|---|---:|---:|---:|---:|
| Yahoo! | 21.04% | 0.337 | 1.18 | 8.34% |
| Google | 25.69% | 0.522 | 1.25 | 16.75% |

Google's superior ROE came from all three components: higher profitability, higher asset efficiency, and slightly higher leverage.

## Netflix Case Logic

The Netflix case trains reading financial statements as evidence, not only formulas.

Likely tested interpretations:

- Revenue growth driver in 2024: increased enforcement of password-sharing rules converting shared users into paying members.
- Liquidity position: about USD 7.81 billion cash and equivalents indicates strong liquidity.
- Short-term debt: debt maturities due within one year, not necessarily financial distress.
- Share repurchase: reduces shares outstanding and tends to increase EPS, all else equal.

Exam trap: a ratio can be true but not answer the question. For example, ROE does not explain the operational cause of revenue growth.

## Real-Life Interpretation

Imagine comparing Netflix and a manufacturing company. Netflix may have huge intangible content and platform value that does not appear cleanly as book equity. A factory-heavy manufacturer may have more PPE on the balance sheet. A naive comparison of book values can miss the economic value driver. That is why market value, enterprise value, profitability, asset turnover, and cash flows must be interpreted together.

## Decision-Use Logic: Which Statement To Check

Financial statement analysis starts from the decision question, not from a random ratio.

| Decision question | First statement to check | Why | Typical follow-up |
|---|---|---|---|
| Is the business profitable? | Income statement | Shows sales, cost layers, EBIT, and net income over a period. | Compare margins and ask whether profit is recurring. |
| Can the company pay near-term obligations? | Balance sheet | Shows cash, receivables, inventory, current liabilities, and short-term debt at one date. | Check quick ratio and cash flow from operations. |
| Is reported profit becoming real cash? | Cash flow statement | Shows cash from operations, investing, and financing. | Compare operating cash flow with net income. |
| Is the firm financially risky? | Balance sheet and income statement | Balance sheet shows debt burden; income statement shows interest coverage. | Ask whether leverage is supported by stable operating income. |
| Is the company cheap or expensive? | Market data plus income statement or balance sheet | P/E uses earnings; M/B uses book equity; EV multiples use operating value. | Add profitability, cash-flow, and quality checks before concluding. |

Mental model:

```text
Income statement = performance engine
Balance sheet = financial position
Cash flow statement = cash reality check
```

Example: a manufacturer can show positive net income on the income statement but negative operating cash flow because receivables and inventory rose on the balance sheet. The decision implication is not automatically "bad company"; it is "investigate cash conversion before lending, investing, or expanding."

## Ratio Interpretation By Decision Maker

Ratios are diagnostic instruments. A ratio becomes useful only when it answers a decision question.

| Ratio family | What it measures | Investor question | CFO question | Manager question | What it cannot prove alone |
|---|---|---|---|---|---|
| Profitability margins | Profit retained from sales after cost layers. | Is the business economically attractive? | Is there enough profit cushion for shocks, interest, reinvestment, and dividends? | Which cost layer needs improvement? | It does not prove cash collection or balance-sheet strength. |
| Liquidity ratios | Ability to meet short-term obligations. | Is there near-term financial stress? | Can we pay suppliers, wages, taxes, and short-term debt? | Are receivables or inventory tying up too much cash? | It does not prove long-term profitability. |
| Leverage ratios | Reliance on debt financing and risk amplification. | Is shareholder return debt-driven and risky? | Is the capital structure sustainable? | Do operating decisions need to be more conservative? | Debt is not automatically bad; stability and coverage matter. |
| Interest coverage | Ability of operating income to cover interest expense. | Is debt service manageable? | How much EBIT decline can we survive? | How much operational slack exists before financing pressure? | EBIT is not cash, so liquidity still matters. |
| Asset turnover | Sales generated per euro of assets. | Is the business asset-light or asset-heavy? | Can growth happen without heavy new investment? | Are stores, factories, inventory, or platforms used efficiently? | High turnover can come with low margins; compare within sector. |
| Return ratios | Return generated on capital or equity. | Does the firm generate attractive returns? | Are operations and capital structure creating value? | Which business units deserve more resources? | ROE can be inflated by leverage. |
| Valuation ratios | Market price relative to earnings, book equity, sales, or operating income. | Am I paying too much? | How does the market value our fundamentals? | Which operating levers could improve valuation? | Cheapness can be a value trap without quality checks. |

Exam answer rule:

```text
Do not calculate and stop.
Say what the ratio measures, whose decision it supports, and what extra evidence is needed.
```

## ROIC Versus ROE

```text
ROIC = EBIT x (1 - Tax Rate) / (Book Value of Equity + Net Debt)
ROE = Net Income / Book Value of Equity
```

Use **ROIC** when asking whether the operating business creates value from the capital invested in it. It is a cleaner operating-quality lens because it focuses on after-tax operating profit and capital supplied by both equity and debt providers.

Use **ROE** when asking how much return shareholders earn on book equity. It is useful for shareholder-return analysis, but it is affected by leverage because debt can reduce the equity base and amplify net income relative to equity.

| Situation | Interpretation |
|---|---|
| High ROIC and high ROE | Strong operations and attractive shareholder return. |
| Low ROIC and high ROE | ROE may be leverage-driven; investigate debt and DuPont equity multiplier. |
| High ROIC and moderate ROE | Operating business is strong; shareholder return may reflect conservative leverage or large equity base. |
| Low ROIC and low ROE | Weak operating economics and weak shareholder return. |

Analogy: ROIC asks whether the restaurant itself turns kitchen, staff, rent, and equipment into operating profit. ROE asks how much profit the owner earns on the owner's book equity. A heavily debt-financed restaurant can show high owner return in good years but also higher risk.

## P/E Versus M/B

```text
P/E = Market Capitalization / Net Income
M/B = Market Value of Equity / Book Value of Equity
```

Use **P/E** when asking how expensive the stock is relative to current earnings power. It works best for profitable firms with meaningful, recurring net income.

Use **M/B** when asking how the market values equity relative to accounting book equity. It is especially useful for value/growth classification and asset-heavy or financial firms, but it can miss intangible assets and future growth.

| Signal | Possible positive interpretation | Possible negative interpretation | Needed follow-up |
|---|---|---|---|
| Low P/E | Cheap relative to earnings. | Earnings may be temporary, declining, or risky. | Check margins, cash flow, leverage, and F-Score-style quality. |
| High P/E | Market expects growth or quality. | Overvaluation risk. | Check growth durability and ROIC. |
| Low M/B | Value candidate relative to book equity. | Distress, obsolete assets, weak profitability, or value trap. | Check F-Score, operating cash flow, leverage, and margins. |
| High M/B | Strong intangibles, growth, brand, technology, or expected profitability. | Overpriced relative to accounting base. | Check whether ROIC and earnings justify market expectations. |

## Compact Company Use Cases

### Same Sector: Two Apparel Retailers

| Ratio | UrbanWear | DiscountFit | Interpretation |
|---|---:|---:|---|
| Gross Margin | 40% | 25% | UrbanWear has stronger pricing power or lower product cost. |
| Net Profit Margin | 9% | 5% | UrbanWear converts sales into more profit. |
| Quick Ratio | 0.65x | 0.40x | DiscountFit depends more on selling inventory to meet short-term obligations. |
| Debt/Equity | 0.83x | 0.60x | UrbanWear uses more debt. |
| Interest Coverage | 7.5x | 8.0x | Both can cover interest; DiscountFit is slightly safer here. |
| Asset Turnover | 1.43x | 2.50x | DiscountFit uses assets more intensely to generate sales. |
| ROE | 30% | 25% | UrbanWear generates higher shareholder return. |
| P/E | 10.0x | 6.0x | DiscountFit is cheaper relative to earnings. |
| M/B | 3.0x | 1.5x | Market values UrbanWear's equity more highly relative to book. |

Decision: UrbanWear looks like the higher-quality company; DiscountFit looks cheaper but weaker. An investor should not buy DiscountFit only because P/E is lower. A manager at DiscountFit should focus on margins and inventory/liquidity pressure.

### Different Sectors: Software Versus Supermarket

| Ratio | CloudSoft | FoodMart | Interpretation |
|---|---:|---:|---|
| Gross Margin | 80% | 20% | Software has low marginal cost; supermarkets structurally have low product margins. |
| Net Profit Margin | 18% | 1.6% | CloudSoft keeps much more profit per euro of sales. |
| Quick Ratio | 2.20x | 0.20x | FoodMart liquidity is inventory-heavy. |
| Debt/Equity | 0.33x | 1.25x | FoodMart is more leveraged. |
| Interest Coverage | 24.0x | 3.0x | CloudSoft has much safer debt-service capacity. |
| Asset Turnover | 0.83x | 2.00x | FoodMart sells high volume through its asset base. |
| P/E | 30.0x | 11.25x | CloudSoft is more expensive relative to earnings. |
| M/B | 9.0x | 1.13x | CloudSoft's market value reflects intangibles and growth expectations. |

Decision: cross-sector comparison explains business-model differences more than it ranks quality. FoodMart is not automatically bad because margins are low; supermarkets typically earn low margins with high turnover. CloudSoft is not automatically attractive because margins are high; valuation may already price in growth.

## Exam-Relevant Decision Rules

- If asked for short-term solvency, use liquidity ratios.
- If asked for debt burden, use leverage and interest coverage.
- If asked for shareholder return, use ROE.
- If asked for operating return independent of financing, use ROIC.
- If asked for valuation comparison, use P/E, EV/EBIT, EV/Sales, or M/B depending on the available data.
- If asked why ROE differs, decompose using DuPont.

## Common Mistakes

- Mixing book value and market value.
- Treating net income as cash flow.
- Using P/E across industries without adjustment.
- Forgetting that enterprise value subtracts cash.
- Interpreting high leverage as always bad; leverage increases risk but can also amplify ROE.
- Using inventory in quick ratio.
- Confusing short-term debt with total debt.

## Practice Questions

1. A company has 5 million shares at USD 22 per share and book equity of USD 50 million. Calculate market cap and M/B.
   - Answer: market cap = USD 110 million; M/B = 110/50 = 2.2.
2. A firm's current assets are 120, current liabilities 80, cash 20, receivables 30, inventory 70. Calculate current and quick ratios.
   - Answer: current ratio = 1.5; quick ratio = (20+30)/80 = 0.625.
3. Explain why two firms with the same ROE can still have different business quality.
   - Answer: ROE can come from margin, turnover, or leverage; high leverage-driven ROE is riskier than operation-driven ROE.
4. Why is EV/EBIT different from P/E?
   - Answer: EV/EBIT values the whole operating firm before interest; P/E values equity after interest and taxes.

## Mermaid Knowledge Map

```mermaid
graph TD
    Q[Decision Question] --> FS[Financial Statements]
    FS[Financial Statements] --> BS[Balance Sheet]
    FS --> IS[Income Statement]
    FS --> CF[Cash Flow Statement]
    Q -->|profit and margins| IS
    Q -->|position and liquidity| BS
    Q -->|cash quality| CF
    BS --> A[Assets]
    BS --> L[Liabilities]
    BS --> E[Book Equity]
    E --> MB[Market-to-Book]
    BS --> NWC[Net Working Capital]
    IS --> EPS[Earnings Per Share]
    CF --> CFO[Operating Cash Flow]
    CF --> CFI[Investing Cash Flow]
    CF --> CFF[Financing Cash Flow]
    FS --> RATIOS[Financial Ratios]
    RATIOS --> PROF[Profitability]
    RATIOS --> LIQ[Liquidity]
    RATIOS --> LEV[Leverage]
    RATIOS --> VAL[Valuation]
    RATIOS --> RET[Operating Returns]
    RET --> ROE[ROE]
    RET --> ROIC[ROIC]
    VAL --> PE[P/E]
    VAL --> EVEBIT[EV/EBIT]
    ROE --> DUPONT[DuPont Identity]
    DUPONT --> MARGIN[Net Profit Margin]
    DUPONT --> TURNOVER[Asset Turnover]
    DUPONT --> EM[Equity Multiplier]
```

## Subject Knowledge Graph

| Node | Meaning |
|---|---|
| Financial statements | Source reports for financial analysis |
| Balance sheet | Point-in-time position of assets, liabilities, equity |
| Income statement | Period performance from revenue to net income |
| Cash flow statement | Cash sources and uses |
| Ratio analysis | Standardized comparison tool |
| Enterprise value | Value of operating business |
| ROE | Return to book equity |
| ROIC | Operating return on invested capital |
| P/E | Market price relative to current earnings |
| M/B | Market price relative to book equity |
| DuPont identity | ROE decomposition |
| Liquidity | Short-term solvency |
| Leverage | Debt reliance and risk amplification |

| From | Relationship | To |
|---|---|---|
| Balance sheet | defines | Assets = Liabilities + Equity |
| Market value of equity | differs from | Book value of equity |
| Enterprise value | equals | Equity value plus net debt |
| Income statement | produces | Net income and EPS |
| Cash flow statement | explains | cash movement |
| Ratio analysis | compares | firms and periods |
| Decision question | selects | statement and ratio focus |
| DuPont identity | decomposes | ROE |
| ROIC | evaluates | operating capital productivity |
| ROE | can be amplified by | leverage |
| P/E | prices | earnings power |
| M/B | prices | accounting equity |
| Leverage | amplifies | ROE and risk |
| Liquidity ratios | measure | short-term solvency |
| Valuation ratios | support | market comparison |

## Links

- Related logistics: `finance-and-investment-management/wiki/_course-logistics.md`
- Related excursus: `finance-and-investment-management/wiki/session-01-02-excursus-fundamental-analysis-german-stock-market/session-01-02-excursus-fundamental-analysis-german-stock-market.md`

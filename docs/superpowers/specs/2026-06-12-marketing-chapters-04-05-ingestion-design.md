# Marketing Chapters 04-05 Ingestion Design

## Objective

Import `GM 2026 Chapter4.pdf` and `GM 2026 Chapter5.pdf` from the Downloads folder into the Marketing course workspace and convert them into durable, exam-ready study artifacts.

## Source Mapping

| Source | Topic | Pages | Destination |
|---|---|---:|---|
| `GM 2026 Chapter4.pdf` | Price | 75 | `marketing/raw/GM 2026 Chapter4.pdf` |
| `GM 2026 Chapter5.pdf` | Promotion/Communication | 89 | `marketing/raw/GM 2026 Chapter5.pdf` |

## Generated Topic Structure

Create:

- `marketing/wiki/chapter-04-price/chapter-04-price.md`
- `marketing/wiki/chapter-04-price/CONTEXT.md`
- `marketing/wiki/chapter-05-promotion-communication/chapter-05-promotion-communication.md`
- `marketing/wiki/chapter-05-promotion-communication/CONTEXT.md`

Each main note will follow the root Markdown standard: source metadata, 80/20 summary, mechanisms, formulas or decision rules, visual interpretation, managerial examples, exam traps, retrieval prompts, practice tasks, Mermaid map, and node/edge knowledge graph.

Each `CONTEXT.md` will define the chapter's canonical terminology, aliases to avoid, formula or metric intuition, relationships, examples, exam traps, and a precise example dialogue.

## Extraction And Visual Audit

1. Copy the original PDFs without modification.
2. Extract text with page boundaries using Poppler.
3. Render slide thumbnails or full-page images for pages whose meaning depends on charts, diagrams, screenshots, experimental conditions, or equations.
4. Use OCR only where embedded text extraction is incomplete.
5. Preserve research-paper findings as paraphrased examinable evidence, including study setup, result, implication, and limits when identifiable.

## Chapter Emphasis

### Chapter 04 Price

Prioritize behavioral pricing, willingness to pay, reference prices and fairness, compromise and decoy effects, pricing objectives and strategies, price differentiation, bundling, cost-oriented pricing, contribution margin and break-even logic, marginal analysis, and managerial pricing decisions.

### Chapter 05 Promotion/Communication

Prioritize the communication process, push versus pull, AIDA and advertising effects, promotional mix, integrated marketing communication, the 5Ms, communication goals, budgeting and media planning, message design, advertising and sales-promotion instruments, public relations, personal selling, digital/social communication, and effectiveness measurement.

## Integration

Update:

- `marketing/wiki/_course-knowledge-graph.md` with graph-first Chapter 04/05 relationships plus supporting node/edge references.
- `learning-system/review-dashboard.md` with two rows whose status is `first pass pending — note generated 2026-06-12`; all retrieval-date cells remain blank.
- `learning-system/weekly-calendar.md` so both chapters appear as prerequisite-aware future candidates after Chapters 01-03 and after the current repair queue. Neither new note becomes an overdue review.

## Verification

- Confirm all 164 pages are represented in extraction artifacts.
- Check image-heavy slides against rendered pages.
- Confirm every required note section exists and Markdown fences are balanced.
- Render all four Markdown files with Pandoc.
- Confirm Chapter 04 precedes Chapter 05 in the Marketing graph and study queue.
- Run `git diff --check`.

## Scope Boundaries

- Do not start active recall automatically.
- Do not set `First Pass` dates for either chapter.
- Do not fabricate unreadable chart values or research findings.
- Do not alter the existing Chapter 01-03 completion state.

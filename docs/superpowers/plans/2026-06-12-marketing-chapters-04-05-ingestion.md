# Marketing Chapters 04-05 Ingestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the 75-slide Price deck and 89-slide Promotion/Communication deck into complete Marketing study artifacts and register them without advancing active-recall dates.

**Architecture:** Original PDFs remain canonical under `marketing/raw/`. Page-delimited text extraction and rendered slide contact sheets provide the evidence layer; two same-slug topic folders provide the learning layer. The Marketing course graph and study-control files are updated only after the notes and context companions pass structural verification.

**Tech Stack:** Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`), Tesseract where needed, ImageMagick, Pandoc, Markdown, Mermaid, shell verification.

---

### Task 1: Preserve Sources And Build Extraction Evidence

**Files:**
- Copy: `/Users/ardaerkan/Downloads/GM 2026 Chapter4.pdf` -> `marketing/raw/GM 2026 Chapter4.pdf`
- Copy: `/Users/ardaerkan/Downloads/GM 2026 Chapter5.pdf` -> `marketing/raw/GM 2026 Chapter5.pdf`
- Create temporarily: `/tmp/marketing-ch04-pages.txt`
- Create temporarily: `/tmp/marketing-ch05-pages.txt`
- Create temporarily: `/tmp/marketing-ch04-slides/`
- Create temporarily: `/tmp/marketing-ch05-slides/`

- [ ] **Step 1: Copy the original PDFs**

Run:

```bash
cp '/Users/ardaerkan/Downloads/GM 2026 Chapter4.pdf' 'marketing/raw/GM 2026 Chapter4.pdf'
cp '/Users/ardaerkan/Downloads/GM 2026 Chapter5.pdf' 'marketing/raw/GM 2026 Chapter5.pdf'
```

- [ ] **Step 2: Verify byte-identical copies**

Run:

```bash
shasum -a 256 '/Users/ardaerkan/Downloads/GM 2026 Chapter4.pdf' 'marketing/raw/GM 2026 Chapter4.pdf'
shasum -a 256 '/Users/ardaerkan/Downloads/GM 2026 Chapter5.pdf' 'marketing/raw/GM 2026 Chapter5.pdf'
```

Expected: each source/destination pair has matching hashes.

- [ ] **Step 3: Extract page-delimited text**

Run `pdftotext -layout` for each PDF and preserve form-feed page boundaries in `/tmp`.

- [ ] **Step 4: Render every slide for visual audit**

Run `pdftoppm -jpeg -r 100` for all 75 and 89 pages.

- [ ] **Step 5: Generate contact sheets and inspect visual-heavy pages**

Use ImageMagick to create manageable contact sheets. Compare slide titles, chart labels, diagrams, experiments, equations, and screenshots against extracted text. OCR individual pages only where extraction misses material meaning.

### Task 2: Generate Chapter 04 Price Learning Artifacts

**Files:**
- Create: `marketing/wiki/chapter-04-price/chapter-04-price.md`
- Create: `marketing/wiki/chapter-04-price/CONTEXT.md`

- [ ] **Step 1: Build a complete page/topic inventory**

Identify all chapter sections, examples, papers, formulas, charts, and exercises from the 75 pages.

- [ ] **Step 2: Write the main note**

Cover the 80/20 summary, behavioral pricing, strategic and differentiated pricing, bundling, determination methods, formulas, examples, exam relevance, retrieval, practice, Mermaid map, and subject node/edge tables.

- [ ] **Step 3: Write the context companion**

Define canonical pricing language, formulas, decision relationships, examples, ambiguity corrections, and exam traps without duplicating the full note.

- [ ] **Step 4: Verify Chapter 04 structure and renderability**

Check required headings, balanced fences, internal links, and Pandoc output.

### Task 3: Generate Chapter 05 Promotion/Communication Learning Artifacts

**Files:**
- Create: `marketing/wiki/chapter-05-promotion-communication/chapter-05-promotion-communication.md`
- Create: `marketing/wiki/chapter-05-promotion-communication/CONTEXT.md`

- [ ] **Step 1: Build a complete page/topic inventory**

Identify all chapter sections, communication models, instruments, studies, campaigns, metrics, charts, and exercises from the 89 pages.

- [ ] **Step 2: Write the main note**

Cover communication logic, push/pull, effect models, 5Ms, promotional instruments, integrated communication, digital/social communication, effectiveness measurement, examples, exam relevance, retrieval, practice, Mermaid map, and subject node/edge tables.

- [ ] **Step 3: Write the context companion**

Define canonical communication language, metric intuition, relationships, examples, ambiguity corrections, and exam traps.

- [ ] **Step 4: Verify Chapter 05 structure and renderability**

Check required headings, balanced fences, internal links, and Pandoc output.

### Task 4: Integrate Marketing Knowledge And Study Control

**Files:**
- Modify: `marketing/wiki/_course-knowledge-graph.md`
- Modify: `learning-system/review-dashboard.md`
- Modify: `learning-system/weekly-calendar.md`

- [ ] **Step 1: Extend the Marketing graph**

Add Price and Promotion branches to the graph-first view, decision flow, subject index, and supporting references.

- [ ] **Step 2: Register both notes in the dashboard**

Add Chapter 04 and Chapter 05 rows with blank `First Pass` and `D+n` cells and status `first pass pending — note generated 2026-06-12`. Preserve Chapter 01 -> 02 -> 03 -> 04 -> 05 order.

- [ ] **Step 3: Refresh the weekly calendar**

Keep today's completed SCM item and current repair queue. Add Price only after Chapter 03 first pass, and Promotion only after Price first pass. Do not schedule either as an overdue review.

### Task 5: Final Verification

**Files:**
- Verify all files above.

- [ ] **Step 1: Verify sources and page counts**

Expected: Chapter 04 = 75 pages; Chapter 05 = 89 pages; copied hashes match downloads.

- [ ] **Step 2: Verify note/context structure**

Confirm required sections, Mermaid blocks, retrieval prompts, practice tasks, and context tables exist in all four artifacts.

- [ ] **Step 3: Render Markdown**

Run Pandoc on both notes, both context files, the graph, dashboard, and calendar.

- [ ] **Step 4: Verify scheduling semantics**

Confirm both new rows have blank completion cells, exact pending-first-pass language, and prerequisite ordering in the calendar.

- [ ] **Step 5: Run repository whitespace check**

Run:

```bash
git diff --check
```

Expected: exit 0.

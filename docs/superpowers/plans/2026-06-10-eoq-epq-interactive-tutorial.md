# EOQ And EPQ Interactive Tutorial Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone interactive EOQ/EPQ tutorial that reproduces all six Topic 05 wiki exercise workflows and a free-practice case with editable inputs and dynamic visuals.

**Architecture:** Keep the delivered tutorial in one self-contained HTML file with embedded CSS and JavaScript. Put pure calculation functions in a marked script block so a dependency-free Node test can extract and execute the same production formulas; keep DOM rendering, SVG generation, workflow presets, and validation separate from those functions.

**Tech Stack:** HTML5, CSS, vanilla JavaScript, inline SVG, Node 23 built-in `node:test`, `assert`, `fs`, and `vm`.

---

## File Structure

- Create `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`: standalone tutorial, styles, calculation functions, workflow data, renderers, charts, and embedded browser self-test status.
- Create `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`: extracts the marked calculation block, verifies all wiki preset results, validates error cases, and checks required HTML structure plus absence of external dependencies.
- Modify `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`: add a short link to the interactive tutorial under the source/companion area.

### Task 1: Formula Contract Tests

**Files:**
- Create: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`
- Test target: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`

- [ ] **Step 1: Write the failing extraction and EOQ tests**

Create a Node test that reads the target HTML, extracts code between `/* CALCULATION_CORE_START */` and `/* CALCULATION_CORE_END */`, evaluates it in `vm`, and asserts:

```js
assertClose(api.basicEoq({ demand: 9600, setupCost: 80, holdingCost: 6 }).quantity, 505.9644);
assertClose(api.basicEoq({ demand: 9600, setupCost: 80, holdingCost: 6 }).ordersPerPeriod, 18.9737);
assertClose(api.basicEoq({ demand: 9600, setupCost: 80, holdingCost: 6 }).averageInventory, 252.9822);
```

Add ABI, Tek Pak, and Kerosene expected results from the wiki answer guides.

- [ ] **Step 2: Run the test and verify RED**

Run:

```bash
node --test supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs
```

Expected: FAIL because the HTML file and calculation block do not exist.

- [ ] **Step 3: Add EPQ and validation contract tests**

Assert Battery, Router, and Shovel expected outputs within `0.02` display tolerance. Assert `epq()` throws or returns a structured invalid result when `productionRate <= demand` and positive-value validation rejects zero or negative demand, setup cost, and holding cost.

- [ ] **Step 4: Re-run and confirm the tests still fail for missing production code**

Expected: FAIL at HTML read/extraction, proving the tests precede implementation.

### Task 2: Minimal Calculation Core

**Files:**
- Create: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`

- [ ] **Step 1: Add the HTML shell and marked calculation block**

Define pure functions:

```js
basicEoq({ demand, setupCost, holdingCost })
eoqTiming({ demand, initialInventory, leadTime, periodsPerYear })
finiteHorizonEoq({ demand, setupCost, holdingCost, horizonPeriods, periodsPerYear })
epq({ demand, productionRate, setupCost, holdingCost, periodsPerYear })
warehousePooling({ warehouseCount, demandPerWarehouse, setupCost, holdingCost })
shovelTechnology({ productionRatePerPeriod, maximumInventory, currentBatch, improvementPercent, setupCost, holdingCost, previousCost, periodsPerYear })
```

Expose them as `globalThis.EOQ_EPQ_CALCULATIONS` inside the marked block.

- [ ] **Step 2: Run formula tests and verify GREEN**

Run the Node test. Expected: all formula and validation tests pass.

- [ ] **Step 3: Refactor shared validation and rounding-independent comparison**

Keep calculations at full precision. Use shared positive-number checks and preserve explicit operational status such as `prepareImmediately` for negative waiting times.

- [ ] **Step 4: Re-run tests**

Expected: all tests pass after refactoring.

### Task 3: HTML Structure And Dependency Tests

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`

- [ ] **Step 1: Add failing static structure assertions**

Require:

- `id="model-router"`
- `id="workflow-selector"`
- `id="input-panel"`
- `id="calculation-ladder"`
- `id="inventory-chart"`
- `id="cost-chart"`
- `id="interpretation-panel"`
- seven workflow buttons with the exact preset keys
- no `<script src=`, `<link rel="stylesheet"`, external image URLs, or `http://`/`https://` dependencies

- [ ] **Step 2: Run tests and verify RED**

Expected: formula tests pass while structure tests fail because the tutorial UI is incomplete.

- [ ] **Step 3: Implement semantic page structure and responsive styles**

Add the header, notation legend, router, EOQ/EPQ comparison, selector, editable inputs, calculation ladder, charts, interpretation panel, exam-trap panel, and self-test status region. Use accessible labels, fieldsets, visible focus, reduced-motion support, and a one-column mobile layout.

- [ ] **Step 4: Run tests and verify GREEN**

Expected: all formula and structure tests pass.

### Task 4: Interactive Workflow Rendering

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`

- [ ] **Step 1: Add failing preset-data assertions**

Extract `globalThis.EOQ_EPQ_PRESETS` from a marked data block and assert the keys:

```text
free-practice
abi-warehouses
tek-pak
kerosene
battery-cell
router-factory
shovel-factory
```

Assert their default inputs equal the wiki values.

- [ ] **Step 2: Run tests and verify RED**

Expected: FAIL because preset data has not been exposed.

- [ ] **Step 3: Implement workflow presets and UI dispatch**

Selecting a workflow must rebuild the input controls, calculate through the pure core, and render workflow-specific metrics, formula steps, interpretation, and traps. Input events must recalculate immediately; reset restores wiki defaults.

- [ ] **Step 4: Implement inline validation**

Show field-level and summary messages. Suppress charts and computed result cards while invalid. For Router timing, show `start preparation immediately` when the computed waiting time is below zero.

- [ ] **Step 5: Run tests and verify GREEN**

Expected: all tests pass, including preset values and validation contracts.

### Task 5: Dynamic SVG Visuals

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`

- [ ] **Step 1: Add failing renderer-presence tests**

Require named functions or markers for:

```text
renderEoqSawtooth
renderEpqTriangle
renderCostBars
renderCandidateBars
```

- [ ] **Step 2: Run tests and verify RED**

Expected: FAIL until renderers exist.

- [ ] **Step 3: Implement EOQ and EPQ inventory diagrams**

Generate inline SVG from calculated outputs. Label quantity, average or maximum inventory, cycle duration, production duration, and slopes. Include a text summary in the chart container.

- [ ] **Step 4: Implement workflow-specific cost diagrams**

Show setup versus holding cost for basic workflows, separate versus pooled cost for ABI, floor versus ceiling candidate costs for Kerosene, and benchmark/new cost comparisons for Battery and Shovel.

- [ ] **Step 5: Run tests and verify GREEN**

Expected: all static and formula tests pass.

### Task 6: Embedded Browser Self-Tests And Wiki Link

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs`

- [ ] **Step 1: Add failing assertions for self-test status and wiki link**

Require an embedded self-test runner that checks representative EOQ, finite-horizon, EPQ, and invalid-rate cases and writes a pass/fail count to `id="self-test-status"`. Require the topic note to link to `eoq-epq-interactive-tutorial.html`.

- [ ] **Step 2: Run tests and verify RED**

Expected: FAIL before the self-test runner and wiki link exist.

- [ ] **Step 3: Implement self-tests and link the artifact**

Run browser self-tests on load without interrupting use. Display `Checks passed: N/N` or a clear failure message. Add a companion-artifact link near the Topic 05 note metadata.

- [ ] **Step 4: Run tests and verify GREEN**

Expected: all tests pass.

### Task 7: Final Verification And Review

**Files:**
- Verify all files above.

- [ ] **Step 1: Run the complete automated test**

```bash
node --test supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.test.mjs
```

Expected: zero failures.

- [ ] **Step 2: Run static checks**

```bash
git diff --check
rg -n '<script[^>]+src=|<link[^>]+rel=["'"']stylesheet|https?://' supply-chain-management/wiki/topic-05-eoq-production-systems-batching/eoq-epq-interactive-tutorial.html
```

Expected: `git diff --check` succeeds and dependency scan returns no matches.

- [ ] **Step 3: Verify every spec requirement**

Check all seven workflows, editable controls, dynamic diagrams, calculation ladders, units, interpretations, exam traps, invalid-input behavior, accessibility attributes, responsive CSS, and the Topic 05 wiki link.

- [ ] **Step 4: Inspect the final diff**

Confirm only the tutorial, its test, the Topic 05 link, and plan-related artifacts changed for this feature. Preserve unrelated user changes in the worktree.


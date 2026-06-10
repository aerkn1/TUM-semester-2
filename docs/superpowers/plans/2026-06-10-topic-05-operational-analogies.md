# Topic 05 Operational Analogies Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the Topic 05 EOQ/EPQ note so every analogy, worked example, and practice task maps formulas to real products, assets, events, costs, timelines, and managerial actions.

**Architecture:** Edit only the Topic 05 wiki note. Add a repeatable learning structure around the existing formulas and results: operating story, asset dictionary, chronological workflow, preserved formula ladder, physical interpretation, managerial action, and exam trap. Verify the resulting Markdown structurally and independently recalculate every numeric example.

**Tech Stack:** Markdown, shell verification with `rg`, `awk`, `git diff --check`, and a dependency-free Node calculation check.

---

### Task 1: Create Structural Verification

**Files:**
- Create: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

- [ ] **Step 1: Write the failing structure test**

The test reads the Topic 05 Markdown and asserts:

- six `#### Operating Story` headings;
- six `#### Asset Dictionary` headings;
- six `#### Full Operational Workflow` headings;
- six `#### Managerial Decision` headings;
- six `#### Exam Trap` headings;
- expanded bakery headings for all six variants;
- five practice tasks containing `Operating setting`, `Asset mapping`, and `Exam-trap check`.

- [ ] **Step 2: Run the structure test and verify RED**

Run:

```bash
node --test supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs
```

Expected: FAIL because the standardized operational sections do not yet exist.

### Task 2: Expand Bakery Variants

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md:119-138`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`

- [ ] **Step 1: Replace the compact bakery table with six operational mini-workflows**

For Basic EOQ, Initial Inventory, Positive Lead Time, Initial Inventory Plus Lead Time, Finite Horizon, and EPQ, add:

- the physical flour asset;
- supplier, storeroom, bakery consumption, or mill production event;
- what changes;
- what stays unchanged;
- the managerial decision;
- the main confusion to avoid.

- [ ] **Step 2: Add one compact comparison timeline**

Show instant delivery, lead-time ordering, finite event deliveries, and gradual production using ASCII arrows.

- [ ] **Step 3: Run the structure test**

Expected: bakery assertions pass while six worked-example assertions remain failing.

### Task 3: Expand EOQ Worked Examples

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md:421-581`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`

- [ ] **Step 1: Expand ABI Warehouses**

Add the spare-part operating story, value-to-asset table, separate and pooled workflow, preserved formulas, physical meaning of both quantities, pooling decision, and duplicated-order-system trap.

- [ ] **Step 2: Expand Tek Pak**

Add the beer-crate operating story, current stock and inbound-delivery timeline, asset table, preserved calculation, quantity-versus-timing decision, and lead-time trap.

- [ ] **Step 3: Expand Kerosene**

Add the seasonal fuel operation, asset table, five-week delivery timeline, continuous-versus-integer order workflow, preserved calculation, delivery schedule decision, and `m`-rounding trap.

- [ ] **Step 4: Run the structure test**

Expected: bakery and EOQ assertions pass; EPQ assertions remain failing.

### Task 4: Expand EPQ Worked Examples

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md:581-748`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`

- [ ] **Step 1: Expand Battery-Cell Line**

Map battery packs, line output, downstream consumption, setup work, and warehouse cost. Add the production/depletion timeline and distinguish total batch from maximum stock.

- [ ] **Step 2: Expand Router Make-To-Stock Factory**

Insert the approved router analogy: finished routers, preparation activities, inventory alarm, simultaneous production and customer withdrawal, production duration, non-production duration, and repeated cycle.

- [ ] **Step 3: Expand Shovel Technology Adoption**

Map observed batch geometry to hidden demand, explain the faster machine as a real asset, preserve the new EPQ calculation, and distinguish annual relevant-cost saving from a full capital-budgeting valuation.

- [ ] **Step 4: Run the structure test**

Expected: all six worked-example structure assertions pass.

### Task 5: Expand Practice Tasks

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md:884-890`
- Test: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`

- [ ] **Step 1: Convert each numbered task into a retrieval card**

Each card must contain:

- `Operating setting`;
- `Asset mapping`;
- `Your task`;
- `Physical interpretation prompt`;
- `Exam-trap check`.

Keep tasks unsolved and retain the original supplied values.

- [ ] **Step 2: Run the structure test and verify GREEN**

Expected: all structural tests pass.

### Task 6: Numerical And Markdown Verification

**Files:**
- Verify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`
- Verify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs`

- [ ] **Step 1: Add numerical assertions to the test**

Independently calculate and assert the existing ABI, Tek Pak, Kerosene, Battery, Router, and Shovel values using JavaScript formulas. The test must not parse displayed answers as its calculation source.

- [ ] **Step 2: Run the complete Node test**

```bash
node --test supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-operational-analogies.test.mjs
```

Expected: zero failures.

- [ ] **Step 3: Check Markdown and whitespace**

```bash
git diff --check
awk '/^```/{count++} END{if (count % 2) exit 1; print "balanced fences:", count}' supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md
```

Expected: clean diff and an even code-fence count.

- [ ] **Step 4: Verify study-state preservation**

Confirm `learning-system/review-dashboard.md` still records Topic 05 as pending first pass and that no completion date was introduced by this clarification refinement.

### Task 7: Final Content Review

**Files:**
- Review: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

- [ ] **Step 1: Check terminology consistency**

Use **order quantity** for EOQ, **production batch** for EPQ, **maximum inventory** for `Imax`, **reorder point** for timing threshold, and **non-production duration** rather than treating the entire factory as idle.

- [ ] **Step 2: Check learning value**

Every example must answer what flows, what each variable represents, what happens over time, what the result physically means, what management does, and what not to confuse.

- [ ] **Step 3: Inspect the final diff**

Ensure this task changes only the Topic 05 note, its verification test, and planning artifacts. Preserve unrelated existing changes.


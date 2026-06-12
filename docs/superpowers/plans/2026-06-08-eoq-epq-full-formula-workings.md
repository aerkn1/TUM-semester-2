# EOQ And EPQ Full Formula Workings Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every EOQ and EPQ worked-example result show the symbolic formula, substituted values, numerical result, and units.

**Architecture:** Keep the main topic note as the complete worked-example source, add the calculation-presentation rule to the terminology companion, and preserve the rule in the paused-session continuation instructions. Do not change the underlying model assumptions or study schedule.

**Tech Stack:** Markdown, deterministic EOQ/EPQ formulas, shell-based numerical verification.

---

### Task 1: Expand The Main Worked Examples

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md`

- [x] Rewrite every answer-guide value as `formula = substitution = result with units`.
- [x] Show both finite-horizon integer candidates and their costs before choosing `m*`.
- [x] Show EOQ/EPQ holding-cost and setup-cost components where total cost is reported.
- [x] Preserve managerial interpretations and use consistent time units.

### Task 2: Add The Durable Recall Rule

**Files:**
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/CONTEXT.md`
- Modify: `supply-chain-management/wiki/topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching-clarification-session-2026-06-07.md`

- [x] Add a mandatory calculation ladder to `CONTEXT.md`.
- [x] Add the same requirement to the saved continuation instructions without rewriting the historical session outcome.

### Task 3: Verify The Documentation

**Files:**
- Verify all three Markdown files above.

- [x] Recalculate all reported numerical values independently.
- [x] Search the exercise section for unsupported result-only lines.
- [x] Run `git diff --check` and inspect the final diff.

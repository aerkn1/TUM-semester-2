# Learning System

This workspace is not only a note repository. It should operate as a retrieval and relearning system for the final 2.5 months before exams.

## Evidence-Based Priorities

Use these principles across all lectures:

1. Retrieval before review.
   - Start each session by recalling from memory before opening notes.
   - Generate short-answer questions, application prompts, and calculation/legal issue-spotting tasks from every deck.

2. Spaced relearning (chained schedule).
   - The schedule starts only after the first active-recall session is completed (`First Pass`). Generating a note does not start the clock.
   - Plan `D+1` as `First Pass + 1 day`, `D+3` as `D+1 completion + 3 days`, `D+7` as `D+3 completion + 7 days`, `D+14` as `D+7 completion + 14 days`, `D+30` as `D+14 completion + 30 days`. Each next interval chains off the prior actual completion date, never off `First Pass`.
   - If a review is failed or missed, reschedule it sooner and record the weakness. The next checkpoint chains from the actual repair completion date, not the original planned date.
   - See `Spaced Repetition Schedule Semantics` in the root `AGENTS.md` for the full rules.

3. Interleaving.
   - Do mixed sessions across lectures and across problem types.
   - Avoid only studying one deck in isolation after the first pass.

4. Elaboration and self-explanation.
   - For each core concept, answer: Why does this exist? When does it apply? What would change the answer? What is a real business example?

5. Feedback and mistake repair.
   - Every wrong or weak answer goes into the mistake ledger.
   - Re-study should target the error cause, not the whole deck.

6. Generative output.
   - Prefer producing a diagram, framework, example, comparison table, issue tree, or calculation setup from memory over rereading.

## Standard Workflow For A New Deck

1. Ingest source material into the lecture `raw/` folder.
2. Generate a comprehensive wiki note using `templates/wiki-note-template.md`.
3. Generate retrieval prompts and practice tasks inside the note.
4. Add the deck to `learning-system/review-dashboard.md` with status `first pass pending — note generated YYYY-MM-DD` and blank `First Pass` plus `D+n` cells.
5. Start coaching with active recall before explanation. The completion date of this first retrieval session becomes `First Pass`.
6. After the session, write the completion date into `First Pass` (or the relevant `D+n` cell), log weak points, and compute the next planned review date by chaining off this completion date.
7. Refresh `learning-system/weekly-calendar.md`.
8. Add or update Weekly Mixed Practice suggestions in `learning-system/review-dashboard.md`.

## Weekly Calendar Workflow

Use `weekly-calendar.md` as the current operational study plan. It should be refreshed after every study session, note ingestion, dashboard update, or review completion.

Default priority order:

1. Overdue chained `D+n` review (the planned next-review date for a topic with a recorded `First Pass` has passed).
2. Due-today chained `D+n` review.
3. Pending-first-pass candidate, chosen to balance against today's D+ load and prefer low-context continuation.
4. New subject ingestion when no wiki note exists yet and raw material is on hand.
5. Add mixed practice when two or more related topics are available.

If a scheduled D+ checkpoint has passed, state that explicitly. Do not silently roll it forward, because the user needs to know when retrieval timing has been missed. The next checkpoint chains from the repair completion date once the missed checkpoint is actually closed.

## Session Types

- `Note generation`: ingest the deck, create the wiki note and `CONTEXT.md`, identify the 80/20 concepts. This does NOT set `First Pass`.
- `First pass (active recall)`: the topic's first closed-book retrieval session. Its completion date becomes the dashboard's `First Pass`, starting the chained `D+1`/`D+3`/`D+7`/`D+14`/`D+30` schedule.
- `Recall pass`: any later closed-book retrieval from prompts, followed by targeted correction; closes the next `D+n` checkpoint.
- `Mixed pass`: interleave old and new decks, especially formulas, frameworks, and case applications.
- `Exam pass`: timed answer production, calculation setup, legal issue spotting, or managerial recommendation writing.

## Source Base

- Dunlosky et al. (2013), review of learning techniques: practice testing and distributed practice are high-utility techniques. https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html
- Roediger and Karpicke (2006), test-enhanced learning. https://pubmed.ncbi.nlm.nih.gov/16507066/
- Cepeda et al. (2006), distributed practice meta-analysis. https://www.semanticscholar.org/paper/Distributed-practice-in-verbal-recall-tasks%3A-A-and-Cepeda-Pashler/634293f80f8e661dc259e4902bca99821bec3014
- Rawson and Dunlosky (2022), successive relearning. https://journals.sagepub.com/doi/10.1177/09637214221100484
- Fiorella and Mayer (2015), generative learning strategies. https://colab.ws/articles/10.1007%2Fs10648-015-9348-9
- Rohrer and colleagues on interleaved practice. https://files.eric.ed.gov/fulltext/ED595322.pdf

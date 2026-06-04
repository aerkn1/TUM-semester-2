# Lektion 03 Active Recall Session: Articles, Negation, Adjectives, Questions

Source note: `lektion-03-city-articles-negation-and-adjectives.md`
Context file: `CONTEXT.md`
Vocabulary glossary: `VOCAB-GLOSSARY.md`
Session saved: 2026-06-04
Status: `active recall in progress`

## Session Scope

This session practiced Lektion 3 grammar production:

- nominative `der/das/die`, `ein/eine`, plural zero article
- `kein/keine` versus `nicht`
- predicate versus attributive adjective endings
- plural adjective pattern: `gute Restaurants` versus `keine guten Restaurants`
- question words: `wer`, `was`, `wo`, `woher`, `wann`
- capitalization and spelling in written German

The first-pass session is not closed yet because the final micro-redo remained open when the user switched to Lektion 2.

## Round 1: Article Grid

| Prompt | User Answer | Feedback |
|---|---|---|
| That is a train. | `Das ist ein Zug` | Correct. |
| That is a restaurant. | `Das ist eine Restaurant` | Correct form: `Das ist ein Restaurant.` `Restaurant` is neuter. |
| That is a city. | `Das ist eine Stadt` | Correct. |
| Those are restaurants. | `Das sind Restaurants` | Correct. |
| That is not a train. | `Das ist kein Zug` | Correct. |
| That is not a restaurant. | `Das ist keine Restaurant` | Correct form: `Das ist kein Restaurant.` `Restaurant` is neuter. |
| That is not a city. | `Das ist keine Stadt` | Correct. |
| Those are no restaurants. | `Das sind keine Restaurants` | Correct. |

Quality: `yellow`.

Weak spot: neuter `das Restaurant` takes `ein/kein`, not `eine/keine`.

## Round 2: Adjective Endings

Task: transform predicate adjective into attributive adjective.

| Prompt | User Answer | Feedback |
|---|---|---|
| `Der Zug ist lang.` | `Das ist ein langer Zug` | Correct. |
| `Das Restaurant ist gut.` | `Das ist ein gutes Restaurant` | Correct. |
| `Die Stadt ist groß.` | `Das ist eine große Stadt` | Correct. |
| `Das Hotel ist modern.` | `Das ist ein modernes Hotel` | Correct. |
| `Das Kind ist klein.` | `Das ist klienes Kind` | Correct form: `Das ist ein kleines Kind.` Need `ein` and spelling `kleines`. |
| `Der Mann ist sportlich.` | `Das ist ein sportlicher Mann` | Correct. |
| `Die Restaurants sind gut.` | `Das sind gute Restaurants` | Correct. |
| `Die Kinder sind klein.` | `Das sind kleine Kinder` | Correct. |

Quality: `green/yellow`.

Weak spot: neuter after `ein` uses adjective `-es`: `ein kleines Kind`.

## Round 3: Predicate Versus Attributive

Task: choose A or B.

| Prompt | User Answer | Feedback |
|---|---|---|
| `Der Zug ist lang.` vs `Der Zug ist langer.` | `A` | Correct. |
| `Das ist ein gut Restaurant.` vs `Das ist ein gutes Restaurant.` | `B` | Correct. |
| `Die Stadt ist groß.` vs `Die Stadt ist große.` | `A` | Correct. |
| `Das ist eine große Stadt.` vs `Das ist eine groß Stadt.` | `A` | Correct. |
| `Die Restaurants sind gute.` vs `Die Restaurants sind gut.` | `B` | Correct. |
| `Das sind gute Restaurants.` vs `Das sind gut Restaurants.` | `A` | Correct. |

Quality: `green`.

Mental model: after `sein`, no adjective ending; before noun, adjective ending needed.

## Round 4: `kein/keine` Versus `nicht`

| Prompt | User Answer | Feedback |
|---|---|---|
| That is not a train. | `Das ist kein Zug` | Correct. |
| The train is not long. | `Der Zug ist nicht lang` | Correct. |
| That is not a city. | `Das ist keine Stadt` | Correct. |
| The city is not big. | `Die stadt ist nicht groß` | Grammar correct; capitalize `Stadt`. |
| Those are not restaurants. | `Das sind keine Restaurants` | Correct. |
| The restaurants are not good. | `Die Restaurants sind nicht gut` | Correct. |
| That is not a good restaurant. | `Das ist nicht gutes Restaurant` | Correct form: `Das ist kein gutes Restaurant.` |
| That is not a modern hotel. | `Das ist nicht modernes hotel` | Correct form: `Das ist kein modernes Hotel.` |

Quality: `yellow`.

Weak spot: use `kein` for negating an indefinite noun phrase: `kein gutes Restaurant`, `kein modernes Hotel`.

## Round 5: Mixed Production

| Prompt | User Answer | Feedback |
|---|---|---|
| That is a good restaurant. | `Das ist ein gutes Restaurant` | Correct. |
| That is not a good restaurant. | `Das ist kein gutes Restaurant` | Correct. |
| The restaurant is not good. | `Das Restaurant ist nicht gut` | Correct. |
| That is a modern hotel. | `Das ist ein modernes hotel` | Correct grammar; capitalize `Hotel`. |
| That is not a modern hotel. | `Das ist keine modernes hotel` | Correct form: `Das ist kein modernes Hotel.` |
| The hotel is not modern. | `Das Hotel ist nicht modern` | Correct. |
| Those are good restaurants. | `Das sind gute Restaurants` | Correct. |
| Those are not good restaurants. | `Das sind nicht gute Restaurants` | Correct form: `Das sind keine guten Restaurants.` |

Quality: `yellow`.

Clarification saved:

- `gute Restaurants` = no article, plural adjective uses `-e`.
- `keine guten Restaurants` = `keine` carries the plural/negative article information, so adjective takes weak plural `-en`.
- Same pattern as `die guten Restaurants`.

## Round 6: Question Words

| Prompt | User Answer | Feedback |
|---|---|---|
| ___ ist das? Das ist ein Restaurant. | `was` | Correct word; capitalize sentence-initial `Was`. |
| ___ ist das? Das ist Frau Müller. | `wer` | Correct word; capitalize `Wer`. |
| ___ ist der Bahnhof? | `Wo` | Correct. |
| ___ kommst du? Ich komme aus der Türkei. | `Woher` | Correct. |
| ___ kommst du? Ich komme am Freitag. | `Wann` | Correct. |
| ___ sind das? Das sind gute Restaurants. | `was` | Correct word; capitalize `Was`. |

Quality: `green`.

## Round 7: Full Mixed Grammar

| Prompt | User Answer | Feedback |
|---|---|---|
| That is a long train. | `Das ist ein langer Zug` | Correct. |
| The train is not long. | `Der Zug ist nicht lang` | Correct. |
| That is not a long train. | `Das ist kein langer Zug` | Correct. |
| That is a big city. | `Das ist eine große Stadt` | Correct. |
| The city is not big. | `Die Stadt ist nicht groß.` | Correct. |
| That is not a big city. | `Das ist keine große Stadt` | Correct. |
| Those are good restaurants. | `Das sind gute Restaurants` | Correct. |
| Those are not good restaurants. | `Das sind keine guten Restaurants` | Correct. |

Quality: `green`.

## Round 8: Error Correction

Task: each sentence had one grammar error; user supplied corrected fragment.

| Prompt | User Answer | Feedback |
|---|---|---|
| `Das ist ein lange Zug.` | `langer` | Correct: `Das ist ein langer Zug.` |
| `Das Restaurant ist gutes.` | `gut` | Correct: `Das Restaurant ist gut.` |
| `Das ist eine gutes Restaurant.` | `ein` | Correct: `Das ist ein gutes Restaurant.` |
| `Das sind gute Restaurant.` | `gutes` | Incorrect target. Correct: `Das sind gute Restaurants.` Need plural noun. |
| `Das sind keine gute Restaurants.` | `guten` | Correct: `Das sind keine guten Restaurants.` |
| `Die Stadt ist große.` | `groß` | Correct: `Die Stadt ist groß.` |
| `Das ist nicht Zug.` | `kein` | Correct: `Das ist kein Zug.` |
| `Das ist kein moderne Hotel.` | `modernes` | Correct: `Das ist kein modernes Hotel.` |

Quality: `yellow`.

Weak spot: after `Das sind`, noun must be plural.

## Round 9: Free Production

| Prompt | User Answer | Feedback |
|---|---|---|
| Write one sentence with `ein langer Zug`. | `Das ist ein langer Zug` | Correct. |
| Write one sentence with `kein langer Zug`. | `Das ist kein langer Zug` | Correct. |
| Write one sentence with `ein gutes Restaurant`. | `Das istein gutes Restaurant` | Correct grammar; fix spacing: `Das ist ein gutes Restaurant.` |
| Write one sentence with `keine guten Restaurants`. | `Das sind keine guten Restaurants` | Correct. |
| Write one sentence with `ist nicht gut`. | `Das ist nicht gut` | Correct; stronger target: `Das Restaurant ist nicht gut.` |
| Write one question using `Wo`. | `Wo ist der Bahnof?` | Correct structure; spelling: `Bahnhof`. |

Quality: `yellow`.

Weak spots: spacing under speed, `Bahnhof` spelling.

## Round 10: Mixed Mini-Dialogue

| Prompt | User Answer | Feedback |
|---|---|---|
| What is that? | `Was ist das?` | Correct. |
| That is a good restaurant. | `Das ist ein gutes restaurant` | Correct grammar; capitalize `Restaurant`. |
| Is that a modern hotel? | `Ist das ein modernes hotel?` | Correct grammar; capitalize `Hotel`. |
| No, that is not a modern hotel. | `Nein, das ist kein modernes hotel` | Correct grammar; capitalize `Hotel`. |
| Those are good restaurants. | `Das sind gute restaurants` | Correct grammar; capitalize `Restaurants`. |
| No, those are not good restaurants. | `Nein, das sind nich gute restaurants` | Correct form: `Nein, das sind keine guten Restaurants.` |
| Where is the train station? | `Wo is der bahnhof?` | Correct form: `Wo ist der Bahnhof?` |

Quality: `yellow/red` for written accuracy.

Weak spots: capitalization, `ist`, `nicht`, `kein/keine`, `Bahnhof`.

## Micro-Redo Before Pause

| Prompt | User Answer | Feedback |
|---|---|---|
| No, that is not a modern hotel. | `Nein, das is keine modernes hotel.` | Correct form: `Nein, das ist kein modernes Hotel.` |
| No, those are not good restaurants. | `Nein, das sind keine guten restaurants` | Correct grammar; capitalize `Restaurants`. |
| Where is the train station? | `Wo ist der Bahnhof?` | Correct. |

Quality: `red/yellow`.

## Open Next Prompts

Resume with these two corrections before closing the session:

1. No, that is not a modern hotel.
2. No, those are not good restaurants.

## Weak Spots

| Weak Spot | Quality | Correction Rule |
|---|---|---|
| `Restaurant` and `Hotel` neuter patterns | yellow | `das Restaurant -> ein/kein gutes Restaurant`; `das Hotel -> ein/kein modernes Hotel`. |
| `nicht` versus `kein/keine` | yellow | Use `kein/keine` for negating noun phrases; use `nicht` for predicate adjectives and verbs. |
| plural adjective with `keine` | yellow | `gute Restaurants`, but `keine guten Restaurants`. |
| capitalization of German nouns | red/yellow | Capitalize `Restaurant`, `Hotel`, `Restaurants`, `Stadt`, `Bahnhof`. |
| spelling under pressure | yellow | `ist`, `nicht`, `Bahnhof`. |

## Refined Mental Models

- Predicate adjective: `Das Restaurant ist gut.` No ending.
- Attributive adjective: `Das ist ein gutes Restaurant.` Ending before noun.
- No article plural: `gute Restaurants`.
- `keine` plural: `keine guten Restaurants`.
- Noun-phrase negation: `kein modernes Hotel`, not `nicht modernes Hotel`.

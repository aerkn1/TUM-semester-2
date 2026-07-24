#!/usr/bin/env python3
"""Build an exam-focused Business Law print bundle from wiki Markdown files."""

from __future__ import annotations

import re
import argparse
import json
import subprocess
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "business-law" / "wiki"
OUT_DIR = WIKI / "_print"
TODAY = date.today().isoformat()

FULL_BASE = f"business-law-exam-print-bundle-{TODAY}"
NAV_BASE = f"business-law-exam-navigation-pack-{TODAY}"
CSS_FILE = OUT_DIR / "exam-print.css"


@dataclass(frozen=True)
class Entry:
    code: str
    section: str
    path: Path


ROUTER_FILES = [
    "exam-strategy-answer-schemas-2026-07-28/exam-strategy-answer-schemas-2026-07-28.md",
    "exam-strategy-answer-schemas-2026-07-28/section-cluster-table-by-case-flow.md",
    "exam-strategy-answer-schemas-2026-07-28/numbers-and-deadlines-cheat-sheet.md",
    "exam-strategy-answer-schemas-2026-07-28/confusable-terms-trap-sheet.md",
    "exam-strategy-answer-schemas-2026-07-28/theory-glossary-and-answer-template.md",
    "exam-strategy-answer-schemas-2026-07-28/minor-capacity-tort-unjust-enrichment-router.md",
    "_course-knowledge-graph.md",
    "_course-logistics.md",
]

TOPIC_ORDER = [
    "week-01-02-introduction-to-business-law",
    "week-03-contract-law-i",
    "week-04-contract-law-ii-rescission-revocation",
    "week-05-contract-law-iii-withdrawal-cancellation-dissolution",
    "week-06-standard-business-terms",
    "week-07-agency",
    "week-08-warranty-rights-i",
    "week-09-warranty-rights-ii",
    "week-10-transfer-of-property",
    "week-11-trade-law",
    "week-12-13-company-law-i-ii",
]

CASE_FILES = [
    "example-exam-i-case-facts/example-exam-i-case-facts.md",
    "example-exam-ii-case-facts/example-exam-ii-case-facts.md",
    "additional-mock-exams-and-external-cheatsheet/additional-mock-exams-and-external-cheatsheet.md",
]


FRONT_MATTER = """# {bundle_title}

Generated: {today}

Scope: {scope}

Excluded by design:

- all `CONTEXT.md` files
- active-recall session logs
- clarification-session logs
- raw Moodle/source files

## Page-Referenced Index

Use these page numbers against the final PDF printout. If a print shop inserts a cover sheet, use the PDF page number shown by the viewer rather than the shop's sheet count.

{page_index}

## Fact-Signal Page Router

Start with the fact signal, then jump to the listed page before opening the full weekly note.

{fact_page_index}

## Recommended Physical Shape

Use a router-first binder, not a chronological booklet.

Print these first pages single-sided so you can annotate them quickly:

1. Universal legal-opinion schema
2. Section cluster table by case flow
3. Numbers and deadlines cheat sheet
4. Confusable terms trap sheet
5. Theory answer template
6. Minor, capacity, tort, and unjust-enrichment side router

Then print the weekly doctrine pages duplex, grouped with divider tabs:

| Tab | Code | What It Is For |
|---|---|---|
| Fast Routing | R | Decide which weekly topic applies before writing. |
| Method + Formation | W01-W03 | Legal method, statute hierarchy, offer, acceptance, validity. |
| Contract Exit Routes | W04-W05 | Rescission, revocation, withdrawal, cancellation, restitution. |
| Clauses + Representation | W06-W07 | Standard terms, agency, authority, principal/agent/third-party routing. |
| Sales Remedies | W08-W09 | Defect, cure, reduction, revocation, damages, warranty exclusions. |
| Ownership + Commercial Overlay | W10-W11 | Transfer of property, good-faith acquisition, merchant status, Section 377 HGB, Prokura. |
| Company Law | W12 | GmbH, AG, organs, representation, liability, Business Judgment Rule. |
| Case Practice | C | Example exams, historical mock routing, issue maps. |

Keep the statutory-law printout separate from this bundle. This bundle tells you where to go; the statute tells you the exact wording.

## How To Use This In The Exam

For every case, write this mini-route in the margin before drafting:

```text
Who wants what from whom based on what?
actor status -> formation -> authority/organs -> clauses -> breach/defect/remedy -> overlay -> consequence
```

Do not start with the remedy. Start with the legal relationship.

1. Identify actor status first: consumer, entrepreneur, merchant, company, organ, agent.
2. Confirm formation and validity before clause review or remedies.
3. If someone acts for someone else, route agency/company representation before obligations.
4. If standard terms appear, review incorporation and content control after contract formation.
5. If a delivered item is defective, start from purchase and warranty, not mistake rescission.
6. If both parties are merchants, apply the HGB overlay before concluding ordinary BGB warranty rights.
7. If the question asks ownership, switch from contract claims to property transfer.
8. Close with legal consequence: claim exists, claim blocked, contract void, contract avoided, restitution, damages, or no liability.

## Cross-Week Inclusion Matrix

| Fact Signal | Primary Route | Also Check | Why It Mixes Weeks |
|---|---|---|---|
| Advertisement, webshop listing, phone order, counteroffer | W03 Contract Law I | W06 SBT, W08 Warranty, W11 Trade | No later remedy works until offer/acceptance is stable. |
| Manager, employee, buyer, salesperson, managing director acts for a business | W07 Agency | W11 Prokura/merchant authority, W12 company organs | Representation can bind the principal/company before you reach breach or defect. |
| Pre-formulated clause, exclusion clause, referral to terms | W06 SBT | W03 formation, W08/W09 warranty exclusions, W05 consumer withdrawal | A clause can only be reviewed after contract formation, and it may alter remedies. |
| Mistake, deceit, threat, wrong declaration | W04 rescission | W03 formation/interpretation, W08 warranty priority | Formation defects use avoidance; delivered defective goods usually use warranty. |
| Online/off-premises consumer transaction | W05 withdrawal | W01 status, W03 formation, W06 SBT | Withdrawal depends on consumer status and transaction channel. |
| Late delivery, non-performance, impossible performance | W05 revocation/damages | W03 valid contract, W04 rescission only if declaration flaw | Performance failures are different from formation flaws. |
| Defective sold good after handover | W08/W09 warranty | W11 Section 377 HGB, W06 warranty exclusion clauses, W10 ownership only if ownership is asked | Sales defects often combine BGB warranty with merchant notice rules. |
| "Who owns it?", double sale, stolen/lost goods, assignment | W10 property | W03 sale contract, W08 defect only if quality issue | Contract validity and ownership transfer are separate layers. |
| Merchant, commercial register, Prokura, business sale | W11 trade law | W07 agency, W08 warranty, W03 formation | HGB modifies BGB defaults and can silently block claims. |
| GmbH/AG, shareholder, director, board decision | W12 company law | W07 agency, W11 merchant-by-form, W05 damages | Company form changes representation, liability, and governance analysis. |
| Theory question asks "distinguish" or "define" | R theory template | Matching weekly cheat sheet | Theory answers need compact rule plus consequence, not full legal opinion. |

## Case Writing Skeleton

Use this exact rhythm unless the question only asks for theory:

```text
1. A could have a claim/right/defense against B under Section X.
2. This requires element 1, element 2, and element 3.
3. Element 1 is fulfilled/not fulfilled because ...
4. Element 2 is fulfilled/not fulfilled because ...
5. Therefore, the legal consequence is ...
```

For modifications, write only what changes:

```text
The result changes only if the modification affects [status / formation / authority / clause / defect / notice / remedy].
All unchanged requirements from the basic constellation remain as above.
```

## Bundle Contents In Print Order

{manifest}
"""


CSS = """
html {
  color: #111;
  background: #fff;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-size: 10.4pt;
  line-height: 1.38;
  max-width: 980px;
  margin: 0 auto;
  padding: 24px;
}

h1, h2, h3, h4 {
  break-after: avoid;
  page-break-after: avoid;
}

h1 {
  font-size: 22pt;
  border-bottom: 2px solid #111;
  padding-bottom: 0.18em;
}

h2 {
  font-size: 15pt;
  margin-top: 1.25em;
}

h3 {
  font-size: 12.5pt;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.8em 0 1.1em;
  font-size: 8.7pt;
}

th, td {
  border: 1px solid #b9b9b9;
  padding: 4px 5px;
  vertical-align: top;
}

th {
  background: #f2f2f2;
}

tr {
  break-inside: avoid;
  page-break-inside: avoid;
}

pre {
  white-space: pre-wrap;
  border: 1px solid #c9c9c9;
  background: #f8f8f8;
  padding: 8px;
  font-size: 8.6pt;
}

code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.92em;
}

blockquote {
  border-left: 4px solid #999;
  margin-left: 0;
  padding-left: 12px;
  color: #333;
}

.page-break {
  break-before: page;
  page-break-before: always;
}

.source-path {
  font-size: 8.6pt;
  color: #555;
}

@media print {
  @page {
    size: A4;
    margin: 12mm 10mm 14mm 10mm;
  }

  body {
    max-width: none;
    margin: 0;
    padding: 0;
    font-size: 9.8pt;
  }

  a {
    color: #111;
    text-decoration: none;
  }

  h1 {
    font-size: 18pt;
  }

  h2 {
    font-size: 13.5pt;
  }

  h3 {
    font-size: 11.4pt;
  }

  table {
    font-size: 7.6pt;
  }
}
"""


DOCX_PAGE_XML = (
    '<w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720" '
    'w:header="360" w:footer="360" w:gutter="0"/>'
)


def is_excluded(path: Path) -> bool:
    name = path.name.lower()
    return (
        name == "context.md"
        or "active-recall-session" in name
        or "clarification-session" in name
        or "_print" in path.parts
    )


def title_for(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def without_first_h1(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:i] + lines[i + 1 :]).strip()
    return text.strip()


def natural_topic_code(folder: str) -> str:
    match = re.match(r"week-(\d+)(?:-(\d+))?", folder)
    if not match:
        return "WXX"
    first = match.group(1)
    second = match.group(2)
    return f"W{first}-{second}" if second else f"W{first}"


def ordered_topic_files(folder: Path) -> list[Path]:
    files = [p for p in folder.glob("*.md") if not is_excluded(p)]
    main = folder / f"{folder.name}.md"
    priority: list[Path] = []
    if main.exists() and main in files:
        priority.append(main)
    for marker in [
        "continuity-bridge",
        "cheatsheet-and-tricks",
        "practice-questions-and-model-answers",
    ]:
        priority.extend(sorted(p for p in files if marker in p.name and p not in priority))
    priority.extend(sorted(p for p in files if p not in priority))
    return priority


def build_entries() -> list[Entry]:
    entries: list[Entry] = []

    for index, rel in enumerate(ROUTER_FILES, start=1):
        path = WIKI / rel
        if path.exists() and not is_excluded(path):
            entries.append(Entry(f"R{index}", "Fast Routing", path))

    for folder_name in TOPIC_ORDER:
        folder = WIKI / folder_name
        if not folder.exists():
            continue
        base = natural_topic_code(folder_name)
        for index, path in enumerate(ordered_topic_files(folder), start=1):
            entries.append(Entry(f"{base}.{index}", "Weekly Doctrine", path))

    for index, rel in enumerate(CASE_FILES, start=1):
        path = WIKI / rel
        if path.exists() and not is_excluded(path):
            entries.append(Entry(f"C{index}", "Case Practice", path))

    used = {entry.path for entry in entries}
    remaining = sorted(
        p for p in WIKI.rglob("*.md") if not is_excluded(p) and p not in used
    )
    for index, path in enumerate(remaining, start=1):
        entries.append(Entry(f"X{index}", "Additional Exam Wiki File", path))

    return entries


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_manifest(entries: list[Entry]) -> str:
    rows = ["| Code | Section | File |", "|---|---|---|"]
    for entry in entries:
        rows.append(f"| {entry.code} | {entry.section} | `{rel(entry.path)}` |")
    return "\n".join(rows)


def page_index(entries: list[Entry], page_map: dict[str, int]) -> str:
    rows = ["| Code | Page | Section | Title |", "|---|---:|---|---|"]
    for entry in entries:
        page = page_map.get(entry.code)
        page_text = f"{page:03d}" if page is not None else "000"
        title = title_for(entry.path)
        rows.append(f"| {entry.code} | {page_text} | {entry.section} | {title} |")
    return "\n".join(rows)


FACT_ROUTE_ROWS = [
    (
        "Advertisement, webshop listing, phone order, counteroffer",
        ["R2", "W03.2", "W03.1"],
        ["W06.2", "W08.2", "W11.2"],
    ),
    (
        "Manager, employee, salesperson, managing director acts",
        ["R2", "W07.2", "W07.1"],
        ["W11.2", "W12-13.2"],
    ),
    (
        "Pre-formulated clause or exclusion clause",
        ["R2", "W06.2", "W06.1"],
        ["W08.2", "W09.2", "W05.3"],
    ),
    (
        "Mistake, deceit, threat, wrong declaration",
        ["R2", "W04.2", "W04.1"],
        ["W03.2", "W08.2"],
    ),
    (
        "Online or off-premises consumer transaction",
        ["R2", "W05.3", "W05.1"],
        ["W01-02.2", "W03.2", "W06.2"],
    ),
    (
        "Late, missing, impossible, or bad performance",
        ["R2", "W05.3", "W05.1"],
        ["W03.2", "W04.2"],
    ),
    (
        "Defective sold good after handover",
        ["R2", "W08.2", "W09.2", "W08.1", "W09.1"],
        ["W11.2", "W06.2"],
    ),
    (
        "Who owns it, double sale, stolen/lost goods, assignment",
        ["R2", "W10.2", "W10.1"],
        ["W03.2", "W08.2"],
    ),
    (
        "Merchant, commercial register, Prokura, Section 377",
        ["R2", "W11.2", "W11.1"],
        ["W07.2", "W08.2"],
    ),
    (
        "GmbH, AG, shareholder, director, board decision",
        ["R2", "W12-13.2", "W12-13.1"],
        ["W07.2", "W11.2"],
    ),
    (
        "Theory question asks define, distinguish, or list",
        ["R5", "R3", "R4"],
        ["W01-02.2", "W03.2", "W06.2", "W12-13.2"],
    ),
    (
        "Example-exam style mixed case",
        ["C1", "C2", "C3"],
        ["R1", "R2"],
    ),
]


def code_lookup(entries: list[Entry], page_map: dict[str, int], codes: list[str]) -> str:
    known = {entry.code for entry in entries}
    parts = []
    for code in codes:
        if code not in known:
            continue
        page = page_map.get(code)
        page_text = f"p. {page:03d}" if page is not None else "p. 000"
        parts.append(f"{code} {page_text}")
    return "; ".join(parts) if parts else "-"


def fact_page_index(entries: list[Entry], page_map: dict[str, int]) -> str:
    rows = ["| Fact Signal | Start Here | Also Check |", "|---|---|---|"]
    for signal, start_codes, also_codes in FACT_ROUTE_ROWS:
        rows.append(
            "| "
            + " | ".join(
                [
                    signal,
                    code_lookup(entries, page_map, start_codes),
                    code_lookup(entries, page_map, also_codes),
                ]
            )
            + " |"
        )
    return "\n".join(rows)


def build_markdown(
    entries: list[Entry], bundle_title: str, scope: str, page_map: dict[str, int]
) -> str:
    parts = [
        FRONT_MATTER.format(
            today=TODAY,
            bundle_title=bundle_title,
            scope=scope,
            page_index=page_index(entries, page_map),
            fact_page_index=fact_page_index(entries, page_map),
            manifest=markdown_manifest(entries),
        )
    ]
    for entry in entries:
        text = entry.path.read_text(encoding="utf-8")
        title = title_for(entry.path)
        body = without_first_h1(text)
        parts.append(
            "\n".join(
                [
                    '<div class="page-break"></div>',
                    "",
                    f"# [{entry.code}] {title}",
                    "",
                    f'<p class="source-path">Source: <code>{rel(entry.path)}</code></p>',
                    "",
                    body,
                    "",
                ]
            )
        )
    return "\n\n".join(parts).rstrip() + "\n"


def run_pandoc(master_md: Path, output: Path, title: str, *extra: str) -> None:
    subprocess.run(
        [
            "pandoc",
            str(master_md),
            "--from=markdown+pipe_tables+fenced_code_blocks+tex_math_dollars",
            "--standalone",
            "--metadata",
            f"title={title}",
            *extra,
            "-o",
            str(output),
        ],
        cwd=ROOT,
        check=True,
    )


def force_docx_a4_layout(path: Path) -> None:
    """Patch Pandoc's DOCX to A4 with compact margins before PDF conversion."""
    tmp = path.with_suffix(".tmp.docx")
    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(
        tmp, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "word/document.xml":
                text = data.decode("utf-8")
                text = re.sub(r"<w:pgSz\b[^>]*/>", "", text)
                text = re.sub(r"<w:pgMar\b[^>]*/>", "", text)
                text = text.replace("</w:sectPr>", DOCX_PAGE_XML + "</w:sectPr>")
                data = text.encode("utf-8")
            zout.writestr(info, data)
    tmp.replace(path)


def bundle_paths(base: str) -> tuple[Path, Path, Path]:
    return (
        OUT_DIR / f"{base}.md",
        OUT_DIR / f"{base}.html",
        OUT_DIR / f"{base}.docx",
    )


def page_map_path(base: str) -> Path:
    return OUT_DIR / f"{base}.page-map.json"


def pdf_path(base: str) -> Path:
    return OUT_DIR / f"{base}.pdf"


def read_page_map(base: str) -> dict[str, int]:
    path = page_map_path(base)
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(k): int(v) for k, v in data.items()}


def write_bundle(
    entries: list[Entry], base: str, title: str, scope: str, page_map: dict[str, int]
) -> tuple[Path, Path, Path]:
    master_md, print_html, print_docx = bundle_paths(base)
    master_md.write_text(build_markdown(entries, title, scope, page_map), encoding="utf-8")
    run_pandoc(
        master_md,
        print_html,
        title,
        "--to=html5",
        f"--css={CSS_FILE.relative_to(ROOT).as_posix()}",
    )
    run_pandoc(master_md, print_docx, title, "--to=docx")
    force_docx_a4_layout(print_docx)
    return master_md, print_html, print_docx


def extract_page_map(pdf: Path, entries: list[Entry]) -> dict[str, int]:
    if not pdf.exists():
        raise SystemExit(f"Missing PDF for page-map extraction: {pdf}")

    text = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], cwd=ROOT)
    pages = text.decode("utf-8", errors="ignore").split("\f")
    codes = sorted((entry.code for entry in entries), key=len, reverse=True)
    code_pattern = "|".join(re.escape(code) for code in codes)
    heading_re = re.compile(rf"^\s*\[({code_pattern})\]\s+.+\s*$")

    found: dict[str, int] = {}
    for page_no, page in enumerate(pages, start=1):
        for line in page.splitlines():
            match = heading_re.match(line)
            if match and match.group(1) not in found:
                found[match.group(1)] = page_no
        if len(found) == len(codes):
            break
    return found


def extract_page_maps(all_entries: list[Entry], nav_entries: list[Entry]) -> None:
    for base, entries in [(FULL_BASE, all_entries), (NAV_BASE, nav_entries)]:
        page_map = extract_page_map(pdf_path(base), entries)
        page_map_path(base).write_text(
            json.dumps(page_map, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        missing = [entry.code for entry in entries if entry.code not in page_map]
        print(f"Extracted page map: {rel(page_map_path(base))} ({len(page_map)} entries)")
        if missing:
            print(f"Missing headings in {base}: {', '.join(missing)}")


def navigation_entries(entries: list[Entry]) -> list[Entry]:
    result: list[Entry] = []
    case_paths = {WIKI / rel_path for rel_path in CASE_FILES}
    for entry in entries:
        name = entry.path.name.lower()
        if entry.code in {"R1", "R2", "R3", "R4", "R5", "R6"}:
            result.append(entry)
        elif "cheatsheet-and-tricks" in name:
            result.append(entry)
        elif entry.path in case_paths:
            result.append(entry)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--extract-page-maps",
        action="store_true",
        help="Extract page numbers from existing PDFs before rebuilding Markdown/HTML/DOCX.",
    )
    args = parser.parse_args()

    if not WIKI.exists():
        raise SystemExit(f"Missing wiki directory: {WIKI}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    entries = build_entries()
    nav_entries = navigation_entries(entries)

    if args.extract_page_maps:
        extract_page_maps(entries, nav_entries)

    CSS_FILE.write_text(CSS.strip() + "\n", encoding="utf-8")

    full_md, full_html, full_docx = write_bundle(
        entries,
        FULL_BASE,
        "Business Law Exam Print Bundle",
        "Full exam-focused archive from `business-law/wiki/`, excluding context and session logs.",
        read_page_map(FULL_BASE),
    )
    nav_md, nav_html, nav_docx = write_bundle(
        nav_entries,
        NAV_BASE,
        "Business Law Exam Navigation Pack",
        "Compact exam desk pack: fast routers, weekly cheat sheets, and case maps only.",
        read_page_map(NAV_BASE),
    )

    excluded = sorted(p for p in WIKI.rglob("*.md") if is_excluded(p))
    print(f"Included files: {len(entries)}")
    print(f"Navigation files: {len(nav_entries)}")
    print(f"Excluded files: {len(excluded)}")
    for path in [full_md, full_html, full_docx, nav_md, nav_html, nav_docx]:
        print(f"Wrote: {rel(path)}")
    print(f"Wrote: {rel(CSS_FILE)}")


if __name__ == "__main__":
    main()

# Week 11 Trade Law - Case Router Shortcut

Source note: [week-11-trade-law.md](week-11-trade-law.md)
Companions: [CONTEXT.md](CONTEXT.md), [week-11-trade-law-cheatsheet-and-tricks.md](week-11-trade-law-cheatsheet-and-tricks.md), [week-11-trade-law-practice-questions-and-model-answers.md](week-11-trade-law-practice-questions-and-model-answers.md)
Created: 2026-07-27
Status effect: no `First Pass` or `D+n` checkpoint advanced. This is a shortcut/refinement aid; a checkpoint closes only after closed-book recall.

## One-Sentence Core

Trade Law is not a replacement for the BGB. It is the merchant/commercial overlay that modifies selected BGB results.

```text
BGB = baseline.
HGB = merchant overlay.
Exam move = state BGB baseline, then ask whether HGB changes this exact point.
```

## When Week 11 Triggers

Use Week 11 when the facts contain one of these signals:

| Trigger in facts | Likely route |
|---|---|
| GmbH, AG, oHG, KG, e.K., registered business, large organized business | Merchant-status gateway |
| "ppa.", Prokurist, procurement manager, internal limit | Prokura under Sections 48-50 HGB |
| "i.V.", purchasing clerk, sales manager, usual business authority | Handlungsvollmacht under Section 54 HGB |
| public shop, showroom, warehouse, sales assistant, cashier | Section 56 HGB shop assistant authority |
| commercial register, listed/revoked Prokura, wrong entry | Section 15 HGB publicity |
| two merchants negotiated, then one sends a confirmation letter | Commercial letter of confirmation |
| long-term commercial service relationship and silence after offer | Section 362 HGB |
| B2B sale of goods with defect notice timing | Section 377 HGB before Section 437 BGB |
| Incoterms, liability waiver, commercial standard terms | SBT route plus Section 310 I BGB |
| oral merchant guarantee or merchant service without price | Sections 350 or 354 HGB |

## Master Trade-Law Router

```text
1. Classify actor status.
   merchant by operation / opt-in registration / legal form / not merchant

2. State the BGB baseline.
   formation / agency / warranty / damages / SBT / property

3. Find the HGB modifier.
   register / Prokura / Handlungsvollmacht / shop authority / silence / Section 377 / form relief

4. Apply the HGB rule narrowly.
   HGB changes only that point.

5. Return to the BGB for the remaining consequence.
```

Do not write "HGB applies instead of BGB." Write:

```text
The BGB route applies, but because this is a commercial/merchant setting, the HGB modifies [specific issue].
```

## Merchant Gateway

| Facts | Route | Conclusion |
|---|---|---|
| Organized commercial business with scale/scope | Section 1 HGB | Merchant if commercial organization is required. |
| Very small business registered as merchant | Section 2 HGB | Merchant by voluntary opt-in registration. |
| GmbH, AG, commercial partnership | Section 6 HGB; Section 13 III GmbHG for GmbH | Merchant by legal form; no scale test needed. |
| Registered business argues it is not really commercial | Section 5 HGB | Register-based merchant appearance can bind. |
| Lawyer, doctor, architect, author, employee, charity, passive landlord | Usually no Section 1 merchant route | Do not apply HGB unless another gateway is proven. |

Shortcut:

```text
GmbH/AG = merchant by form.
Small business = merchant only if registered.
Liberal profession / employee / passive asset manager = usually not merchant.
```

## Section 15 HGB Register Publicity

| Register fact pattern | Route | Result |
|---|---|---|
| True fact should be registered, but is not | Section 15 I HGB | Merchant usually cannot assert it against good-faith third party. |
| True fact is registered and published | Section 15 II HGB | Third party must usually accept it. |
| Register/publication is wrong | Section 15 III HGB | Good-faith third party may rely on the wrong published content. |

Memory:

```text
15 I = register silence protects third party.
15 II = published truth is assertable.
15 III = wrong publication can still protect third party.
```

## Commercial Authority Picker

| Person in facts | Correct route | Key limit |
|---|---|---|
| Prokurist / `ppa.` / expressly granted Prokura | Sections 48-50 HGB | Very broad; internal limits usually ineffective externally. |
| Prokurist selling/encumbering land | Section 49 II HGB | Needs specific real-estate authorization; good faith does not fix statutory scope. |
| Several Prokurists must act together | Section 48 II HGB | Joint participation required; exact same-minute signing is not. |
| Prokurist contracts with own business | Section 181 BGB overlay | Self-dealing blocks unless permission, ratification, existing duty, or only legal advantage. |
| Purchasing clerk / business manager without Prokura | Section 54 HGB | Usual-business scope; loans/litigation/land need specific authority. |
| Store/showroom employee selling to customer | Section 56 HGB | Covers customary sales/receipts at public premises only. |
| Repeated tolerated signing without formal authority | BGB agency-by-estoppel route | Not Prokura, but principal's tolerated appearance may bind. |

## Silence And Confirmation

| Facts | Route | Result |
|---|---|---|
| Existing commercial service relationship; merchant receives usual-business offer and does not answer | Section 362 HGB | Silence can count as acceptance. |
| Merchants negotiated; one promptly sends good-faith confirmation; recipient stays silent | Commercial letter of confirmation | Contract can be fixed by confirmed content. |
| Sender knowingly inserts materially wrong terms into confirmation | Bad-faith confirmation | Silence does not bind the recipient to the wrong content. |

Trap:

```text
BGB silence baseline = no acceptance.
HGB silence exceptions = narrow and fact-heavy.
```

## Section 377 HGB Warranty Filter

In B2B goods cases, Section 377 comes before ordinary warranty remedies.

```text
mutual commercial purchase
-> delivery
-> defect
-> inspection duty
-> notice duty
-> no fraudulent concealment
-> if late: goods deemed approved, Section 437 rights excluded
```

| Defect timing | Buyer duty | Result if buyer fails |
|---|---|---|
| Obvious defect recognizable on proper inspection | Inspect after delivery and notify without undue delay | Goods deemed approved. |
| Hidden defect not recognizable at delivery | Notify without undue delay after discovery | Late discovery alone is not fatal. |
| Seller fraudulently concealed defect | Section 377 protection blocked | Seller cannot rely on late notice. |

Shortcut:

```text
B2B defect case = Section 377 before Section 437.
Obvious defect clock starts at delivery.
Hidden defect clock starts at discovery.
```

## Cross-Topic Correlation Map

Week 11 is the commercial overlay. It often appears inside a case whose main topic is another week.

| Related topic | Aspect it decides | How Week 11 changes or links to it | Exam shortcut |
|---|---|---|---|
| Contract Law I | Offer, acceptance, silence, interpretation | HGB can turn silence into acceptance in narrow commercial cases and commercial usage can shape interpretation. | Start with BGB formation, then check Section 362 or confirmation-letter facts. |
| Contract Law II | Mistake/deceit and register reliance | If a party says "the register was wrong" or "authority was revoked," Section 15 HGB may protect good-faith reliance. | Do not solve register cases only as ordinary mistake; use publicity logic. |
| Contract Law III | Delay, damages, revocation | HGB may raise merchant-care expectations; SBT/Incoterms may allocate delivery duties, but BGB damages rules still supply the claim. | HGB changes business standard or term context; BGB gives remedy. |
| Standard Business Terms | B2B clauses, Incoterms, liability waivers | In B2B, Sections 308/309 BGB do not apply directly, but Section 307 still controls through Section 310 I. | Do not say "B2B means all clauses valid." Use Section 307 via Section 310 I. |
| Agency | Representation by employees/managers | Prokura, Handlungsvollmacht, and shop authority are special commercial authority routes layered onto Section 164 BGB. | Run Section 164 structure, then choose the HGB authority type. |
| Warranty Rights I | Defect gateway and cure | Section 377 can destroy Section 437/439 remedies in mutual commercial purchases. | In merchant-to-merchant goods sale, Section 377 comes before cure/replacement. |
| Warranty Rights II | Damages for defective goods | If Section 377 deems goods approved, damages routes under Section 437 No. 3 can be blocked too. | Late notice can kill not only cure but also warranty damages. |
| Transfer of Property | Ownership and possession | HGB may explain who had authority to sell or why a shop sale binds, but Section 929 still decides ownership transfer. | HGB authority first if seller's representative is in question; property route second. |
| Company Law | GmbH/AG, directors, organs, commercial register | Legal form can make an entity merchant automatically; company organs can grant Prokura; registration can be constitutive for companies but declaratory for Prokura. | Company form answers merchant gateway and who can grant authority. |
| Finance/security/business practice | Guarantees, services, commercial credit | Merchant guarantee form protection is weaker under Section 350; merchant services are presumed paid under Section 354. | Merchant professionalism reduces protective formalities. |

## All High-Yield Combinations

| Facts | Route | Conclusion sentence |
|---|---|---|
| GmbH buys goods | Sections 6 HGB, 13 III GmbHG | GmbH is merchant by legal form; HGB layer can apply. |
| Large organized sole trader sells repeatedly | Section 1 HGB | Merchant if commercial organization is required. |
| Small side business not registered | No HGB gateway unless Section 1 scale met | Stay with BGB baseline. |
| Revoked Prokura not registered | Section 15 I HGB | Good-faith third party can rely on register silence. |
| Revoked Prokura registered/published | Section 15 II HGB | Merchant can assert the revocation. |
| Register wrongly still lists Prokura | Section 15 III HGB | Good-faith third party may rely on wrong publication. |
| Prokurist signs ordinary supply contract despite internal cap | Sections 48-50 HGB | Business bound; internal cap does not bind unaware third party. |
| Prokurist sells land without special authority | Section 49 II HGB | Business not bound; real estate is statutory scope exception. |
| Prokurist contracts with own company | Section 181 BGB | Provisionally invalid unless exception or ratification. |
| Two joint Prokurists sign same deal sequentially | Section 48 II HGB | Valid if both participated jointly. |
| Clerk with Handlungsvollmacht takes out loan | Section 54 II HGB | Not bound unless specific loan authority. |
| Showroom employee sells carpet to customer | Section 56 HGB | Store bound for customary sale/receipt. |
| Forwarder stays silent after regular client's usual shipment offer | Section 362 HGB | Silence can be acceptance. |
| Merchant sends knowingly wrong confirmation letter | Confirmation-letter rule fails | Bad-faith sender cannot use recipient's silence. |
| Merchant buyer gives late notice for obvious defect | Section 377 HGB | Goods deemed approved; warranty remedies excluded. |
| Latent defect discovered later and notified same day | Section 377 III HGB | Warranty rights survive. |
| B2B standard term waives all delay damages | Sections 307, 310 I BGB | Clause may fail even though 308/309 do not apply directly. |
| Merchant gives oral commercial guarantee | Section 350 HGB | Ordinary Section 766 BGB form protection removed. |
| Merchant provides business service without price agreement | Section 354 HGB | Remuneration usually presumed. |

## Multi-Layer Business Case Sequence

For a full exam case with merchants, use this stack:

```text
1. Actor status
   consumer / entrepreneur / merchant / company form

2. BGB baseline
   formation, agency, warranty, damages, SBT, property

3. HGB gateway
   merchant? commercial transaction? mutual commercial purchase?

4. HGB modifier
   register / authority / silence / Section 377 / form relief / merchant diligence

5. Return to BGB consequence
   claim, no claim, contract bound, warranty blocked, damages survive
```

## Exam Answer Skeleton

```text
The BGB baseline is [formation / agency / warranty / damages / SBT].
Because [party] is a merchant / this is a mutual commercial purchase, I must check whether the HGB modifies this point.
The relevant HGB rule is [section].
Its requirements are [list].
Here, [apply].
Therefore, the HGB [does / does not] change the BGB result, so [final consequence].
```

## 12-Minute Retention Drill

Do this closed-book. Say only route and consequence first.

1. GmbH buys goods. Why is it a merchant?
2. Small unregistered craft seller sells once. HGB or BGB only?
3. Prokura revoked but not registered; third party checks register. Which Section 15 route?
4. Register wrongly lists Prokura because of registry error. Which Section 15 route?
5. Prokurist signs above an internal EUR 30,000 cap. Bound?
6. Prokurist sells land without special authority. Bound?
7. Purchasing clerk with Handlungsvollmacht signs a loan. Bound?
8. Sales assistant sells a showroom item. Which authority?
9. Forwarder stays silent after regular client's shipment request. Which silence rule?
10. Confirmation letter intentionally states 500 instead of 250 goods. Does silence bind?
11. Merchant buyer notices obvious cracks 17 days after delivery. Warranty?
12. Hidden defect appears three weeks later, notice same day. Warranty?

Target: 10/12 clean route choices before opening the full Week 11 note.

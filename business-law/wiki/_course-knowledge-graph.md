# Business Law Course Knowledge Graph

This file aggregates the Business Law concepts learned so far. It is intentionally graph-view-first for visual recall.

Scope: Business Law only. Do not add cross-lecture concepts unless they are needed to explain Business Law material.

## Course Graph View

```mermaid
graph LR
    BL[Business Law] -->|governs decisions through| LegalSystem[Legal system]
    BL -->|is mainly composed of| Fields[Legal fields]
    BL -->|is learned through| Method[Legal method]

    Fields -->|includes| Civil[Private civil law]
    Fields -->|includes| Commercial[Commercial law]
    Fields -->|includes| Company[Company law]
    Fields -->|also touches| PublicCommercial[Public and international commercial law]

    LegalSystem -->|uses sources| Sources[Sources of law]
    Sources -->|primary in Germany| Statutes[Statutes: BGB, HGB, AktG, GmbHG]
    Sources -->|interprets and stabilizes| CaseLaw[Case law]
    Sources -->|fills gaps through| Custom[Customary law and analogies]
    Sources -->|created by parties as| PrivateRules[Standard business terms]

    LegalSystem -->|belongs to| CivilLawSystem[Civil-law system]
    CivilLawSystem -->|prioritizes| Statutes
    CivilLawSystem -->|contrasts with| CommonLawSystem[Common-law system]
    CommonLawSystem -->|prioritizes| Precedent[Precedent / stare decisis]

    LegalSystem -->|is constrained by| NormHierarchy[Hierarchy of norms]
    NormHierarchy -->|highest where applicable| EULaw[EU law]
    EULaw -->|includes secondary law| Regulation[Regulation]
    EULaw -->|includes secondary law| Directive[Directive]
    Regulation -->|creates| UniformRules[Uniform EU rules]
    Directive -->|requires| NationalTransposition[National transposition]
    NormHierarchy -->|domestic level| FederalLaw[Federal law]
    NormHierarchy -->|domestic level| StateLaw[State law]
    FederalLaw -->|prevails over under Art. 31 GG| StateLaw

    LegalSystem -->|classifies disputes into| PublicPrivate[Public vs private law]
    PublicPrivate -->|state authority / subordination| PublicLaw[Public law]
    PublicPrivate -->|equal actors / autonomy| PrivateLaw[Private law]
    PrivateLaw -->|core future topic| ContractLaw[Contract law]
    ContractLaw -->|starts with| Formation[Contract formation]
    ContractLaw -->|is grounded in| PrivateAutonomy[Private autonomy]
    ContractLaw -->|can be altered by| Termination[Contract termination routes]

    Formation -->|requires| Offer[Offer]
    Formation -->|door sections| FormationSections[130, 133/157, 145, 146, 148, 150 II BGB]
    Formation -->|requires| Acceptance[Acceptance]
    Offer -->|must contain| Essentialia[Essentialia negotii]
    Offer -->|becomes effective through| IssuingReception[Issuing and reception]
    Acceptance -->|must mirror| Offer
    Acceptance -->|if modified becomes| CounterOffer[Rejection plus counter-offer]
    Formation -->|uses| DoI[Declaration of intent]
    DoI -->|has external side| ObjectiveElement[Objective element]
    DoI -->|has internal side| SubjectiveElement[Subjective element]
    SubjectiveElement -->|includes| IntentionBound[Intention to be legally bound]
    IntentionBound -->|separates offer from| Invitatio[Invitatio ad offerendum]

    PrivateAutonomy -->|allows| FreedomContract[Freedom of conclusion, party, form, content]
    PrivateAutonomy -->|limited by| LimitsAutonomy[Mandatory limits]
    LimitsAutonomy -->|lock sections| ValiditySections[125, 134, 138, 305 ff., 276 III BGB]
    LimitsAutonomy -->|statutory prohibition| S134[Section 134 BGB]
    LimitsAutonomy -->|public policy / usury| S138[Section 138 BGB]
    LimitsAutonomy -->|standard terms| S305[Sections 305 ff. BGB]
    LimitsAutonomy -->|consumer protection| B2C[B2C rules]

    Termination -->|formation flaw| Rescission[Rescission]
    Termination -->|performance problem| Revocation[Revocation]
    Termination -->|consumer protection| Withdrawal[Withdrawal]
    Termination -->|continuing obligation| Cancellation[Cancellation]
    Termination -->|mutual agreement| Dissolution[Dissolution]

    Rescission -->|grounds| ErrorDeceitDuress[Error, deceit, duress]
    Rescission -->|emergency-exit sections| RescissionSections[119, 120, 123, 143, 121/124, 144, 142, 122 BGB]
    Rescission -->|effect| ExTunc[Void ex tunc]
    Revocation -->|grounds| PerformanceBreach[Primary duty, ancillary duty, impossibility]
    Revocation -->|return-desk sections| RevocationSections[323, 324, 326 V, 349, 346-348, 325 BGB]
    Revocation -->|effect| Restitution346[Restitution under Sections 346-348 BGB]
    Withdrawal -->|requires| ConsumerTrader[Consumer and trader]
    Withdrawal -->|covers| DistanceOffPremises[Distance / off-premises contracts]
    Cancellation -->|requires for extraordinary termination| CompellingReason[Compelling reason]
    Cancellation -->|effect| ExNunc[Termination ex nunc]
    Dissolution -->|requires| Agreement[Offer and acceptance]

    Method -->|starts from| LegalNorm[Legal norm]
    LegalNorm -->|has| Conditions[Conditions if]
    LegalNorm -->|leads to| Consequence[Legal consequence then]
    Method -->|requires| Interpretation[Statutory interpretation]
    Interpretation -->|asks text meaning| Wording[Wording]
    Interpretation -->|asks purpose| Telos[Purpose / telos]
    Interpretation -->|asks legal location| SystemContext[Systematic context]
    Interpretation -->|asks origin| History[Historical interpretation]
    Method -->|uses| BGBStructure[BGB structure]
    BGBStructure -->|organized by| Bracketing[Bracketing technique]
    Bracketing -->|general rules apply to| SpecificRules[Specific books and chapters]
    Method -->|resolves overlap through| LexSpecialis[Lex specialis]
    LexSpecialis -->|specific rule prevails over| GeneralRule[General rule]
```

## Legal Analysis Flow View

```mermaid
flowchart TD
    Facts[Business facts] --> Classify[Classify legal area]
    Classify --> PublicCheck{State authority involved?}
    PublicCheck -->|Yes| PublicLaw[Public law analysis]
    PublicCheck -->|No, equal private parties| PrivateLaw[Private law analysis]

    PrivateLaw --> SourceCheck[Find statutory source]
    PublicLaw --> SourceCheck
    SourceCheck --> HierarchyCheck[Check hierarchy: EU, federal, state]
    HierarchyCheck --> Norm[Select legal norm]
    Norm --> Elements[Break into conditions]
    Elements --> Apply[Apply facts to each condition]
    Apply --> Interpret{Ambiguous term?}
    Interpret -->|Yes| Lenses[Use wording, telos, system, history]
    Interpret -->|No| Consequence[State legal consequence]
    Lenses --> Consequence
    Consequence --> LexCheck{General and specific rules overlap?}
    LexCheck -->|Yes| Lex[Apply lex specialis]
    LexCheck -->|No| Result[Legal result]
    Lex --> Result
```

## Contract Law Decision View

```mermaid
flowchart TD
    Start[Contract issue] --> FormationQuestion{Is the contract formed?}
    FormationQuestion -->|No / uncertain| Formation[Check offer and acceptance]
    Formation --> DoorSections[Door sections: 130, 133/157, 145, 146, 148, 150 II]
    Formation --> OfferCheck[Offer: essentialia negotii + intention to be bound]
    OfferCheck --> ReceptionCheck[Effective DoI: issuing + reception]
    ReceptionCheck --> AcceptanceCheck[Acceptance mirrors offer?]
    AcceptanceCheck -->|No| CounterOffer[Rejection plus counter-offer]
    AcceptanceCheck -->|Yes| ValidContract[Contract formed]

    FormationQuestion -->|Yes| ValidContract
    ValidContract --> ValidityCheck{Validity problem?}
    ValidityCheck -->|Yes| LockSections[Lock sections: 125, 134, 138, 305 ff., 276 III]
    ValidityCheck -->|No| ProblemType{What problem occurred?}
    LockSections --> ProblemType

    ProblemType -->|Flawed declaration of intent| Rescission[Rescission]
    Rescission --> Grounds119123[Sections 119, 120, 123 BGB]
    Grounds119123 --> RescissionSteps[Ground + declaration + time limit + no exclusion]
    RescissionSteps --> ExTunc[Effect ex tunc]

    ProblemType -->|Performance breach in reciprocal contract| Revocation[Revocation]
    Revocation --> S323324326[Sections 323, 324, 326 V BGB]
    S323324326 --> Restitution[Return performances under Sections 346-348 BGB]

    ProblemType -->|Consumer wants out of protected situation| Withdrawal[Withdrawal]
    Withdrawal --> ConsumerScope[Consumer + trader]
    ConsumerScope --> DistancePremises[Distance or off-premises contract]
    DistancePremises --> WithdrawalPeriod[Usually 14 days if properly informed]

    ProblemType -->|Continuing obligation should end| Cancellation[Cancellation]
    Cancellation --> SpecialRules[Check special provisions first]
    SpecialRules --> S314[Section 314 model]
    S314 --> Compelling[Compelling reason + warning/period if needed]
    Compelling --> ExNunc[Effect ex nunc]

    ProblemType -->|Both parties agree to end| Dissolution[Dissolution]
    Dissolution --> Agreement[Termination agreement through offer and acceptance]
```

## Subject Graph Index

| Subject / Deck | Wiki Note | Main Visual Logic | Last Updated |
|---|---|---|---|
| Week 01-02 Introduction To Business Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` | Legal system map: sources, hierarchy, public/private classification, BGB method | 2026-05-14 |
| Week 03 Contract Law I | `week-03-contract-law-i/week-03-contract-law-i.md` | Contract formation and validity sections: door and lock memory map | 2026-05-25 |
| Week 04 Contract Law II | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` | Exit routes: emergency exit for rescission and return desk for revocation | 2026-05-25 |
| Week 05 Contract Law III | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` | Termination II: withdrawal, cancellation, dissolution, and full termination decision tree | 2026-05-14 |

## Supporting Node Reference

| Node | Meaning | Source Note |
|---|---|---|
| Business Law | Legal fields relevant for business decisions | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Law | Binding and enforceable norms | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Statutory Law | Written legal rules such as BGB, HGB, AktG, GmbHG | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Case Law | Court decisions interpreting legal rules | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Civil Law System | Statutes as primary foundation | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Common Law System | Precedent as stronger formal foundation | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| EU Law | Supranational legal order with primacy where applicable | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Regulation | Directly applicable EU secondary law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Directive | EU secondary law requiring national transposition | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Public Law | Law involving state authority or subordination | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Private Law | Law between equal private actors | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| BGB Structure | Five-book structure with general and specific rules | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Bracketing Technique | General rules apply across more specific books/chapters | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Lex Specialis | Specific rule prevails over general rule | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Conditions / Legal Consequence | If-then structure of legal norms | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Statutory Interpretation | Wording, purpose, system, and history | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Declaration of Intent | External expression of will aimed at legal consequence | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Offer | DoI enabling contract conclusion by acceptance alone | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Acceptance | Agreement with the offer | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Private Autonomy | Freedom to shape contractual relations | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Door sections | Formation anchors: receipt, interpretation, offer, expiry, deadline, modified acceptance | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Lock sections | Validity anchors: form, prohibition, public policy, standard terms, intentional liability | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Rescission | Right to eradicate a flawed DoI | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Revocation | Right to undo a valid reciprocal contract due to performance problem | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Emergency exit sections | Rescission anchors: mistake, deceit/duress, declaration, timing, exclusion, effects | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Return desk sections | Revocation anchors: breach routes, declaration, restitution, damages | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Withdrawal | Consumer-protection exit right | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |
| Cancellation | Termination of continuing obligation | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |
| Dissolution | Consensual termination agreement | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |

## Supporting Edge Reference

| From | Relationship | To | Source Note |
|---|---|---|---|
| Business Law | is built from | Civil Law / Commercial Law / Company Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Law | differs from | Morality / Rechtsgefühl | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Civil Law System | prioritizes | Statutory Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Case Law | interprets | Statutory Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| EU Law | can override | National Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Federal Law | prevails over | State Law | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Regulation | creates | Uniform EU Rules | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Directive | requires | National Transposition | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Public Law | involves | State Authority | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Private Law | relies on | Private Autonomy | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| BGB Structure | uses | Bracketing Technique | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Lex Specialis | resolves conflict between | General Rule and Specific Rule | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Legal Norm | contains | Conditions / Legal Consequence | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Statutory Interpretation | clarifies | Ambiguous Legal Terms | `week-01-02-introduction-to-business-law/week-01-02-introduction-to-business-law.md` |
| Contract | requires | Offer and Acceptance | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Offer | must include | Essentialia Negotii | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Acceptance | must mirror | Offer | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Private Autonomy | is limited by | Sections 134 and 138 BGB | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Contract formation | is routed through | Door sections | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Contract validity | is tested by | Lock sections | `week-03-contract-law-i/week-03-contract-law-i.md` |
| Rescission | attacks | Declaration of Intent | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Rescission | is routed through | Emergency exit sections | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Revocation | responds to | Performance Problem | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Revocation | is routed through | Return desk sections | `week-04-contract-law-ii-rescission-revocation/week-04-contract-law-ii-rescission-revocation.md` |
| Withdrawal | protects | Consumer | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |
| Cancellation | applies to | Continuing Obligation | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |
| Dissolution | requires | Agreement | `week-05-contract-law-iii-withdrawal-cancellation-dissolution/week-05-contract-law-iii-withdrawal-cancellation-dissolution.md` |

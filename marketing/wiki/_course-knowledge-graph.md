# Marketing Course Knowledge Graph

This file aggregates the Marketing concepts learned so far. It is graph-view-first for visual recall.

Scope: Marketing only. Do not add cross-lecture global concepts unless needed to explain Marketing material.

## Course Graph View

```mermaid
graph LR
    Marketing[Marketing] -->|creates and manages| ValueExchange[Value exchange]
    ValueExchange -->|starts from| CustomerNeeds[Customer needs]
    ValueExchange -->|delivered by| Offering[Supplier offering]
    Marketing -->|aims for| CompetitiveAdvantage[Sustainable competitive advantage]
    CompetitiveAdvantage -->|requires| NoticeableValue[Lasting, substantial, noticeable value]

    Marketing -->|managed through| ManagementProcess[Marketing management process]
    ManagementProcess --> Situation[Situation analysis]
    Situation --> Forecast[Forecast]
    Forecast --> Goals[Marketing goals]
    Goals --> Strategy[Marketing strategy]
    Strategy --> MarketingMix[4Ps marketing mix]
    MarketingMix --> ProductP[Product]
    MarketingMix --> PriceP[Price]
    MarketingMix --> PromotionP[Promotion]
    MarketingMix --> PlaceP[Place]
    MarketingMix --> Implementation[Implementation]
    Implementation --> Controlling[Marketing controlling]

    Marketing -->|builds| SuccessChain[Marketing success chain]
    SuccessChain --> CustomerValue[Customer value]
    CustomerValue --> Acquisition[Customer acquisition]
    Acquisition --> Satisfaction[Customer satisfaction]
    Satisfaction --> Retention[Customer retention]
    Retention --> EconomicSuccess[Economic success]
    Satisfaction -->|driven by| Disconfirmation[Expectation-performance disconfirmation]
    Satisfaction --> Complaints[Complaints]
    Complaints --> Recovery[Recovery]
    Recovery --> ThreeRs[3Rs: recruitment, retention, recovery]

    Marketing -->|uses| Segmentation[Segmentation]
    Segmentation --> Targeting[Targeting]
    Targeting --> Positioning[Positioning]
    Marketing -->|studies| ConsumerBehavior[Consumer behavior]
    ConsumerBehavior --> Involvement[Involvement]
    ConsumerBehavior --> GoodsTypes[Types/properties of goods]
    GoodsTypes --> SearchGoods[Search properties]
    GoodsTypes --> ExperienceGoods[Experience properties]
    GoodsTypes --> TrustGoods[Trust properties]

    Marketing -->|creates meaning through| Branding[Branding]
    Branding --> BrandIdentity[Brand identity]
    Branding --> BrandImage[Brand image]
    BrandImage --> BrandAssociations[Brand associations]
    BrandAssociations --> Strength[Strength]
    BrandAssociations --> Favorability[Favorability]
    BrandAssociations --> Uniqueness[Uniqueness]
    Branding --> BrandKnowledge[Brand knowledge]
    BrandKnowledge --> Awareness[Brand awareness]
    BrandKnowledge --> Image[Brand image]
    BrandKnowledge --> CBBE[Customer-based brand equity]
    CBBE --> Salience[Salience]
    Salience --> Performance[Performance]
    Salience --> Imagery[Imagery]
    Performance --> Judgments[Judgments]
    Imagery --> Feelings[Feelings]
    Judgments --> Resonance[Brand resonance]
    Feelings --> Resonance
    Branding --> BrandPositioning[Brand positioning]
    BrandPositioning --> POP[Points of parity]
    BrandPositioning --> POD[Points of difference]
    BrandPositioning --> BrandMantra[Brand mantra]
    Branding --> BrandArchitecture[Brand architecture]
    BrandArchitecture --> LineExtension[Line extension]
    BrandArchitecture --> BrandExtension[Brand extension]
    BrandArchitecture --> Multibranding[Multi-branding]
    Branding --> BrandLeverage[Brand leverage]
    BrandLeverage --> Alliances[Brand alliances]
    BrandLeverage --> Licensing[Licensing]
    BrandLeverage --> Endorsement[Celebrity endorsement]

    ProductP --> ProductPolicy[Product policy]
    ProductPolicy --> ProductLevels[Product levels]
    ProductLevels --> CoreBenefit[Core benefit]
    ProductLevels --> ExpectedProduct[Expected product]
    ProductLevels --> AugmentedProduct[Augmented product]
    ProductLevels --> PotentialProduct[Potential product]
    ProductPolicy --> Digitalization[Product digitalization]
    Digitalization --> DigitalProduct[Physical to digital]
    Digitalization --> HybridProduct[Physical plus digital element]
    ProductPolicy --> Packaging[Packaging]
    ProductPolicy --> Assortment[Assortment decisions]
    Assortment --> Breadth[Breadth]
    Assortment --> Depth[Depth]
    ProductPolicy --> Elimination[Product elimination]
    ProductPolicy --> Recommenders[AI recommender systems]
    Recommenders --> Collaborative[Collaborative filtering]
    Recommenders --> ContentBased[Content-based filtering]
    Recommenders --> FATE[Fairness/accountability/transparency/explainability]
    Recommenders --> Privacy[Privacy concerns]
    ProductPolicy --> Innovation[Product innovation]
    Innovation --> TechPush[Technology push]
    Innovation --> MarketPull[Market pull]
    Innovation --> LeadUsers[Lead users]
    Innovation --> CoCreation[Customer co-creation]
    Innovation --> Agile[Agile/lean startup]
    ProductPolicy --> Conjoint[Conjoint analysis]
    Conjoint --> Attributes[Attributes and levels]
    Conjoint --> Utilities[Part-worth utilities]
    Conjoint --> CBC[Choice-based conjoint]

    PriceP --> Pricing[Pricing policy]
    Pricing --> Behavioral[Behavioral pricing]
    Behavioral --> ReferencePrice[Reference price and fairness]
    Behavioral --> ChoiceEffects[Compromise and decoy effects]
    Pricing --> Differentiation[Price differentiation]
    Differentiation --> Yield[Yield management]
    Differentiation --> Bundling[Bundling and two-part tariffs]
    Pricing --> Determination[Price determination]
    Determination --> BreakEven[Break-even and contribution margin]
    Determination --> Elasticity[Elasticity and demand functions]
    Elasticity --> Monopoly[MR equals MC monopoly optimum]

    PromotionP --> Communication[Marketing communication]
    Communication --> FiveMs[Mission Money Message Media Measurement]
    Communication --> PushPull[Push and pull]
    Communication --> MediaMetrics[Reach frequency GRP CPT]
    Communication --> Integrated[Integrated communication]
    Communication --> WOM[WOM and eWOM]
    WOM --> Credibility[Credibility and helpfulness]
    Communication --> Influencer[Influencer marketing]
    Influencer --> PKM[Persuasion Knowledge Model]
```

## Decision Flow View

```mermaid
flowchart TD
    Start[Marketing problem] --> Customer{Who is the customer and need?}
    Customer --> Segment[Segment market]
    Segment --> Evaluate[Check identifiable, profitable, reachable]
    Evaluate --> Target[Choose target group]
    Target --> Position[Define positioning]
    Position --> POPPOD[Set POPs and PODs]
    POPPOD --> Mix[Design 4Ps]

    Mix --> ProductDecision{Product question?}
    ProductDecision -->|Basic value| Levels[Define product levels]
    ProductDecision -->|Innovation| Develop[Run development process]
    Develop --> Source{Innovation source?}
    Source --> Tech[Technology push]
    Source --> Pull[Market pull]
    Source --> Lead[Lead users/co-creation]
    Develop --> AgileTest[Test assumptions iteratively]
    ProductDecision -->|Preference measurement| ConjointStep[Use conjoint/CBC]
    ConjointStep --> Utility[Estimate attribute utilities]

    Mix --> BrandDecision{Brand question?}
    BrandDecision --> Knowledge[Diagnose brand knowledge]
    Knowledge --> Assoc[Check association strength/favorability/uniqueness]
    BrandDecision --> Equity[Build CBBE pyramid]
    Equity --> ResonanceGoal[Target resonance]
    BrandDecision --> Architecture[Choose architecture or alliance]

    Mix --> RelationshipDecision{Relationship question?}
    RelationshipDecision --> Acquire[Recruitment/acquisition]
    RelationshipDecision --> Retain[Retention/switching barriers]
    RelationshipDecision --> Recover[Recovery/complaint handling]
    Recover --> AvoidDouble[Prevent double deviation]

    Mix --> PriceDecision{Price question?}
    PriceDecision -->|Customer perception| BehaviorRoute[Reference price fairness choice effects]
    PriceDecision -->|Segment WTP| DifferenceRoute[Differentiation bundling yield]
    PriceDecision -->|Required economics| PriceMath[Contribution break-even elasticity MR equals MC]

    Mix --> PromotionDecision{Communication question?}
    PromotionDecision --> Objective[Define audience and objective]
    Objective --> FiveMRoute[Apply the 5Ms]
    FiveMRoute --> Channel[Choose owned paid earned media]
    Channel --> Metric[Measure reach fit memory attitude behavior]
    PromotionDecision --> WOMRoute[Assess WOM eWOM influencer persuasion]

    Mix --> Control[Implementation and marketing controlling]
```

## Subject Graph Index

| Subject / Deck | Wiki Note | Main Visual Logic | Last Updated |
|---|---|---|---|
| Chapter 01 Basic Concepts Of Marketing | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` | Value exchange -> marketing process -> 4Ps/3Rs -> satisfaction/segmentation/consumer behavior | 2026-05-14 |
| Chapter 02 Branding | `chapter-02-branding/chapter-02-branding.md` | Brand knowledge -> associations -> positioning -> CBBE -> architecture/leverage | 2026-05-14 |
| Chapter 03 Product | `chapter-03-product/chapter-03-product.md` | Product levels -> digitalization/packaging/assortment -> innovation/co-creation/agile -> conjoint | 2026-05-14 |
| Chapter 04 Price | `chapter-04-price/chapter-04-price.md` | Behavioral evaluation -> differentiation/bundling -> break-even/elasticity -> profit decision | 2026-06-12 |
| Chapter 05 Promotion And Communication | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` | 5Ms -> media planning/measurement -> WOM/eWOM -> influencer persuasion knowledge | 2026-06-12 |

## Supporting Node Reference

| Node | Meaning | Source Note |
|---|---|---|
| Marketing | Market-oriented management of value exchange | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| 4Ps | Product, Price, Promotion, Place | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| 3Rs | Recruitment, Retention, Recovery | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Customer Satisfaction | Expectation-performance emotional reaction | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Disconfirmation | Difference between expectations and perceived performance | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Segmentation | Dividing markets into targetable groups | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Brand | Identifier and differentiator with associations and meaning | `chapter-02-branding/chapter-02-branding.md` |
| Brand Knowledge | Brand awareness plus brand image | `chapter-02-branding/chapter-02-branding.md` |
| CBBE | Differential consumer response caused by brand knowledge | `chapter-02-branding/chapter-02-branding.md` |
| Points of Parity | Category legitimacy associations | `chapter-02-branding/chapter-02-branding.md` |
| Points of Difference | Distinctive choice-driving associations | `chapter-02-branding/chapter-02-branding.md` |
| Product | Bundle of attributes offering benefit | `chapter-03-product/chapter-03-product.md` |
| Product Levels | Core, generic, expected, augmented, potential layers | `chapter-03-product/chapter-03-product.md` |
| Product Digitalization | Physical-to-digital transformation or digital augmentation | `chapter-03-product/chapter-03-product.md` |
| Product Assortment | Breadth and depth decisions | `chapter-03-product/chapter-03-product.md` |
| Lead Users | Users ahead of mainstream needs | `chapter-03-product/chapter-03-product.md` |
| Co-Creation | Customer participation in product/value creation | `chapter-03-product/chapter-03-product.md` |
| Conjoint Analysis | Preference measurement through attribute tradeoffs | `chapter-03-product/chapter-03-product.md` |
| Reference Price | Benchmark used to evaluate an observed price | `chapter-04-price/chapter-04-price.md` |
| Price Differentiation | Different prices designed to capture heterogeneous willingness to pay | `chapter-04-price/chapter-04-price.md` |
| Contribution Margin | Revenue remaining after variable cost | `chapter-04-price/chapter-04-price.md` |
| Price Elasticity | Percentage demand response to a percentage price change | `chapter-04-price/chapter-04-price.md` |
| 5Ms | Mission, Money, Message, Media, and Measurement | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| Weighted CPT | Contact cost adjusted for target-group fit | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| eWOM | Online consumer communication available to broad audiences | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| Persuasion Knowledge | Consumer knowledge of persuasion goals and tactics | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |

## Supporting Edge Reference

| From | Relationship | To | Source Note |
|---|---|---|---|
| Marketing | creates | Customer Value | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Customer Value | drives | Acquisition/Satisfaction/Retention | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Expectations | compared with | Perceived Performance | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Disconfirmation | determines | Satisfaction | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Segmentation | enables | Targeting | `chapter-01-basic-concepts-of-marketing/chapter-01-basic-concepts-of-marketing.md` |
| Brand Knowledge | creates | Customer-Based Brand Equity | `chapter-02-branding/chapter-02-branding.md` |
| Brand Associations | evaluated by | Strength/Favorability/Uniqueness | `chapter-02-branding/chapter-02-branding.md` |
| Positioning | requires | Points of Parity and Difference | `chapter-02-branding/chapter-02-branding.md` |
| Brand Elements | build/protect | Brand Equity | `chapter-02-branding/chapter-02-branding.md` |
| Product Levels | structure | Customer value layers | `chapter-03-product/chapter-03-product.md` |
| Digitalization | changes | Product form and business model | `chapter-03-product/chapter-03-product.md` |
| Lead Users | reveal | Future market needs | `chapter-03-product/chapter-03-product.md` |
| Co-Creation | provides | Need and solution information | `chapter-03-product/chapter-03-product.md` |
| Conjoint Analysis | estimates | Attribute-level utilities | `chapter-03-product/chapter-03-product.md` |
| Reference Price | shapes | Price Fairness | `chapter-04-price/chapter-04-price.md` |
| Heterogeneous WTP | enables | Price Differentiation | `chapter-04-price/chapter-04-price.md` |
| Contribution Margin | determines | Break-Even Volume | `chapter-04-price/chapter-04-price.md` |
| Marginal Revenue | equals at optimum | Marginal Cost | `chapter-04-price/chapter-04-price.md` |
| Communication Mission | guides | Message Media Measurement | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| Target-Group Fit | corrects | CPT | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| Satisfaction And Trust | generate | eWOM | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |
| Persuasion Recognition | activates | Coping Response | `chapter-05-promotion-communication/chapter-05-promotion-communication.md` |

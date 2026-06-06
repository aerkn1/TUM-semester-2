# Supply Chain Management Course Knowledge Graph

This file aggregates the Supply Chain Management concepts learned so far. It is intentionally graph-view-first for visual recall.

Scope: Supply Chain Management only. Do not add cross-lecture concepts unless they are needed to explain Supply Chain Management material.

## Course Graph View

```mermaid
graph LR
    SCM[Supply Chain Management] -->|matches| SupplyDemand[Supply and demand]
    SCM -->|starts with operational use case| Kristen[Kristen Cookies case]
    SupplyDemand -->|is hard because of| LeadTime[Lead time]
    SupplyDemand -->|is hard because of| DemandUncertainty[Demand uncertainty]

    Kristen -->|shows| ProcessFlow[Process flow]
    Kristen -->|teaches| Bottleneck[Bottleneck]
    Kristen -->|measures| ThroughputTime[Throughput time]
    Kristen -->|measures| CycleTime[Cycle time]
    Kristen -->|links strategy to| StrategicFit[Strategic fit]
    Bottleneck -->|determines| Capacity[System capacity]
    CycleTime -->|determines| Capacity

    DemandUncertainty -->|requires| Forecasting[Forecasting]
    Forecasting -->|produces| PointEstimate[Point estimate]
    Forecasting -->|evaluated by| ErrorMetrics[Forecast error metrics]
    ErrorMetrics -->|bias| ME[ME]
    ErrorMetrics -->|typical miss| MAD[MAD]
    ErrorMetrics -->|large-error penalty| MSE[MSE]
    Forecasting -->|uses| TimeSeries[Time-series methods]
    TimeSeries --> Naive[Naive]
    TimeSeries --> MovingAverage[Moving average]
    TimeSeries --> ExponentialSmoothing[Exponential smoothing]
    Forecasting -->|can use| Regression[Regression]
    Forecasting -->|monitored by| ControlLimits[Control limits]

    DemandUncertainty -->|is modeled by| RandomVariables[Random variables]
    RandomVariables -->|have| SampleSpace[Sample space]
    RandomVariables -->|use| Distribution[Probability distribution]
    Distribution -->|count demand| Poisson[Poisson distribution]
    Distribution -->|rough interval| Uniform[Uniform distribution]
    Distribution -->|high-volume demand| Normal[Normal distribution]
    Distribution -->|uses| CDF[CDF F(q)=P(D<=q)]
    Distribution -->|continuous shape| PDF[PDF]
    Normal -->|uses| ZScore[z-score]
    Poisson -->|large lambda approx| NormalApprox[Normal approximation]
    CDF -->|equals when stocking q| ServiceLevel[Service level]

    PointEstimate -->|supports deterministic planning| EOQ[EOQ]
    ServiceLevel -->|feeds| Newsvendor[Newsvendor model]
    CDF -->|inverse gives| DemandQuantile[Demand quantile]
    DemandQuantile -->|determines| NewsvendorQ[Newsvendor Q*]
    Newsvendor -->|balances| Underage[Underage cost]
    Newsvendor -->|balances| Overage[Overage cost]
    Underage -->|raises| ServiceLevel
    Overage -->|lowers| ServiceLevel
    Newsvendor -->|uses critical fractile| CriticalFractile[c_u/(c_u+c_o)]
    DemandUncertainty -->|managed repeatedly by| OrderUpTo[Order-up-to model]
    LeadTime -->|creates exposure to| DemandLPlusOne[Demand over l+1 periods]
    DemandLPlusOne -->|evaluated by| OrderUpTo
    OrderUpTo -->|targets| OrderUpToLevel[S order-up-to level]
    OrderUpTo -->|uses state variable| InventoryPosition[Inventory position]
    InventoryPosition -->|determines| PeriodOrder[Period order quantity]
    ServiceLevel -->|sets quantile for| OrderUpToLevel
    OrderUpToLevel -->|evaluated by| OUTPerformance[Order-up-to performance]
    OUTPerformance -->|includes| ExpectedBackorders[Expected backorders B(S)]
    OUTPerformance -->|includes| ExpectedInventory[Expected leftover inventory I(S)]

    EOQ -->|assumes| DeterministicDemand[Deterministic constant demand]
    EOQ -->|balances| SetupCost[Setup/order cost]
    EOQ -->|balances| HoldingCost[Holding cost]
    SetupCost -->|decreases with larger Q| EOQTradeoff[EOQ tradeoff]
    HoldingCost -->|increases with larger Q| EOQTradeoff
    EOQTradeoff -->|gives| EOQFormula[Q*=sqrt(2Klambda/h)]
    EOQ -->|lead time changes| ReorderPoint[Reorder point lambda*l]
    EOQ -->|initial inventory delays| FirstOrder[First order timing]
    EOQ -->|finite horizon requires| IntegerOrders[Integer number of orders]

    EOQ -->|extended by| ProductionSystems[Production systems and batching]
    ProductionSystems -->|position inventory| MTS[Make-to-stock]
    ProductionSystems -->|position inventory| ATO[Assemble-to-order]
    ProductionSystems -->|position inventory| MTO[Make-to-order]
    ProductionSystems -->|position inventory| ETO[Engineer-to-order]
    ProductionSystems -->|trade off| CustomerLeadTime[Customer lead time]
    ProductionSystems -->|trade off| InventoryInvestment[Inventory investment]
    ProductionSystems -->|batch logic| BatchQueue[Batch-and-queue]
    BatchQueue -->|reduces| SetupFrequency[Setup frequency]
    BatchQueue -->|increases| WIP[WIP and waiting]
    BatchQueue -->|modeled by| EPQ[EPQ]
    EPQ -->|finite production rate| ProductionRate[p]
    ProductionRate -->|with demand creates| NetBuildRate[p-lambda]
    NetBuildRate -->|determines| MaxInventory[Imax]
    MaxInventory -->|changes| EPQFormula[Q*=EOQ*sqrt(p/(p-lambda))]

    BatchQueue -->|can amplify upstream signals through| OrderBatching[Order batching]
    OrderBatching -->|is a cause of| Bullwhip[Bullwhip effect]
    Bullwhip -->|means higher upstream| OrderVolatility[Order volatility / CV]
    Bullwhip -->|caused by| OrderSync[Order synchronization]
    Bullwhip -->|caused by| ForwardBuying[Trade promotions and forward buying]
    Bullwhip -->|caused by| ShortageGaming[Shortage gaming]
    Bullwhip -->|caused by| ReactiveOrdering[Reactive and over-reactive ordering]
    Bullwhip -->|worsens| CapacityDecisions[Suboptimal capacity decisions]
    Bullwhip -->|increases| SafetyStocks[Safety stocks]
    Bullwhip -->|increases| LogisticsCosts[Upstream logistics and purchasing costs]
    Bullwhip -->|mitigated by| InfoSharing[POS / EDI / CPFR]
    Bullwhip -->|mitigated by| SmoothFlow[VMI / EDLP / Lean flow]
    Bullwhip -->|mitigated by| IncentiveAlignment[Promotion, return, turn-and-earn policies]

    ProcessFlow -->|applied in service case| OceanCove[OceanCove process analysis]
    OceanCove -->|uses| ValueMap[Value map]
    OceanCove -->|uses| LittlesLaw[Little's Law I=R*T]
    OceanCove -->|calculates| ServiceCapacity[Service capacity]
    ServiceCapacity -->|finds| ServiceBottleneck[Service bottleneck]
    ServiceBottleneck -->|drives| ServiceLeadTime[Service lead time and waiting]
    ServiceCapacity -->|supports| CapacityExpansion[Capacity expansion recommendation]

    Capacity -->|becomes network constraint in| FacilityLocation[Facility location and transportation]
    FacilityLocation -->|uses| TransportLP[Transportation LP]
    TransportLP -->|decision variable| Xij[x_ij shipments]
    TransportLP -->|requires| DemandConstraints[Demand constraints]
    TransportLP -->|requires| CapacityConstraints[Capacity constraints]
    FacilityLocation -->|adds fixed opening decisions in| CPLP[CPLP]
    CPLP -->|binary variable| Yi[y_i open facility]
    Yi -->|activates| CapacityActivation[q_i y_i]
    FacilityLocation -->|multi-tier extension| TwoEchelon[Two-echelon location model]
    FacilityLocation -->|coverage model| Covering[Location covering problem]
    Covering -->|uses| CoverageMatrix[a_ij coverage matrix]
    FacilityLocation -->|routing model| Dijkstra[Dijkstra shortest path]
    FacilityLocation -->|routing model| TSP[Traveling Salesman Problem]
    TSP -->|requires| SubtourElimination[Subtour elimination]
    FacilityLocation -->|selection model| Knapsack[Knapsack]

    SCM -->|designs financial flows with| SupplyChainFinance[Supply chain finance]
    SupplyChainFinance -->|improves| WorkingCapital[Working capital]
    WorkingCapital -->|depends on| DSO[Days sales outstanding]
    WorkingCapital -->|depends on| DPO[Days payable outstanding]
    SupplyChainFinance -->|often uses| ReverseFactoring[Reverse factoring]
    ReverseFactoring -->|pays early| SupplierLiquidity[Supplier liquidity]
    ReverseFactoring -->|uses| BuyerCredit[Buyer credit quality]
    SupplyChainFinance -->|requires| SupplierAdoption[Supplier adoption speed]
    SupplierAdoption -->|driven by| EfficiencyMotive[Efficiency motive]
    SupplierAdoption -->|driven by| LegitimacyMotive[Legitimacy motive]

    SCM -->|protects against disruptions through| SupplyChainResilience[Supply chain resilience]
    SupplyChainResilience -->|trades off with extreme| LeanTradeoff[Lean efficiency]
    SupplyChainResilience -->|strategy| Redundancy[Redundancy]
    SupplyChainResilience -->|strategy| Flexibility[Flexibility]
    SupplyChainResilience -->|uses| VulnerabilityMap[Vulnerability map]
    SupplyChainResilience -->|uses framework| Blackhurst[Blackhurst enhancers and reducers]
    SupplyChainResilience -->|uses archetypes| TripleP[Triple-p archetypes]
    TripleP -->|process complexity| ProcessStandardization[Process standardization]
    TripleP -->|partnership complexity| VisibilityEnhancement[Visibility enhancement]
    TripleP -->|product complexity| FootprintDiversification[Footprint diversification]
    SupplyChainResilience -->|requires finding| HiddenBottleneck[Hidden bottleneck]

    SCM -->|improves flow through| LeanManagement[Lean management]
    LeanManagement -->|starts with| LeanValue[Customer value]
    LeanManagement -->|maps| LeanValueStream[Value stream]
    LeanValueStream -->|reveals| Muda[Muda / seven wastes]
    LeanManagement -->|creates| LeanFlow[Flow]
    LeanManagement -->|uses| PullProduction[Pull production]
    PullProduction -->|controlled by| Kanban[Kanban]
    LeanManagement -->|pursues| LeanPerfection[Perfection]
    LeanManagement -->|redesign option| ManufacturingCells[Manufacturing cells]
    LeanManagement -->|incremental improvement| Kaizen[Kaizen]
    LeanManagement -->|radical change| Kaikaku[Kaikaku]
    LeanManagement -->|prevents errors with| PokaYoke[Poka-yoke]
    LeanFlow -->|supported by| Standardization[Standardization]
    LeanFlow -->|paced by| TaktTime[Takt time]
    LeanFlow -->|requires| VisualControl[Visual control]

    SCM -->|is practiced through| SampleExamPractice[Sample exam practice]
    SampleExamPractice -->|routes to| Forecasting
    SampleExamPractice -->|routes to| OrderUpTo
    SampleExamPractice -->|routes to| EOQ
    SampleExamPractice -->|routes to| OceanCove
    SampleExamPractice -->|routes to| FacilityLocation
    SampleExamPractice -->|routes to| SupplyChainFinance
    SampleExamPractice -->|routes to| LeanManagement
```

## Decision Flow View

```mermaid
flowchart TD
    Start[Supply chain decision] --> DemandKnown{Is demand known and deterministic?}

    DemandKnown -->|No| Forecast[Forecast demand]
    Forecast --> Evaluate[Evaluate ME, MAD, MSE]
    Evaluate --> SelectForecast[Select suitable method on same validation window]
    SelectForecast --> Monitor[Monitor errors with control limits]
    Forecast --> ModelUncertainty[Model demand uncertainty]
    ModelUncertainty --> DistributionChoice{Which distribution fits?}
    DistributionChoice -->|count arrivals| PoissonModel[Poisson]
    DistributionChoice -->|rough bounded range| UniformModel[Uniform]
    DistributionChoice -->|high-volume aggregate| NormalModel[Normal]
    PoissonModel --> CDFStep[Compute CDF/service level]
    UniformModel --> CDFStep
    NormalModel --> ZStep[Use z-score]
    ZStep --> CDFStep
    CDFStep --> NewsvendorDecision[Newsvendor if single-period uncertain order]
    NewsvendorDecision --> Costs[Compute c_u and c_o]
    Costs --> SL[SL=c_u/(c_u+c_o)]
    SL --> Quantile[Q*=F^-1(SL)]
    CDFStep --> OUTDecision[Order-up-to if repeated replenishment with lead time]
    OUTDecision --> LeadDemand[Aggregate demand over l+1 periods]
    LeadDemand --> OUTSL[Choose cost-based or rule-of-thumb service level]
    OUTSL --> OUTS[S=F^-1(SL)]
    OUTS --> OUTState[Use inventory position to order]
    OUTS --> OUTMeasures[Compute F(S), B(S), and I(S)]

    DemandKnown -->|Yes| DeterministicInv[Deterministic inventory planning]
    DeterministicInv --> EOQDecision{Instant replenishment?}
    EOQDecision -->|Yes| BasicEOQ[Use EOQ]
    BasicEOQ --> EOQQ[Q*=sqrt(2Klambda/h)]
    BasicEOQ --> Lead{Lead time?}
    Lead -->|Yes| ROP[Reorder point=lambda*l]
    BasicEOQ --> Horizon{Finite horizon?}
    Horizon -->|Yes| Finite[Compute m_hat and check floor/ceil]

    EOQDecision -->|No, finite production rate| EPQDecision[Use EPQ]
    EPQDecision --> EPQQ[Q*=sqrt(2Klambda/h)*sqrt(p/(p-lambda))]
    EPQDecision --> BatchImplication[Interpret setup vs WIP/lead-time tradeoff]
    BatchImplication --> CoordinationRisk{Could local decisions distort upstream orders?}
    CoordinationRisk -->|Yes| BullwhipDiagnosis[Diagnose bullwhip cause]
    BullwhipDiagnosis --> CauseType{Cause type?}
    CauseType -->|Order batching/synchronization| SmoothOrders[Smooth ordering and product flow]
    CauseType -->|Promotion or shortage gaming| AlignIncentives[Redesign incentives and policies]
    CauseType -->|Information distortion| ShareInfo[Share POS data, EDI, or CPFR]
    SmoothOrders --> BullwhipMitigation[Reduce order variability amplification]
    AlignIncentives --> BullwhipMitigation
    ShareInfo --> BullwhipMitigation

    Start --> ProcessQuestion{Is this a process-capacity case?}
    ProcessQuestion -->|Yes| ProcessMap[Map flow unit, activities, queues]
    ProcessMap --> LL[Use Little's Law when I, R, T are linked]
    ProcessMap --> CapTable[Compute resource capacities]
    CapTable --> BN[Find bottleneck]
    BN --> CapacityDecision[Recommend bottleneck or expansion action]

    Start --> NetworkQuestion{Is this a network design or routing case?}
    NetworkQuestion -->|Ship from fixed facilities| LPModel[Form transportation LP]
    LPModel --> LPConstraints[Demand and capacity constraints]
    NetworkQuestion -->|Open facilities and ship| CPLPModel[Form CPLP with x_ij and y_i]
    CPLPModel --> OpenLink[Link shipments to q_i y_i]
    NetworkQuestion -->|Cover customers| CoverModel[Use covering model and heuristic]
    NetworkQuestion -->|Shortest origin-destination route| DijkstraFlow[Use Dijkstra]
    NetworkQuestion -->|Visit all customers| TSPFlow[Use TSP and prevent subtours]

    Start --> FinanceFlowQuestion{Is cash flow the constraint?}
    FinanceFlowQuestion -->|Yes| WCModel[Compute AR, AP, DSO, DPO, and NWC]
    WCModel --> SCFChoice{Can buyer credit improve supplier financing?}
    SCFChoice -->|Yes| ReverseFactoringFlow[Design reverse factoring / SCF program]
    SCFChoice -->|No| ReceivablesOrTerms[Assess receivables finance or term changes]

    Start --> ResilienceQuestion{Is disruption risk central?}
    ResilienceQuestion -->|Yes| BottleneckSearch[Find obvious and hidden bottlenecks]
    BottleneckSearch --> ComplexityType{Dominant complexity?}
    ComplexityType -->|Process| Standardize[Use process standardization]
    ComplexityType -->|Partnership| Visibility[Use visibility enhancement]
    ComplexityType -->|Product| Diversify[Use footprint diversification]
    ResilienceQuestion --> StrategyChoice{Need buffer or adaptability?}
    StrategyChoice -->|Buffer| RedundancyFlow[Use redundancy]
    StrategyChoice -->|Adaptability| FlexibilityFlow[Use flexibility]

    Start --> LeanQuestion{Is the prompt about waste, flow, or pull?}
    LeanQuestion -->|Yes| ValueFirst[Define customer value]
    ValueFirst --> StreamMap[Map value stream]
    StreamMap --> WasteClass[Classify muda]
    WasteClass --> LeanTool{Which lean mechanism fits?}
    LeanTool -->|Demand-triggered replenishment| KanbanFlow[Use Kanban / pull]
    LeanTool -->|Radical layout change| CellFlow[Use manufacturing cells / Kaikaku]
    LeanTool -->|Error prevention| PokaFlow[Use Poka-yoke]
    LeanTool -->|Ongoing refinement| KaizenFlow[Use Kaizen]

    Start --> ExamQuestion{Is this sample-exam practice?}
    ExamQuestion -->|Yes| RouteModel[Name the model first]
    RouteModel --> FormulaSetup[Write formula and align units]
    FormulaSetup --> InterpretResult[Interpret operational consequence]
```

## Subject Graph Index

| Subject / Deck | Wiki Note | Main Visual Logic | Last Updated |
|---|---|---|---|
| Topic 01 Kristen Cookies Company Case | `topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md` | Process flow -> bottleneck -> cycle time/capacity -> improvement logic | 2026-05-14 |
| Topic 02 Forecasting | `topic-02-forecasting/topic-02-forecasting.md` | Demand uncertainty -> forecast methods -> error metrics -> monitoring | 2026-05-14 |
| Topic 03 Newsvendor Model | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` | Forecast distribution -> underage/overage tradeoff -> service level -> order quantity | 2026-05-14 |
| Topic 04 Modeling Uncertain Demand With Random Variables | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` | Real demand -> random variable -> distribution -> CDF/service level -> inventory decision | 2026-05-14 |
| Topic 05 EOQ, Production Systems, And Batching | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` | Deterministic demand -> setup/holding tradeoff -> EOQ -> lead time/finite horizon -> EPQ/batching | 2026-06-04 |
| Topic 06 Supply Chain Coordination And The Bullwhip Effect | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` | Local ordering behavior -> upstream variability amplification -> coordination through information, flow, and incentives | 2026-06-04 |
| Topic 08 OceanCove Process Analysis And Capacity Management | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` | Value map -> process flow -> Little's Law -> capacity table -> bottleneck -> expansion decision | 2026-06-04 |
| Topic 09 Facility Location, Transportation, And Shipping | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` | Network decision -> LP/CPLP/covering/routing model -> variables and constraints -> operational interpretation | 2026-06-04 |
| Topic 10 Multi-Period Inventory Management And Order-Up-To Model | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` | Demand over l+1 periods -> service level -> order-up-to level S -> inventory position and performance measures | 2026-06-04 |
| Topic 12 Supply Chain Finance And Resilience | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` | Working-capital gap -> SCF/reverse factoring -> supplier adoption; disruption risk -> redundancy/flexibility/triple-p/hidden bottlenecks | 2026-06-04 |
| Topic 13 Lean Management And Lean Simulation | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` | Value -> value stream -> muda -> flow -> pull/Kanban -> Kaizen/Kaikaku/Poka-yoke | 2026-06-04 |
| Sample Examinations Exam Practice | `sample-examinations-exam-practice/sample-examinations-exam-practice.md` | Exam routing -> MCQ traps -> numerical methods -> case recommendations | 2026-06-04 |

## Supporting Node Reference

| Node | Meaning | Source Note |
|---|---|---|
| Kristen Cookies Case | Make-to-order cookie operation used to study process flow and capacity | `topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md` |
| Process Flow | Ordered sequence of operational steps, waits, and buffers | `topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md` |
| Bottleneck | Resource limiting system capacity | `topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md` |
| Forecasting | Estimating future demand for operational decisions | `topic-02-forecasting/topic-02-forecasting.md` |
| ME | Mean signed error; bias | `topic-02-forecasting/topic-02-forecasting.md` |
| MAD | Mean absolute deviation; typical absolute miss | `topic-02-forecasting/topic-02-forecasting.md` |
| MSE | Mean squared error; large-error penalty | `topic-02-forecasting/topic-02-forecasting.md` |
| Control Limits | Bounds for forecast-error monitoring | `topic-02-forecasting/topic-02-forecasting.md` |
| Newsvendor Model | Single-period order decision under uncertain demand | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Underage Cost | Cost of ordering one unit too few | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Overage Cost | Cost of ordering one unit too many | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Critical Fractile | `c_u / (c_u + c_o)` | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Random Variable | Function mapping uncertain outcomes to numbers | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| Poisson Distribution | Count-demand model with parameter `lambda` | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| Uniform Distribution | Equal-density model over interval `[A, B]` | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| Normal Distribution | Bell-shaped model with `mu` and `sigma` | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| CDF | `F(q)=P(D<=q)`; service level at stock/order quantity q | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| EOQ | Deterministic order quantity model | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Reorder Point | Inventory level for placing order under deterministic lead time | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Finite Horizon | Inventory problem with limited selling period and integer orders | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Production Systems | Make-to-stock, assemble-to-order, make-to-order, engineer-to-order positioning | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| EPQ | EOQ extension with finite production rate | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Bullwhip Effect | Upstream amplification of demand/order variability | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Order Batching | Lumpy ordering behavior that can amplify upstream signals | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Forward Buying | Buying ahead during promotions, creating an artificial order spike | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Shortage Gaming | Inflating orders during scarcity to receive a larger allocation | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| POS / EDI / CPFR | Information-sharing mechanisms for reducing bullwhip | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| VMI / EDLP / Lean Flow | Flow-smoothing mechanisms for reducing bullwhip | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Little's Law | `I = R*T`; links inventory, flow rate, and flow time | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Service Bottleneck | Lowest-capacity required service resource | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Lead Time | Waiting plus processing time from order/customer start to completion | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Plant Location LP | Continuous model choosing shipment quantities from plants to customers | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| CPLP | Facility-opening plus shipment model with fixed costs and capacities | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Location Covering Problem | Binary model selecting facilities so every customer is covered | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Dijkstra's Algorithm | Shortest-path algorithm for one origin and destination | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| TSP | Shortest tour visiting every required customer exactly once | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Knapsack | Binary selection model maximizing value under capacity | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Order-Up-To Model | Multi-period replenishment policy restoring inventory position to target `S` | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Inventory Position | On-order plus on-hand minus backorders; state variable for ordering | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Demand Over `l+1` Periods | Demand exposure horizon in the order-up-to model | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Expected Backorders | Expected unmet units at period end, `B(S)` | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Supply Chain Finance | Structured working-capital and supplier-liquidity design across buyer-supplier networks | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Reverse Factoring | Buyer-led financing of approved supplier invoices | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Working Capital | Operating capital tied in receivables, inventory, and payables | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Supplier Adoption Speed | How quickly suppliers join an SCF program | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Supply Chain Resilience | Ability to absorb, respond to, recover from, and adapt after disruptions | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Redundancy | Resilience through extra inventory, suppliers, capacity, or assets | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Flexibility | Resilience through switching, reconfiguration, and adaptive response | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Triple-P Archetypes | Process, partnership, and product complexity categories for resilience strategy choice | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Hidden Bottleneck | Non-obvious constraint exposed by disruption or demand shift | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Lean Management | Customer-value and waste-removal system for improving flow, pull, quality, and continuous improvement | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Muda | Waste in the value stream | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kanban | Visual replenishment signal and WIP/queue limiter | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kaizen | Continuous incremental improvement | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kaikaku | Radical process or layout change | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Poka-yoke | Mistake-proofing to prevent defects | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Manufacturing Cells | Product-flow-oriented production layout | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Sample Exam Practice | Routing skill for MCQ traps, numerical methods, and case recommendations | `sample-examinations-exam-practice/sample-examinations-exam-practice.md` |

## Supporting Edge Reference

| From | Relationship | To | Source Note |
|---|---|---|---|
| Bottleneck | determines | System Capacity | `topic-01-kristen-cookie-case/topic-01-kristen-cookie-case.md` |
| Forecast Error | is measured by | ME / MAD / MSE | `topic-02-forecasting/topic-02-forecasting.md` |
| MAD / MSE | support | Forecast Method Selection | `topic-02-forecasting/topic-02-forecasting.md` |
| Control Limits | monitor | Forecast Method Stability | `topic-02-forecasting/topic-02-forecasting.md` |
| Forecast Distribution | feeds | Newsvendor Model | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Underage Cost | increases | Service Level | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Overage Cost | decreases | Service Level | `topic-03-newsvendor-model/topic-03-newsvendor-model.md` |
| Random Variable | models | Real-life uncertain demand | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| CDF | gives | Service Level | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| z-score | converts | General normal to standard normal | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| Poisson Distribution | can be approximated by | Normal Distribution when lambda is large | `topic-04-modeling-uncertain-demand-random-variables/topic-04-modeling-uncertain-demand-random-variables.md` |
| EOQ | balances | Setup/order cost and holding cost | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Lead Time | determines | Reorder Point | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Finite Horizon | requires | Integer order decision | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Batch-And-Queue | reduces | Setup frequency | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Batch-And-Queue | increases | WIP and waiting | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| EPQ | extends | EOQ with finite production rate | `topic-05-eoq-production-systems-batching/topic-05-eoq-production-systems-batching.md` |
| Order batching | can cause | Bullwhip Effect | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Trade promotions | cause | Forward buying | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Shortage gaming | inflates | Orders during scarcity | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Bullwhip Effect | increases | Safety stock, logistics costs, and capacity mistakes | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| POS / EDI / CPFR | reduce | Information distortion | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| VMI / EDLP / Lean Flow | smooth | Product flow and order signals | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Incentive alignment | reduces | Pathological ordering behavior | `topic-06-supply-chain-coordination-bullwhip-effect/topic-06-supply-chain-coordination-bullwhip-effect.md` |
| Process Flow Diagram | supports | Bottleneck identification | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Little's Law | links | Average inventory, flow rate, and flow time | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Service Bottleneck | determines | System capacity | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Waiting inventory | increases | Lead time | `topic-08-oceancove-process-analysis-capacity-management/topic-08-oceancove-process-analysis-capacity-management.md` |
| Plant Location LP | uses | Shipment variables `x_ij` | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| CPLP | adds | Binary open variables `y_i` | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Capacity activation `q_i y_i` | prevents | Shipments from closed facilities | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Location covering problem | uses | Coverage matrix `a_ij` | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Dijkstra's Algorithm | solves | Shortest path | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| TSP | requires | Subtour elimination | `topic-09-facility-location-transportation-shipping/topic-09-facility-location-transportation-shipping.md` |
| Lead Time | creates exposure to | Demand over `l+1` periods | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Order-Up-To Model | targets | Order-up-to level `S` | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Inventory Position | determines | Period order quantity | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Cost-based service level | determines | Order-up-to level `S` | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Expected Backorders | help compute | Expected leftover inventory | `topic-10-multi-period-inventory-management-order-up-to-model/topic-10-multi-period-inventory-management-order-up-to-model.md` |
| Working Capital | is affected by | DSO and DPO | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Reverse Factoring | uses | Buyer credit quality | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Reverse Factoring | improves | Supplier liquidity | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Supplier Adoption Speed | is driven by | Efficiency and legitimacy motives | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Redundancy | increases | Disruption absorption | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Flexibility | improves | Resource reconfiguration | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Triple-P Archetypes | determine | Resilience strategy choice | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Hidden Bottleneck | constrains | Disruption recovery | `topic-12-supply-chain-finance-and-resilience/topic-12-supply-chain-finance-and-resilience.md` |
| Lean Management | starts with | Customer value | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Value Stream | reveals | Muda | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kanban | enables | Pull production | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Manufacturing Cells | improve | Flow | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Poka-yoke | prevents | Defect waste | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kaikaku | creates | Radical process redesign | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Kaizen | sustains | Continuous improvement | `topic-13-lean-management-lean-simulation/topic-13-lean-management-lean-simulation.md` |
| Sample Exam Practice | requires | Model routing before formulas | `sample-examinations-exam-practice/sample-examinations-exam-practice.md` |
| Sample Exam Practice | combines | MCQ traps, numerical methods, and case recommendations | `sample-examinations-exam-practice/sample-examinations-exam-practice.md` |

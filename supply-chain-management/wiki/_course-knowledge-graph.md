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
```

## Subject Graph Index

| Subject / Deck | Wiki Note | Main Visual Logic | Last Updated |
|---|---|---|---|
| Topic 01 Kristen Cookies Company Case | `topic-01-kristen-cookie-case.md` | Process flow -> bottleneck -> cycle time/capacity -> improvement logic | 2026-05-14 |
| Topic 02 Forecasting | `topic-02-forecasting.md` | Demand uncertainty -> forecast methods -> error metrics -> monitoring | 2026-05-14 |
| Topic 03 Newsvendor Model | `topic-03-newsvendor-model.md` | Forecast distribution -> underage/overage tradeoff -> service level -> order quantity | 2026-05-14 |
| Topic 04 Modeling Uncertain Demand With Random Variables | `topic-04-modeling-uncertain-demand-random-variables.md` | Real demand -> random variable -> distribution -> CDF/service level -> inventory decision | 2026-05-14 |
| Topic 05 EOQ, Production Systems, And Batching | `topic-05-eoq-production-systems-batching.md` | Deterministic demand -> setup/holding tradeoff -> EOQ -> lead time/finite horizon -> EPQ/batching | 2026-05-14 |

## Supporting Node Reference

| Node | Meaning | Source Note |
|---|---|---|
| Kristen Cookies Case | Make-to-order cookie operation used to study process flow and capacity | `topic-01-kristen-cookie-case.md` |
| Process Flow | Ordered sequence of operational steps, waits, and buffers | `topic-01-kristen-cookie-case.md` |
| Bottleneck | Resource limiting system capacity | `topic-01-kristen-cookie-case.md` |
| Forecasting | Estimating future demand for operational decisions | `topic-02-forecasting.md` |
| ME | Mean signed error; bias | `topic-02-forecasting.md` |
| MAD | Mean absolute deviation; typical absolute miss | `topic-02-forecasting.md` |
| MSE | Mean squared error; large-error penalty | `topic-02-forecasting.md` |
| Control Limits | Bounds for forecast-error monitoring | `topic-02-forecasting.md` |
| Newsvendor Model | Single-period order decision under uncertain demand | `topic-03-newsvendor-model.md` |
| Underage Cost | Cost of ordering one unit too few | `topic-03-newsvendor-model.md` |
| Overage Cost | Cost of ordering one unit too many | `topic-03-newsvendor-model.md` |
| Critical Fractile | `c_u / (c_u + c_o)` | `topic-03-newsvendor-model.md` |
| Random Variable | Function mapping uncertain outcomes to numbers | `topic-04-modeling-uncertain-demand-random-variables.md` |
| Poisson Distribution | Count-demand model with parameter `lambda` | `topic-04-modeling-uncertain-demand-random-variables.md` |
| Uniform Distribution | Equal-density model over interval `[A, B]` | `topic-04-modeling-uncertain-demand-random-variables.md` |
| Normal Distribution | Bell-shaped model with `mu` and `sigma` | `topic-04-modeling-uncertain-demand-random-variables.md` |
| CDF | `F(q)=P(D<=q)`; service level at stock/order quantity q | `topic-04-modeling-uncertain-demand-random-variables.md` |
| EOQ | Deterministic order quantity model | `topic-05-eoq-production-systems-batching.md` |
| Reorder Point | Inventory level for placing order under deterministic lead time | `topic-05-eoq-production-systems-batching.md` |
| Finite Horizon | Inventory problem with limited selling period and integer orders | `topic-05-eoq-production-systems-batching.md` |
| Production Systems | Make-to-stock, assemble-to-order, make-to-order, engineer-to-order positioning | `topic-05-eoq-production-systems-batching.md` |
| EPQ | EOQ extension with finite production rate | `topic-05-eoq-production-systems-batching.md` |

## Supporting Edge Reference

| From | Relationship | To | Source Note |
|---|---|---|---|
| Bottleneck | determines | System Capacity | `topic-01-kristen-cookie-case.md` |
| Forecast Error | is measured by | ME / MAD / MSE | `topic-02-forecasting.md` |
| MAD / MSE | support | Forecast Method Selection | `topic-02-forecasting.md` |
| Control Limits | monitor | Forecast Method Stability | `topic-02-forecasting.md` |
| Forecast Distribution | feeds | Newsvendor Model | `topic-03-newsvendor-model.md` |
| Underage Cost | increases | Service Level | `topic-03-newsvendor-model.md` |
| Overage Cost | decreases | Service Level | `topic-03-newsvendor-model.md` |
| Random Variable | models | Real-life uncertain demand | `topic-04-modeling-uncertain-demand-random-variables.md` |
| CDF | gives | Service Level | `topic-04-modeling-uncertain-demand-random-variables.md` |
| z-score | converts | General normal to standard normal | `topic-04-modeling-uncertain-demand-random-variables.md` |
| Poisson Distribution | can be approximated by | Normal Distribution when lambda is large | `topic-04-modeling-uncertain-demand-random-variables.md` |
| EOQ | balances | Setup/order cost and holding cost | `topic-05-eoq-production-systems-batching.md` |
| Lead Time | determines | Reorder Point | `topic-05-eoq-production-systems-batching.md` |
| Finite Horizon | requires | Integer order decision | `topic-05-eoq-production-systems-batching.md` |
| Batch-And-Queue | reduces | Setup frequency | `topic-05-eoq-production-systems-batching.md` |
| Batch-And-Queue | increases | WIP and waiting | `topic-05-eoq-production-systems-batching.md` |
| EPQ | extends | EOQ with finite production rate | `topic-05-eoq-production-systems-batching.md` |

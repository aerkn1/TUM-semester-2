# Active Recall Session: Topic 02 Forecasting

Course: Supply Chain Management
Wiki note: `supply-chain-management/wiki/topic-02-forecasting/topic-02-forecasting.md`
Date: 2026-05-14
Session type: `first-pass`

## Session Focus

Build quantitative intuition for forecasting through a small coffee-shop muffin demand example.

## Example Data

Actual demand:

| Day | Actual Demand |
|---:|---:|
| 1 | 40 |
| 2 | 44 |
| 3 | 43 |
| 4 | 47 |
| 5 | 50 |

Naive forecast rule:

```text
Tomorrow = today
F_t = A_{t-1}
```

Naive forecasts:

| Day | Forecast |
|---:|---:|
| 2 | 40 |
| 3 | 44 |
| 4 | 43 |
| 5 | 47 |

Error formula:

```text
e_t = A_t - F_t
```

## User Answers

### Error Calculation

Prompt:

Calculate errors for Days 2-5.

User answer:

> day 3 = -1
> day4 = 4
> day5=3

Feedback:

- Quality: `green-yellow`
- Day 3, Day 4, and Day 5 are correct.
- Day 2 was skipped.

Correct errors:

| Day | Error |
|---:|---:|
| 2 | 4 |
| 3 | -1 |
| 4 | 4 |
| 5 | 3 |

### ME, MAD, MSE

Prompt:

Compute ME, MAD, and MSE from errors `4, -1, 4, 3`.

User answer:

> ME= 2.5
> mad =3
> MSE= 16 + 1 + 16 + 9 / 4 = 42/4  =  10.25

Feedback:

- ME quality: `green`; `(4 - 1 + 4 + 3) / 4 = 2.5`.
- MAD quality: `green`; `(4 + 1 + 4 + 3) / 4 = 3`.
- MSE quality: `yellow`; the setup is correct, but `42 / 4 = 10.5`, not `10.25`.

Correct metrics:

```text
ME = 2.5
MAD = 3
MSE = 10.5
```

Interpretation:

```text
ME > 0 means the naive forecast is underforecasting on average.
MAD = 3 means typical absolute miss is 3 muffins.
MSE = 10.5 punishes the larger errors of 4 more strongly.
```

### Two-Day Moving Average

Prompt:

Use a 2-day moving average:

```text
F_t = average of the last 2 actual demand values
```

User answer:

> f3= 42
> f4 = 43.5
> f5 = 45

Feedback:

- Quality: `green`; all forecasts are correct.

Correct forecasts:

| Day | Formula | Forecast |
|---:|---|---:|
| 3 | `(40 + 44) / 2` | 42 |
| 4 | `(44 + 43) / 2` | 43.5 |
| 5 | `(43 + 47) / 2` | 45 |

Prompt:

Compute errors for Days 3-5.

User answer:

> e3=1
> e4=3.5
> e5=5

Feedback:

- Quality: `green`; all errors are correct.

Correct errors:

| Day | Error |
|---:|---:|
| 3 | 1 |
| 4 | 3.5 |
| 5 | 5 |

Prompt:

Compute MAD.

User answer:

> mad = 3.1 for moving average

Feedback:

- Quality: `green-yellow`; the interpretation is right, but exact MAD is `9.5 / 3 = 3.17`.
- Compared with naive MAD of `3`, the 2-day moving average is slightly worse in this small data set.

Key interpretation:

```text
Moving average smooths noise, but it can lag when demand is trending upward.
```

### Naive With Trend

Prompt:

Use naive with trend:

```text
F_t = A_{t-1} + (A_{t-1} - A_{t-2})
```

User answer:

> f3=48
> f4=44
> f5=51

Feedback:

- Quality: `yellow`; Day 3 and Day 5 are correct, Day 4 has a sign error.

Correct forecasts:

| Day | Formula | Forecast |
|---:|---|---:|
| 3 | `44 + (44 - 40)` | 48 |
| 4 | `43 + (43 - 44)` | 42 |
| 5 | `47 + (47 - 43)` | 51 |

Prompt:

Compute errors for Days 3-5.

User answer:

> e3=5
> e4=5
> e5= -1

Feedback:

- Quality: `yellow`; Day 4 and Day 5 are correct if using the corrected forecast table.
- Day 3 has the wrong sign under the course convention `e_t = A_t - F_t`.

Correct errors:

| Day | Actual | Forecast | Error |
|---:|---:|---:|---:|
| 3 | 43 | 48 | -5 |
| 4 | 47 | 42 | 5 |
| 5 | 50 | 51 | -1 |

Prompt:

Compute ME and MAD for naive with trend.

User answer:

> ME = -1 / 3 = -0.3333
> MAD = 11/3 = 3.7
>
> almost same with moving average

Feedback:

- ME quality: `green`; `(-5 + 5 - 1) / 3 = -1 / 3 = -0.33`.
- MAD quality: `green`; `(5 + 5 + 1) / 3 = 11 / 3 = 3.67`.
- Interpretation quality: `yellow`; it is close in scale, but worse than both naive and 2-day moving average in this example.

Comparison:

| Method | MAD | Interpretation |
|---|---:|---|
| Naive | 3.00 | Best on this small example |
| 2-day moving average | 3.17 | Slightly worse; lags upward trend |
| Naive with trend | 3.67 | Worst here; overreacts to short-term changes |

Key interpretation:

```text
Naive with trend reacts strongly to the last observed change. It can help when the trend is stable, but it can overreact when the last change was temporary.
```

### Exponential Smoothing

Prompt:

Use exponential smoothing with `alpha = 0.5` and `F2 = 40`.

```text
F_t = alpha * A_{t-1} + (1 - alpha) * F_{t-1}
```

User answer:

> f3 = 0.5 * 44 + 0.5 * 40 = 22 + 20 = 42
> f4 = 0.5 * 43 + 0.5 * 42 = 21.5 + 21 = 42.5
> f5 = 0.5 * 47 + 0.5 * 42.5 = 23.5 + 21.25 = 44.75

Feedback:

- Quality: `green`; all forecasts are correct.

Correct forecasts:

| Day | Formula | Forecast |
|---:|---|---:|
| 3 | `0.5 * 44 + 0.5 * 40` | 42 |
| 4 | `0.5 * 43 + 0.5 * 42` | 42.5 |
| 5 | `0.5 * 47 + 0.5 * 42.5` | 44.75 |

Key interpretation:

```text
Exponential smoothing keeps memory of older demand through the previous forecast, but alpha controls how strongly the newest actual value pulls the next forecast.
```

Prompt:

Compute errors and MAD for exponential smoothing.

User answer:

> e3 = 43-42 = 1
> e4 = 47 - 42.5 = 4.5
> e5 = 50 - 44.75 = 5.25
>
> MAD =  16.27

Feedback:

- Error quality: `green`; all errors are correct.
- Metric quality: `yellow`; `16.27` is the MSE, not MAD.

Correct metrics:

```text
MAD = (|1| + |4.5| + |5.25|) / 3 = 10.75 / 3 = 3.58
MSE = (1^2 + 4.5^2 + 5.25^2) / 3 = 48.8125 / 3 = 16.27
```

Comparison so far:

| Method | MAD | MSE |
|---|---:|---:|
| Naive | 3.00 | 10.50 |
| 2-day moving average | 3.17 | not computed |
| Naive with trend | 3.67 | 17.00 |
| Exponential smoothing, `alpha = 0.5` | 3.58 | 16.27 |

### Regression Forecasting

Prompt:

Use a simple trend regression:

```text
F_t = 40 + 2t
```

Calculate `F_6` and `F_10`, then explain what the slope `2` means operationally.

User answer:

> f6 = 52
> f10 = 60

Feedback:

- Calculation quality: `green`; both forecasts are correct.
- Interpretation pending: explain the business meaning of the slope.

Correct calculations:

| Period | Formula | Forecast |
|---:|---|---:|
| 6 | `40 + 2 * 6` | 52 |
| 10 | `40 + 2 * 10` | 60 |

Key interpretation:

```text
The slope is the average demand change per time period. A slope of 2 means expected demand increases by 2 units each period.
```

Prompt:

Use regression with a weekend dummy variable:

```text
F_t = 40 + 2t + 10 * Weekend
Weekend = 1 if weekend, 0 otherwise
```

Calculate the forecast for `t = 6` on a weekday and on a weekend.

User answer:

> f6 = 52
> f6 weekend = 62

Feedback:

- Quality: `green`; both forecasts are correct.

Correct calculations:

| Case | Formula | Forecast |
|---|---|---:|
| Weekday, `t = 6` | `40 + 2 * 6 + 10 * 0` | 52 |
| Weekend, `t = 6` | `40 + 2 * 6 + 10 * 1` | 62 |

Key interpretation:

```text
The weekend dummy adds a fixed weekend uplift. Here, weekend demand is forecasted to be 10 units higher than an otherwise identical weekday.
```

### Control Limits

Prompt:

Given:

```text
Mean error = 0
RMSE = 4
95% control limits = mean error +/- 1.96 * RMSE
```

Calculate `UCL` and `LCL`, then decide what to do if a new error is `+3`.

User answer:

> + 7.97
> -7.97 interval
>
> changing methodloldy?

Feedback:

- Calculation quality: `yellow`; the structure is correct, but `1.96 * 4 = 7.84`, not `7.97`.
- Decision quality: `yellow`; an error of `+3` is inside the control limits, so this is not enough evidence to change the method.

Correct answer:

```text
UCL = 0 + 1.96 * 4 = 7.84
LCL = 0 - 1.96 * 4 = -7.84
```

Decision for new error `+3`:

```text
+3 is inside [-7.84, 7.84], so treat it as normal forecast noise. Do not change the method based on this single error.
```

Prompt:

Using the same control limits `[-7.84, +7.84]`, interpret a new forecast error of `+10`.

User answer:

> investigate the root cause as it goes out of the range interval and see if this is a systematic change or a one time seasonal or demand-supply arised cause etc.?

Feedback:

- Quality: `green`; this is the correct management response.

Correct interpretation:

```text
+10 exceeds the upper control limit, so the error is unusually large under the historical error distribution.
```

Correct action:

```text
Investigate the root cause before changing the forecasting method. Check for systematic demand shift, missing seasonal effect, promotion/event effect, data issue, supply disruption, or one-off shock.
```

Key interpretation:

```text
Control limits prevent overreaction. A manager should investigate or update the method only when errors exceed limits or show a persistent systematic pattern.
```

## Closing Synthesis

User synthesis:

> so as a conclusion, while determining the demand forecasting via the historical data, we have to go through all possible forecasting methodologies to check which one has the lover MAD. If it contains seasonality or systematic patterns, regression is better to formulate it and determine as a control limit interval for the up and down boundaries and monitor until the error goes out of this range ?

Refined exam-ready version:

```text
Forecasting is a cycle: identify the demand pattern, compare suitable methods using MAD/MSE on the same data window, choose the best-performing method for the objective, then monitor future errors with control limits to detect when the model may no longer fit reality.
```

Important refinements:

| Point | Correct version |
|---|---|
| Method selection | Do not test every possible method blindly; compare suitable methods for the observed pattern. |
| Error metric | Lower MAD means lower typical absolute error; lower MSE matters when large errors are especially costly. |
| Regression | Regression is useful when trend, seasonality, or systematic drivers can be represented in a formula. |
| Control limits | Control limits are for monitoring future forecast errors after method selection. |
| Manager response | If errors stay inside limits, treat them as normal noise; if they exceed limits or show repeated bias, investigate and possibly update the method. |

## Weak Spots

| Concept | Quality | Fix |
|---|---|---|
| Completing all periods | `yellow` | Do not skip the first forecastable period. |
| MSE arithmetic | `yellow` | Formula setup correct; recalculate division carefully. |
| Forecast error sign | `yellow` | Use course convention consistently: `e_t = A_t - F_t`. |
| Trend sign | `yellow` | In naive with trend, the trend term can be negative if the previous actual decreased. |
| MAD vs MSE | `yellow` | MAD averages absolute errors; MSE averages squared errors. |
| Control-limit arithmetic | `yellow` | `1.96 * 4 = 7.84`; check multiplication carefully. |
| Control-limit decision | `yellow` | Do not change the method for one error inside the limits. |

## D+1 Repair Pass: 2026-05-16

Session type: `spaced-repetition-repair`
Reason: D+1 checkpoint from 2026-05-15 was missed; repaired on 2026-05-16.

### User Raw Answers

1. Forecast error definition:

> error for possible expectations of demand for the future

Feedback:

- Quality: `yellow`
- Correction: forecast error is the realized difference between actual demand and forecast demand.
- Course convention: `e_t = A_t - F_t`.

2. ME, MAD, MSE:

> ME= bias for over or under forecasting , MAD = absolute error rate , MSE = exponential calculation to determine the penalization of the model fit

Feedback:

- ME quality: `green`; ME indicates average bias.
- MAD quality: `green-yellow`; MAD is average absolute error, not a rate unless normalized.
- MSE quality: `yellow`; MSE uses squared errors, not exponential calculation. It penalizes large errors more strongly because squaring magnifies them.

3. Error when actual demand is 50 and forecast is 44:

> 6

Feedback:

- Quality: `green`
- Correct: `e_t = 50 - 44 = 6`, meaning underforecasting by 6 units.

4. Why MSE punishes large errors more than MAD:

> because it is exponential calculation

Feedback:

- Quality: `yellow`
- Correction: because MSE squares each error. Example: error 2 becomes 4, error 6 becomes 36.

5. When to change forecasting method:

> if the error rate goes beyond the control limit intervals for expected error rates

Feedback:

- Quality: `green-yellow`
- Correct: errors outside control limits signal investigation.
- Refinement: also investigate repeated systematic patterns even if single errors are not extreme. Do not change methods after one ordinary bad forecast inside control limits.

### Repaired Mental Models

```text
Forecast error = actual - forecast.
ME = average signed error; bias indicator.
MAD = average absolute error; typical miss size.
MSE = average squared error; strongly penalizes large misses.
Control limits = monitoring tool; investigate out-of-control errors or systematic patterns.
```

### Remaining Weak Spots

| Concept | Quality | Fix |
|---|---|---|
| Forecast error definition | `yellow` | Say `actual minus forecast`, not generic expectation error. |
| MSE wording | `yellow` | Say squared error, not exponential error. |
| Control limits | `green-yellow` | Investigate out-of-limit or systematic pattern before changing method. |

### Next Recall Prompts

1. If `A_t = 38` and `F_t = 45`, what is `e_t` and what does the sign mean?
2. Compute ME, MAD, and MSE for errors `-2, 4, -6`.
3. Explain why a lower MAD is preferred when comparing methods on the same data window.
4. Give one reason regression beats moving average when seasonality exists.
5. Explain when a forecast-control chart should trigger investigation.

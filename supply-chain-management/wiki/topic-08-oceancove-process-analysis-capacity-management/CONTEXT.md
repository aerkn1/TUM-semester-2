# Ubiquitous Language: Topic 08 OceanCove Process Analysis And Capacity Management

Source note: `topic-08-oceancove-process-analysis-capacity-management.md`
Course: Supply Chain Management
Definition sources: OceanCove slides, capacity-management workbook, answer key; enriched with standard operations-management terminology where needed.

This file is a standalone terminology and formula companion for process analysis, Little's Law, capacity, utilization, bottlenecks, queues, and Gantt charts.

## Process Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Flow Unit** | The entity moving through the process, such as a customer, meal, order, ton of iron ore, or project activity. | resource, worker |
| **Process Flow Diagram** | Visual or textual map of activities, queues, decision points, and flows. | org chart |
| **Physical Flow** | Movement of the actual unit, such as food or material. | information flow |
| **Information Flow** | Movement of signals or orders, such as waiter tickets to the kitchen. | physical product |
| **Queue** | Units waiting before being processed. | inventory only |
| **Work-In-Process (WIP)** | Units started but not completed; in service cases, orders/customers waiting or being processed. | finished output |
| **Flow Time** | Average time a flow unit spends in the process. | processing time only |
| **Lead Time** | Time from request/order start to delivery/completion, including waiting and processing. | fastest processing time |

## Capacity Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Capacity** | Maximum sustainable output rate of a resource or process under stated assumptions. | demand, inventory |
| **Flow Rate (`R`)** | Average output or throughput per time period. | capacity |
| **Average Inventory (`I`)** | Average number of flow units in the process. | storage only |
| **Bottleneck** | Resource with the smallest required-process capacity; it constrains system output. | slow-looking step |
| **Utilization** | `flow rate / capacity`; the share of capacity being used. | capacity |
| **Parallel Resources** | Multiple identical or substitutable resources performing the same step, increasing capacity. | sequential resources |
| **System Capacity** | Capacity of the entire process, usually the minimum capacity among required steps. | sum of all capacities |
| **Mix Constraint** | Product mix relationship that affects effective capacity, such as grilled fish being twice as popular as fried fish. | average demand |
| **Occupancy Adjustment** | Conversion from theoretical seat-turn capacity to actual customer flow when average table occupancy is below full seating capacity. | utilization automatically |
| **Bottleneck Utilization** | Flow rate divided by the capacity of the process bottleneck; often used as shorthand for overall process utilization. | average of all utilizations |
| **Whole-Customer Capacity** | Capacity rounded or constrained to complete customer units when fractional service rates are not meaningful in the answer key. | exact decimal always |

## Formula Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Little's Law** | `I = R * T`; average inventory equals flow rate times flow time. | bottleneck formula |
| **Resource Capacity** | `number of parallel resources / processing time per unit`. | utilization |
| **Waiting Time From Queue** | `average waiting inventory / average flow rate`. | processing time |
| **Capacity Utilization** | `flow rate / capacity`, usually reported as a percentage. | total capacity |
| **Project Duration** | Calendar time from project start to completion, respecting precedence and resource availability. | sum of task durations |
| **Calculation Ladder** | Exam-answer structure: formula, substitution, arithmetic result, unit, and interpretation. | final answer only |

## Project Scheduling Language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Gantt Chart** | Calendar-based schedule showing when activities occur and which resources are assigned. | process flow diagram |
| **Predecessor Activity** | Activity that must be completed before another starts. | parallel task |
| **Resource Availability** | Calendar weeks or periods when a worker/resource can perform a task. | capacity rate |
| **Renovation On Hold** | A calendar gap where no task progresses despite the project not being complete. | normal waiting inside a process |

## Relationships Between Canonical Terms

- **Flow unit** must be defined before using **Little's Law**.
- **Capacity** is a maximum rate; **flow rate** is the actual or implied rate.
- **Bottleneck** determines **system capacity** only for required process steps.
- **Lead time** includes **queue** time and processing time.
- **Gantt chart** uses **predecessor activity** and **resource availability**, not only task duration.
- **Mix constraint** can turn multiple resource capacities into one effective menu or product capacity.
- **Occupancy adjustment** explains why 160 seat-turns/hour can become 120 customers/hour when tables average 3 occupied seats out of 4.
- **Bottleneck utilization** can differ from individual resource utilizations; non-bottlenecks usually have lower utilization at the same demand flow.

## Worked-Calculation Recall Standard

Use this standard for OceanCove, ProfiCutZ, Circored, Gantt scheduling, and similar capacity questions.

```text
1. Define the flow unit.
2. State the formula before using numbers.
3. Convert all time units into the same denominator.
4. Substitute values visibly.
5. Compute the result with units.
6. Interpret the operational meaning.
7. State the exam trap or boundary condition.
```

Capacity ladder:

```text
capacity = number of parallel resources / processing time per flow unit
capacity = n / (time in hours per unit)
result = units per hour
interpretation = compare with other required resources to find the bottleneck
```

Little's Law ladder:

```text
I = R x T
R = I / T
T = I / R
```

Use `I` for average inventory or WIP, `R` for flow rate, and `T` for flow time. Always attach the unit, for example customers/hour, orders/minute, tons/hour, or weeks.

Utilization ladder:

```text
utilization = actual flow rate / capacity
```

If the answer key reports one utilization number for a whole process, check whether it means bottleneck/overall utilization. If the prompt asks for each resource, compute `demand flow / resource capacity` for every resource.

## Visual Memory Aid

```mermaid
flowchart TD
    FlowUnit[Choose flow unit] --> Map[Map process flow]
    Map --> Times[Collect process times and resources]
    Times --> Capacity[Compute step capacities]
    Capacity --> Bottleneck[Find bottleneck]
    Bottleneck --> SystemCap[System capacity]
    Map --> Inventory[Measure average inventory]
    Inventory --> Little[Little's Law I=R*T]
    Little --> FlowRate[Flow rate or waiting time]
    FlowRate --> Lead[Lead time = wait + processing]
    SystemCap --> Recommendation[Capacity recommendation]
```

## Example Dialogue

> **Student:** "OceanCove has 160 seats after expansion, so lunch capacity is 213 customers per hour."
>
> **Professor:** "That is dining-area capacity. The **system capacity** at lunch is still constrained by **assembly** at 144 meals/hour unless assembly capacity changes."
>
> **Student:** "So capacity is not the same as demand or seats?"
>
> **Professor:** "Correct. Calculate each required resource, then let the **bottleneck** decide the process capacity."

## Flagged Ambiguities

| Ambiguous Phrase | Canonical Recommendation |
|---|---|
| "Customers in the restaurant" | Use **average inventory** if applying Little's Law. |
| "How fast the restaurant is" | Specify **flow rate**, **capacity**, or **lead time**. |
| "Waiting time" | State whether it is queue waiting or full lead time. |
| "Kitchen capacity" | Specify fish, fries, assembly, expediting, or the minimum of all required steps. |
| "Project takes 12 weeks because the calendar shows 12 weeks" | Use **project duration** from actual start to completion, respecting task timing. |

## Exam Trap Corrections

| Trap | Correction |
|---|---|
| Adding capacities across sequential steps. | The bottleneck, not the sum, determines system capacity. |
| Forgetting parallel resources. | Multiply by the number of parallel resources. |
| Mixing time units. | Convert minutes to hours before calculating customers/hour. |
| Using processing time as lead time. | Add waiting time when the case includes a queue. |
| Ignoring product mix. | Use the mix ratio to compute effective capacity. |
| Treating non-bottleneck expansion as automatically useful. | Check whether the bottleneck changes. |
| Reporting only final numbers. | Show formula, substitution, result, unit, and interpretation. |
| Treating seat capacity as customer flow. | Apply occupancy or table-use assumptions before revenue calculations. |
| Treating answer-key `75%` utilization as every Circored resource's utilization. | `75%` is overall/bottleneck utilization at demand flow; individual resources have their own utilization rates. |

## Compact Answer Language

```text
Define the flow unit.
Draw the process and identify queues/resources.
Compute each resource capacity in the same time unit.
The bottleneck is the minimum required capacity.
Use Little's Law when inventory, flow time, and flow rate are linked.
Interpret the result as a customer-service and profitability consequence.
Never leave a numerical answer as result-only; show formula -> substitution -> result -> unit -> interpretation.
```

# Capital-Growth Project Selection Under Cost and Time Constraints

## Problem Statement

A company preparing to get listed on an exchange wants its **financials to appear strong and stable**. Their **profits come from projects**, and a financial advisor has proposed two important constraints when selecting these projects:

1. **Capital Ascendancy**:  
   Projects must be selected in **increasing order of cost** to reflect consistent financial growth.

2. **Cashflow Consistency Across Time**:  
   Projects are grouped by time periods. Each group must contribute **exactly one project** to ensure there's no accounting period with missing revenue.

---

## Inputs

### Format

The input begins with:
<J> <T>

- `J`: Number of project groups (time periods)  
- `T`: Number of test scenarios

Then for each of the `J` groups:

c1:r1 c2:r2 ... ck:rk
Each project in the group has a **cost** `c` and a **revenue** `r` (all valid: `r ≥ c ≥ 1`)

Finally, `T` lines of:
<C> ``` Where `C` is the initial capital for each scenario.

---

## Objective
For each scenario:
- Select exactly one project from each group
- Project costs must be strictly increasing across time
- At any point, you can only select a project if its cost ≤ current capital
- Upon completing a project, your capital increases by its profit `(r - c)`
- Return: The maximum final capital after completing one project from each group in order and if no valid selection is possible, return "impossible"

--- 

## Sample Input

3 1
3:8 5:7
6:9 8:11
10:13 15:20
4

---

## Sample Output

11

---

## Approach

1. Dynamic Programming with greedy transitions per group
2. Track all possible capital values that satisfy the ascending cost and affordability constraint
3. For each group:
  - From all previous capital values, try picking one affordable project
  - Update new capital if the project cost is greater than the last
4. Sort each group’s projects by cost
  - For each group `j`, iterate over the set of valid capital states from group `j-1`
  - Use binary search (or two-pointer) to find affordable project choices
  - Use a dictionary to track capital states efficiently across transitions

---

## Time Complexity
Let:

`J` = number of groups (≤ 1000)

`K` = max number of projects per group (≤ 50)

`S` = number of capital states tracked in DP (bounded by group × project combinations)

Complexity:
Per group: O(S × K)

Total: O(J × S × K)
In practice, capital states can be pruned significantly to keep runtime efficient.

---

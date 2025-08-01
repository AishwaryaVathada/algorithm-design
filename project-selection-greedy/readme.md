# Project Selection for Capital Maximization

## Problem Statement

As the **chief project manager**, your job is to **select up to `k` projects** from a given list, such that:

- Each project `i` has:
  - a **cost** `cᵢ`
  - a **revenue** `rᵢ`
- You can **only select a project** if your current capital `C` is **greater than or equal to `cᵢ`**
- Once selected, the **profit** from project `i` is:

profit = rᵢ - cᵢ

and is added to your capital
- The goal is to select projects in a way that **maximizes final capital** after exactly `k` selections

---

## Input Format

1. First line:
n  s
where `n` is the number of projects (≤ 100,000), and `s` is the number of scenarios to test

2. Second line: `n` project definitions:
c₁:r₁ c₂:r₂ ... cn:rn
Each entry describes a project with cost and revenue

3. Next `s` lines:
Each line describes a scenario with:
C k
where:
- `C`: Initial capital
- `k`: Number of projects to be selected

---

## Sample Input

4 2
2:4 1:2 5:8 4:7
1 2
2 3

### Explanation
- Scenario 1: Start with capital `1`, select 2 projects
- Scenario 2: Start with capital `2`, select 3 projects

---

## Output Format

- For each scenario, output the **maximum final capital** achievable after selecting `k` projects.

### Sample Output
5
10

---

## Approach

This is a **greedy optimization** problem, where you:
1. Sort all projects by cost
2. At each step, pick the **most profitable** project you can afford (i.e., whose `cost ≤ capital`)
3. Use a **max-heap (priority queue)** to always select the next best project within your capital range

### Data Structure

- `heapq`: Python’s built-in priority queue (use with negative profits to simulate max-heap)

### Time Complexity

- **Sorting projects**: `O(n log n)`
- **Each scenario**:
  - Insert into heap: `O(n log k)`
  - Pop top k projects: `O(k log k)`
- **Total for s scenarios**:  
  O(n log n + s * k log k)
Efficient enough for large inputs (`n ≤ 100,000`, `k ≤ n`)

---

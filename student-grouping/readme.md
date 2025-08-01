# Grouping Students in a Student Care Center

## Problem Statement

In a student care center, students are grouped together after school for supervised self-study. Some students may be **twins**, and to maintain a productive environment, **twin pairs are not allowed to be placed in the same group**.

Your task is to calculate how many valid ways the center can partition `n` students into `k` non-empty groups under the following conditions:

---

## Constraints

- Total students: `n` (3 ≤ n ≤ 50)
- Twin pairs: `m` (0 ≤ m ≤ 5)
- Total groups: `k` (3 ≤ k ≤ 20)
- Each twin pair contains **two students**
- It is guaranteed that `2 × m ≤ n`
- Groups must be **non-empty**
- The **order of groups does not matter**, i.e., grouping `[A, B] [C]` is the same as `[C] [A, B]`

---

## Input Format

- First line: number of test cases `T`
- Next `T` lines: three integers per line:

  n m k
  Where:
  - `n` = number of students
  - `m` = number of twin pairs
  - `k` = number of groups

---

## Output Format

For each test case, output a single integer representing the number of **valid groupings** of students such that **no twin pair is placed in the same group**.

---

## Sample Input

2
5  1  3
6  2  4

### Sample Output

20
90

---

## Approach

This is a **Dynamic Programming and Combinatorics** problem involving:

1. **Counting valid partitions** using **Stirling Numbers of the Second Kind**:
   - Number of ways to partition `n` distinguishable items into `k` non-empty, **unordered** groups
   - `S(n, k)` where `S` is the Stirling number of the second kind

2. **Subtracting invalid configurations**:
   - Use **inclusion-exclusion** to eliminate all groupings where **at least one twin pair** ends up in the same group.

### Key Concepts Used

- Stirling numbers of the second kind: `S(n, k)`
- Inclusion-Exclusion Principle
- Precomputed factorials and combinations to efficiently calculate partitions and exclude invalid ones
- Memoization for repeated subproblems

### Time Complexity

- Precomputation: `O(n * k)`
- Each query: ~ `O(2^m * m * k)` (since twin pair combinations are ≤ 2⁵)

Efficient for `n ≤ 50`, `m ≤ 5`, and `k ≤ 20`

---

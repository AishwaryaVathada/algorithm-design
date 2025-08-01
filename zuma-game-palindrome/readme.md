# Zuma Palindromic Elimination Game

## Problem Overview

Inspired by the classic Zuma game, this variant introduces a **palindromic twist**:  
You are given a sequence of colored balls, where each color is represented by an integer. Your goal is to eliminate the entire sequence using the **minimum number of shots**, where:

- Each **shot** eliminates a contiguous **palindromic subsequence**.
- After a shot, the sequence is updated by concatenating the segments left and right of the eliminated part.
- The process continues until no balls remain.

---

## Objective

Implement the function:
```python
def min_shot(sequence: List[int]) -> int
```
min shots required to destroy the complete sequence

---

## Constraints
- Up to 10 sequences per input set
- Each sequence has length ≤ 500
- Colors are represented as integers
- A valid palindromic shot removes at least one element

---

## Sample Examples
### Example 1:
Input: [1, 2, 3, 2, 1]
Output: 1
Explanation: The entire sequence is a palindrome.

### Example 2:
Input: [1, 2, 3, 4, 5, 5, 4, 2, 1]
Output: 2
Explanation: [1, 2, 3, 4, 5, 5, 4, 2, 1] is not a palindrome. Split into: [1, 2, 3, 4, 5] → not a palindrome
But two palindromes exist: [1, 2, 3, 4, 5, 5, 4, 2, 1] = [1, 2, 3, 4, 5], [5, 4, 2, 1]
Eliminate in 2 steps.

---

## Approach
This is a classic Dynamic Programming problem with the following characteristics:
- State: `dp[i][j]` = minimum number of shots to eliminate sequence[i:j+1]
- Base Case:
  - A single element (or palindrome) takes 1 shot: `dp[i][i] = 1`
- Transition:
  - If sequence[i:j+1] is a palindrome → `dp[i][j] = 1`
  - Otherwise, try all splits: `dp[i][j] = min(dp[i][k] + dp[k+1][j]) for all k in [i, j)`

### Complexity
Let n be the length of the sequence:

Time complexity: O(n³) (due to checking palindromes and DP splits)

Space complexity: O(n²); Efficient for n ≤ 500.

---

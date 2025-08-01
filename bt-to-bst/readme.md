# Transform a Binary Tree to a Binary Search Tree (BST)

## Problem Description

You are given an **arbitrary binary tree** `T`, and your task is to **convert it to a Binary Search Tree** `T'` such that:

- The **structure remains the same** between `T` and `T'`
- The **left and right subtree sizes** of each node remain the same
- The new tree `T'` satisfies the **Binary Search Tree (BST)** property

---

## Objective

For each node `n` in the original tree `T` and corresponding node `n'` in `T'` (same location in the tree):
- Number of nodes in `n.left` = number of nodes in `n'.left`
- Number of nodes in `n.right` = number of nodes in `n'.right`
- The final tree `T'` should obey the BST property:

all(left_subtree_keys) < node.key < all(right_subtree_keys)

---

## Input Format

- First line: an integer `T` representing the number of test cases.
- Each of the next `T` lines describes a binary tree.

Each tree is defined by space-separated node definitions in the format:
<node>:<left>:<right>


- `x` represents a `null` node
- Nodes are unordered (not necessarily level- or pre-order)
- Keys are distinct integers

### Example Input

1
0:x:x -1:1:-2 -2:0:x 1:x:x

This represents a binary tree:
  -1
 /  \
1    -2
    /
   0

---

## Output Format

For each test case, output the pre-order traversal (root → left → right) of the resulting BST with the same structure.

### Example Output
-1 -2 1 0


---

## Constraints

- Maximum tree height: `100`
- Maximum number of nodes: `1,000,000`
- Key range: `[-2^31, 2^31 - 1]`
- All keys are **distinct**

---

## Approach

1. **Build the original binary tree** from the input list of node definitions.
2. **Collect all node keys** from the original tree.
3. **Sort the keys** to satisfy BST in-order property.
4. **Traverse the original tree in in-order**, and replace each node's key with the next smallest key.
   - This preserves the structure but transforms the key values to enforce BST rules.
5. **Pre-order traverse** the new BST and output the sequence.

---

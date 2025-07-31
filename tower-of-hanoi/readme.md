# Tower of Hanoi

## Problem Statement

The **Tower of Hanoi** is a mathematical puzzle invented by the French mathematician **Édouard Lucas** in 1883.

There is a famous story involving an Indian temple in **Kashi Vishwanath**, which contains a large room with three ancient posts surrounded by **64 golden disks**. According to an ancient prophecy, **Brahmin priests** have been moving these disks according to the **immutable rules of Brahma**, and when all disks are moved, the world will end.

### Puzzle Rules

- There are `n` disks and **three pegs**: A, B, and C.
- Disks are all **different sizes**, and are **initially placed** on peg A in increasing size from top to bottom.
- Only **one disk can be moved at a time**, from the **top of one peg** to:
  - an **empty peg**, or
  - a **peg with a larger disk** on top.
- The **goal** in the classic version is to move all disks from peg A to another peg (B or C).

It is proven that the **minimum number of moves** to complete the puzzle with `n` disks is:

---

### Disk Movement Pattern

To reach a specific intermediate configuration using the **minimum number of moves**, the following strategy can be used:

- **Disk 1 (smallest)** moves on all **odd-numbered moves**: 1st, 3rd, 5th, etc.
- Disk 1 moves in a **circular counterclockwise pattern**:

A → C → B → A → C → ...

---

- On **even-numbered moves**, move the **only possible legal disk** that isn't disk 1.

#### Example (3 disks):
Initial state: All disks on peg A

After 5 moves:
- D1 is back on A
- D2 is on B
- D3 is on C

The moves:

D1: A → C

D2: A → B

D1: C → B

D3: A → C

D1: B → A

---

### 🔍 Your Task

Given a final state of `n` disks across pegs A, B, and C (with sizes increasing from top to bottom), write a program to:

1. Determine the **initial peg** the disks were placed on
2. Determine the **number of moves** made to reach the given state
3. Output `impossible` if no valid move sequence could result in the state

---

### 📥 Input Format

- The first line contains an integer `T` – the number of test cases
- Each of the next `T` lines describes the state of the three pegs:

Each peg has disk numbers in ascending order (top to bottom), separated by spaces
PegA, PegB, PegC
---

### 📤 Output Format

For each test case, output:
<InitialPeg> <MoveCount>
Or:
Impossible

⚠️ Note: If all disks are on a single peg, treat it as an **initial state** (0 moves), not a final one.

---

### 🧠 Constraints

- Number of disks: `3 ≤ n ≤ 64`
- Valid number of moves: `0 ≤ moves ≤ 2^n - 2`

---

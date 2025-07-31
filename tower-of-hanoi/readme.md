# Tower of Hanoi

## Problem Statement

The Tower of Hanoi is a mathematical puzzle invented by the French mathematician Édouard 
Lucas in 1883. There is a story about an Indian temple in Kashi Vishwanath which contains a large 
room with three time-worn posts in it, surrounded by 64 golden disks. Brahmin priests, acting out 
the command of an ancient prophecy, have been moving these disks in accordance with the 
immutable rules of Brahma since that time. The puzzle configuration and rules are as follows:
• There are n disks and three pegs: A, B, C. The n disks are different in size, and all disks 
are initially placed on peg A that their sizes increase from top to bottom.
• Only one disk can be moved at a time, from the top of a peg to an empty peg or to a peg 
with larger disk than itself on top.
• The goal is to move all n disks from peg A to either peg B or peg C – this is the goal of the 
original tower of Hanoi puzzle, but our goal in this question is slightly different.
It is easy to prove that the minimum number of moves needed to complete the puzzle with n
disks is 2n-1 using recursion. 

Given a state with all disks on peg A, A simple algorithm to move 
all disks to another peg with the minimum number of 
moves is to move the smallest disk (disk 1: D1) on odd 
moves (the 1st, 3rd, 5th… moves) in a circular manner 
ACBACB… (counterclockwise, as shown left); and 
make the only possible move which does not involve
disk 1 on even moves (the 2nd, 4th, 6th… moves). For 
example, with 3 disks initially placed on peg A, 5 moves
will lead to a state of having D1 on A, D2 on B and D3 
on C as shown left. According to the simple algorithm
above, the 5 moves are: (D1:A→C), (D2:A→B), 
(D1:C→B), (D3:A→C) and (D1:B→A) where D1 is the 
smallest disk, D3 is the largest disk and (D2:A→B) means disk 2 (the middle disk) is moved from 
peg A to peg B.
Given a state of n disks placed on pegs A, B and C with their sizes increasing from top to bottom,
please write a program to determine which peg the disks were initially placed, and how many 
moves there were to reach this state.
Test inputs begin with a number indicating the number of test cases below, and each test case is 
described by a line describing the state with disks on pegs A, B, C separated by commas, and then 
separated by spaces between disks on the same peg in ascending order. For each test case, output 
(i) the initial peg, and (ii) the number of moves. Output “impossible” if no matter which peg to 
start with, the described state is non-reachable. For the special case that all disks are on the same 
peg, as this state can be an initial state or a final state, please take it as an initial state. The number 
of moves should be between 0 and 2
n-2 both inclusive.
Arrows demonstrate 
the counterclockwise 
direction of
moving disk 1.
Disk 1 
on peg A
Disk 2 
on peg B
Disk 3 
on peg C
The total number of disks is between 3 and 64.

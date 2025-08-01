# GTA MRT Journey Time Optimization

## Problem Statement

On **March 22, 2024**, the **Ground Transport Authority (GTA)** announced a new policy:  
> Commuters who transfer between **any two different MRT/LRT stations within 30 minutes** on foot will not incur additional boarding charges.

To evaluate the **impact of this policy**, GTA has asked you, a **data scientist**, to:
- Build a system that computes **time savings** for commuters when **walking is allowed** between nearby stations.
- Compare this to journeys where **only trains (and transfer delays)** are used.

---

## Your Goal

Given two stations `U` and `V`:
- Compute:
  - `x` = shortest travel time from `U` to `V` **using only trains and transfers**
  - `y` = shortest travel time from `U` to `V` **with both trains and walking allowed**
- Return:  
  Time Saving = x - y
`x - y` should always be ≥ 0 since `y` ≤ `x`.

---

## Input Format

### First Line

`x - y` should always be ≥ 0 since `y` ≤ `x`.

---

## Input Format

### First Line

n m
- `n`: Number of MRT stations
- `m`: Number of MRT lines

---

### MRT Lines (`m` lines)

Each of the next `m` lines represents one MRT line:

<wait_time> <station1> <travel_time> <station2> ... <stationN>

Example:
99 S20 186 S19 192 S18

Meaning:
- Wait time: 99 seconds
- S20 —186s→ S19 —192s→ S18

---

### Interchange Stations

After MRT lines, the next line contains an integer:

<k> # number of interchange stations

Then for each interchange station:

<station_id> line1:line2:transfer_time line1:line3:transfer_time ...

Example:

S0 L0:L3:48 L0:L5:75 L3:L5:122

Indicates:
- Transfers between listed line pairs are possible at station `S0`
- Transfer times are symmetric

---

### Walking Time

After interchange info:

<w> # number of walkable paths

Then `w` lines follow:

<stationA> <stationB> <walk_time_in_seconds>

- Walking is **symmetric** and **transitive**
- Multiple walks between stations are allowed
- Walking time ≤ 15 minutes (900 seconds)

---

## Output

For each pair of stations `U` and `V`, compute:
x - y
Where:
- `x`: shortest travel time from U to V **using only trains**
- `y`: shortest travel time from U to V **allowing walking + trains**

---

## Sample Explanation

For the trip from **S20 (Bencoolen)** to **S1 (Bras Basah)**:
- **Train-only path**:  
  99 + 186 + 192 + 40 + 80 + 89 + 134 + 75 + 140 + 90 = **1125 seconds**
- **Walking-only option**:  
  `S20 → S1` = **120 seconds**
- **Time Saving**: `1125 - 120 = 1005 seconds`

---

## Approach

1. **Parse input** into appropriate data structures:
   - MRT lines: store graph edges with `wait + travel` time
   - Interchanges: map station + line pair → transfer time
   - Walking paths: add walkable connections to graph

2. **Construct Graph(s)**:
   - Build weighted graph for stations
   - One graph with **only train + transfer connections**
   - Another graph with **train + transfer + walking**

3. **Compute shortest paths**:
   - Use **Dijkstra’s algorithm** (efficient for weighted graphs)
   - Compute:
     - `x = shortest(train-only path from U to V)`
     - `y = shortest(train+walking path from U to V)`

4. **Output**:  
Time Saving = x - y

---

## Constraints

- Max 20 MRT lines
- Max 50 stations per line → ~1000 stations
- Max 100 interchange stations
- Max 4 lines per interchange
- Max 50 walkable connections
- Efficient graph traversal needed (e.g., Dijkstra with priority queue)

---

## Time Complexity

The solution uses **Dijkstra’s algorithm** to compute the shortest path from each station to all others. The graph is constructed with a detailed model of:

- Train connections
- Waiting and transfer times
- Walking connections (if allowed)

Let:

- `n` = number of stations (nodes)
- `m` = number of MRT lines
- `E` = number of edges (train connections + transfers + walk paths)

### Graph Construction

- Each station has:
  - One `(station, None)` node for waiting state
  - One node per line it appears on (typically ≤ 4 lines)
- Total nodes `V = O(n × lines_per_station) = O(n)`
- Total edges `E = O(n)` from:
  - Adjacent train station connections
  - Transfers at interchanges
  - Walking paths (≤ 50)

### Dijkstra’s Algorithm

- Dijkstra is run once **per station** to compute shortest paths:
  - Each run: `O(E log V)` → for us: `O(n log n)`
- Total runs: `n`
- **Total complexity**:
  O(n × n log n) = O(n² log n)
---

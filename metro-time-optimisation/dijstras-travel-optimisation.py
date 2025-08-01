import sys
import heapq
from collections import defaultdict

def compute_transit_time(use_walking):

    # mappings for nodes
    node_id_map = {}
    node_id_to_station = []
    adjacency = []

    
    station_lines = defaultdict(list) # list of lines serving this station
    node_id = 0

    # Create nodes for (station, None) and (station, line)
    for s in range(n):
        # Node for being at a station without being on any line
        node_id_map[(s, None)] = node_id
        node_id_to_station.append(s)
        adjacency.append([])
        node_id = node_id + 1

    for line in range(m):
        stations = station_list[line]
        for s in stations:
            # Node for being at a station on a specific line
            if (s, line) not in node_id_map:
                node_id_map[(s, line)] = node_id
                node_id_to_station.append(s)
                adjacency.append([])
                node_id += 1
            station_lines[s].append(line)

    total_nodes = node_id  # Total number of nodes

    # Prepare walking adjacency list
    walking_adj = defaultdict(list)
    if use_walking:
        for (u, v), t in walking.items():
            walking_adj[u].append((v, t))
            walking_adj[v].append((u, t))

    # Build adjacency list
    for s in range(n):
        node_none = node_id_map[(s, None)]
        # Edges for boarding trains
        for line in station_lines[s]:
            node_line = node_id_map[(s, line)]
            adjacency[node_none].append((node_line, waiting[line]))
        # Edges for walking between stations
        if use_walking:
            for neighbor, t in walking_adj.get(s, []):
                neighbor_node = node_id_map[(neighbor, None)]
                adjacency[node_none].append((neighbor_node, t))

    # Edges for traveling and transferring on train lines
    for line in range(m):
        stations = station_list[line]
        travels = traveling[line]
        for i, s in enumerate(stations):
            node_curr = node_id_map[(s, line)]
            # Travel to next station
            if i < len(stations) - 1:
                next_s = stations[i + 1]
                node_next = node_id_map[(next_s, line)]
                adjacency[node_curr].append((node_next, travels[i]))
            # Travel to previous station
            if i > 0:
                prev_s = stations[i - 1]
                node_prev = node_id_map[(prev_s, line)]
                adjacency[node_curr].append((node_prev, travels[i - 1]))
            # Transfers to other lines at the same station
            if s in transfer:
                for (b4_line, after_line), trans_t in transfer[s].items():
                    if b4_line == line:
                        node_transfer = node_id_map[(s, after_line)]
                        cost = trans_t + waiting[after_line]
                        adjacency[node_curr].append((node_transfer, cost))
            # Walking edges from line nodes
            if use_walking:
                for neighbor, t in walking_adj.get(s, []):
                    neighbor_node = node_id_map[(neighbor, None)]
                    adjacency[node_curr].append((neighbor_node, t))

    # Compute shortest paths using Dijkstra's algorithm

    result = []
    for x in range(n):
        result.append([0] * n)

    
    for start_s in range(n):
        dist = [float('inf')] * total_nodes
        min_t_to_station = [float('inf')] * n
        start_node = node_id_map[(start_s, None)]
        dist[start_node] = 0
        heap = [(0, start_node)]
        while heap:
            curr_t, node = heapq.heappop(heap)
            if curr_t > dist[node]:
                continue
            station = node_id_to_station[node]
            if curr_t < min_t_to_station[station]:
                min_t_to_station[station] = curr_t
            for neighbor_node, cost in adjacency[node]:
                new_t = curr_t + cost
                if new_t < dist[neighbor_node]:
                    dist[neighbor_node] = new_t
                    heapq.heappush(heap, (new_t, neighbor_node))
        result[start_s] = min_t_to_station
    return result
    
def compare_transit_time():
    res1 = compute_transit_time(False)
    res2 = compute_transit_time(True)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = res1[i][j] - res2[i][j]
    return res

s = sys.stdin.readline().split()
n, m = int(s[0]), int(s[1])
waiting = []
station_list = []
traveling = []
for _ in range(m):
    s = sys.stdin.readline().split()
    waiting.append(int(s[0]))
    st, tr = [], []
    for i in range(1, len(s), 2):
        st.append(int(s[i][1:]))
        if i + 1 < len(s):
            tr.append(int(s[i+1]))
    station_list.append(st)
    traveling.append(tr)
nn = int(sys.stdin.readline())
transfer = {}
for _ in range(nn):
    s = sys.stdin.readline().split()
    st = int(s[0][1:])
    transfer[st] = {}
    for i in range(1, len(s)):
        ss = s[i].split(':')
        l1, l2, t = int(ss[0][1:]), int(ss[1][1:]), int(ss[2])
        transfer[st][l1, l2], transfer[st][l2, l1] = t, t
mm = int(sys.stdin.readline())
walking = {}
for _ in range(mm):
    s = sys.stdin.readline().split()
    s1, s2, t = int(s[0][1:]), int(s[1][1:]), int(s[2])
    walking[s1, s2], walking[s2, s1] = t, t
transit_time = compare_transit_time()
for i in range(n):
    print(' '.join([str(j) for j in transit_time[i]]))
import sys
import heapq

def project_selection(projects, initial_c, k):
    projects_sorted = sorted(projects, key=lambda x: x[0])  # Sort by cost
    max_heap = []
    current_capital = initial_c
    index = 0
    n = len(projects_sorted)
    
    for _ in range(k):
        # Add all projects that can be afforded with current capital to the heap
        while index < n and projects_sorted[index][0] <= current_capital:
            cost, revenue = projects_sorted[index]
            profit = revenue - cost
            heapq.heappush(max_heap, (-profit, cost, revenue))  # Using min-heap as max-heap
            index += 1
        
        if not max_heap:
            break  # No more projects can be selected
        
        # Select the project with maximum profit
        neg_profit, cost, revenue = heapq.heappop(max_heap)
        profit = -neg_profit
        current_capital += profit
    
    return current_capital

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    first_line = input_lines[0].split()
    n = int(first_line[0])
    s = int(first_line[1])
    
    projects = []
    cr_pairs = input_lines[1].split()
    for pair in cr_pairs:
        c, r = map(int, pair.split(':'))
        projects.append((c, r))
    
    projects_sorted = sorted(projects, key=lambda x: x[0])
    
    for i in range(s):
        line = input_lines[2 + i].split()
        initial_c = int(line[0])
        k = int(line[1])
        print(project_selection(projects_sorted, initial_c, k))
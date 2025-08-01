import sys


def project_selection(c):
    
    groups = len(cr) 
      
    dp = {}  
    
    dp[-1] = c  # Base case: starting capital is set to intial capital c
        
    for j in range(groups):
        dp_new = {}  

        # Calculate profit of each project in the current group
        for cost, revenue in cr[j]:
            profit = revenue - cost  
            
            # Check all previous groups' entries to see if a valid project can be chosen
            for prev_cost, prev_capital in dp.items():
                               
                if (cost > prev_cost) and (prev_capital >= cost):  # Ensure cost is in ascending order and project cost is within current capital                    

                    a = dp_new.get(cost, 0)
                    b = prev_capital + profit
                    
                    dp_new[cost] = max(a,b)

        dp = dp_new

        # If no valid selection plan, return "impossible"
        if not dp:
            return "impossible"

    # Set c to the maximum capital achievable across all final selections    
    c = max(dp.values())
    
    return c


a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
init_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(init_cap[i]))
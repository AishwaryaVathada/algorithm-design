import sys

def stirling_second_kind(n, k):
    # Initialize a DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    
    return dp[n][k]

def num_grouping(n, m, k):
    if m > k:
        return 0
    
    total_ways = stirling_second_kind(n, k)
    
    for i in range(1, m + 1):
        if n - 2 * i >= 0 and k - i >= 0:
            total_ways -= comb(m, i) * stirling_second_kind(n - 2 * i, k - i)
    
    return total_ways-(m*3)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    print(num_grouping(n, m, k))

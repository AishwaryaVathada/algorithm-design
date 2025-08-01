import sys

def min_shot(i, color):
    n = len(color)
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if color[i] == color[j]:
                dp[i][j] = dp[i + 1][j - 1] if length > 2 else 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]

num_line = int(sys.stdin.readline())
for i in range(num_line):
    color = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(i, color))
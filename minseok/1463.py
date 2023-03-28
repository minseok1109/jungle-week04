import sys

input = sys.stdin.readline
n = int(input())
dp = [float("inf") for _ in range(n + 1)]
dp[0] = dp[1] = 0

for i in range(2, n + 1):
    # 2와 3으로 나눠질 때
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
    # 2로 나눠질 때
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    # 3으로 나눠질 때
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    # -1만 될 때
    else:
        dp[i] = dp[i - 1] + 1

print(dp[n])

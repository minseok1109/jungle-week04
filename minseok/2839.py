# 설탕 배달
import sys

input = sys.stdin.readline
n = int(input())
dp = [float("inf")] * (n + 5)
dp[3] = dp[5] = 1

for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[n] if dp[n] < float("inf") else -1)

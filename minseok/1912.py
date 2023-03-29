import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * (n)
numbers = list(map(int, input().split()))
dp[0] = numbers[0]

for i in range(1, n):
    Max = -sys.maxsize
    for j in range(0, i):
        dp[i] = dp[i - 1] + numbers[i]


print(max(dp))

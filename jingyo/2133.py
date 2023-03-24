# 타일채우기
import sys

input = sys.stdin.readline
x = int(input())
d = [0]*31
d[2]=3

# def dp(x):
#     if d[x] != 0:
#         return d[x]
#     result = 3 * d[x-2]
#     for i in range(3, x+1):
#         if i % 2 == 0:
#             result += 2*d[x-i]
#     d[x] = result
#     return d[x]


print(dp(x))

#바텀업
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, x+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else:
        dp[i] = 0
print(dp[x])

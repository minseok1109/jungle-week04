import sys

input = sys.stdin.readline
x = int(input())

# #bottom up 방식
dp = [0]*91

dp[0]=0
dp[1]=1
for i in range(2,91):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[x])

#top-down방식
dp = [0]*91
dp[0]=0
dp[1]=1


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(x))

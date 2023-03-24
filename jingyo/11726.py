# 2×n 타일링
import sys

input = sys.stdin.readline
x = int(input())
dp = [0]*10001


def sequence(x):
    if x == 0 or x == 1:
        return 1
    if x==2:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = sequence(x-1) + sequence(x-2)
    return dp[x] % 10007


print(sequence(x))

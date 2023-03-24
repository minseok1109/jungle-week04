import sys

input = sys.stdin.readline

def dp(coins, target):
    d = [0]*(target+1)
    d[0] = 1
    for coin in coins:
        for i in range(coin, target+1):
            d[i] += d[i-coin]
    return d[target]

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())  # 금액
    print(dp(coins, target))

# 동전0
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
coins.sort(key=lambda x: -x)

def greedy_coin():
    result = []
    money = k
    for coin in coins:
        num = 0
        if money - coin < 0:
            continue
        elif money - coin == 0:
            num += 1
            result.append(num)
            return sum(result)
        else:
            num = money//coin
            result.append(num)
            money = money%coin
    return sum(result)

print(greedy_coin())
import sys
input = sys.stdin.readline

# 동전의 종류 개수, 만들어야 할 합
n, k = map(int, input().split())

# 동전의 가치 (오름차순)
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

needs = [0] * n

for i in range(n):
    # 나눈 몫 저장
    needs[i] = k // coins[i]
    
    # 나눈 나머지 저장
    k %= coins[i]

print(sum(needs))
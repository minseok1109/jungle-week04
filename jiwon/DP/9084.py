import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 동전 가지 수
    n = int(input())

    # n가지 동전의 각 금액 (오름차순)
    coins = list(map(int, input().split()))

    # n가지 동전으로 만들어야 할 금액
    m = int(input())

    # 인덱스를 알기 쉽게 보기 위해, 1 ~ m+1
    result = [0] * (m+1)

    # 어떤 동전이든 0원을 만들 수 있는 가지수는 1가지 존재
    result[0] = 1

    for coin in coins:
        for my in range(1, m+1):
            if my >= coin:
                result[my] += result[my-coin]

    print(result[m])
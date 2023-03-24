import sys
input = sys.stdin.readline

# 물품의 수, 버틸 수 있는 무게
n, k = map(int, input().split())

# 무게, 가치
graph = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

# 가방 리스트
bag = [[0] * (k+1) for _ in range(n+1)]

# i : 물건, j : 가방
for i in range(1, n+1):
    for j in range(1, k+1):
        # 무게, 가치
        weight, value = graph[i][0], graph[i][1]

        if j < weight:
            # 현재 물건이 해당열의 무게보다 크면 담을 수 없음
            # 그래서 위의 것 그대로 적용
            bag[i][j] = bag[i-1][j]
        else:
            # 현재 물건이 해당열의 무게보다 작으면 담을 수 있음

            # 1) 물건을 넣은 뒤 남은 무게를 채울 수 있는 최댓값을 위의 행에서 가져와 더해줌
            # 2) 현재 물건 말고 다른 물건들로 채움
            
            # 1, 2번 중에 큰 값을 넣음

            # max(현재 물건 가치 + bag[이전 물건][현재 가방 무게 - 현재 물건 무게], bag[이전 물건][현재 가방 무게])
            bag[i][j] = max(value + bag[i-1][j-weight], bag[i-1][j])

print(bag[n][k])
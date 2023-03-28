# DP, 비트마스킹, 비트필드 사용
# 1) 각 도시를 방문했는지의 여부 -> 비트마스킹 ( 0001, 0002 ... 1111 )
# 2) 현재 도시에서의 최소비용 -> DP
# 3) 도시를 방문하는 것 -> DFS

# 0001(2) = 1 이라면 => 0번 도시만을 거침
# 0011(2) = 3 이라면 => 0, 1 번 도시를 거침
# 1111(2) = 15 이라면 => 0, 1, 2, 3 번 도시를 거침

import sys
input = sys.stdin.readline

# 도시의 수
n = int(input())

# 비용 행렬 저장
graph = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 만들어 최대값으로 초기화
# 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용 저장
dp = [[0] * (1 << n) for _ in range(n)]

maxvalue = sys.maxsize

def nextCity(now, visited):
    # 이미 값이 갱신되어 있다면,
    if dp[now][visited]:
        return dp[now][visited]

    # 마지막 여행지라면,
    if visited == (1 << n)-1:
        return graph[now][0] if graph[now][0] > 0 else maxvalue

    # 각 상태에서 구해야하는 값
    cost = maxvalue
    for i in range(1, n):
        # 방문할 수 있으며, 아직 방문하지 않았다면,
        if graph[now][i] and not visited & (1 << i):
            next_cost = nextCity(i, visited | (1 << i))
            cost = min(cost, next_cost + graph[now][i])

    # dp에 값 갱신
    dp[now][visited] = cost
    return dp[now][visited]

print(nextCity(0, 1))
#외판원 순회

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]는 도시 i를 마지막으로 방문한 상태에서, 이전에 방문한 도시들의 집합이 j일 때의 최소 비용
dp = [[-1] * (1 << n) for _ in range(n)]

def tsp(cur, visited):
    # 모든 도시를 방문한 경우, 현재 위치에서 출발점으로 가는 비용을 반환
    if visited == (1 << n) - 1:
        return w[cur][0] if w[cur][0] > 0 else float('inf')

    # 이미 계산한 경우, 저장된 값 반환
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # 최소 비용 계산
    min_cost = float('inf')
    for i in range(n):
        # 방문하지 않은 도시를 선택해서 비용 계산
        if (visited & (1 << i)) == 0 and w[cur][i] > 0:
            cost = tsp(i, visited | (1 << i)) + w[cur][i]
            min_cost = min(min_cost, cost)

    # 계산된 최소 비용 저장
    dp[cur][visited] = min_cost
    return min_cost


# 시작점에서 출발하는 경우로 초기화
print(tsp(0, 1 << 0))

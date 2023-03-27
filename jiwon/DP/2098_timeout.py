# 브루트포스 알고리즘, 백트래킹 사용

import sys
input = sys.stdin.readline

# 도시의 수
n = int(input())

# 비용 행렬 저장
graph = [list(map(int, input().split())) for _ in range(n)]

# 최소 비용 저장
result = sys.maxsize

# 출발지(인덱스), 다음 도착지(인덱스), 비용, 방문한 도시(리스트)
def nextCity(start, next, value, visited):
    global result

    if len(visited) == n:
        # 마지막 여행지에서 출발지로 돌아올 수 있다면, (0이 아니라면)
        if graph[next][start] != 0:
            result = min(result, value + graph[next][start])
        return
    
    for i in range(n):
        # 만약 다음 출발지로 갈 수 있다면,
        # 비용이 0이 아니고, 이미 방문한 도시가 아니고, 지금 result보다 크지 않으면,
        if graph[next][i] != 0 and i not in visited and value < result:
            # 방문자에 추가하고 방문
            visited.append(i)
            nextCity(start, i, value + graph[next][i], visited)
            visited.pop()

for i in range(n):
    nextCity(i, i, 0, [i])

print(result)
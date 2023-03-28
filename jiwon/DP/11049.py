import sys
input = sys.stdin.readline

# ABCDE 연속행렬 곱의 최솟값 =
#     min(ABCDE,
#     min(A) + min(BCDE) + 합치는 비용(A행 * A열 * E열),
#     min(AB) + min(CDE) + 합치는 비용(A행 * B열 * E열),
#     min(ABC) + min(DE) + 합치는 비용(A행 * C열 * E열),
#     min(ABCD) + min(E) + 합치는 비용(A행 * D열 * E열)
# )

# 행렬의 개수
n = int(input())

# 행렬의 크기 r, c
graph = [list(map(int, input().split())) for _ in range(n)]

# 최소값 저장
dp = [[0] * n for i in range(n)]

# 몇 번째 대각선인지
for i in range(1, n):
    # 몇 번째 열인지
    for j in range(n-i):
        x = i + j

        # 최대값을 미리 넣어줌
        dp[j][x] = 2 ** 32

        # k는 첫 행렬부터 마지막 행렬-1 까지 순회
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], 
                           # dp[첫 행렬 위치][k] + dp[k+1][마지막 행렬 위치] + graph[첫 행렬 위치][0] * graph[k][1] * graph[마지막 행렬 위치][1]
                           dp[j][k] + dp[k+1][x] + graph[j][0] * graph[k][1] * graph[x][1])

# 맨 오른쪽 위가 얻고자 하는 최소값
print(dp[0][n-1])
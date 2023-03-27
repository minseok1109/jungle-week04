import sys

N, M = map(int, sys.stdin.readline().split())
dp = [[float("inf")] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]
dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))

# 크기가 작은 돌은 건너뛰기
for i in range(2, N + 1):
    if i in stone_set:
        continue
    # i번째 돌에서 x가 j일 때 j - 1, j, j + 1을 확인하여
    # i번째 돌에 갈 수 있는 최소 점프 횟수의 + 1
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float("inf"):
    print(-1)
else:
    print(min(dp[N]))

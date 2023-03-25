#행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] +
                           mat[i][0]*mat[k][1]*mat[j][1])
print(dp[0][-1])

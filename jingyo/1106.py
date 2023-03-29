#호텔

import sys

input = sys.stdin.readline

c, n = map(int, input().split())
invest_list = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
invest_list.sort(key=lambda x:x[1])

dp = [[0]*(c+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(1,c+1):
        if i == 0:
            dp[i][j] = float('inf')
        else:
            r = j//invest_list[i][1]  # 몫
            k = j % invest_list[i][1]  # 나머지
            if r == 0:
                dp[i][j] = min(invest_list[i][0], dp[i-1][j])
            else:
                dp[i][j] = min(invest_list[i][0]*r+dp[i][k], dp[i-1][j])

print(dp[-1][-1])

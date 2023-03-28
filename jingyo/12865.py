#평범한 배낭
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
datas = [[0, 0]]  # [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]
for _ in range(n):
    w, v = map(int, input().split())
    datas.append([w,v])

dt = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        r = j-datas[i][0]  # '탐색하는 무게'-'탐색하는 물건의 무게'의 차를 기준으로 판별하자
        if r>=0:
            # 왼쪽은 현재탐색중인 물건을 넣지 않았을 경우 vs 현재 탐색중인 물건을 넣을 경우(현재 탐색중 물건의 가치+ 넣지않았을 때 나머지무게에 맞는 가치)
            dt[i][j] = max(datas[i][1] + dt[i-1][r], dt[i-1][j])
        else: #탐색하는 물건을 담을 수 없으면
            dt[i][j] = dt[i-1][j]
print(dt[-1][-1])


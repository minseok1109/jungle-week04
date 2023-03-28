import sys
input = sys.stdin.readline

# 돌의 개수, 크기가 작아 올라갈 수 없는 돌의 개수
n, m = map(int, input().split())

dp = [[sys.maxsize] * (int((2 * n) ** 0.5) + 2) for _ in range(n+1)] 
dp[1][0] = 0

# 작은 돌들 저장, 중복 제거
stones = set([int(input()) for _ in range(m)])

# 등차수열 속도 증가시 : k번째 돌에서 a만큼의 최대 속도를 가질 수 있다면, k = a(a+1)/2
# a = sqrt(2*k+(1/4))-1/2 이기 때문에 현재 위치(stone)에서 int(sqrt(2*stone))+1까지 검사하면
# 가능한 모든 속도에서의 값을 조사 가능

for stone in range(2, n+1):
    if stone in stones:
        continue

    for j in range(1, int((2 * stone) ** 0.5) + 1):
        # X-1, X, X+1 속도로 갈 수 있음
        dp[stone][j] = min(dp[stone-j][j-1], dp[stone-j][j], dp[stone-j][j+1]) + 1

result = min(dp[n])
print(result if result != sys.maxsize else -1)
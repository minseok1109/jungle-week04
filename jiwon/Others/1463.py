import sys
input = sys.stdin.readline

# 1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2) X가 2로 나누어 떨어지면, 2로 나눈다.
# 3) 1을 뺀다.

# 1, 2, 3번의 경우의 수 모두 구해야 함, 즉 셋 다 시도

# 1로 만들려는 초기값
n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    # 1을 먼저 빼고 시작하는 이유는
    # 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문
    # 즉 셋 다 시도하는 게 맞음

    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])
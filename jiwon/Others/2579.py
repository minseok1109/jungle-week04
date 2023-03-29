import sys
input = sys.stdin.readline

# 1) 계단은 한 계단 혹은 두 계단 씩 오를 수 있음
# 2) 연속된 세 개의 계단을 모두 밟아서는 안됨
# 3) 시작점은 계단에 포함하지 않으며 마지막 도착 계단은 반드시 밟아야 함

# 게임에서 얻을 수 있는 최대값 출력

# 계단의 개수
n = int(input())

# 각 계단의 점수
steps = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(steps))

else:
    # 각 계단마다의 최대값 저장
    result = [0] * n

    result[0] = steps[0]
    result[1] = steps[0] + steps[1]

    for i in range(2, n):
        # 연속해서 세개의 계단 밟을 수 없음
        # 현재로부터 -1, -3 계단을 밟을 수 있거나, -2 계단을 밟을 수 있거나
        result[i] = max(
                    # i 계단값 + i-1 계단값 + i-3의 최대값
                    steps[i] + steps[i-1] + result[i-3],
                    # i 계단값 + i-2의 최대값
                    steps[i] + result[i-2])

    print(result[-1])
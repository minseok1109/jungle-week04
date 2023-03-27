import sys
input = sys.stdin.readline

# 회의의 수
n = int(input())

# 회의 시작 시간, 끝나는 시간
meetings = [list(map(int, input().split())) for _ in range(n)]

# 끝나는 시간, 시작 시간 순으로 정렬 (오름차순)
meetings = sorted(meetings, key = lambda a : a[0])
meetings = sorted(meetings, key = lambda a : a[1])

# 최대 회의 개수 저장
count = 0

# 조건에 적합하는 회의의 끝나는 시간
next_end = 0

for start, end in meetings:
    # 먼저 회의의 끝나는 시간 <= 다음 회의의 시작 시간
    if next_end <= start:
        count += 1
        next_end = end

print(count)
import sys

input = sys.stdin.readline
n = int(input())
classrooms = sorted(
    [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0])
)


result = [classrooms[0]]
# 끝나는 시간으로 오름차순 정렬하고 시작하는 시간순으로 다시 오름차순 정렬해야함
for i in range(1, n):
    if result[-1][1] <= classrooms[i][0]:
        result.append(classrooms[i])

print(len(result))

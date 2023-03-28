#회의실 배정
import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((end, start)) #종료시간이 빨라야 최대한 많은 회의 배정 가능

arr.sort()
schedule = [arr[0]] #제일 빠른건 무조건 등록
for i in arr[1:]:
    if i[1] >= schedule[-1][0]: #이전에 배정된 회의의 종료시간과 현재 회의의 시작 시간 비교
        schedule.append(i)

print(len(schedule))

    







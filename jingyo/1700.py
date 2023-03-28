#멀티탭 스케줄링
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = deque(map(int, sys.stdin.readline().split()))

plugged = set()  # 현재 멀티탭에 꽂혀 있는 전기용품의 집합
cnt = 0  # 멀티탭에서 뽑아내는 횟수

while arr:
    tool = arr.popleft()
    if tool in plugged:  # 이미 꽂혀있는 경우
        continue
    elif len(plugged) < n:  # 자리가 남은 경우
        plugged.add(tool)
    else:  # 자리가 없는 경우
        max_idx, max_tool = -1, -1
        for p in plugged: #꽂혀있는 tool중에서
            try:
                idx = arr.index(p) #arr에 몇번째 들어있나 봐바
            except ValueError:  # 이후에 사용되지 않는 경우
                idx = len(arr) #없으면 arr의 맨 마지막 값 을 idx로 주고
            if idx > max_idx: 
                max_idx = idx  #사용될 tool중 가장 늦게 사용되는 tool의 index저장
                max_tool = p  
        plugged.remove(max_tool) #늦게 사용되는 거 빼기
        plugged.add(tool) # 지금 써야되는거 꽂기
        cnt += 1

print(cnt)







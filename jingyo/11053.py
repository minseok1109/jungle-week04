#가장 긴 증가하는 부분 수열
import sys
from bisect import bisect_left
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))

stack = []
for a in arr:
    if not stack or stack[-1] <a:
        stack.append(a)
    else:
        i = bisect_left(stack, a)
        stack[i] = a

print(len(stack))

input = sys.stdin.readline

x = int(input())

arr = list(map(int, input().split()))

dp = [1]*x

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)


#틀린 풀이(5,1,2,3)
# print(max(dp))


# x = int(input())

# arr = [0] + list(map(int, input().split()))  # [0,10, 20, 10, 30, 20, 50]

# dp = [0] + [1]*(x)

# temp=0
# for j in 
# for i in range(1,x+1):
#     if temp < arr[i]: #temp보다 탐색하는 요소가 크다면
#         temp = arr[i] #temp를 그 요소로 업데이트
#         dp[i] = dp[i-1] +1
#     else:
#         dp[i] = dp[i-1]

# print(dp[-1])

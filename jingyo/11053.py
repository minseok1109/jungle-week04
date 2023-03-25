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


# x = int(input())

# arr = list(map(int, input().split()))

# dp = [1]*x

# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))


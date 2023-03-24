#lcs
import sys
input = sys.stdin.readline

a = str(input().rstrip())
b = str(input().rstrip())
len_a = len(a)
len_b = len(b)
dt = [[0]*(len_a+1) for _ in range(len_b+1)]

for i in range(1,len_b+1):
    for j in range(1,len_a+1):
        if b[i-1] == a[j-1]:
            dt[i][j] = dt[i-1][j-1] +1
        else:
            dt[i][j] = max(dt[i-1][j],dt[i][j-1])
print(dt[-1][-1])

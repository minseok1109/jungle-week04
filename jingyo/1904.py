import sys

input = sys.stdin.readline
n = int(input())
# #바텀업
# d = [0]*(n+1)

# d[0]=1
# d[1]=1

# for i in range(2, n+1):
#     d[i] = (d[i-1] + d[i-2]) % 15746

# print(d[n])

#탑다운
dp = [0]*100

def sequence(x):
    if x == 0 or x == 1:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = sequence(x-1) + sequence(x-2)
    return dp[x]

print(sequence(n))
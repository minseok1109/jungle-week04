import sys

input = sys.stdin.readline
n = int(input())

#bottom-up
dp=[0]*(n+1)

dp[0] = 1
dp[1]=1

for i in range(2,n+1):
    dp[i]= (dp[i-1]+dp[i-2])%15746

print(dp[n])


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
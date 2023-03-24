import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()

lcs = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

# 마지막 문자열까지 확인해야 함으로 +1
for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        # 서로의 문자열을 하나씩 비교
        if first[i-1] == second[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(first)][len(second)])
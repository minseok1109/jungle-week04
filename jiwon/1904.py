import sys
input = sys.stdin.readline

# 00과 1만으로 자리수가 n인 수를 만드는 것
# 만들 수 있는 개수 리턴

# 자릿수
n = int(input())

values = [0, 1, 2, ]

for i in range(3, n+1):
    values.append((values[i-2] + values[i-1]) % 15746)

print(values[n])
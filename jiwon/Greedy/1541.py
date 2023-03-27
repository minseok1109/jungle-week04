import sys
input = sys.stdin.readline

# - 기호를 기준으로 문자열을 나눔
values = input().strip().split('-')
results = []

# + 기호가 포함되어 있으면 해당 숫자들을 더함
for value in values:
    if '+' in value:
        numbers = value.split('+')
        results.append(sum(map(int, numbers)))
    else:
        results.append(int(value))

# 차례대로 빼줌
result = results[0]
for i in range(1, len(results)):
    result -= results[i]

print(result)
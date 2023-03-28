#잃어버린 괄호
#- 뒤의 숫자를 다 더해서 앞에 숫자에 빼는 것이 가장 최소의 값.-가 또나타면 그 앞끼리 묶어야함.
import sys

input = sys.stdin.readline
datas = input().rstrip().split('-')

result = sum(map(int, datas[0].split('+')))

for i in range(1, len(datas)): #-뒤에꺼는 몽땅 - 붙여서 계산.
    result -= sum(map(int, datas[i].split('+')))

print(result)

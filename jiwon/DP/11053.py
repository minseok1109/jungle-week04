import sys
input = sys.stdin.readline

# 수열의 크기
n = int(input())

# 수열
values = [0] + list(map(int, input().split()))
lengths = [0] * (n+1)

for i in range(n+1):
    # values[i]가 어디 뒤에 붙을 수 있는지,
    # 뒤에 붙을 수 있는 값이 여러개라면, lengths 값이 큰 애로 선택
    # 그 lengths 값 + 1로 저장

    # 붙을 수 있는 값 저장
    result = []
    for j in range(i):
        if values[i] > values[j]:
            # 붙을 수 있는 값의 '인덱스' 저장
            result.append(j)

    # 그 중 가장 큰 아이 선정
    maxvalue = 0
    for k in range(len(result)):
        maxvalue = max(maxvalue, lengths[result[k]])

    # 인덱스 0은 제외
    if i != 0:
        lengths[i] = maxvalue + 1

print(max(lengths))
import sys
input = sys.stdin.readline

# 멀티탭 구멍의 개수, 용품의 총 사용 개수
n, k = map(int, input().split())

# 전기용품들 (사용 순서대로 주어짐)
things = list(map(int, input().split()))

# 플러그에 꽂혀있는 전기용품들
plugs = []

# 플러그를 빼는 횟수, 리턴 변수
result = 0

for i in range(k):
    # 이미 있다면
    if things[i] in plugs:
        continue

    # 빈공간이 있다면
    if len(plugs) != n:
        plugs.append(things[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_thing = 0
    temp = 0

    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 앞으로 사용할 플러그에 해당 전기용품이 없으면,
        if plug not in things[i:]:
            # 해당 전기용품을 뺄 것
            temp = plug
            break

        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면,
        elif things[i:].index(plug) > far_thing:
            # 해당 전기용품을 뺄 것
            far_thing = things[i:].index(plug)
            temp = plug

    # temp의 인덱스를 찾아 해당 자리에 새 전기용품 꽂음
    final_index = plugs.index(temp)
    plugs[final_index] = things[i]
    result += 1

print(result)
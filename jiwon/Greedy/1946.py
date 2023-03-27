import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 지원자의 숫자
    n = int(input())

    # 서류 성적 순위, 면접 성적 순위 (동석차 없이 결정된다고 가정)
    scores = [list(map(int, input().split())) for _ in range(n)]

    # 서류 성적 순위 기준으로 정렬 (오름차순)
    scores = sorted(scores, key= lambda x: x[0])

    # 이제부터 면접 성적 순위로 따짐
    # 서류 성적이 1등인 사람은 무조건 통과, 그 사람 기준으로 판단
    standard = scores[0][1]

    # 통과한 사람
    count = 1

    for i in range(1, n):
        # 내 면접 순위 < 앞사람 면접 순위
        if scores[i][1] < standard:
            count += 1
            standard = scores[i][1]

    print(count)
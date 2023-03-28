import sys
input = sys.stdin.readline


t=int(input())
for i in range(t):
    n = int(input())

    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort(key=lambda x:(-x[0],-x[1]))
    result=[]
    pop = rank.pop()
    result.append(pop) #처음꺼 비교용으로 하나 넣어주기

    for _ in range(n):
        while rank:
            score1, score2 = rank.pop()
            if result[-1][0] > score1 or result[-1][1] > score2:
                result.append([score1, score2])
        

    print(len(result))
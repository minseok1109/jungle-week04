import sys

input = sys.stdin.readline
n, k = map(int, input().split())
things = []
for _ in range(n):
    w, v = map(int, input().split())
    things.append((w, v))


def knapsack(items, capacity):
    n = len(items)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], value + table[i - 1][j - weight])

    return table[n][capacity]


v, items = knapsack(things, k)
print(v)

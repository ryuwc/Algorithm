import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def solve(x, visit, graph):
    for g in graph[x]:
        if g not in visit:
            visit.add(g)
            solve(g, visit, graph)


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = set()
    rst = 0

    for i in range(1, N+1):
        if i not in visit:
            solve(i, visit, graph)
            rst += 1

    print(rst)


if __name__ == '__main__':
    main()
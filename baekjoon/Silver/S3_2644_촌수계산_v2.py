import sys
from collections import defaultdict


def solve(p1, p2, visit, G, cnt):
    if p1 == p2:
        return cnt

    visit.add(p1)
    for u in G[p1]:
        if u not in visit:
            rst = solve(u, p2, visit, G, cnt + 1)
            if rst != -1:
                return rst

    return -1


def main():
    N = int(sys.stdin.readline())
    p1, p2 = map(int, sys.stdin.readline().strip().split())
    M = int(sys.stdin.readline())

    G = defaultdict(list)

    for _ in range(M):
        x, y = map(int, sys.stdin.readline().strip().split())
        G[x].append(y)
        G[y].append(x)

    visit = set()

    cnt = 0

    print(solve(p1, p2, visit, G, cnt))


if __name__ == '__main__':
    main()

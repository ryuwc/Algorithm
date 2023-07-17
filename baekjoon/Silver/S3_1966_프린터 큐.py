import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().strip().split())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    Q = deque([[i, int(x)] for i, x in enumerate(lst)])
    cnt = 0
    while True:
        cur = Q.popleft()
        if any(cur[1] < x[1] for x in Q):
            Q.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                print(cnt)
                break

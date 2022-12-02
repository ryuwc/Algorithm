import sys; from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
info = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
Q = deque(i for i in range(1, N+1))
for idx in info:
    if Q[0] == idx:
        Q.popleft()
        continue
    else:
        # test = len(Q)
        # print(test)
        if Q.index(idx) > len(Q)//2:
            while Q[0] != idx:
                Q.appendleft(Q.pop())
                cnt += 1
            Q.popleft()
        else:
            while Q[0] != idx:
                Q.append(Q.popleft())
                cnt += 1
            Q.popleft()

print(cnt)

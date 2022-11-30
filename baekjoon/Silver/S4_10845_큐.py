import sys; from collections import deque

N = int(sys.stdin.readline())

Q = deque()

for _ in range(N):
    info = list(sys.stdin.readline().strip().split())
    if info[0] == 'push':
        Q.append(info[1])
    elif info[0] == 'pop':
        if len(Q) == 0:
            print(-1)
            continue
        print(Q.popleft())
    elif info[0] == 'size':
        print(len(Q))
    elif info[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif info[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif info[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])


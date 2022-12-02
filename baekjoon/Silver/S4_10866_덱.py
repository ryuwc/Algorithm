import sys; from collections import deque

N = int(sys.stdin.readline().strip())

Q = deque()
for _ in range(N):
    info = list(sys.stdin.readline().strip().split())
    if 'push_f' in info[0]:
        Q.appendleft(info[1])
    elif 'push_b' in info[0]:
        Q.append(info[1])
    elif 'pop_f' in info[0]:
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif 'pop_b' in info[0]:
        if not Q:
            print(-1)
        else:
            print(Q.pop())
    elif info[0] == 'size':
        print(len(Q))
    elif info[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif info[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif info[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])


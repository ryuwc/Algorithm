import sys;

N = int(sys.stdin.readline())

S = []
for _ in range(N):
    info = list(sys.stdin.readline().strip().split())
    if info[0] == 'push':
        S.append(info[1])
    elif info[0] == 'pop':
        if not S:
            print(-1)
            continue
        print(S.pop())
    elif info[0] == 'size':
        print(len(S))
    elif info[0] == 'empty':
        if S:
            print(0)
        else:
            print(1)
    elif info[0] == 'top':
        if not S:
            print(-1)
            continue
        print(S[-1])




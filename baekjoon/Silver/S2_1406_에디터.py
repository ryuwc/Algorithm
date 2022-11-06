import sys; import collections

S = list(sys.stdin.readline().strip())
Q = collections.deque()

N = int(sys.stdin.readline().strip())

for _ in range(N):
    info = list(sys.stdin.readline().strip().split())
    if info[0] == 'L' and S:
        Q.append(S.pop())
    elif info[0] == 'D' and Q:
        S.append(Q.pop())
    elif info[0] == 'B' and S:
        S.pop()
    elif info[0] == "P":
        S.append(info[1])

Q.reverse()
S.extend(Q)
print(''.join(S))

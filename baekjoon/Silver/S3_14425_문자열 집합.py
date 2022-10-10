import sys

N, M = map(int, sys.stdin.readline().strip().split())
N_lst = []
M_lst = []
for _ in range(N):
    tmp = sys.stdin.readline().strip()
    N_lst.append(tmp)
cnt = 0
for _ in range(M):
    tmp = sys.stdin.readline().strip()
    if tmp in N_lst:
        cnt += 1

print(cnt)
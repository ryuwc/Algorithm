import sys

# dfs탐색, 순회하며 cnt를 증가, p2를 만나면 cnt를 rst에 저장하고 return
def solve(v, cnt):
    global visit, rst
    if v == p2:
        rst = cnt
        return
    visit.add(v)
    for u in G[v]:
        if u not in visit:
            solve(u, cnt+1)

N = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline().strip())

# 갈 수 있는 경로
G = [[]for _ in range(N+1)]
for m in range(M):
    p, c = map(int, sys.stdin.readline().strip().split())
    G[c].append(p)
    G[p].append(c)

rst = -1
# 사람들이 1, 2, 3, 4 .. 의 숫자를 가지고 있어서 set사용 가능
visit = set()
solve(p1, 0)
print(rst)

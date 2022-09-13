import sys
from collections import defaultdict

N = int(input())
tree = defaultdict(list)
P = set()
depth = defaultdict(list)
for _ in range(N):
    node, left, right = map(int, sys.stdin.readline().split())
    tree[node] = [left, right]
    P.add(left)
    P.add(right)

def solve():
    root = find_root()
    find_depth(root, 1)
    result = [0, 0]
    for i in sorted(depth):
        width = max(depth[i]) - min(depth[i]) + 1
        if result[1] < width:
            result = [i, width]
    print(*result)

cnt = 1
def find_depth(v, d):
    global cnt
    if v == -1:
        return
    find_depth(tree[v][0], d+1)
    depth[d].append(cnt)
    cnt += 1
    find_depth(tree[v][1], d+1)

def find_root():
    root = 1
    for i in range(1, N + 1):
        if i not in P:
            root = i
            break
    return root

solve()
print(P)

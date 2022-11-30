import sys;
sys.setrecursionlimit(10**6)

def solve(s, e):
    if s > e:
        return
    m = s+1
    root = tree[s]
    for i in range(s, e+1):
        if tree[i] > root:
            m = i; break

    solve(s+1, m-1)
    solve(m, e)
    print(root)

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

N = len(tree)

solve(0, N-1)
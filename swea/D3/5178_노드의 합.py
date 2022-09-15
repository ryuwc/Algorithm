import sys; sys.stdin = open('input_노드의 합.txt', 'r')
sys.setrecursionlimit(10 ** 6)


def postorder(v):
    if v <= N:
        postorder(v*2)
        postorder(v*2+1)
        if tree[v] == 0:
            tree[v] = tree[v*2] + tree[v*2+1]

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * 1000
    for m in range(M):
        e, n = map(int, input().split())
        tree[e] = n

    postorder(1)
    print(f'#{tc+1}', tree[L])



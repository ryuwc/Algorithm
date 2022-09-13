import sys; sys.stdin = open('input_subtree.txt', 'r')

def find_root():
    root = 1
    for i in range(1, V+1):
        if i not in P:
            root = i
            break
    return root

cnt = 0
def inorder(v):
    global cnt
    if v == 0:
        return
    inorder(L[v])
    cnt += 1
    inorder(R[v])
    return cnt

for tc in range(int(input())):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [0] * (E + 2)
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = set()

    for i in range(0, E * 2, 2):
        parent, child = arr[i], arr[i + 1]
        if L[parent] == 0:
            L[parent] = child
        else:
            R[parent] = child
        P.add(child)

    print(f'#{tc+1} {inorder(N)}')
    cnt = 0

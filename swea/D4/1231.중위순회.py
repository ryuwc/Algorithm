import sys; sys.stdin = open('1231.txt', 'r')

def inorder(v):
    if v == 0:
        return
    inorder(L[v])
    print(W[v], end='')
    inorder(R[v])

for tc in range(1, 11):
    N = int(input())

    W = [''] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)

    for n in range(N):
        arr = list(input().split())
        W[int(arr[0])] = arr[1]

        for i in range(2, len(arr)):
            if L[int(arr[0])] == 0:
                L[int(arr[0])] = int(arr[i])
            else:
                R[int(arr[0])] = int(arr[i])
    print(f'#{tc}', end=' ')
    inorder(1)
    print()

# import sys; sys.stdin = open('5248.txt', 'r')


def find_set(x):
    val = P[x]
    if x == val:
        return x
    else:
        return find_set(P[x])

def union(x, y):
    P[find_set(x)] = P[find_set(y)]

for tc in range(int(input())):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    P = [i for i in range(N+1)]

    for i in range(0, M*2, 2):
        a, b = info[i], info[i+1]
        union(a, b)

    rst = set()
    for i in range(1, N+1):
        rst.add(find_set(i))

    print(f'#{tc+1}', len(rst))
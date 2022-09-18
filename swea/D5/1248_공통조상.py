import sys; sys.stdin = open('input_공통조상.txt', 'r')
# 공통조상

def find_n1_n2_p():
    for n1 in n1_p:
        for n2 in n2_p:
            if n1 == n2:
                return n1
cnt = 0
def solve(v):
    global cnt
    if v == 0:
        return
    cnt += 1
    solve(L[v])
    solve(R[v])


for tc in range(int(input())):
    V, E, n1, n2 = map(int, input().split())
    tmp = list(map(int, input().split()))
    L = [0] * (V+1)
    R = [0] * (V+1)
    P = [0] * (V+1)

    for i in range(0, E*2, 2):
        p, c = tmp[i], tmp[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p

    n1_p = [P[n1]]
    n2_p = [P[n2]]
    while n1_p[-1] != 0:
        n1_p.append(P[n1_p[-1]])
    while n2_p[-1] != 0:
        n2_p.append(P[n2_p[-1]])

    n1_n2_p = find_n1_n2_p()
    solve(n1_n2_p)
    print(f'#{tc+1}', n1_n2_p, cnt)
    cnt = 0





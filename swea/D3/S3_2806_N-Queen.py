# import sys; sys.stdin = open('input_N-Queen.txt', 'r')

def n_queen(visit_j, depth):
    global cnt
    if promising(visit_j, depth):
        if depth == N:
            cnt += 1
        else:
            for j in range(1, N+1):
                visit_j[depth+1] = j
                n_queen(visit_j, depth+1)

def promising(visit_j, depth):
    k = 1
    flag = True
    while k < depth and flag:
        if visit_j[depth] == visit_j[k] or abs(visit_j[depth] - visit_j[k]) == (depth-k):
            flag = False
        k += 1
    return flag

for tc in range(int(input())):
    N = int(input())

    visit = [0]*(N+1)
    cnt = 0
    n_queen(visit, 0)
    print(f'#{tc+1}', cnt)

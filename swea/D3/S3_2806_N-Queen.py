import sys
# def nQueen(row, visit):
def nQueen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    else:
        # col은 열번호
        for col in range(N):
            val = (1<<col)
            # if visit & (1<<col): continue    # 같은 열은 제외
            if visit[col]: continue

            # 대각에 대해서 체크
            a = row + col
            b = row - col + (N-1)
            if line1[a] or line2[b]: continue

            line1[a] = line2[b] = 1
            visit[col] = 1
            # nQueen(row+1, visit | (1<<col))
            nQueen(row+1)
            line1[a] = line2[b] = 0
            visit[col] = 0

N = int(sys.stdin.readline())

visit = [0] * N
line1 = [0]*(N*N)   # /  (row + col)
line2 = [0]*(N*N)   # \  (row + col + (N - 1))
cnt = 0

# nQueen(0, 0)
nQueen(0)
print(cnt)
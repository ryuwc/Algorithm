
def solve(n, r, c):
    global rst
    if r == tr and c == tc:
        print(rst)
        exit()
    # 찾는 위치에서 벗어난 경우 n의 범위만큼 더해주고 return
    if not(r <= tr < r+n and c <= tc < c+n):
        rst += (n * n)
        return
    # n이 1인경우 Z자로 1씩 더해감
    if n == 1:
        rst += 1
        return
    half = n//2
    # 제 1사분면
    solve(half, r, c)
    # 2사분면
    solve(half, r, c + half)
    # 3사분면
    solve(half, r + half, c)
    # 4사분면
    solve(half, r + half, c + half)


if __name__ == '__main__':
    N, tr, tc = map(int, input().split())
    rst = 0
    solve(2**N, 0, 0)

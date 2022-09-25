import sys

def solve(start, end):
    # 탈출 조건
    if end - start <= 1:
        # start를 포함한 숫자 부터 end미만의 숫자이므로 start를 return하며 종료
        return start
    mid = (start+end)//2
    rst = 0
    for item in cable:
        rst += (item//mid)
    # 자른 랜선이 필요한 수 보다 작으면 start부터 mid의 안에서 탐색
    if rst < N:
        return solve(start, mid)
    # 많으면 mid부터 end안에서 탐색
    else:  # rst >= N
        return solve(mid, end)


K, N = map(int, sys.stdin.readline().strip(' ').split())
cable = [int(sys.stdin.readline().strip(' ')) for _ in range(K)]

max_cable = max(cable)

print(solve(1, max_cable+1))


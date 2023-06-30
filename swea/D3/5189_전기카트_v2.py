import sys;

sys.stdin = open('5189.txt', 'r')


def solve(now, cur_sum, cart, visit, rst, N):
    if 0 not in visit:
        rst = min(rst, cur_sum + cart[now][0])
        return rst
    if cur_sum > rst:
        return rst

    for next in range(1, N):
        if visit[next]: continue
        visit[next] = 1
        rst = min(solve(next, cur_sum + cart[now][next], cart, visit, rst, N), rst)
        visit[next] = 0

    return rst


def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        cart = [list(map(int, input().split())) for _ in range(N)]
        visit = [1] + [0] * (N - 1)
        rst = 9e9
        print(f'#{tc}', solve(0, 0, cart, visit, rst, N))


if __name__ == '__main__':
    main()

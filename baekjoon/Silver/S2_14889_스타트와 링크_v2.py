import sys

def solve(n, index, N, skill, visit, a_skill, b_skill, rst):
    if n == N//2:
        a_team = 0
        b_team = 0
        for i in range(N):
            if visit[i]:
                a_team += a_skill[i]
            else:
                b_team += b_skill[i]

        return min(abs(a_team - b_team), rst)

    for i in range(index, N):
        visit[i] = True
        rst = min(solve(n+1, i+1, N, skill, visit, a_skill, b_skill, rst), rst)
        visit[i] = False

    return rst

def main():
    N = int(sys.stdin.readline().strip())
    skill = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    visit = [0] * N

    a_skill = [sum(r) for r in skill]
    b_skill = [sum(c) for c in zip(*skill)]

    print(solve(0, 0, N, skill, visit, a_skill, b_skill, 9e9))


if __name__ == '__main__':
    main()
import sys


def dfs(now_empl):
    for work in employee[now_empl]:
        if visited[work]:
            continue
        visited[work] = True

        if assign_list[work] == 0 or dfs(assign_list[work]):
            assign_list[work] = True
            return True

    return False


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    employee = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        info = list(map(int, sys.stdin.readline().strip().split()))[1:]
        for j in info:
            employee[i].append(j)

    assign_list = [0] * (M + 1)
    rst = 0

    for i in range(1, N + 1):
        visited = [False] * (M + 1)
        if dfs(i):
            rst += 1

    print(rst)

import sys

sys.stdin = open('sample_input_전기카트.txt', 'r')


def dfs(now, s, visited, arr, N, result):
    if 0 not in visited:
        return min(s, result)
    elif s > result:
        return result
    else:
        for next in range(N):
            if next == now or visited[next]:
                continue

            if next == 0 and 0 in visited[1:]:
                continue

            visited[next] = 1
            result = dfs(next, s + arr[now][next], visited, arr, N, result)
            visited[next] = 0

        return result


def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        visited = [0] * N
        result = dfs(0, 0, visited, arr, N, float('inf'))
        print(f'#{tc}', result)


if __name__ == '__main__':
    main()

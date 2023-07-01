import sys

sys.setrecursionlimit(10 ** 6)


def dfs(arr, visited, N, M, r, c):
    visited[r][c] = 1
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(arr, visited, N, M, nr, nc)


def solve(N, M, K, coordinates):
    arr = [[0] * M for _ in range(N)]
    for k in range(K):
        r, c = coordinates[k]
        arr[r][c] = 1

    visited = [[0] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(arr, visited, N, M, i, j)
                result += 1
    return result


def main():
    T = int(sys.stdin.readline())
    for tc in range(1, T + 1):
        N, M, K = map(int, sys.stdin.readline().split())
        coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
        print(solve(N, M, K, coordinates))


if __name__ == '__main__':
    main()

import sys;

sys.stdin = open('4881.txt', 'r')


def solve(depth, cur_sum):
    global min_sum
    if cur_sum >= min_sum:  # 가지치기
        return
    if depth == N:  # 모든 줄에서 숫자를 선택했다면
        min_sum = cur_sum  # 최소 합 갱신
        return
    for i in range(N):
        if not visited[i]:  # 아직 선택되지 않은 열이라면
            visited[i] = True
            solve(depth + 1, cur_sum + matrix[depth][i])  # 해당 숫자를 선택하고 다음 행으로 진행
            visited[i] = False


def main():
    T = int(input())
    for tc in range(1, T + 1):
        global N, matrix, visited, min_sum
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        visited = [False] * N
        min_sum = 9e9
        solve(0, 0)
        print(f'#{tc} {min_sum}')


if __name__ == '__main__':
    main()

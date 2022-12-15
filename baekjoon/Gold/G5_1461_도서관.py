import sys


def main():
    # 일단 정렬
    books.sort()

    # 가장 긴 거리 모두 음수일 수 있으므로 둘 다 abs처리
    max_dist = max(abs(books[0]), abs(books[-1]))

    # 음수, 양수 따로 반복문을 돌 것 이기때문에 기준 점 정하기
    turn_idx = N

    # 이 때 모두 음수라면 turn_idx는 그냥 N일 것이니까 양수 일 때의 반복문을 돌지 않음
    for i in range(N):
        if books[i] > 0:
            turn_idx = i
            break

    rst = 0
    for i in range(N-1, turn_idx-1, -M):
        rst += books[i] * 2
    for i in range(0, turn_idx, M):
        rst += abs(books[i]) * 2
    return rst - max_dist


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    books = list(map(int, sys.stdin.readline().strip().split()))

    print(main())

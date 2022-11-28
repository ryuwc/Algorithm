import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().strip().split()))

S = []
# 결과 값을 담을 리스트
rst = []

# 아무 조건에 충족하지 않으면 rst에 0을 추가 (왼쪽에 나보다 큰놈이 없는 경우)
# 그리고 그 인덱스와 높이를 S에 추가
for i in range(N):
    pointer = 0
    hei = arr[i]
    # S에 추가된 놈들 중 나보다 작은놈은 pop해버리기
    while S and S[-1][0] < arr[i]:
        S.pop()
    # 위의 과정을 거쳤는데 S에 뭐가 남아있으면 그게 내 왼쪽에서 나보다 큰놈의 정보임
    if S:
        pointer = S[-1][1] + 1

    rst.append(pointer)
    S.append([hei, i])

print(*rst)

import sys;
from collections import deque;
import heapq


def solve():
    # 첫 번째 D는 정해졌으니 인덱스 1부터 시작
    for i in range(1, N):
        val = fir_nums[i]
        # Q의 맨 뒤의 값이 현재 값보다 크다면 계속 pop
        while Q and Q[-1] > val:
            Q.pop()
        # 나보다 큰놈 다 뺏으면 내가 들어감 (내가 제일 작은놈임)
        Q.append(val)

        # 이 부분이 좀 힘들었는데 L이 3이고 arr가 [1, 2, 2, 3..] 이고 3번째 인덱스 즉 3일 때
        # Q는 [1, 2, 2, 3]이 된다. 이때 제일 작은놈(0번째 인덱스)가 1인데 이놈을 i-L번째 인덱스와 비교해서 같으면 빼줘야됨
        # 빼줘야 한다는 것은 지금까지 pop이 안되었다는 상황임
        if i >= L and Q[0] == fir_nums[i - L]:
            Q.popleft()
        rst.append(Q[0])
    return rst


if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().strip().split())
    fir_nums = list(map(int, sys.stdin.readline().strip().split()))
    Q = deque()

    # L이 뭐가 나오든 일단 첫 번째 요소는 Q에 들어가야됨
    Q.append(fir_nums[0])
    # 위와 동일
    rst = [fir_nums[0]]

    print(*solve())

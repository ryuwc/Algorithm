import sys; sys.stdin = open('input_벌꿀채취.txt', 'r')
from itertools import combinations

# 숫자를 담은 리스트를 넘겨주면 그 숫자들의 모든 조합에서 최대의 꿀 값을 찾아낸다.
def comb(nums):

    candi_cnt = 0
    for k in range(1, M+1):
        aa = list(combinations(nums, k))

        for num in aa:
            tmp_cnt = 0
            if sum(num) > C:
                continue
            for l in range(k):
                tmp_cnt += num[l-1]**2
            candi_cnt = max(candi_cnt, tmp_cnt)
    return candi_cnt


for tc in range(int(input())):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 첫 일꾼의 숫자들을 담을 리스트
    rst_nums = []
    # 그 부분의 인덱스 번호들
    rst_idx = []
    # 최대의 꿀 값
    rst_cnt = 0
    # 먼저 첫 번째 일꾼이 최대의 꿀을 채취한다.
    for i in range(N):
        for j in range(N-M+1):
            tmp_idx = []
            tmp_nums = []
            # 임시 벌꿀 가격
            tmp_cnt = 0
            for m in range(M):
                tmp_idx.append((i, j+m))
                tmp_nums.append(honey[i][j+m])
            if sum(tmp_nums) <= C:
                for num in tmp_nums:
                    tmp_cnt += num**2
            elif sum(tmp_nums) > C:
                tmp_cnt = comb(tmp_nums)
            if rst_cnt < tmp_cnt:
                rst_cnt = tmp_cnt
                rst_nums = tmp_nums
                rst_idx = tmp_idx

    # 첫 번째 일꾼이 채취한 부분을 -1로 바꿔준다.
    while rst_idx:
        r, c = rst_idx.pop()
        honey[r][c] = -1

    # 두 번째 일꾼
    rst2_nums = []
    rst2_idx = []
    rst2_cnt = 0
    # 첫 번째 일꾼이 채취한 방식과 똑같지만, -1영역은 채취를 하지 않는다.
    for i in range(N):
        for j in range(N - M + 1):
            tmp_idx = []
            tmp_nums = []
            tmp_cnt = 0
            for m in range(M):
                tmp_idx.append((i, j + m))
                tmp_nums.append(honey[i][j + m])
            if -1 in tmp_nums:
                continue
            if sum(tmp_nums) <= C:
                for num in tmp_nums:
                    tmp_cnt += num ** 2
            elif sum(tmp_nums) > C:
                tmp_cnt = comb(tmp_nums)
            if rst2_cnt < tmp_cnt:
                rst2_cnt = tmp_cnt
                rst2_nums = tmp_nums
                rst2_idx = tmp_idx

    print(f'#{tc+1}', rst_cnt+rst2_cnt)




import sys
from itertools import combinations

N = int(sys.stdin.readline())
skills = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

nst = [i for i in range(1, N+1)]

rst = 9e9
# 조합 사용해서 풀기 N은 짝수이므로 일단 두 팀이 될 수 있는 모든 조합을 생성
candi_t1_all = list(combinations(nst, N//2))

# t1의 팀이 정해지면 t2는 그 외의 나머지 선수니까 구한 조합의 반만 사용해도 됨
for i in range(len(candi_t1_all)//2):
    t1 = candi_t1_all[i]
    t2 = [i for i in range(1, N+1) if i not in t1]
    tmp = 0
    t1_score = 0
    t2_score = 0

    # t1의 모든 스킬 더해주기
    for t1_man in t1:
        for t1_ano in t1:
            t1_score += skills[t1_man-1][t1_ano-1]

    # t2의 모든 스킬 더해주기
    for t2_man in t2:
        for t2_ano in t2:
            t2_score += skills[t2_man-1][t2_ano-1]

    # 두 팀의 능력치의 차이
    tmp = abs(t1_score - t2_score)
    rst = min(rst, tmp)

print(rst)

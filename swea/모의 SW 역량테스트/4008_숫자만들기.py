import sys; sys.stdin = open('4008.txt')
from itertools import permutations
def solve(index, AA):
    global max_AA, min_AA, oper
    if index == N:
        max_AA = max(max_AA, AA)
        min_AA = min(min_AA, AA)
        return
    # 계산할 피연산자 solve함수의 매개변수 index를 사용해서 지정
    val = nums[index]
    # 사칙연산의 경우의 수 4개
    candi = [AA+val, AA - val, AA*val, int(AA/val)]

    # 남아있을 때 까지 모든 경우의 수
    if oper[0] > 0:
        oper[0] -= 1
        solve(index+1, candi[0])
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        solve(index+1, candi[1])
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        solve(index+1, candi[2])
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        solve(index+1, candi[3])
        oper[3] += 1

for tc in range(int(input())):
    N = int(input())
    # 연산자의 정보
    oper = list(map(int, input().split()))
    # 피연산자 숫자
    nums = list(map(int, input().split()))

    min_AA = 0xfffffffff
    max_AA = -0xfffffffff

    solve(1, nums[0])

    print(f'#{tc+1}', max_AA - min_AA)

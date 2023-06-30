import sys
from itertools import permutations
sys.stdin = open('5189.txt', 'r')

def solve(N, arr):
    min_battery = float('inf')
    for perm in permutations(range(1, N)):  # 사무실을 제외한 모든 경로의 순열을 생성
        battery = arr[0][perm[0]] + arr[perm[-1]][0]  # 처음과 마지막 구간의 배터리 사용량
        for i in range(len(perm)-1):  # 중간 구간의 배터리 사용량
            battery += arr[perm[i]][perm[i+1]]
        min_battery = min(min_battery, battery)  # 최소 배터리 사용량 갱신
    return min_battery

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc+1}', solve(N, arr))

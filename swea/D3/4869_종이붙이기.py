import sys; sys.stdin = open('4869.txt', 'r')

def func(n):            # 가로 길이를 만들 수 있는 종이의 경우의 수 함수 선언
    if memo[n] == -1:   # memoization사용한 memo, 인덱스 0, 1 외에는 -1로 되어 있음
        memo[n] = func(n-1) + func(n-2) + func(n-2)
        # 재귀 선언, 이 경우의 수는 특별한 패턴이 있음, 피보나치와 비슷하지만, n-2를 하나 더 더해주면 패턴이 완성됨
    return memo[n]

memo = [-1]*30
memo[0] = 3
memo[1] = 5

for tc in range(int(input())):
    N = int(input())
    num = (N//10)-2
    print(f'#{tc+1}', func(num))

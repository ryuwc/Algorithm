# 백준 1003 피보나치 함수 - 피보나치 함수를 재귀로 구현하면 시간초과가 발생한다.
# 따라서 메모이제이션을 이용하여 구현한다.
# 메모이제이션은 한 번 계산한 결과를 메모리 공간에 메모하는 기법이다.
# 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져온다.
# 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다.

# 0과 1이 출력되는 횟수를 저장하는 리스트
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[n], one[n]))


t = int(input())
for i in range(t):
    n = int(input())
    fibonacci(n)


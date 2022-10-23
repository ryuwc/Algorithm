import sys; import math

# 소수인지 판별하는 함수
def is_prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

for tc in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())

    # 효율적으로 답을 찾기위해 반으로 나누어 left와 right로 나누어 판별
    left = N//2
    right = N - left
    rst = [0, 0]
    while left > 0:
        if is_prime(left) and is_prime(right):
            print(left, right)
            break
        left -= 1
        right += 1

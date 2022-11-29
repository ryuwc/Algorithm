import sys; import math

def is_prime(num):
    if num == 1: return 0
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    rst = 0
    for num in nums:
        rst += is_prime(num)

    print(rst)
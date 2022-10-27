import sys; import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().strip().split())


for i in range(M, N+1):
    if i == 1: continue
    if is_prime(i):
        print(i)

import sys

# S5 2751 수 정렬하기 2

N = int(sys.stdin.readline().strip())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()

for num in nums:
    sys.stdout.write(str(num) + '\n')

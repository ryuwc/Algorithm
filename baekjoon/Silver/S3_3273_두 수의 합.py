import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
t_num = int(sys.stdin.readline())

nums.sort()
rst = 0

left, right = 0, N-1
while left < right:
    tmp = nums[left] + nums[right]
    if tmp == t_num:
        rst += 1
        left += 1
        right -= 1
        continue
    if tmp < t_num:
        left += 1
        continue
    right -= 1

print(rst)
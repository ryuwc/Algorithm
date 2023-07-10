import sys

while 1:
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if sum(nums) == 0: break
    nums.sort()

    if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        print('right')
    else:
        print('wrong')



# import sys
#
# N = int(sys.stdin.readline().strip())
#
# nums = []
# for _ in range(N):
#     nums.append(int(sys.stdin.readline().strip()))
#
# nums_sort = sorted(nums)
#
# rst = []
# while True:
#     target_ori = nums_sort.pop()
#     target = target_ori
#     if target in nums:
#         tar_idx = nums.index(target)
#     else:
#         continue
#     nums[tar_idx] = 0
#     for i in range(tar_idx-1, -1, -1):
#         val_left = nums[i]
#         if val_left < target:
#             target = val_left
#             nums[i] = 0
#         else:
#             break
#     target = target_ori
#     for i in range(tar_idx+1, N):
#         val_right = nums[i]
#         if val_right < target:
#             target = val_right
#             nums[i] = 0
#         else:
#             break
#     rst.append(tar_idx+1)
#     if sum(nums) == 0:
#         break
#
# rst.sort()
# print('\n'.join(map(str, rst)))

# -----------------------------------------------------
import sys

N = int(sys.stdin.readline().strip())

# 좌, 우 살피면서 확인할 것이니까 좌, 우에 0추가
nums = [0]
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.append(0)

rst = []
# 숫자들의 좌, 우가 나보다 작거나 같으면 터뜨려야되는 지뢰임
for i in range(1, N+1):
    if nums[i-1] <= nums[i] >= nums[i+1]:
        rst.append(i)

print('\n'.join(map(str, rst)))

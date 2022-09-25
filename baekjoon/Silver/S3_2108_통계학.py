from collections import Counter
from heapq import nsmallest
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

print(round(sum(nums)/N))
nums.sort()
print(nums[N//2])
counter = Counter(nums)
conut_num = counter.most_common()
# num_lst = []
# for _ in range(len(conut_num)):
#     a = conut_num[_][0]
#     num_lst.append(a)
if len(conut_num) > 1:
    if conut_num[0][1] == conut_num[1][1]:
        print(conut_num[1][0])
    else:
        print(conut_num[0][0])
else:
    print(conut_num[0][0])

print(nums[-1] - nums[0])
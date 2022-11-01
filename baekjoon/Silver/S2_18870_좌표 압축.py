import sys; import collections

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

new_nums = list(set(nums))
new_nums.sort()

graph = collections.defaultdict(int)

for i in range(len(new_nums)):
    graph[new_nums[i]] = i

for num in nums:
    print(graph[num], end=' ')

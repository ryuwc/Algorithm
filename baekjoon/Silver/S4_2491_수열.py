# import sys; sys.stdin = open('input_수열.txt', 'r')


N = int(input())
nums = list(map(int, input().split()))


a = 1
result_a = 1
for i in range(1, N):
    if nums[i-1] <= nums[i]:
        result_a += 1
        if result_a >= a:
            a = result_a
    else:
        result_a = 1

b = 1
result_b = 1
for i in range(1, N):
    if nums[i-1] >= nums[i]:
        result_b += 1
        if result_b >= b:
            b = result_b
    else:
        result_b = 1

print(max(a, b))
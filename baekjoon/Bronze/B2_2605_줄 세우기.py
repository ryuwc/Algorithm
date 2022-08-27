
N = int(input())
nums = list(map(int, input().split()))

students = []
for i in range(1, N+1):
    students.append(i)

for i in range(N):
    for j in range(0, nums[i]):
        students[i-j-1], students[i-j] = students[i-j], students[i-j-1]

print(*students)
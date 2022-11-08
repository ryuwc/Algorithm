
A, B, N = map(int, input().split())

rst = 0
for i in range(N):
    A = (A%B)*10
    rst = A//B

print(rst)


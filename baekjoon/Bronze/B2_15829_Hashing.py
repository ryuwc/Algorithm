N = int(input())
st = input()

M = 1234567891
rst = 0

for i in range(N):
    num = ord(st[i]) - 96
    val = num * (31 ** i) % M
    rst = (rst + val) % M

print(rst)

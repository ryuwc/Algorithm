N = int(input())

cnt = 1
minus = 1

while N > 1:
    cnt += 1
    N -= minus * 6
    minus += 1

print(cnt)

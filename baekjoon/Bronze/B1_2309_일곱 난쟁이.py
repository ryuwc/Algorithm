import sys; sys.stdin = open('input_난쟁이.txt', 'r')

nan = [0]*9
for _ in range(9):
    nan[_] = int(input())

nan_7 = []
for i in range(1<<9):
    sums = 0
    result = []
    for j in range(9):
        if i & (1<<j):
            sums += nan[j]
            result.append(nan[j])
    if sums == 100 and len(result) == 7:
        nan_7 = result
nan_7.sort()
for i in nan_7:
    print(i)

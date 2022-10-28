N = list(map(int, input()))

num_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rst = 1
for num in N:
    if num in num_set:
        num_idx = num_set.index(num)
        num_set[num_idx] = -1
    elif num not in num_set:
        if num == 6 and 9 in num_set:
            num_idx = num_set.index(9)
            num_set[num_idx] = -1
        elif num == 9 and 6 in num_set:
            num_idx = num_set.index(6)
            num_set[num_idx] = -1
        else:
            rst += 1
            for i in range(10):
                if i == num:
                    continue
                num_set.append(i)

print(rst)
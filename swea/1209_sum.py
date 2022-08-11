
for tc in range(1, 11):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = [0]*4

    r_max = 0
    for i in range(100):
        r_sum = 0
        for j in range(100):
            r_sum += arr[i][j]
        if r_sum > r_max:
            r_max = r_sum
    result[0] = r_max
    c_max = 0
    for i in range(100):
        c_sum = 0
        for j in range(100):
            c_sum += arr[j][i]
        if c_sum > c_max:
            c_max = c_sum
    result[1] = c_max
    cross_left_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                cross_left_sum += arr[i][j]
    result[2] = cross_left_sum
    cross_right_sum = 0
    for i in range(100):
            cross_right_sum += arr[i][99-i]
    result[3] = cross_right_sum

    final_value = 0
    for i in result:
        if i > final_value:
            final_value = i

    print(f'#{tc} {final_value}')




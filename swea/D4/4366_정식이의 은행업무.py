import sys; sys.stdin = open('input_정식이의 은행업무.txt', 'r')

# # 2진수를 10진수로 변환하는 함수
# def bin_to_ten(num):
#     res = 0
#     for i in range(len(num)):
#         res += int(num[i]) * (2 ** (len(num)-1-i))
#     return res
#
# # 3진수를 10진수로 변환하는 함수
# def tri_to_ten(num):
#     res = 0
#     for i in range(len(num)):
#         res += int(num[i]) * (3 ** (len(num)-1-i))
#     return res
#
# # 2진수를 3진수로 변환하는 함수
# def bin2tri(num):
#     res = ''
#     for i in range(len(num)):
#         if num[i] == '0':
#             res += '1'
#         else:
#             res += '2'
#     return res
#
# # 3진수를 2진수로 변환하는 함수
# def tri2bin(num):
#     res = ''
#     for i in range(len(num)):
#         if num[i] == '0':
#             res += '1'
#         elif num[i] == '1':
#             res += '0'
#         else:
#             res += '2'
#     return res
#
# # 2진수를 3진수로 변환한 후 10진수로 변환하는 함수
# def bin2tri2dec(num):
#     return tri2dec(bin2tri(num))
#
# # 3진수를 2진수로 변환한 후 10진수로 변환하는 함수
# def tri2bin2dec(num):
#     return bin2dec(tri2bin(num))

def solve():
    tmp = '012'
    for k in range(3):
        for i in range(len(tri_num)):
            tri_num_copy = tri_num[:]
            if tri_num[i] != tmp[k]:
                tri_num_copy[i] = (int(tmp[k])+1)%3
                val2 = int(''.join(map(str, (tri_num_copy))), 3)
                if val2 in bin_ten_set:
                    return print(f'#{tc}', val2)



T = int(input())
for tc in range(1, T+1):
    tmp_bin = input()
    tmp_tri = input()
    bin_num = []
    tri_num = []
    for _ in range(len(tmp_bin)):
        bin_num.append(int(tmp_bin[_]))
    for _ in range(len(tmp_tri)):
        tri_num.append(int(tmp_tri[_]))


    bin_ten_set = set()

    for i in range(len(bin_num)):
        # bin_num_copy = bin_num[:]
        if bin_num[i] == 0:
            change_bin = bin_num[:i]+[1]+bin_num[i+1:]
            val = ''.join(map(str, (change_bin)))
            bin_ten_set.add(int(val, 2))
        elif bin_num[i] == 1:
            change_bin = bin_num[:i] + [0] + bin_num[i + 1:]
            val = ''.join(map(str, (change_bin)))
            bin_ten_set.add(int(val, 2))

    solve()


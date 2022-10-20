import sys

N = int(sys.stdin.readline())
max_hei = 0
max_idx = 0
len_info = 0
# 기둥의 최대 수는 1000, 입력되는 위치에 기둥을 추가 할 것
record = [0] * 1001
for _ in range(N):
    p, h = map(int, sys.stdin.readline().strip().split())

    # 가장 높은 기둥을 중심으로 양쪽에서 접근 할 것이므로 가장 높은 기둥의 위치 정보가 필요함
    if h > max_hei:
        max_hei = h
        max_idx = p

    # 마지막 기둥이 있는 위치
    len_info = max(len_info, p)
    record[p] = h

rst = 0
tmp = 0
# 첫 위치부터 제일 큰 기둥이 있는 위치까지 비교하며 값을 저장
for i in range(max_idx):
    if tmp >= record[i+1]:
        rst += tmp
    else:
        rst += tmp
        tmp = record[i+1]

tmp = 0
# 맨 오른쪽의 기둥부터 제일 큰 기둥이 있는 위치까지 접근하며 값을 저장
for i in range(len_info+1, max_idx, -1):
    if tmp >= record[i - 1]:
        rst += tmp
    else:
        rst += tmp
        tmp = record[i - 1]

print(rst+max_hei)


import sys

N = int(sys.stdin.readline().strip())
S = []
rst = 0
for _ in range(N):
    hei = int(sys.stdin.readline().strip())

    # 스택이 있고 그 스택의 마지막의 키가 나보다 작으면 그 수를 pop과 rst에 +
    # pop하는 경우는 나와 이어지는 경우임
    while S and S[-1][0] < hei:
        rst += S.pop()[1]

    # 스택이 빈 경우 그냥 넣어주기
    if not S:
        S.append([hei, 1])

    # 스택의 마지막 키가 나와 같은 경우, 일단 pop해서 그 수를 rst에 더해주고
    elif S and S[-1][0] == hei:
        cnt = S.pop()[1]
        rst += cnt

        # 이때 스택이 남아있다면, 나와 그 스택안의 값이 이어지므로 +1
        if S:
            rst += 1

        # 내 키와 현재 그 키의 수를 +1해서 스택에 append
        S.append([hei, cnt + 1])

    # 스택이 비어있지 않고, 위의 조건에 만족하지 못할 때, 내 키와 수=1 을 추가하고 rst에 1추가(나와 스택안의 이어짐)
    else:
        S.append([hei, 1])
        rst += 1

print(rst)

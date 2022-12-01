import sys; from collections import deque; import re

for tc in range(int(sys.stdin.readline().strip())):
    func = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())

    # 일단 [1, 2, 3, 4]이런식으로 입력오는 것을 문자열로 다 받음
    info = sys.stdin.readline().strip()

    # re.sub를 사용해서 숫자 아닌 것을 공백으로 바꿔줌
    new_info = re.sub(r"[^0-9]", " ", info)

    # strip사용해서 좌우 공백 없애줌
    new_info = new_info.strip()

    # 이제 '1 2 3 4' 이렇게 있을텐데 이걸 큐에 넣어줌
    Q = deque(new_info.split())

    # error출력했으니까 Q에 남아있는 요소를 출력 안해도됨 그걸 판별하기 위한 변수
    can_print = False

    # 이게 핵심인데 뒤집는거 R나온다고 계속 뒤집으면 시간 초과나니까
    # 이 flag사용해서 맨 앞에 있는거 혹은 맨 뒤에 있는거 pop할지 고르고
    # 마지막에 뒤집을지 말지도 결정해주는 변수임
    flag = False
    for f in func:
        if flag == False and f == 'D':
            if not Q:
                can_print = True
                print('error')
                break
            else:
                Q.popleft()
        elif f == 'R':
            if flag == True:
                flag = False
            else:
                flag = True
        elif flag == True and f == 'D':
            if not Q:
                can_print = True
                print('error')
                break
            else:
                Q.pop()
    if flag:
        Q.reverse()

    # print(can_print)
    if can_print:
        continue
    else:
        print("[" + ','.join(Q) + "]")
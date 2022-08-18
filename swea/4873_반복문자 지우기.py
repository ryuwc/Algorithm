import sys; sys.stdin = open('4873.txt', 'r')

for tc in range(int(input())):
    s = input()
    stack = [0]*10000
    top = -1

    top += 1
    stack[top] = s[0]          # 스택에 일단 s의 첫 번째 원소를 넣어준다.
    for i in s[1:]:            # 첫 번째 원소는 넣었으니 1부터 돌려준다.
        if stack[top] != i:    # 스택의 top이 i와 같지 않은 경우는
            top += 1           # 스택에 추가해준다.
            stack[top] = i
        elif stack[top] == i:  # 스택의 top이 i와 같을 경우는
            top -= 1           # 넣지도 않고, pop시켜 준다.
    print(f'#{tc+1} {len(stack[0:top+1])}')
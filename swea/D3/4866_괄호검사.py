import sys; sys.stdin = open('4866.txt', 'r')



for tc in range(int(input())):
    tmp = input()
    stack = [0]*100
    top = -1
    result = 1            # 결과를 print할 변수 설정
    for i in tmp:
        if i == '(' or i == '{':     # 여는 괄호가 나올 경우 stack에 넣어주고 top += 1
            top += 1
            stack[top] = i
        elif i == ')' or i == '}':     # 닫는 괄호가 나올 경우
            if len(stack) == 0:        # stack이 비어 있을 때
                result = 0             # 출력 변수를 0으로 설정하고 break
                break
            elif i == ')' and stack[top] == '{':   # 닫는 괄호의 형태가 다른 괄호일 경우 break
                result = 0
                break
            elif i == '}' and stack[top] == ')':
                result = 0
                break
            else:                      # 정상적인 닫는 괄호가 나올 경우 top -= 1
                top -= 1

    if top == -1:
        print(f'#{tc+1}', result)
    else:
        print(f'#{tc+1}', 0)



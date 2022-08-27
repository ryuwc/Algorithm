import sys; sys.stdin = open('input_계산기2.txt', 'r')

def isp(s):
    if s == '*' or s == '/':
        return 2
    elif s == '(':
        return 0
    else:
        return 1

def icp(s):
    if s == '*' or s == '/':
        return 2
    elif s == '(':
        return 3
    else:
        return 1

def cal_1(lst):          # 후위 표기식으로 변환하는 함수
    stack = []
    for i in lst:
        if i.isdigit():             # 숫자인 경우 빈 리스트에 넣어준다.
            result_1.append(i)
        elif i == '(':              # 여는 괄호일 경우 무조건 스택에 넣어준다.
            stack.append(i)
        elif i == ')':              # 닫는 괄호가 나오면 여는 괄호가 나올 때 까지 pop해준다.
            while stack and stack[top] != '(':
                result_1.append(stack.pop())
            stack.pop()             # 여는 괄호를 pop해준다.
        elif i == '*' or i == '/':  # 곱하기나 나누기가 나오면
            if not stack:           # 스택이 비어있으면 무조건 넣어주고
                stack.append(i)
            else:                   # 스택의 isp와 자기의 icp를 확인해서 isp가 낮은 연산자가 낳올 때 까지 pop해준다.
                while stack and isp(stack[-1]) >= icp(i):
                    result_1.append(stack.pop())
                stack.append(i)     # pop을 다 해주고 넣어준다.
        elif i == '+' or i == '-':  # 더하기와 빼기도 똑같다.
            if not stack:
                stack.append(i)
            else:
                while stack and isp(stack[-1]) >= icp(i):
                    result_1.append(stack.pop())
                stack.append(i)
    while stack:                   # 스택이 빌 때 까지 리스트에 pop해준다.
        result_1.append(stack.pop())

def cal2(lst):                  # 후위 표기식을 계산하는 함수
    stack = []
    for i in lst:               # i가 숫자면 무조건 스택에 넣어준다.
        if i.isdigit():
            stack.append(i)
        elif i == '+':          # 연산자가 나오면 (스택의 두번째 pop) 연산자 (스택의 첫번째 pop) 값을 넣어준다.
            a = stack.pop()
            b = stack.pop()
            c = int(b) + int(a)
            stack.append(c)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            c = int(b) - int(a)
            stack.append(c)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            c = int(b) * int(a)
            stack.append(c)
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            c = int(b) // int(a)
            stack.append(c)
    return int(stack[-1])


for tc in range(1, 11):
    N = int(input())
    nums = list(input())
    result_1 = []
    cal_1(nums)
    print(f'#{tc}', cal2(result_1))
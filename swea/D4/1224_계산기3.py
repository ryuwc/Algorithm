import sys; sys.stdin = open('1224.txt', 'r')

'''
[1단계] 중위표기법 => 후위표기법으로 변환
1) 입력 받은 중위 표기식에서 토큰을 읽는다.
2) 토큰이 피연산자이면 토큰을 출력한다
3) 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4) 토큰이 오른쪽 괄호 ‘)’이면 스택 top에 왼쪽 괄호 ‘(‘가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5) 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6) 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
 - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
'''

'''
[2단계] 후위표기법 수식을 계산 
1) 피연산자를 만나면 스택에 push 한다. 
2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다. 
3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
'''
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
            while stack and stack[-1] != '(':
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

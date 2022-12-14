import sys

# 먼저 괄호의 짝이 제대로 맞는지 확인부터 하는 함수
# main함수에서 확인 할 수 있지만 그렇게 하면 코드가 너무 복잡하고 지저분해짐
def is_right():
    stack = []
    for s in st:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s == ']':
            if not stack:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


def main():
    S = []
    for s in st:
        # 여는 괄호면 일단 무조건 append
        if s == '(' or s == '[':
            S.append(s)
        # 닫는 괄호가 나오고 스택의 탑이 같은 타입의 여는 괄호면 일단 2, 3을 넣어줌
        elif s == ')':
            if S[-1] == '(':
                S.pop()
                S.append(2)
            # 스택의 탑이 숫자면, 괄호의 값을 구해줘야함 괄호의 짝이 무조건 맞기 때문에
            # 여는 괄호가 나올때 까지 == 스택의 탑이 숫자일 때 까지 tmp에 더해주고
            # 2 또는 3을 곱하여 괄호의 값을 구해줌
            else:
                tmp = 0
                while type(S[-1]) == int:
                    tmp += S.pop()
                S.pop()
                S.append(tmp*2)

        elif s == ']':
            if S[-1] == '[':
                S.pop()
                S.append(3)
            else:
                tmp = 0
                while type(S[-1]) == int:
                    tmp += S.pop()
                S.pop()
                S.append(tmp * 3)

    return sum(S)


if __name__ == '__main__':
    st = sys.stdin.readline().strip()

    if is_right():
        print(main())
    else:
        print(0)

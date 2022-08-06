# 1번 방식
def func(s):
    s = s.lower()             # 일단 소문자화
    alnum = []                # 새로운 리스트를 만들어 준다.
    for i in s:               # 받은 문자열을 순회해준다. 이때 공백도 포함이 된다
        if i.isalnum():       # 문자열이 알파벳이거나 숫자인경우에
            alnum.append(i)   # 새로만든 리스트에 저장
    if alnum == alnum[::-1]:  # 리스트가 거꾸로해도 똑같은 경우
        return True
    else:
        return False

# 2번 방식
import re                     #re 모듈을 불러온다.

def func(s):   
    s = s.lower()             # 일단 소문자화 시켜준다.
    s = re.sub('[^0-9a-z]', '', s) 
    # re.sub('[]')에서 [^a-z]등으로 설정하면 ^다음에 입력한 값들 이 아닌건 ''으로 없애준다.
    # 앞에 ^를 안해주면 a-z 즉, 알파벳을 ''으로 없애주는 기능이 적용된다.
    return s == s[::-1]   #거꾸로 해서 일치하는지를 리턴
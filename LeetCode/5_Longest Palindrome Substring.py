def func(s):
    if s == s[::-1]:
        return s
    
    lst = []     # 먼저 빈리스트를 만들어 준다. -> 결과 예상 값 ['c', 'bb', 'b', 'b', 'd']
    for i in range(len(s)):              # 문자열의 갯수를 기준으로 range를 for문으로 돌려준다. (우리가 구해야 할 것은 index이기 때문)
        for j in range(len(s), i, -1):   # 첫 조건문의 값과 비교하기 range를 거꾸로 돌려주고, 첫 반복문 인덱스 번호의 문자열의 갯수는 초과하면 안되기 때문에 i를 넣어준다.(??) 
            if s[i:j] == s[i:j][::-1]:   # 조건문을 돌린 인덱스 값을 이용한 슬라이싱으로 비교를 해준다.
                lst.append(s[i:j])       # lst에는 모든 팰린드롬을 넣을 것이다.
    
    result = ''             # 이제 lst에는 모든 팰린드롬 문자열이 있을 것이고 이를 뽑아와야한다.
    num = 0                 # 예로 lst에 ['c', 'bb', 'b', 'b', 'd']가 있으면 bb를 뽑아야 한다. 
    for i in lst:           # bb를 뽑을 간단한 방법이 있을 것 같지만 모르기 때문에 이방법을 쓴다.
        if len(i) > num:
            num = len(i)
            result = i
    return result

print(func('babad'))
print(func('cbbd'))
# 1번 방식
import re

def func(s:str):     
    s = s.lower()     # 일단 소문자화
    s = s.replace(banned_str, '')  # replace를 통해 banned의 단어를 지워줌
    s = re.sub('[^a-z]', ' ', s)   # re.sub를 통해 알파벳이 아닌건 공백으로 만들어줌
    lst = s.split()   # 공백을 기준으로 단어들을 리스트로 묶어줌
    lst_count = 0     # 제일 많이 나온 단어의 수를 넣어줌(다른 단어의 수랑 비교하기 위해)
    str_count = ''    # 제일 많이 나온 단어를 넣어줄 문자열을 만든다.
    for i in lst:
        if lst.count(i) > lst_count: # 만약 단어의 수가 lst_count보다 많은 경우에는
            lst_count = lst.count(i) # 그 수를 lst_count에 넣어준다.
            str_count = i            # 그 단어 역시 str_count에 넣어준다.
    return str_count

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
banned_str = ''.join(banned)
print(func(paragraph))

# 2번 방식
import re
from collections import Counter

def func(s:str):     
    s = s.lower()    
    s = s.replace(banned_str, '') 
    s = re.sub('[^a-z]', ' ', s)
    lst = s.split()  
    counts = Counter(lst)      
    # Counter모듈을 불러와서 리스트의 요소들을 key로, 그 숫자를 value로 하는 딕셔너리를 쉽게 만들 수 있다.
    return counts.most_common()
    # 허나 이 딕녀서리를 추출 하려면 .most_common이 필요하다.
    # most_common(1)을 하면 [(ball: 2)]형태로 출력되어 슬라이싱해 ball을 꺼내온다.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
banned_str = ''.join(banned)

print(func(paragraph))

# 3번 방식
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 입력 값을 모두 소문자로 banned는 리스트 형식이라 for문으로 변환함.
paragraph = paragraph.lower()

for num in range(len(banned)):
    banned[num] = banned[num].lower()

# paragraph에서 문자와 띄어쓰기를 제외하고 없애기
new_paragraph = ""
for alpha in paragraph:
    if alpha.isalpha() or alpha == " ":
        new_paragraph += alpha
    
# new_paragraph를 공백 단위로 쪼개서 리스트 만들기
paragraph_list = new_paragraph.split()

# 리스트에서 banned 단어 제외하고 많이 나온 단서 세기
paragraph_dict = dict()
for word in paragraph_list:
    if (word not in banned) and (word in paragraph_dict):
        paragraph_dict[word] += 1
    # else로만 설정할 경우 banned 단어로만 구성된 문장이 나올 경우 오답이 나올 수 있음.
    else:
        paragraph_dict[word] = 1
print(paragraph_dict)
result = sorted(paragraph_dict.items(), key = lambda x: x[1], reverse = True)

print(result[0][0])
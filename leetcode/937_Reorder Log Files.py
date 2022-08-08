# 1번 방식
def func(logs):
    letters, digits = [], []         # 로그의 식별자 다음이 숫자, 문자인 리스트 두 개를 만들어준다.
    for log in logs:
        if log.split()[1].isdigit(): # 식별자 다음의 요소가 숫자인 경우, digits리스트에 넣어준다.
            digits.append(log)
        else:                        # 식별자 다음의 요소가 문자인 경우, letters리스트에 넣어준다.
            letters.append(log)
    letters = sorted(letters, key=lambda x: (x.split()[1], x.split()[0])) 
    # ↑ letters를 sorted와 lambda를 통해 정리, 정리 기준은 식별자 다음의 요소, 같을 경우, 식별자를 기준으로 정렬
    return letters + digits          # 두 리스트를 더해준다.

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(func(logs))

# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
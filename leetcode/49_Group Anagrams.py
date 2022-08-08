import collections

def func(lst):
    dic = collections.defaultdict(list)  # defaultdict를 통해 value가 list인 딕셔너리를 만든다.
    for i in lst:
        abc = ''.join(sorted(i))  # abc는 오름차순으로 만든 단어 i이다.
        dic[abc].append(i)        # 딕셔너리에 key는 abc, value에는 i라는 리스트를 추가해준다.
    return list(dic.values())

print(func(['eat','tea','tan','ate','nat','bat']))
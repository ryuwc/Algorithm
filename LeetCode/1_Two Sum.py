def func(nums, target):
    result = []
    nex = 0                  # 두 번째 조건문의 인덱스를 바꿔줘야 하기 때문에 변수 설정
    for i in nums[:-1]:      # nums의 마지막 요소를 빼고 반복문을 돌려줌
        nex += 1
        for j in nums[nex:]:                # nums의 nex번째 인덱스부터 순회할 것임
            if i + j == target:             # 순회하는 요소들이 target과 같아지는 순간
                result.append(nums.index(i)) # result에 첫 번째 요소의 index번호가 들어갈 것
                nums.pop(result[0])          # 첫 번째 요소를 nums에서 지워줌
                nums.insert(result[0], 'a')  # 첫 번째 요소의 자리에 임의의 문자열을 하나 넣어줌
                result.append(nums.index(j)) # 두 번째 요소의 인덱스 값을 result에 넣어줌
                return result
                # ↑ pop과 insert를 사용한 이유는 [3,3], 6같은 경우 i의 인덱스와 j의 인덱스를 넣어줘야 하는데,
                # 둘다 0이 들어가버림 중복 방지용
print(func([1, 2, 5, 3], 8))
print(func([2, 7, 11, 15], 9))
print(func([1, 2, 3, 4], 4))
print(func([3, 3], 6))       # 이 경우
print(func([2, 7, 11, 15], 9))

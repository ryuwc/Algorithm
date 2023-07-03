import sys


def main():
    # 입력받기
    N = int(sys.stdin.readline().strip())
    tmp_nums = list(map(int, sys.stdin.readline().strip().split()))

    # 입력받은 수들을 인덱스와 함께 쌍으로 묶어 nums 리스트 생성
    nums = [(i, tmp_nums[i]) for i in range(N)]

    target_idx = 0  # 현재 타겟 인덱스 초기화
    rst = []  # 결과값을 담을 리스트 초기화

    for i in range(N):
        idx, num = nums.pop(target_idx)  # nums에서 타겟 인덱스에 해당하는 요소를 추출
        rst.append(idx)  # 인덱스 값을 결과 리스트에 추가

        # 타겟 인덱스를 새로 계산
        if nums:  # nums가 비어있지 않은 경우만 인덱스를 계산
            if num > 0:
                target_idx = (target_idx + num - 1) % len(nums)
            else:
                target_idx = (target_idx + num) % len(nums)

    # 결과값 출력
    for num in rst:
        print(num + 1, end=' ')


if __name__ == '__main__':
    main()

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        lst_ordered = sorted(nums)
        result = 0
        for idx, i in enumerate(lst_ordered):
            if idx % 2 == 0:
                result += i

        return result
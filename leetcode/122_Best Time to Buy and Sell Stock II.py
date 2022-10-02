class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rst = 0
        # 현재 값과 다음 값을 비교해서 다음 값이 더 크면 차이를 더해준다.
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                rst += prices[i+1] - prices[i]
        return rst
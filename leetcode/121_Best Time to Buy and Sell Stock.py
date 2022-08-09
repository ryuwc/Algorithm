class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0   # 가장 큰 수익
        me = prices[0]   # # 내가 산 가격을 일단 처음 가격으로 가정
        for i in prices:
            profit_now = i - me  # profit_now는 현재 팔때의 수익
            if profit_max < profit_now:  # 만약 profit_max가 내가 팔 때의 수익보다 낮다면
                profit_max = profit_now  # profit_max는 내가 팔 때의 수익이 됨
            if i < me:  # 근데 만약 내가 삿던 가격보다 지금 가격이 더 싸면
                me = i  # 내가 산 가격은 이 때가 됨
        return profit_max
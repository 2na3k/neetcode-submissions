class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        # for i in range(len(prices) - 1):
        #     print("price", prices[i])
        #     print("prices other", prices[i + 1:])
        #     if prices[i] <= min(prices[i + 1:]):
        #         return max(prices[i + 1:]) - prices[i]
        # return 0
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        return maxP
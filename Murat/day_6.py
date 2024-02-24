class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = [[0]*2 for _ in len(prices)]
        return self.helper(prices,0,1)

    def helper(self,prices, left, right):
        if right >= len(prices):
            return 0
        if prices[left] > prices[right]:
            return self.helper(prices,right, right+1)
        else:
            val1 = self.helper(prices,left, right+1)
            val2 = prices[right]-prices[left]

            return max(val1,val2)
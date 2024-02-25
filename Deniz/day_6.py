class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        start, end = 0, 1
        length = len(prices)
        while end < length:
            tmp = prices[end] - prices[start]
            if tmp > 0:
                maxProf = tmp if tmp > maxProf else maxProf
            else:
                start = end 
            end += 1
        return maxProf

// Solution for 21. Best Time to Buy and Sell Stock
// link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length<2)
            return 0;

        int buy = 0;
        int sell = 1;
        int profit = 0;
        int temp;

        while(sell!=prices.length) {
            temp = prices[sell] - prices[buy];

            if (temp>profit) {
                profit = temp;
                sell++;
            } else if (temp<0) {
                buy++;
                if (buy==sell &&sell<prices.length-1)
                    sell++;
            } else {
                sell++;
            }
        }

        return profit;
    }
}
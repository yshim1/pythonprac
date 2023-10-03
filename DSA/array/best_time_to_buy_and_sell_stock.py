class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        profit = 0
        for i in range(0, len(prices)):
            if prices[i] < prices[buy_pointer]:
                buy_pointer = i
            profit = max(profit, prices[i] - prices[buy_pointer])
        return profit


#OR

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_point = prices[0]

        for price in prices:
            if price < buy_point:
                buy_point = price
            profit = max(profit, price - buy_point)
        return profit
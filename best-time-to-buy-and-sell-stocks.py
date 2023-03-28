#Given an array of stock prices, we want to find the maximum profit that can be obtained by buying and selling a stock. In other words, we want to find the largest difference between any two prices, where the second price is greater than the first.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # initialize to an arbitrary large value
        max_profit = 0
                
        for price in prices:
            min_price = min(min_price, price)  # update minimum price
            profit = price - min_price  # calculate the profit for the current price
            max_profit = max(max_profit, profit)  # compare with the maximum profit seen so far
        
        return max_profit

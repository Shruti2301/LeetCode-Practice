# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# We are given stock prices for each day. 
# We can buy once and sell once, and we must buy before we sell.
# Our goal is to find max profit.
# If no profit is possible --> return 0
# We can say that while we move through the array, whatever is the lowest element in the array
# is the lowest price observed so far (Best Day to Buy a Stock), so for each day, we can calculate
# (Profit = Current Price - Lowest Price So Far), and we will keep track of maximum profit.
#
# # Why?
# 
# Max Profit = Buying at Lowest Price and Selling at a Higher Price
# We can scan the array once and then update the values as we go. 
# Let's start with min-price = 1 (This is the min price on Day 1)
# Initially, our max-profit = 0
# We can traverse the prices or array from left to right
# If today's price is lower than min-price, we should update the min-price and calculate profit if sold today.
# If the max-profit is higher, we update max-profit. 
# At the end, we shall return max-profit and if profit keeps on decreasing, profit remains 0

# This approach will use Greedy/One Pass Pattern

class Solution(object):
    def maxProfit(self,prices):
        if not prices:
            return 0
        
        min_price = prices[0] # Initialize minimum price as first day price
        max_profit = 0 # Initialize maximum profit as 0
        
        # Traverse through the prices
        for currentprice in prices:
            
            # Update min price if current price is lower
            if currentprice < min_price: 
                min_price = currentprice
            else:
            # Calculate profit if sold at current price
                profit = currentprice - min_price
                
                # Update max if current profit is higher
                if profit > max_profit: 
                    max_profit = profit
        
        # Return the maximum profit
        return max_profit
    
sol = Solution()

# Test Case 1
prices1 = [7,1,5,3,6,4]
res1 = sol.maxProfit(prices1)
print("Test Case 1 Output:", res1)

# Test Case 2
prices2 = [7,6,4,3,1]
res2 = sol.maxProfit(prices2)
print('Test Case 2 Output:', res2)

# Test Case 3
prices3 = [5]
res3 = sol.maxProfit(prices3)
print("Test Case 3 Output:", res3)

# Test Case 4
prices4 = [3,2,6,1,4]
res4 = sol.maxProfit(prices4)
print('Test Case 4 Output:', res4)
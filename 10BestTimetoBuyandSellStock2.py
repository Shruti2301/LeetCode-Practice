# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
# However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
# Find and return the maximum profit you can achieve.

# In this problem, we can buy and sell multiple times. We can only hold one stock at a time.
# We can sell and buy on the same day but different stocks or numbers.
# Our goal is to return the maximum profit. In prev question, only one transaction was allowed.
# and we needed to find one single max profit. But, in this case, we can do multiple transactions and in the end, we can add all the profitable moves. 
# So, we need to track whenever the price goes up from one day to the next day, and store the profit. 
# We can say, if price[i] > price[i-1] ---> Add the ( difference = price[i] - price[i-1] ) to the profit.
# Every increasing sequence can be split into small profits.
# Adding all small profits will give us one big profit.
# Lets initialize profit = 0 in the beginning. 
# We can traverse through the array from start to end.
# If today's price is greater than yesterday's price, we buy yesterday and sell today and add the difference to the profit.
# If prices keep falling, then we do nothing. At the end, we will return total profit.

# If the stock goes from 1 -> 2 -> 3, the total profit is 2.
# How? We do (2-1) + (3-2) = 2 that is we add up all the positive day to day differences
class Solution(object):
    def maxProfit(self, prices):
        # Initialize Profit to 0 
        profit = 0
        # Traverse array from second day to the last day.
        for i in range(1, len(prices)):
            # If prices increase from yesterday --> add the profit
            if prices[i] > prices[i-1]:
                difference = prices[i] - prices[i-1]
                profit = profit + difference
        
        return profit

# Test Cases
sol = Solution()

# Test Case 1 : Multiple peaks and valleys
prices1 = [7,1,5,3,6,4]
res1 = sol.maxProfit(prices1) # 5-1 = 4 and 6-3 =3 so therefore total profit = 4+3 = 7
print('Test Case 1 Output:', res1)


# Test Case 2 : Continuously Increasing
prices2 = [1,2,3,4,5]
res2 = sol.maxProfit(prices2) # 1+1+1+1 = 4
print('Test Case 2 Output:', res2)

# Test Case 3 : Continuously Decreasing
prices3 = [7,6,4,3,1]
res3 = sol.maxProfit(prices3) # Total = 0
print('Test Case 1 Output:', res3)

# Test Case 4 : Flat Prices
prices4 = [2,2,2,2]
res4 = sol.maxProfit(prices4) # Total Profit = 0 
print('Test Case 1 Output:', res4)

# Time Complexity : O(n) : Traverse the pricess array of length n exactly once
# Space Complexity : O(1) : Use profit and difference in place and not anything else
    

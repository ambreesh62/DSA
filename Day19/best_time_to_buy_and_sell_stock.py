# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

# Example
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.max_profit(prices))  # Output should be 5

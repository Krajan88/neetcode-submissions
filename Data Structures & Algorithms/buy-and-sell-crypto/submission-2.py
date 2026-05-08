class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers
        #if left prices < right price, profit: price right - price left
        #update max_profit using max() method

        #if left price > right price, shift the left pointer to the right pointer
        
        #always increment the r

        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r

            r+=1

        return max_profit


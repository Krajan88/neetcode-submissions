class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers
        #if left prices < right price, profit: price right - price left
        #update max_profit using max() method

        #if left price > right price, shift the left pointer to the right pointer
        
        #always increment the r

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

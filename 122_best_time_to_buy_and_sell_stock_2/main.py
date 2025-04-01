class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        max_profit = 0
        
        for i in range(1, len(prices)):
            k = i - 1
            if prices[k] < prices[i]:
                profit =  prices[i] -prices[k] 
                
                max_profit+=profit
                
        return max_profit
            


prices = [7,1,5,3,6,4]
s1 = Solution()
print(s1.maxProfit(prices))
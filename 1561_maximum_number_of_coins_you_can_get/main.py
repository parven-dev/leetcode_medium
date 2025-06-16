class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        
        piles.sort()
        n = len(piles)//3
        total = 0
        for i in range(len(piles)-2, n -1, -2):
            total+=piles[i]
            
        return total
            
            

s1 = Solution()
piles = [2,4,1,2,7,8]
# piles = [9,8,7,6,5,1,2,3,4]

print(s1.maxCoins(piles))
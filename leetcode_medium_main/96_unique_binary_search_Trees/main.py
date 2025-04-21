class Solution:
    def numTrees(self, n: int) -> int:
        
        memo = {}
        def unique_trees(n):
            
            if n == 0 or n == 1:
                return 1
            
            if n in memo:
                return memo[n]
        
            
            total = 0
            for i in range(1,n+1):            
                left = i - 1 
                right = n - i 
            
                total+=unique_trees(left) * unique_trees(right)
            
            memo[n] = total
            print(memo)

            return total
        return unique_trees(n)
    

n = 19
s1 = Solution()
print(s1.numTrees(n))
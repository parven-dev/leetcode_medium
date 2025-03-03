class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        
        max_value = 0
        for i in str(n):
            if int(i) > max_value:
                max_value = int(i)
        
        return max_value
    
    
    
s1 = Solution()

n = 82734
print(s1.minPartitions(n))
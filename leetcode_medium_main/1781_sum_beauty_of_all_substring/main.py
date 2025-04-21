
from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        my_list = []
        
        n = len(s) 
        my_dict = {}
        total = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                freq = Counter(substring)
                min_freq = min(freq.values())
                max_freq = max(freq.values())
                result = max_freq - min_freq
                total+=result
                
            
                
        return total
    
        
s = "aabcb"

s1 = Solution()
print(s1.beautySum(s))
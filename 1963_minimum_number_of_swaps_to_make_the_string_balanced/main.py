
import math

class Solution:
    def minSwaps(self, s: str) -> int:
        
        balance = 0
        max_balance = 0
        for i in range(len(s)):
            
            if s[i] == "[":
                balance+=1
                
            else:
                balance-=1
                
            
            print(balance)  
            if balance < 0:
                max_balance = max(max_balance, abs(balance))
            
        return math.ceil(max_balance/2)
            
                
        # swap =  min(balance,) 
        # return math.ceil(abs(swap)/2)
    

s1 = Solution()
s = "]]][[["

# s = "[]"
print(s1.minSwaps(s))
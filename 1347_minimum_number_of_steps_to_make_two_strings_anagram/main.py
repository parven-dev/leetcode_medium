class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        anangram_s = {}
        anangram_t = {}
        
        total = 0
        for i in range(len(s)):
            anangram_s[s[i]] = anangram_s.get(s[i], 0) + 1
            anangram_t[t[i]] = anangram_t.get(t[i], 0) + 1
            
        
        
        for key in anangram_s:
            if key in anangram_t:
                if anangram_s[key] > anangram_t[key]:
                    left_value = anangram_s[key] - anangram_t[key]
                    total +=left_value
                
            else:
                total+=anangram_s[key]
                    
        return total

                
                    
                    
            
            
        
    
    
    
    
    

s1 = Solution()

# s = "bab"
# t = "aba"
s = "leetcode"
t = "practice"

print(s1.minSteps(s, t))
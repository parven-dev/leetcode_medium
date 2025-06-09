class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
   
        
        left = 0
        right = 0
        total = 0
        
        while left < len(s) and right  < len(t):
            if s[left] == t[right]:
                total += 1
                left += 1
                right += 1
                
            else:
                left+=1
                
            
                
        return abs(total-len(t))
                
                

s1 = Solution()

s = "coaching"
t = "coding"



# s = "abcde"
# t = "a"

print(s1.appendCharacters(s, t))
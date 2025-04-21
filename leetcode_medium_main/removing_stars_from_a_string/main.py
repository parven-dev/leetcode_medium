class Solution:
    def removeStars(self, s: str) -> str:
        star_stack = []
        
        stack_append = []
        for i in range(len(s)):
            star_stack.append(s[i])
            # print(star_stack[-1])
            if  star_stack[-1] == "*":
                star_stack.pop()
                star_stack.pop()
            
        return star_stack
    
    

# s = "leet**cod*e"
s = "erase*****"
s1 = Solution()
print(s1.removeStars(s))
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        my_stack = []
        extra = 0
        for i in s:
            if i == "(":
                my_stack.append(i)
                extra +=1
                
            if i == ")":
                if my_stack and my_stack[-1] == "(":
                    my_stack.pop()
                    extra-=1
                else:
                    my_stack.append(i)
                    
        
        return  len(my_stack) 
                

                    
                
    
    
# s = "())"
s = "((("
# s = "()"
s1 = Solution()
print(s1.minAddToMakeValid(s))
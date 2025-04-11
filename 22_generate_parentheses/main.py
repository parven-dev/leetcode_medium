class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # open_parenthesis = "("
        # close_parenthesis = ")"
        
        my_string = []
        # currs = []
        def backTrack(curr, open, close):
            if (len(curr) == 2 * n):
                my_string.append(curr)
                return
                
            if open < n:
                backTrack(curr + "(", open+1, close)
            
            if close < open:
                backTrack(curr + ")", open,  close + 1)
            
            # currs.append(curr)
            
        
        backTrack("", 0,0)
    
        return my_string
    
    

n = 3
s1 = Solution()
print(s1.generateParenthesis(n))
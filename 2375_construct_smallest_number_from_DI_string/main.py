class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        my_stack = []
            
        
        counter = []
        
        for i in range(len(pattern) + 1):
            my_stack.append(i+1)

            if i == len(pattern) or pattern[i] == "I":
                while my_stack:
                    counter.append(str(my_stack.pop()))
     
        
        return "".join(counter)
         
    
    
    
    
    
pattern = "IIIDIDDD"
s1 = Solution()
print(s1.smallestNumber(pattern))
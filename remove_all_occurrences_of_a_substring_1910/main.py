class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack_data = []

        for i in range(len(s)):
            stack_data.append(s[i])
            my_element_of_stack = "".join(stack_data[-len(part):])

            if my_element_of_stack == part:
                del stack_data[-len(part):]
            
        return stack_data
        
        

s = "daabcbaabcbc"
part = "abc"
s1 = Solution()
print(s1.removeOccurrences(s, part))
# binary = bin(9)
# print(binary[2:])


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        result = []
        reversed_result = []
        counter = 2
        
        while counter <= n -2:
            binary = ""
            temp = n
            while temp > 0:
                remainder = temp % counter
                binary = str(remainder) + binary
                temp = temp // counter
                
            result.append(binary)
            reversed_result.append("".join(reversed(binary)))
            if result != reversed_result:
                return False
            counter+=1
            
        return result == reversed_result
                
    
    

s1 = Solution()    
n = 9
print(s1.isStrictlyPalindromic(n))

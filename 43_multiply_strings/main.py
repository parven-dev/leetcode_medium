
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0
        char_to_int = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
        for i in num1:
            # print(number1, char_to_int[i])
            # print(f"{number1}, {char_to_int[i]}")

            number1 = number1 * 10 + char_to_int[i]
        for j in num2:
            number2 = number2 * 10 + char_to_int[j]
        return number1 * number2
            
            
                
                
                
s1 = Solution()
print(s1.multiply(num1="12", num2="33"))
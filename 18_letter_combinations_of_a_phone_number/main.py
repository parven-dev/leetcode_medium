
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
     
        my_dict = {
        2: "abc",
        3: "edf",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
        my_list = []
    
        result  = []
        for i in digits:
            if int(i) in my_dict:
                my_list.append(my_dict[int(i)])
        for j in product(*(my_list)):
            result.append("".join(j))
            
        if my_list:
            return result
        else:
            return my_list
digits = "23"
s1 = Solution()
print(s1.letterCombinations(digits))

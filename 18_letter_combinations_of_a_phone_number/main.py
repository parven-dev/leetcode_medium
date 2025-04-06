
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        my_dict = {
    2: "abc",
    3: "edf",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqr",
    8: "stu",
    9: "vwx"
}
        my_list = []
        
        result  = []
        for i in digits:
            if int(i) in my_dict:
                my_list.append(my_dict[int(i)])
        for j in product(*(my_list)):
            result.append("".join(j))
            
        return result
digits = "23"
s1 = Solution()
print(s1.letterCombinations(digits))
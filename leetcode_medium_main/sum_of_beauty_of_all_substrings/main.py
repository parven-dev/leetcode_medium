from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        
        sum_of_beauty = 0
        for i in range(len(s)):
            my_dict = defaultdict(int)
            for j in range(i, len(s)):
                my_dict[s[j]] +=1
                print(my_dict)
                max_frequcny = max(my_dict.values())
                min_frequcny = min(my_dict.values())
                beauty = max_frequcny - min_frequcny
                sum_of_beauty+=beauty
        
        return sum_of_beauty
    
    
    
s1 = Solution()
s = "aabcb"
print(s1.beautySum(s))

from collections import Counter

class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        
        
        list_without_duplicate = []
        for response in responses:
            list_without_duplicate.extend(set(response))
     
        freq = Counter(list_without_duplicate)
        max_freq = max(freq.values())
        
        count_values = []
        for key, value in freq.items():
            if value == max_freq:
                count_values.append(key)
                
                
        return min(count_values)


s1 = Solution()
# responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]
print(s1.findCommonResponse(responses))
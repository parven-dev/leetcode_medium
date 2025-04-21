

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # my_data = {}
        
        # print(len(["",""]))
        if not strs:
            return []
        
        result = defaultdict(list)

        for i in strs:
            sorted_str = "".join(sorted(i))
            result[sorted_str].append(i)

        
        # for key, value in my_data.items():
        #     if value in my_data.values():
        #         result[value].append(key)
        
        return list(result.values())
            
            
    
    

# strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["",""]
s1 = Solution()
print(s1.groupAnagrams(strs))
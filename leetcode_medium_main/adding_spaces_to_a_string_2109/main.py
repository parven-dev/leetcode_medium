class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        
        index = 0
        # index = spaces[indexx]
        my_list = []
        # print(index)
        
        for i in range(len(spaces)):
            sliced_string = s[index:spaces[i]]
            my_list.append(sliced_string)
            index = spaces[i]
        
        combine_lists = " ".join(my_list) + " " +  s[spaces[-1]:]
        return combine_lists
            
    
    
    
s = "LeetcodeHelpsMeLearn" 
spaces = [8,13,15]
# s = "icodeinpython"
# spaces = [1,5,7,9]


s = "spacing"
spaces = [0,1,2,3,4,5,6]
s1 = Solution()
print(s1.addSpaces(s, spaces))
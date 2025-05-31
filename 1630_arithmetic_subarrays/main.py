

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r:list[int]) -> list[bool]:
    
        all_lists = []
        
        for i in range(len(l)):
            
            main_index = l[i]
            main_index2 = r[i]
            listts = nums[main_index: main_index2+1]
            sorted_list = sorted(listts)
            all_lists.append(sorted_list)
            
        my_lists = [[] for _ in range(len(all_lists))] 
        # print(my_lists)
        index= 0
        # print(len(all_lists))
        while index < len(all_lists):
            for j in range(1, len(all_lists[index])):
                k = j - 1
                common_value = all_lists[index][k] - all_lists[index][j]
                my_lists[index].append(common_value)
            index+=1
        result = []
        for sublist in my_lists:
            if len(sublist) == 0 or len(set(sublist)) == 1:
                result.append(True)
            else:
                result.append(False)
        return result
            
       
            
        
        
    

s1 = Solution()
# nums = [4,6,5,9,3,7]
# l = [0,0,2]
# r = [2,3,5]

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
print(s1.checkArithmeticSubarrays(nums, l, r))
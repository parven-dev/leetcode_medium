class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()        
        group_array = []

        group_len = len(nums) // 3
        for i in range(0, len(nums), 3):
            sliced_group = nums[i:i+3]
            
            min_value  = min(sliced_group)
            max_value = max(sliced_group)
           
            
            max_diff = max_value - min_value
            
            if max_diff <= k:
                group_array.append(sliced_group)
              
        if len(group_array) != group_len:
            return []
        else:
            return group_array
    
    
    


s1 = Solution()
# nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
# k = 14

nums = [2,4,2,2,5,2]
k = 2
print(s1.divideArray(nums, k))
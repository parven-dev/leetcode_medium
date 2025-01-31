class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) -1
        
        first_index = -1
        last_index = -1
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                first_index = middle
                right = middle -1
            
            elif target < nums[middle] :
                right = middle - 1
                
            elif target > nums[middle]:
                left = middle  + 1

        
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = (left + right ) // 2
            
            if nums[middle] == target:
                last_index = middle
                left = middle + 1
            
            elif target < nums[middle]:
                right = middle - 1
                
            
            elif target > nums[middle] :
                left = middle + 1


        return [first_index, last_index]

# nums, target  = [5,7,7,8,8,10],  8
nums, target = [], 0
s1 = Solution()
print(s1.searchRange(nums, target))
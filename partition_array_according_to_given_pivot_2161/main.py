class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        
        greater = []
        lesser = []
        middle = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                lesser.append(nums[i])
            
            elif nums[i] == pivot:
                middle.append(nums[i])
            else:
                greater.append(nums[i])

        return lesser+middle+  greater

s1 = Solution()
# nums = [9,12,5,10,14,3,10]
# pivot = 10

nums = [-3,4,3,2]
pivot = 2
print(s1.pivotArray(nums, pivot))
    
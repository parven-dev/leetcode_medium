class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        start = 0
        end = len(nums)-1
        
        while start < end:
            middle = (start + end ) // 2
            
            
            if nums[middle] < nums[middle+1]:
                start = middle + 1
            else:
                end = middle 
                
        return start
    


nums = [1,2,3,1]
s1 = Solution()
print(s1.findPeakElement(nums))
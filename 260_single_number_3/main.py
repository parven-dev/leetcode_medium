class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        
        counter = []
        
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter.append(nums[i])
            else:
                counter.remove(nums[i])
                
        return counter
        
        
        
    
    
nums = [1,2,1,3,2,5]
s1 = Solution()
print(s1.singleNumber(nums))
    
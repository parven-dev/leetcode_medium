class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        my_result = []
        
        nums.sort()
        
        for i in range( len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum == 0:
                    my_result.append([nums[i], nums[left], nums[right]])
                    
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1
                        
                    left+=1
                    right-=1
                
                if total_sum < 0 :
                    left +=1
                    
                if total_sum > 0:
                    right -=1
                    
                    
        return my_result
                
                
                
    
    
    
    
s1 = Solution()
nums = [-1,0,1,2,-1,-4]
result = s1.threeSum(nums)
print(result)
    
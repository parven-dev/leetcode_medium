class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        
        
        sorted_value = sorted(nums)
        
        left = 0
        right = len(nums)-1
        
        result = []
        while left <= right:
            
            result.append(sorted_value[left]+sorted_value[right])
            left+=1
            right-=1
        return  max(result)
                
        

nums = [3,5,2,3]
s1 = Solution()
print(s1.minPairSum(nums))
    
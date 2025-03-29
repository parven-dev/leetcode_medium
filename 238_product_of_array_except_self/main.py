class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        product_of_nums = [1]
        sums = 1
        product_of_nums2 = [1]
        
        for i in range(1,len(nums)):
            k = i-1
            sums = sums*nums[k]
            product_of_nums.append(sums)
            
        sums2 = 1
        for j in reversed(range(1,len(nums))):
            
            sums2 = sums2*nums[j]
            product_of_nums2.append(sums2)
            
        
        product_of_nums.reverse()
            
        result = [a*b for a, b in (zip(product_of_nums2, product_of_nums))]
        result.reverse()
        return result
            
    
    
        
nums = [1,2,3,4]
s1 = Solution()
print(s1.productExceptSelf(nums))     
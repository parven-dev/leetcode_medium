class Solution:
    
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        
        positive_integers = []
        negative_integers = []
        result = []
        for i in nums:
            if i < 0:
                negative_integers.append(i)
            else:
                positive_integers.append(i)
                
        pointer_one = 0
        pointer_second = 0
        
        
        for j in range(len(nums)):
            
            if j % 2 == 0:
                result.append(positive_integers[pointer_one])
                pointer_one+=1
            else:
                result.append(negative_integers[pointer_second])
                pointer_second+=1
                
                
        return result
                
    







s1 = Solution()
nums = [3,1,-2,-5,2,-4]

print(s1.rearrangeArray(nums))
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        total = []
        counter = 1
        
        for i in range(len(nums)):
            if not total:
                total.append(nums[i])
            min_value = total[0]
            left_value =  nums[i] - min_value
            if left_value <= k:
                total.append(nums[i])
                
            else:
                total= [nums[i]]
                counter+=1
                    
             
        return counter
    


nums = [3,6,1,2,5]
k = 2
s1 = Solution()
print(s1.partitionArray(nums, k))
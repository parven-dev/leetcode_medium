class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        index = 0
        my_list = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] =  nums[index] * -1
            
            elif nums[index] < 0:
                my_list.append(abs(nums[i]))
        
        return my_list
            




# nums = [4,3,2,7,8,2,3,1]
nums = [10,2,5,10,9,1,1,4,3,7]

s1 = Solution()
print(s1.findDuplicates(nums))    
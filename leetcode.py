class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reversed_array = nums[::-1]
     
        # first_part = reversed_array[:k]
        # first_part_reversed = first_part[::-1]
        
        # second_part = reversed_array[k:]
        # second_part_reversed = second_part[::-1]

        # return first_part_reversed + second_part_reversed


        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
        

nums = [1,2,3,4,5,6,7] 
k = 3
# nums = [-1,-100,3,99]
# k = 2
s1 = Solution()

print(s1.rotate(nums, k))
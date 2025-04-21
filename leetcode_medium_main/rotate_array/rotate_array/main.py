class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reversed_array = nums[::-1]
        # len_of_array = len(nums)
        # print(len_of_array)
        # print(reversed_array)
        first_part = reversed_array[:k]
        # print(first_part)
        first_part_reversed = first_part[::-1]
        print(first_part_reversed)
        
        second_part = reversed_array[k:]
        second_part_reversed = second_part[::-1]
        return first_part_reversed + second_part_reversed
        # print(firs_part, second_part)
        # rotate_kth_element = reversed_array
        # print(first_part + second_part)
        # return first_part_reversed + second_part
    

nums = [1,2,3,4,5,6,7] 
k = 3
# nums = [-1,-100,3,99]
# k = 2
s1 = Solution()

print(s1.rotate(nums, k))
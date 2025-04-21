class Solution:
    
    def peakIndexInMountainArray_helper(self,arr, start, end):
        
        if start == end:
            return start
        
        middle_index = (start + end) // 2
        
       
        
        if arr[middle_index] > arr[middle_index+1]:
            return self.peakIndexInMountainArray_helper(arr, start, middle_index)
        
        return self.peakIndexInMountainArray_helper(arr, middle_index+1, end)
    
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        
       return self.peakIndexInMountainArray_helper(arr, 0, len(arr)-1)
    
    
    
arr = [0,10,5,2]
# arr = [0,1,0]
s1 = Solution()
print(s1.peakIndexInMountainArray(arr))
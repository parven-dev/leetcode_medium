

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1

        while start <= end:
            middle = (start + end) // 2 
    

            if target < matrix[middle][0]:
                end = middle - 1
                
            elif target > matrix[middle][-1]:
                start = middle + 1
                
            else:
                left = 0
                right = len(matrix[middle]) -1
                
                while left <= right:
                    
                    middle_left_right = (left + right ) // 2 
                    
                    if matrix[middle][middle_left_right] == target:
                        return True
                    elif matrix[middle][middle_left_right] < target:
                        left = middle_left_right + 1
                    else:
                        right = middle_left_right - 1
                return False
                
        return False
    
s1 = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(s1.searchMatrix(matrix, target))
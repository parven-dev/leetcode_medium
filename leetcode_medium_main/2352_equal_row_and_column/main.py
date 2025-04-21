class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        columns = [tuple(col) for  col  in zip(*grid)]

        col_dictionary = {}
        
        counter = 0
        for col in columns:
            col_dictionary[col] = col_dictionary.get(col, 0) + 1
        
      
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in col_dictionary:
                counter+=col_dictionary[row_tuple]
            
        return counter
    
    
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
s1 = Solution()
print(s1.equalPairs(grid))

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        columns = list(zip(*grid))

        columns_dictionary = {i: list(column) for  i , column in enumerate(columns)}
        row_dictionary = {}
        
        counter = 0
        for i in range(len(grid)):
            row_dictionary[i] = grid[i]
        
        for value in row_dictionary.values():
            if value in columns_dictionary.values():
                counter+=1
        
        
     
        return counter
    
    
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
s1 = Solution()
print(s1.equalPairs(grid))
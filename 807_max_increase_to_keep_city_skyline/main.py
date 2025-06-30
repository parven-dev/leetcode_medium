class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        
        max_row = []
        max_col = []
        cols_range = len(grid[0])
        total_max_result = 0
        
        for i in range(cols_range):
            max_row_value = max(grid[i])
            max_col_value = max([col[i] for col in grid])
            max_row.append(max_row_value)
            max_col.append(max_col_value)
            
        
        for j in range(cols_range):
            for k in range(cols_range):
                current = grid[j][k]
                row_max = max_row[j]
                col_max = max_col[k]
                
                min_value = min(row_max, col_max)
                # print(min_value, current)
                total_value = min_value - current
                total_max_result+=total_value
                
        return total_max_result
                
                
                
                

s1 = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(s1.maxIncreaseKeepingSkyline(grid))
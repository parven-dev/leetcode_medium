class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        
       

        row_count, col_count = len(grid), len(grid[0])
        
        # index = 0
        col_matrix = []
        row_matrix = grid
        
        
        result_matrix = []
        
       
        for j in range(col_count):
            col = [grid[i][j] for i in range(row_count)]
            col_matrix.append(col)
        
        for k in range(row_count):
            result = []
            for l in range(col_count):
                ones_row = row_matrix[k].count(1)
                zeros_row = row_matrix[k].count(0)
                ones_col =  col_matrix[l].count(1)
                zeros_col = col_matrix[l].count(0)
                
                total = ones_row + ones_col - zeros_row - zeros_col
                result.append(total)
            result_matrix.append(result)
            # print(f"row{k} one: {ones_row} row{k} zero: {zeros_row}, col{k} one: {ones_col} col{k} zero: {zeros_col}")
    
        return result_matrix


martix = Solution()
grid = [[0,1,1],[1,0,1],[0,0,1]]
print(martix.onesMinusZeros(grid))
        
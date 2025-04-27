class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        
        index_value = []
        for i  in range(len(score)):
            index_value.append(score[i][k])
        
        return index_value
         
                
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2  
s1 = Solution()
print(s1.sortTheStudents(score, k))
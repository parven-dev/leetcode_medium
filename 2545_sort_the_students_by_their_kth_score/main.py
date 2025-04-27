class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return score, k
    
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2  
s1 = Solution()
print(s1.sortTheStudents(score, k))
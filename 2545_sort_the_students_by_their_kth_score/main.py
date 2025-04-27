class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        
        index_value = []
        result = []
        
        for i  in range(len(score)):
            index_value.append((score[i][k], i))
        
        index_value.sort(reverse=True)
        
        for value, ids in index_value:
            result.append(score[ids])
        
        print(index_value)
        # sorted_index = set(index_value)
        # print(sorted_index)
        
        
        # for index in range(len(score)):
        #     if any(item in sorted_index for item in score[index]):
        #         result.append(score[index])
        # for index in range(len(score)):
        #     for j in range(len(sorted_index)):
        #         # print(sorted_index[j])
        #         if sorted_index[j] in score[index]:
        #             # print(score[j])
        #             result.append(score[j])
        # for j in range(len(score)):
        #     print()
        #     if sorted_index[index] in score[j]:
        #         result.append(score[i])
        #         index+=1
        #     else:
        #         index+=1
  
                    
        return result
                
         
                
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2  
s1 = Solution()
print(s1.sortTheStudents(score, k))
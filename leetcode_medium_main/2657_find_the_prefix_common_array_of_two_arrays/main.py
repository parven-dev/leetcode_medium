class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        
        A_list_values = []
        B_list_values = []
        
        result = []
        for i in range(len(A)):
            A_list_values.append(A[i])
            B_list_values.append(B[i])
            common_values = list(set(A_list_values) & set(B_list_values))
            
            if common_values:
                result.append(len(common_values))
            
            else:
                result.append(0)
        
        
        return result
        
    
    
A = [1,3,2,4] 
B = [3,1,2,4]

s1 = Solution()
print(s1.findThePrefixCommonArray(A, B))
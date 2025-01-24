
from collections import Counter


class Solution:
   
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        # converted_word1 = set(word1)
        # converted_word2 = set(word2) 
         
        # if len(converted_word1) == len(converted_word2):
        #         return True
        
        word1 = list(word1)
        word2 = list(word2)

        for i in range(len(word1)):
            for j in range(len(word2)):   
                                 
                    # temp1 = list[word1]
                    # temp2  = list[word2]
                    temp1 = list(word1)
                    temp2 = list(word2)
                    
                    # temp = word1[i]
                    # # print(word1)
                    # word1[i] = word2[j]
                    # word2[j] = temp
                    
                    temp1[i], temp2[j] = temp2[j], temp1[i]
                    
                    
                    if len(set(temp1)) == len(set(temp2)):
                        return True
        
        return False
                           
                    
                
            
  


# word1 = "abcc"
# word2 = "aab"

# word1 = "aa"

# word2 = "bcd"

word1 = "abcc"
word2 = "aab"

s1 = Solution()

print(s1.isItPossible(word1, word2))
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        my_vowels = []
        
        my_List = []
        for vowel in range(len(s)):
            my_List.append(s[vowel])
            if s[vowel] in vowels:
                my_vowels.append(s[vowel])
                
        vowel_index = 0
        sorted_vowels = sorted(my_vowels)
        for i in range(len(my_List)):
            if my_List[i] in vowels:
                my_List[i]= sorted_vowels[vowel_index]
                vowel_index+=1
        
        return "".join(my_List)
                
                
        
                    
            
            
    
    
    

s1 = Solution()
s = "bCaAdE"
print(s1.sortVowels(s))
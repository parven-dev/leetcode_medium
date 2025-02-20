class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        result = 0
        for item in  range(len(word)):
            # print(word[item])
            if word[item] in vowels:
                # pass
        
                data = (item + 1) * (len(word) - item)
                result+=data
    
        return result
    
    

word = "aba"
s1 = Solution()
print(s1.countVowels(word))
        
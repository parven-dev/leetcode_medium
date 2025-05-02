class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        my_index_dictionary = {}
        unique_string = set(s)
        # print(unique_string)
        check = []
        # print(sorted(s))
        for i in reversed(range((len(s)))):
            if s[i] in unique_string:
                if s[i] not in check:
                    check.append(s[i])
                    my_index_dictionary[s[i]] = i
    
        
        result = []
    
        start_index = 0
        max_value =  0
        for j in range(len(s)):
            if s[j] in my_index_dictionary:
                if max_value < my_index_dictionary[s[j]]:
                    max_value = max(max_value, my_index_dictionary[s[j]])
                    
                if j == max_value:
                    size = j - start_index + 1
                    result.append(size)
                    start_index= j + 1
                
                    
        return result
                
    
    
    

s1 = Solution()
s = "ababcbacadefegdehijhklij"
print(s1.partitionLabels(s))
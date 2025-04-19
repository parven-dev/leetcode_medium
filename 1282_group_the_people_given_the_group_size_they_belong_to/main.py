class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        
        my_list = []
        my_dict = {}
        
        for i , size in enumerate(groupSizes):
            if size not in my_dict:
                my_dict[size] = []

            my_dict[size].append(i)
            
            print(my_dict[size])   
            if len(my_dict[size]) == size:
                my_list.append(my_dict[size])
                my_dict[size]  = []
                
                
        return my_list
            
            
        
    
    
groupSizes = [3,3,3,3,3,1,3]
s1 = Solution()
print(s1.groupThePeople(groupSizes))
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        two_d_list = []
        
        temp = nums[:]
        
        while len(temp) > 0:
            check_list = []

            for num in temp[:]:
                if num not in check_list:
                    check_list.append(num)
                      
            two_d_list.append(check_list)
            
            for num in check_list:
                # print(num)
                temp.remove(num)
            
            
        return two_d_list
            
        
        
    
    

s1 = Solution()
nums = [1,3,4,1,2,3,1]
print(s1.findMatrix(nums))
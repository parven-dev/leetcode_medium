class Solution:
    def validStrings(self, n: int) ->list[str]:
        
        my_queue = ["0", "1"]
        
        while len(my_queue[0]) < n:
            item = my_queue.pop(0)
            print(item)
            my_queue.append(item+"1")
            
            
            if item[-1] == "1":
                my_queue.append(item + "0")

        return my_queue
                
      
        
     


n = 1
s1 = Solution()
print(s1.validStrings(n))
    
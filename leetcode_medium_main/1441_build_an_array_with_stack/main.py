class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        my_stack = []

        count = []
        print(target[-1])
        for i in range(1,n+1):
           
            my_stack.append(i)
            count.append("Push")
            last_value = my_stack.pop()

            if last_value not in target :
                count.append("Pop")
            else:
                my_stack.append(last_value) 
                
            if i == target[-1]:
                break
   
        return count

# target = [2,4]
# n = 4
# target = [1,3]
# n = 3
target = [1,2]
n = 4
s1 = Solution()
print(s1.buildArray(target, n))

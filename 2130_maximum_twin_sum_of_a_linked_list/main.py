from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, val):
        new_node = ListNode(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_stack = []
        
        temp = head
        sum_of_values = []
        while temp is not None:
            my_stack.append(temp.val)
            temp = temp.next
        
        for i in range(len(my_stack)//2):
            sum_of_int = my_stack[i]  + my_stack.pop()
            sum_of_values.append(sum_of_int)
        return  max(sum_of_values)
            
         
    
   
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
 
    
ll = Solution()
# my_list = [1,2,3,3,4,4,5] 
my_list = [5,4,2,1]

for i in range(len(my_list)):
    ll.insert(my_list[i]) 

# print(ll.tail.val)
ll.display()
print("After")

print(ll.pairSum(ll.head))
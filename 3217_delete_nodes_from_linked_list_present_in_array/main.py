
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
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
            
            
    
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        unique_num = set(nums)
        
        dummy = ListNode(0)
        current = dummy
        
        temp = head
        
        while temp  is not None:
            if temp.val not  in unique_num:
                current.next = temp
                current = temp
            temp = temp.next
            
        current.next = None
            
        return dummy.next
        
     
    
    
    def display(self, head):
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next
    
ll = Solution()
my_list = [1,2,3,4,5]

for i in range(len(my_list)):
    ll.insert(my_list[i])
    
nums = [1,2,3]



# ll.display()
result = ll.modifiedList(nums, ll.head)

ll.display(result)


    
    
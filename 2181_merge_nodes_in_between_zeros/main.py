from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        dummy = ListNode(0)
        tail = dummy
        sums= 0
        while temp is not None:
            if temp.val != 0:
                sums+=temp.val
            else: 
                if sums > 0:
                    new_node = ListNode(sums)
                    tail.next = new_node
                    tail = new_node
                    sums = 0
            
            temp = temp.next
            
        return dummy.next
            
    
    def insert_nodes(self, val):
        new_node = ListNode(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else: 
            self.tail.next  = new_node
            self.tail = new_node
            
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

ll = Solution()
my_list = [0,3,1,0,4,5,2,0]

my_list = [0,1,0,3,0,2,2,0]
for i in range(len(my_list)):
    ll.insert_nodes(my_list[i])

print(ll.mergeNodes(ll.head))
    
# ll.display()
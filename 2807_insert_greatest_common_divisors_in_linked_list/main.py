
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        


class LinkedList:
    def __init__(self):
        self.head = None
        
    def gcd_of_linked_list(self,a, b):
        while b:
            a , b = b, a % b
            
        return a
    
    def append(self, val):
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            return 
        
        next_node = self.head
        while next_node.next:
            next_node = next_node.next
    
        next_node.next = new_node
        
        
        
    def insertGreatestCommonDivisors(self, head: Optional[Node]) -> Optional[Node]:
        
        if not head or not head.next:
            return head
        
        temp = head
        
        while temp and temp.next:
            get_gcd = self.gcd_of_linked_list(temp.val, temp.next.val)
            
            new_node = Node(get_gcd)
            
            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node
            
            temp = next_node
            
        return head
        
    def display(self):
        temp = self.head
        
        while temp is not None:
            print(temp.val)
            temp = temp.next
            
ll = LinkedList()
ll.append(18)
ll.append(6)
ll.append(10)
ll.append(3)

# ll.display()
ll.insertGreatestCommonDivisors(ll.head)

ll.display()
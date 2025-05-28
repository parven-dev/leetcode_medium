from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
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
            
            
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummy = ListNode(0)
        current = dummy
        
        my_stack  = []
        reverse_stack = []
        carry = 0
        
        while temp:
            my_stack.append(temp.val)
            temp = temp.next
        
        reverse_stack = my_stack[::-1]  
        
        result = []
        for item in reverse_stack:
            double_digit = item * 2 + carry
            carry = double_digit // 10
            result.append(double_digit % 10)
        
        if carry:
            result.append(carry)
        
        while result:
            poped_num = result.pop()
            new_node = ListNode(poped_num)
            current.next = new_node
            current = new_node
            
            
        return dummy.next
        
    
                                

            
    def display(self, head):
        temp = head
        
        while temp is not None:
            print(temp.val)
            temp = temp.next
            
 
ll = LinkedList()
   
my_list = [9,9,9,9]

for num in my_list:
    ll.insert(num)
    
# ll.display()
# print(ll.doubleIt(ll.head))

result = ll.doubleIt(ll.head)

ll.display(result)

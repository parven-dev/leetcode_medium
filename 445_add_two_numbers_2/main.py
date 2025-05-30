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
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        
        temp1 = l1
        temp2 = l2
        
        dummy = ListNode(0)
        current = dummy
        
        while temp1:
            stack1.append(temp1.val)
            temp1 = temp1.next
            
        while temp2:
            stack2.append(temp2.val)
            temp2 = temp2.next
            
        carry = 0
        result = []
        
        while stack1 or stack2:
            
            pop_value_temp1 = stack1.pop() if  stack1 else 0
            pop_value_temp2 = stack2.pop() if stack2  else 0
                    
            sum_value = pop_value_temp1 + pop_value_temp2 + carry
            carry = sum_value // 10
            result.append(sum_value % 10)
            
        if carry:
            result.append(carry)
        # print(reversed(result)
        
        for node_value in result:
            new_node = ListNode(node_value)
            current.next = new_node
            current = new_node
        
        return dummy.next
        
    
            
l1 = [7,2,4,3]
l2 = [5,6,4]

ll = LinkedList()
ll2 = LinkedList()

for item in l1:
    ll.insert(item)
    
for item2 in l2:
    ll2.insert(item2)

# print(ll.head.val, ll2.head.val)
result = ll.addTwoNumbers(ll.head, ll2.head)
print(result.val)
    
    
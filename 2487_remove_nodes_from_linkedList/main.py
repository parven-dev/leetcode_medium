from typing import Optional
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def removeNodes(self, head: Optional[Node]) -> Optional[Node]:
        my_list = []
        temp = head
        while temp:
            my_list.append(temp.val)
            temp = temp.next
        
        my_stack = []
        
        dummy = Node(0)
        current = dummy
        
        for i in range(len(my_list)):
            while my_stack and my_list[i] >  my_list[my_stack[-1]]:
                my_stack.pop()
            
         
            my_stack.append(i)
        for item in my_stack:
            new_node = Node(my_list[item])
            current.next = new_node
            current = new_node
        
        return dummy.next
            
        
        
            
    def display(self,head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next
            
ll = LinkedList()

my_list = [5,2,13,3,8]

for item in my_list:
    ll.insert(item)
            
# ll.display()
result = ll.removeNodes(ll.head)
ll.display(result)
# print(result)
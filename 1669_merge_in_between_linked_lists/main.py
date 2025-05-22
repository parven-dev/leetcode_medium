# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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
            
    def display(self):
        temp = self.head
        
        while temp is not None:
            print(temp.val)
            temp = temp.next   
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        temp2 = list1
        dumy = list2
        counter = 0
        counter2 = 0
        
        while counter < a-1:
            temp = temp.next
            counter+=1
        
        while counter2 < b:
            
            temp2 = temp2.next
            counter2+=1
            
        temp.next = dumy
        dumy = temp
        
        prevoious = None
        while temp is not None:
            prevoious = temp

            temp = temp.next
        
        prevoious.next = temp2.next
        temp = prevoious
        
        return list1
            
        # print(prevoious.val, temp2.next.val)

ll = Solution()
ll2 = Solution()

    
list1 = [10,1,13,6,9,5]

list2 = [1000000,1000001,1000002]

for i in range(len(list1)):
    ll.insert(list1[i])
    
for i in range(len(list2)):
    ll2.insert(list2[i]);

# print(ll.head.val)
# print(ll2.head.val)
a = 3
b = 4
print(ll.mergeInBetween(ll.head,a, b, ll2.head))
# ll.display()


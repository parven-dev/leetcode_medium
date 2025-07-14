from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        dummy = ListNode(0)
        current = dummy
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
            
        last_n_element = stack[-n:]
        remove_element = last_n_element[1:]
        
        sliced_list = stack[:-n]
        prefix_suffix_list = sliced_list + remove_element
        
        for num in prefix_suffix_list:
            new_value = ListNode(num)
            
            current.next = new_value
            current = new_value
        
        return dummy.next.val
        
       
      
    
    

s1 = Solution()
# head = [1,2,3,4,5],
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2

result = s1.removeNthFromEnd(head, n)
print(result)
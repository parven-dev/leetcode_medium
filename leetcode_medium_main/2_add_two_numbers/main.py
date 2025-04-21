class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list1 = LinkedList()
linked_list1.append(2)
linked_list1.append(4)
linked_list1.append(3)

linked_list2 = LinkedList()
linked_list2.append(5)
linked_list2.append(6)
linked_list2.append(4)


# print("Linked List 1:")
# linked_list1.display()

# print("Linked List 2:")
# linked_list2.display()

def a(linked_list1, linked_list2):
    carry = 0
    my_list = LinkedList()
    
    temp1 = linked_list1.head
    temp2 = linked_list2.head
    while temp1 is not None or temp2 is not None:
        if temp1 is not None and temp2 is not None:
            # print(temp1.data)
            l1 = temp1.data
            l2 = temp2.data
            
            total_value = l1 + l2 + carry
            node_value = total_value % 10
            carry = total_value // 10
            my_list.append(node_value)

            temp1 = temp1.next
            temp2 = temp2.next
            
        
    return my_list

print(a(linked_list1,  linked_list2))

result = a(linked_list1, linked_list2)
result.display()
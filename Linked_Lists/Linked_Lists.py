# 5. LINKED LISTS

# A Linked List is a linear data structure where each element (node) contains:
# 1. Data (the value to store)
# 2. A reference (or pointer) to the next node
class LLNode:
    def __init__(self,data):
        self.data = data
        self.next = None


# Types of Linked Lists:
# - Singly Linked List
class SLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# - Doubly Linked List (able to traverse backwards or forwards)
class DLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# - Circular Linked List (last node will point back to self.head (first node))
class CLLNode:
    def __init__(self,data):
        self.data = data
        self.next = self.head


# 5.1 Singly Linked List
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # - Insert at the beginning
    def insert_at_start(self,data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node

    # - Insert at the end
    def insert_at_end(self,data):
        new_node = SLLNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # - Delete by value
    def delete_by_value(self,value):
        if not self.head: # Case 1: List is empty
            return
        temp = self.head
        prev = None

        # Traverse the list to find the node
        while temp.data != value:
            prev = temp
            temp = temp.next

        # Case 2: Value not found
        if not temp:
            return
        
        # Case 3: Head node needs to be deleted
        if temp == self.head:
            self.head = temp.next
            return

        # Case 4: Delete the node in the middle or end
        prev.next = temp.next


    # - Print the linked list
    def print_LL(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
        print('None')


# 5.2 Doubly Linked List
class DoubleLinkedList ():
    def __init__(self):
        self.head = None
# - Insert at the end
    def insert_at_end(self,data):
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp != None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
# - Print the linked list
    def print_linked_list(self,data):
        temp = self.head
        if not self.head:
            print('empty list')
            return
        while temp != None:
            print(temp.data)
            temp = temp.next
        print('None')


# 6. PRACTICE QUESTIONS
# 1. Implement a Singly Linked List with insert, delete, and print methods.
# 2. Reverse a Singly Linked List.
# 3. Find the Middle Element of a Linked List.
# 4. Detect a Cycle in a Linked List.
# 5. Implement a Doubly Linked List with insert and print methods.
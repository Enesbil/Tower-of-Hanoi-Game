class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: #stack implementation using linked list
    def __init__(self):
        self.head = None #head will refer to top of stack. initialized as none for the empty stack.

    def push(self, value):
        new_disk = Node(value)
        new_disk.next = self.head
        self.head = new_disk

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def get_all_values(self): #pulls all the values in the stack as a list. top to bottom.
        current = self.head
        values_list = []
        while current != None:
            values_list.append(current.value)
            current = current.next
        return values_list
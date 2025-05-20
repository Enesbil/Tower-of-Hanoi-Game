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

class TowerOfHanoi:
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.moves = 0
        self.tower_1 = Stack()
        self.tower_2 = Stack()
        self.tower_3 = Stack()
        for i in range(num_disks, 0, -1):
            self.tower_1.push(i)
        self.towers = [self.tower_1, self.tower_2, self.tower_3]

    def is_valid_move(self, from_tower, to_tower):
        if self.towers[from_tower].peek() != None:
            if self.towers[to_tower].is_empty() and not(self.towers[from_tower].is_empty()):
                return True
            elif (self.towers[to_tower].peek() > self.towers[from_tower].peek()):
                return True
            else: 
                return False 
        else:
            return False

    def move_disk(self, from_tower, to_tower):
        if not(self.is_valid_move(from_tower, to_tower)):
            return False
        else:
            value_to_move = self.towers[from_tower].peek()
            self.towers[from_tower].pop()
            self.towers[to_tower].push(value_to_move)
            self.moves += 1
            return True

    def is_game_won(self): 
        if self.num_disks > 0 and (self.tower_1.is_empty() and self.tower_2.is_empty()):
            return True #no need to check if order of tower 3 is correct since other functions ensure correct gameplay
        else:
            return False


    def get_tower_state(self, tower_index):
        return self.towers[tower_index].get_all_values()

    def get_move_count(self):
        return self.moves
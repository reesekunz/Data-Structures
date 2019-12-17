from double_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')
# stack - used for recursion
# Last in First out
# Changing a pointer = O(1)
# Changing ALL the pointers = O(n)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?

    def push(self, value):  # push - Add items to the end of an array.
        # [1, 2, 3] => [1, 2, 3, 4] so need to make 4 the TAIL and point 3 to 4 instead of 3 => None
        self.size += 1
        # add value to the tail and store that value
        self.storage.add_to_tail(value)

    def pop(self):  # pop - Remove an item from the end of an array
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else: # if empty
            return None

    def len(self):  # length of stack
        return self.size

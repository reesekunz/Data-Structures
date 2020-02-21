from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')

# Stack - Last in First out (Stack of plates)


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):  # push - Add items to the end (tail)
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):  # pop - Remove items from end (tail)
         # if line is empty
        if self.size == 0:
            return None
        # if line isnt empty
        else:
            self.size -= 1
            return self.storage.remove_from_tail()  # make sure you return

    def len(self):
        return self.size

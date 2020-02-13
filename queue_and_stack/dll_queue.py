from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# Queue - First one in first one out (Line)


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):  # add item to back - tail- of queue (constant time of o(1))
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):  # remove and return item from front - head - of queue(constant time of o(1))
       # if line is empty
        if self.size == 0:
            return None
        # if line isnt empty
        else:
            self.size -= 1
            return self.storage.remove_from_head()  # make sure you return

    def len(self):
        return self.size

from double_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')
# queue - a line of items, first in first out
#   * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.
# Linked list better cause O(1) to add/remove from front or back


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):  # add item to back of queue (constant time or o(1))
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):  # remove and return item from front of queue (next person in line) (constant time or o(1))
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:  # if empty
            return None

    def len(self):  # length of items in queue
        return self.size

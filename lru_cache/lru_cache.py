from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # max number of nodes
        self.size = 0  # current number of nodes its holding
        # a doubly linked list that holds the key-value entires in correct order
        self.order = DoublyLinkedList()
        # storage dictionary that provides access to every node
        self.storage = dict()  # same as {}
        # Using two different data structures - DoublyLinkedList and Dictionary. Dictionaries are good for look up. DLL are good for insert and remove.

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
# Defining head as Most Recently Used, tail as Least Recently Used

    def get(self, key):
        # check to see if key exists in storage (dictionary)
        if key in self.storage:
            # get value out of storage with key as the parameter
            node = self.storage[key]
            # move value to head since it is now the most recently used
            # self.order because we are accessing move_to_front Doubly Linked List function. pass in node to move to front.
            self.order.move_to_front(node)
            return node.value[1]
        # key isnt in storage
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key is in cache already
        if key in self.storage:
            # get node from self.storage with key as parameter
            node = self.storage[key]
            node.value = (key, value)
            # update position, its now the Most Recently Used (MRU) - move to front
            self.order.move_to_front(node)
            # key isnt in cache and needs to be added
            return

            # cache is full - need to make room. same thing as above but just remove from head first.
        if self.size == self.limit:
            # remove LRU (remove from tail since we defined head as Most Recently Used) from both DLL and dict
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1
        # Adding to cache
        # add value to head as MRU
        self.order.add_to_head((key, value))
        # add to dictionary
        self.storage[key] = self.order.head
        # update size
        self.size += 1

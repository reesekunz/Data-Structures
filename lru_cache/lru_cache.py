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
        # a doubly linked list that holds the key-value entires
        # dont use dictionary to keep track of order cause dictionaries are unordered and changeable
        self.order = DoublyLinkedList()
        # storage dictionary that provides access to every node stored in the cache
        self.storage = {}
        # print("self.storage", self.storage)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            print("node", node)
            # moves to end, meaning its the most recently used
            self.order.move_to_end(node)
            return node.value
            # This is already being done in move_to_end DLL
            # return value if node is already at tail
        #     if self.order.tail == node:
        #         return node.value
        #     else:
        #         # move the key-value pair to the end of the order such that the pair is considered most-recently used.
        #         self.order.delete(node)
        #         self.order.add_to_tail(node)
        #     # Retrieves the value associated with the given key
        #         return node.value
        else:
            # Returns None if the key-value pair doesn't exist in the cache.
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
        # Check the length - if length is at limit, delete last
        # Check to see if key is in cache - cache is combo of dictionary and linked list
        if key in self.storage:
            # print("KEY IN STORAGE", key)
            # print("STORAGE", self.storage)
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        # If it is in the cache, move key to the front and update value
        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1
        # If not in the cache, add to the front of the cache
        # Defining head as most recent, tail as oldest
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1

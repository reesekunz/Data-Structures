# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# stack, queues, linked lists are linear
# trees, graphs, etc. are non linear


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # error handling
        if value is None:
            return
        # check if tree is empty - self.value is root of the tree
        elif self.value is None:
            # inserted value becomes root.
            self.value = BinarySearchTree(value)
        # tree exists.
        # insert RIGHT of root
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # insert LEFT of root
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # BASE CASE
        # 1. target found
        if target == self.value:
            return True
        # 2. or we hit None (target not in tree) - being handled below
        # RECURSIVE CASE
        # 1. Compare target to self.value. If target is greater go right, lesser go left
        if target >= self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False  # We hit None (target not in tree)
            # target < self.value, so go left
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False  # We hit None (target not in tree)

        # Return the maximum value found in the tree
    def get_max(self):
        # Go right as far as you can to find max.
        # 1. If right exists, go right
        if self.right is not None:
            return self.right.get_max()
        # 2. Otherwise, you found max value. Return value.

        else:
            return self.value

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)  # root value
        # BASE CASE: left and right are both None
        # RECURSIVE CASE:
        # Go Left and Right all the way down the tree
        # Go left
        if self.left is not None:
            self.left.for_each(cb)
        # Go right
        if self.right is not None:
            self.right.for_each(cb)

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

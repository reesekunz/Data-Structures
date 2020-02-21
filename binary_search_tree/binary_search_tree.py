from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('./queue_and_stack')

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

        # Iterative solution:
        # runtime of O(n)

        # cur = self
        # # Right as far as you can go
        # while self.right is not None:
        #     cur = cur.right
        # return cur.value

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)  # root value
        # BASE CASE: left and right are both None
        # RECURSIVE CASE:
        # Go Left and Right all the way down the tree
        if self.left is not None:
            self.left.for_each(cb)
        # Go right
        if self.right is not None:
            self.right.for_each(cb)
# use two if statements because you want to run both - theyre independent conditions
# BASE CASE: else both are none, stop recursion. dont need this since not returning anything
    # def iterative_for_each(self, cb):
    #     if self is None:
    #         print("BST is empty")
    #         return
    #     # Root node:
    #     cb(self.value) # call function on current node value
    #     # add left child to stack (if exists)
    #     # add right child to stack (if exists)

    #     # All children of root node:
    #     while len(stack) > 0: # still nodes left
    #         # pop top_of_stack
    #         #cb(top_of_stack)
    #         # go left - if left child, push onto stack
    #         # go right - if right child, push onto stack

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # in order = left, root, right

        # 1. Base Case: when do we stop? when we're at bottom of the tree
        # node is None or node has no children
        if node is None:
            return

        # 2. Recursive Case - how do we get to the bottom of the tree.
        # go left (as far as possible)
        self.in_order_print(node.left)
        print(node.value)
        # go right (as far as possible)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # set up a QUEUE - FIFO. Queue represents the nodes we need to backtrack to.
        # initialize with root node
        q = Queue()
        q.enqueue(node)

        # while queue NOT empty
        while q.len() > 0:
            # dequeue node
            current_node = q.dequeue().value
            print("BFT current node value", current_node.value)
            # print node.value
            # print("BFT current node value", current_node.value)
            # enqueue node.left
            if current_node.left:
                q.enqueue(current_node.left)
            # enqueue node.right
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # set up a STACK - LIFO. Stack represents the nodes we need to backtrack to (haven't visited both children yet)
        # initialize with root node
        stack = Stack()
        stack.push(node)

        # while stack is NOT empty
        while stack.len() > 0:
            # pop node from stack
            current_node = stack.pop().value
            # print value
            print("DFT current node value", node.value)
            # push node.left
            if current_node.left:
                stack.push(current_node.left)
            # push node.right
            if current_node.right:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # in_order a good reference

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

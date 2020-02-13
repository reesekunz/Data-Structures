"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):  # Unlinking - changing the pointers before and after it to skip a node
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
       # 1. create new Node with value being passed
        # need to pass in None otherwise throw error "NoneType object not callable"
        new_node = ListNode(value, None, None)
        self.length += 1  # 2. Adding to list, need to allocate space for it.
      # 3. if list is empty, insert into the empty list
        if not self.head:
            # if self.head is None:
            self.head = new_node
            self.tail = new_node
    # 4. Inserting head into a list that already exists
        else:
            # set next pointer of new Node to old head... new node => old head
            new_node.next = self.head
            # set previous pointer of old head to new Node... new node <= old head
            self.head.prev = new_node
            # update 'head' to be new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    # Dont need all of this since you can call delete function down below that includes it
    def remove_from_head(self):
        # # remove from an empty linked list (dont have to do anything since already empty)
        # if self.head == None:
        #     return
        # # remove from linked list with 1 element (head and tail are now None since it will be empty)
        # elif self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # # everything else
        # else:
        #     # new head is now old head's next Node
        #     self.head = self.head.next
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # 1. create new Node with value being passed
        # need to pass in None otherwise throw error "NoneType object not callable"
        new_node = ListNode(value, None, None)
        self.length += 1  # 2. Adding to list, need to allocate space for it.
      # 3. if list is empty, insert into the empty list
        # if self.head is None:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
    # 4. Inserting head into a list that already exists
        else:

            # set next pointer of old tail to new node ... old tail => new node
            self.tail.next = new_node
            # set previous pointer of new node to old tail... old tail <= new node
            new_node.prev = self.tail
            # update "tail" to be new node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    # Dont need all of this since you can call delete function down below that includes it
    def remove_from_tail(self):
        # # remove from an empty linked list (dont have to do anything since already empty)
        # if self.head == None:
        #     return
        # # remove from linked list with 1 element (head and tail are now None since it will be empty)
        # elif self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # # everything else
        # else:
        #     # new tail is now old tails's previous Node
        #     self.tail = self.tail.prev
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # check to see if node is already at the front
        if node is self.head:
            return
        # node is not at front already
        else:
            value = node.value  # grab the node value
            self.delete(node)  # delete the node in its current spot
            # take node value grabed and move it to the front
            self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # check to see if node is already at the end
        if node is self.tail:
            return
        # node is not at endalready
        else:
            value = node.value  # grab the node value
            self.delete(node)  # delete the node in its current spot
            # take node value grabed and move it to the end
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # remove from an empty linked list (dont have to do anything since already empty)
        # if self.head == None:
        if not self.head and not self.tail:
            return
        self.length -= 1  # remove length by 1 since deleting
        # remove from linked list with 1 element (head and tail are now None since it will be empty)
        if self.head == self.tail:
            self.head = None
            self.tail = None
            # If deleted node is the head
        elif self.head is node:
            self.head = node.next  # new head is old head's next pointer
            node.delete()  # delete old head
            # If deleted node is the tail
        elif self.tail is node:
            self.tail = node.prev  # new tail is old tails previous pointer
            node.delete()  # delete old tail
            # Everything else
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        current_node = self.head
        max_value = current_node.value
        while current_node is not None:  # while were not at the end (tail)
            if current_node.value > max_value:  # Compare values
                max_value = current_node.value  # Update max value
            current_node = current_node.next  # Current node becomes next node
        return max_value

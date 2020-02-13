class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list (if head == None, linked list empty)
        self.head = None
    # reference to the tail of the list
        self.tail = None

    def add_to_head(self, value):
        # 1. create new Node with value being passed
        new_node = Node(value)
        # 2. set next pointer of new Node => old head
        new_node.set_next(self.head)
        if self.head is None:  # 3a. if list is empty, insert into the empty list
            self.head = new_node
            self.tail = new_node
        else:  # 3b. Inserting head into a list that already exists
         # update 'head' to be new node
            self.head = new_node

    def add_to_tail(self, value):
       # 1. create new Node with value being passed
        new_node = Node(value)

        # 2a. if list is empty, insert into the empty list
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # 2b. Inserting tail into a list that already exists
        else:
            # update 'tail' to be new node
            self.tail = new_node
            # 3. set next pointer of old tail => new Node
            self.tail.set_next(new_node)

    def remove_head(self):
        # remove from an empty linked list
        if self.head == None:
            return
        # remove from linked list with 1 element (head and tail are equal)
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # general
        else:
            # new head = old head's next Node
            self.head = self.head.get_next()

    # STRETCH

    def insert_at(self, value, position):
        pass

    def contains(self, value):
        current_node = self.head
        while(current_node.get_next() is not None):  # while were not at the end (tail)
            # do stuff
            current_node = current_node.get_next()

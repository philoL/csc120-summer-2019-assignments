class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        return str(self._value)

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, node):
        node._next = self._head
        self._head = node
        self._size += 1
        if node._next == None:
            self._tail = node

    def append(self, node):
        if self._tail == None:
            self.add(node)
        else:
            self._tail._next = node
            self._tail = node
            self._size += 1

    def print_nodes(self):
        cur =  self._head
        while cur:
            print(cur._value)
            cur = cur._next

    def remove_first(self):
        first_node = self._head
        if first_node:
            self._size -= 1
            self._head = first_node._next
            first_node._next = None
        return first_node

    def sort(self):
        _sorted = LinkedList()
        curr = self._head
        if curr == None:
            return
        else:
            curr = self.remove_first()
            while curr != None:
                _sorted.insert(curr) #insert curr into _sorted
                curr = self.remove_first()
        self._head = _sorted._head
        self._tail = _sorted._tail
        self._size = _sorted._size

    def insert(self, node):
        #insert a node into a sorted linked list
        if self._head == None: # edge case: empty list

        else:
            curr = self._head
            if curr._value >= node._value: # case 1: insertion at beginning

            else:
                is_inserted = False
                while next != None: # case 2: insertion in middle


                if not is_inserted: # case 3: insertion at end


    def concat(self, other):
        self._tail._next = other._head
        self._size += other._size
        if other._tail:
            self._tail = other._tail

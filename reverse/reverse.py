class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if not self.head: #if not head, keep movin
            return
        if not node.get_next(): #if we're at the last node, set it to the head
            self.head = node
            node.set_next(prev) #set the next node to the previous node
            return

        new_next = node.get_next() #save the current node's next
        node.set_next(prev) #set the next node to the previous node
        self.reverse_list(new_next, node)

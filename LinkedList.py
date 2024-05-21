class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        songs = []
        current = self.head
        while (current):
            songs.append(str(current.data))
            current = current.next

        return songs

    def delete(self, value):
        # Handle empty list
        if not self.head:
            return

        # Delete head node if value matches
        if self.head.data == value:
            self.head = self.head.next
            return

        # Traverse to find the node
        current = self.head
        previous = None
        while current:
            if current.data == value:
                # Update previous node's next pointer to bypass the deleted node
                previous.next = current.next
                return
            previous = current
            current = current.next

        # Value not found
        print("Value not found in the linked list")

        def __iter__(self):
            """
            Makes the LinkedList class iterable.
            """
            current = self.head
            return self

        def __next__(self):
            """
            Iterator protocol for moving to the next node.
            Raises StopIteration when the end of the list is reached.
            """
            if not current:
                raise StopIteration
            data = current.data
            current = current.next
            return data

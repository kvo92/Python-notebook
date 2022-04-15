class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


def insertNodeAtHead(llist, data):
    # Write your code here
    pass

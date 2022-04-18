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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    if llist:
        # the next of the node is linked to the rest of the linked list
        node.next = llist
    return node


def nullCheck(llist):
    if llist:
        print("not null")
    else:
        print("null")


llist = SinglyLinkedList()
nullCheck(llist)

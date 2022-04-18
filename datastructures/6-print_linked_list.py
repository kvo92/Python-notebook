class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            node.next = self.head
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def printLinkedList(head):
        # create a temp and asign its value with head
        temp = head
        # while temp.next isn't equal to None
        while (temp.next != None):
            # print temp.data
            print(temp.data)
            # assign temp with next node
            temp = temp.next
        # at the end of the while loop, there still the last node
        # print that node data
        print(temp.data)

    def printLinkedListRecursive(head):
        print(head.data)
        if (head.next == None):
            return
        SinglyLinkedList.printLinkedListRecursive(head.next)

    def insertNodeAtTheEnd(node):

        pass


if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    SinglyLinkedList.printLinkedList(llist.head)
    SinglyLinkedList.printLinkedListRecursive(llist.head)

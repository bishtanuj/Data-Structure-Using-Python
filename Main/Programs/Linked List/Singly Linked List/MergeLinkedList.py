# Program to merge two linked lists

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class to create a linked list
class LinkedList:
    # create an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # function to insert the elements into linked list
    def insertion(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    # function to display the elements of linked list
    def display(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value


# driver
if __name__ == '__main__':
    # create an object of linked list 1
    items_1 = LinkedList()

    # insert the following elements into the linked list 1
    items_1.insertion(12)
    items_1.insertion(13)
    items_1.insertion(14)

    # print the elements of linked list 1
    print("Elements of linked list 1:", end=" ")
    for i in items_1.display():
        print(i, end="->")
    print(None)

    # create an object of linked list 2
    items_2 = LinkedList()

    # insert the following elements into the linked list 2
    items_2.insertion(16)
    items_2.insertion(17)
    items_2.insertion(18)

    # print the elements of linked list 2
    print("Elements of linked list 2:", end=" ")
    for i in items_2.display():
        print(i, end="->")
    print(None)

    # create an object for linked list containing solution
    items_3 = LinkedList()

    # merge both the linked lists
    for i in items_1.display():
        items_3.insertion(i)
    for i in items_2.display():
        items_3.insertion(i)

    # print the solution
    print("Merged Linked List:", end=" ")
    for i in items_3.display():
        print(i, end="->")
    print(None)

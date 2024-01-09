# Program to compute alternate elements of linked list

# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class to create a linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def display(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    # function to compute alternative elements of linked list
    def compute_alternative_elements(self):
        current, temp = self.head, self.head
        while current.next:
            temp = current.next
            current.next = temp.next
            current = temp.next


# driver
if __name__ == '__main__':

    # create an object for the linked list
    items = LinkedList()

    # insert the following elements in the linked list
    items.insertion(12)
    items.insertion(13)
    items.insertion(14)
    items.insertion(15)
    items.insertion(16)
    items.insertion(17)
    items.insertion(18)
    items.insertion(19)
    items.insertion(20)

    # display the elements of linked list
    print("Elements of linked list:", end=" ")
    for i in items.display():
        print(i, end="->")
    print(None)

    # display the alternative elements of linked list
    items.compute_alternative_elements()
    print("\nAlternative elements of linked list:", end=" ")
    for i in items.display():
        print(i, end="->")
    print(None)

# Program to create a linked list

# Program to create a linked list

# class to create a node
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


# class for the linked list
class LinkedList:
    # function to create an empty node
    def __init__(self):
        self.head = None
    
    # function to insert the insert the elements from the tail
    def insertion(self, data: int):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
    
    # function to display the linked list
    def display(self):
        if self.head:
            print("Linked List:",end=" ")
            current = self.head
            while current:
                print(current.data, end="->")
                current = current.next
            print(None)
        else:
            print("Linked List is empty!!")


if __name__ == '__main__':
    #  create the object of the LinkedList class
    linkedlist = LinkedList()

    # insert the following elements in the linkedlist
    linkedlist.insertion(45)
    linkedlist.insertion(42)
    linkedlist.insertion(43)
    linkedlist.insertion(48)
    linkedlist.insertion(54)
    linkedlist.insertion(58)
    linkedlist.insertion(75)
    linkedlist.insertion(87)
    linkedlist.insertion(92)
    linkedlist.insertion(98)
    linkedlist.insertion(100)

    # call the display function to print the linked list
    linkedlist.display()

"""
OUTPUT:
Linked List: 45->42->43->48->54->58->75->87->92->98->100->None
"""

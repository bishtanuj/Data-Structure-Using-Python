# Program to create a singly linked list

# class to create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


# class to create a linked list
class LinkedList:
  # function to create an empty linked list
  def __init__(self):
    self.head = None
    self.tail = None

  # function to insert the data into linked list
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
  # create an object of class LinkedList
  items = LinkedList()

  # insert the following elements into the linked list
  items.insertion(12)
  items.insertion(13)
  items.insertion(14)
  items.insertion(15)
  items.insertion(16)

  # display the elements of linked list
  print("Elements of linked list:", end=" ")
  for i in items.display():
    print(i, end="->")
  print(None)

# Program to compute the product of elements of linked list

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

  # function to insert the elements into the linked list
  def insertion(self, data):
    node = Node(data)
    if self.tail:
      self.tail.next = node
      self.tail = node
    else:
      self.head = node
      self.tail = node

  # function to compute the product of linked list
  def ComputeProduct(self):
    current = self.head
    temp = 1
    while current:
      temp *= current.data
      current = current.next
    return temp

  # function to display the elements of linekd list
  def display(self):
    current = self.head
    while current:
      value = current.data
      current = current.next
      yield value


# driver
if __name__ == '__main__':
  # create an object of class linked list
  items = LinkedList()

  # insert the following elements into the linked list
  items.insertion(1)
  items.insertion(2)
  items.insertion(3)

  # print the elements of linked list
  print("Elements of linked list:", end=" ")
  for i in items.display():
    print(i, end="->")
  print(None)

  # print the product of the elements of linked list
  print(f"Product of the linked list: {items.ComputeProduct()}")


'''
OUTPUT:
Elements of linked list: 1->2->3->None
Product of the linked list: 6
'''

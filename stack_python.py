class StackOfStrings():
  # stack implementation using linked lists

  class Node():
    # node class to implement linked lists
    item = ''
    nxt = None


  def __init__(self):
    # create an empty stack
    self.first = None 

  def push(self, item):
    # insert a new string into the stack
    old_first = self.first
    self.first = StackOfStrings.Node()
    self.first.item = item
    self.first.nxt = old_first

  def pop(self):
    # remove and return the most recently added string
    item = self.first.item
    self.first = self.first.nxt
    return item

  def is_empty(self):
    # check to see if the stack is empty
    return self.first == None
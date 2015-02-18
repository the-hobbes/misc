class QueueOfStringsLinkedList():
  '''
    Queue =   
      first - node - node - node - last
    Create a queue using a linked list as the data structure.
  '''

  class Node():
    item = ''
    nxt = None

  def __init__(self):
    self.last = QueueOfStringsLinkedList.Node()
    self.first = QueueOfStringsLinkedList.Node()

  def enqueue(self, item):
    # save a link to the last node
    # create a new node for the end
    # link the new node to the end of the list

    old_last = self.last
    self.last = QueueOfStringsLinkedList.Node()
    self.last.item = item
    self.last.nxt = None
    
    # handle empty queue
    if self.is_empty():
      self.first = self.last
    else:
      old_last.nxt = self.last  
    
  def dequeue(self):
    # save item to return
    # delete first node
    # return saved item
    
    item = self.first.item
    self.first = self.first.nxt

    # handle empty queue
    if self.is_empty():
      self.last = QueueOfStringsLinkedList.Node()

    return item
  
  def is_empty(self):
    if self.first == None:
      return True
    elif self.first.item  == '':
      return True
    
    return False
  
  def print_queue(self):
    node = self.first
    while(node.item):
      print node.item
      if node.nxt == None:
        break
      node = node.nxt
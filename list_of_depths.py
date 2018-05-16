#!/usr/bin/python

"""Given a binary tree, design an algorithm which creates a list of all the
		nodes at each depth (if you have a tree with depth d, you'll have d lists).
"""

import random

class BinaryTree:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

  def __str__(self):
      return "( " + str(self.data) + " ( " + str(self.left) + " | " + str(self.right) + "))"

def binaryTreeToListBFS(btree):
  # breadth-first search using queue.
  if btree is None:
      return []
  # Start by creating a sublist for the current node by itself.
  listofnodes = [[btree.data]]
  # Make a list of the tree instance.
  queue = [btree]
  # While there are still items in the queue...
  while len(queue) > 0:
    new_queue = []
    for node in queue:
  		# Add the left and right values of the node to a new list.
      if node.left is not None:
          new_queue.append(node.left)
      if node.right is not None:
          new_queue.append(node.right)
    # Set the queue to the new list of discovered nodes at each level.
    queue = new_queue
    # If we don't discover any new nodes, stop.
    if len(queue) == 0:
        break
    listofnodes.append([x.data for x in queue])
  return listofnodes

def binaryTreeToListDFS(btree, level, lists=None):
	if btree == None:
		return  # base case

	if lists is None:
		lists = []  # https://developmentality.wordpress.com/2010/08/23/python-gotcha-default-arguments/

	if len(lists) == level:  # this level isn't in lists yet
		lists.append([btree.data])
	else:
		lists[level].append(btree.data)
	binaryTreeToListDFS(btree.left, level + 1, lists)
	binaryTreeToListDFS(btree.right, level + 1, lists)
	return lists

def makeRandomBalancedTree(depth):
  if depth > 0:
      tree = BinaryTree(random.randint(0, 100))
      tree.left=makeRandomBalancedTree(depth-1)
      tree.right=makeRandomBalancedTree(depth-1)
      return tree

def main():
	n = 3
	balanced_tree = makeRandomBalancedTree(n)
	print "Balanced tree:"
	print balanced_tree

	print "\nBFS:"
	print binaryTreeToListBFS(balanced_tree)

	print "\nDFS:"
	print binaryTreeToListDFS(balanced_tree, 0)

if __name__ == '__main__':
	main()

#!/usr/bin/python

'''
	As an exercise, replicate the output of the unix command pstree.

	From PSTREE man page:

	pstree shows running processes as a tree.  The tree is rooted at either pid or init if pid is omitted.  If a user name is 
	specified, all process trees rooted at processes owned by that user are shown.

    pstree visually merges identical branches by putting them in square brackets and prefixing them with the repetition count, e.g.

	   init-+-getty
	        |-getty
	        |-getty
	        `-getty

       becomes

           init---4*[getty]

	Child threads of a process are found under the parent process and are shown with the process name in curly braces, e.g.

           icecast2---13*[{icecast2}]

Algorithm Idea:

- Look through the /proc/ vfs, and loop through all of the names of the directories that are integers. These represent processes.
- For each of these processes, look in the /stat file, and examine the 4th entry in the space delimeted file. This is the PID of
  the processes parent.
- add an entry to a dictionary whose key is the parent, and whose values are a list of child processes
- once the directory is filled, loop through it, printing the parents and children in a tree like form ** TBD **
'''

import subprocess, sys
from pprint import pprint

class AdjacencySetTree:
	'''
		A representation of a tree using a dictionary with adjacency sets.
		For example:

		N = {
					1 : set([1, 2, 3, 4, 5]),
					2 : set([6, 7, 8, 9]),
					... 
		}
	'''

	def __init__(self):
		self.N = {}

	def add_process(self, parent, child):
		if parent in self.N.keys():
			self.N[parent].update(child)
		else:
			self.N[parent] = set()
			self.N[parent].update(child)

	def __str__(self, *args, **kwargs):
		return str(self.N)


def make_tree(process_input):
	'''
		args: process_input, the input from get_processes
		returns: process_tree, a tree in dictionary format of processes
	'''
	BASE = '/proc/'
	STAT = '/stat'

	process_tree = AdjacencySetTree()

	for process in process_input:
		current_process = str(process)
		PATH = BASE + str(process) + STAT
		
		out = subprocess.Popen(['cat', PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		for line in out.stdout:
			line = line.split(' ')
			parent = line[3]
			process_tree.add_process(int(parent), [int(current_process)]) # a list because sets only accept iterables, and an int isn't an iterable

	return process_tree

def print_tree(parent, process_tree,  indent=' '):
	'''
		print the tree, recursively
		args: process_tree, the tree to be printed

		N = {
					1 : set([1, 2, 3, 4, 5]),
					2 : set([6, 7, 8, 9]),
					... 
		}
	'''
	print parent
	if parent not in process_tree:
		return
	for child in process_tree[parent]:
		sys.stdout.write(indent + '|-')
		print_tree(child, process_tree, indent + '| ')
		
	child = list(process_tree[parent])[-1]
	sys.stdout.write(indent + '`-')
	print_tree(child, process_tree, indent + '  ')

def get_processes():
	'''
		returns: a list of the integer directories representing processes in /proc/
	'''
	process_directories = []
	proc = subprocess.Popen(['ls', '/proc/'], stdout=subprocess.PIPE)
	
  # NOTE: instead of using a cast, it would be much better to use a regular
  # expression to just grab the numerical directories:
  # /proc/[0-9]*/ would do the trick.
	for line in proc.stdout:
		try:
			process_directories.append(int(line))
		except Exception, e: # ignore non-integers, as they aren't processes
			continue
	
	# Another note: Instead of crawling the numerical directories in /proc/, you could just run the following:
	# ps -e -o pid,ppid,command
	# which would give you the processes pid,  ppid, and command path
	# so, something like:
	# proc = subprocess.Popen(['ps', '-e', '-o', 'pid,ppid,command'], stdout=subprocess.PIPE)

	return process_directories

def main():
	process_directories = get_processes()
	process_tree = make_tree(process_directories)
	print_tree(0, process_tree.N)

	# test datastructure
	# new_tree = AdjacencySetTree()
	# new_tree.add_process('1', '3')
	# new_tree.add_process('1', '4')
	# new_tree.add_process('3', '4')
	# new_tree.add_process('3', '4')
	# new_tree.add_process(1, [3])
	# new_tree.add_process(1, [4])
	# print new_tree


main()

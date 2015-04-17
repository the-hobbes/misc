#!/usr/bin/python
from subprocess import Popen, PIPE

if __name__ == '__main__':
  items = ['a', 'b', 'c']
	for item in items:
		p = Popen(['some', 'command', 'here-%s' % item],
			stdout=PIPE)
		output, err = p.communicate(b"some message")
		if 'some_string' in output:
			print 'matches %s' % item

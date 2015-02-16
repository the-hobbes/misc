#!/usr/bin/python

'''
  Python implementation of tail.

  Tail prints the last 10 lines of a file to stdout. 
'''

import sys, os

def simple_method(filename):
  # open(filename).readlines()[-10:] will give you the last 10 lines in an array.
  # you use ''.join() to join each of those lines into an array into a string that can be printed.
  # if the file is large, performance suffers.
  print ''.join(open(filename).readlines()[-10:])

def seek_method(filename):
  # a method to do the same, but using the seek() function,
  # instead of reading in the whole file, we jump to the appropriate place in memory and read from there.
  # therefore, if the file is large, performance does not suffer.

  NUM_LINES = 10
  INITIAL_CHUNK_SIZE = 4096
  MAX_CHUNK_SIZE = 1024 * 1024

  with open(filename) as f: # 'with' pattern calls __enter__ and __exit__ methods automatically
    line_ends_seen = 0
    chunk_size = INITIAL_CHUNK_SIZE
    last_char = True
    remaining_bytes = os.stat(filename).st_size # os.stat performs a stat system call, and st_size is the size of file, in bytes
    chunk = ''

    while remaining_bytes:
      # Read chunk_size bytes from somewhere near the end of the stream
      if chunk_size < remaining_bytes:
        remaining_bytes -= chunk_size
      else:
        chunk_size = remaining_bytes
        remaining_bytes = 0

      f.seek(remaining_bytes) # this will push the pointer down the file by remaining_bytes bytes, the offset 

      # From the end of the chunk, go through byte-by-byte, counting newlines.
      # Stop when we reach the beginning of the chunk, or when we've seen
      # enough line endings.
      chunk = f.read(chunk_size)
      i = chunk_size
      while line_ends_seen <= NUM_LINES:
        i -= 1
        if i < 0: 
          break
        # hunt through the chunk of file, looking for newlines
        if chunk[i] == '\n' or last_char:
          line_ends_seen += 1
          last_char = False

      # If we've seen enough line endings, then we're done.
      if line_ends_seen > NUM_LINES:
        break

      # Expand the chunk size for greater efficiency.
      chunk_size = min(MAX_CHUNK_SIZE, chunk_size * 2)


    if chunk:
      # 'i' is the position in the chunk of the last newline.
      #
      # Current seek position is at the end of chunk, so we can just read out
      # from that.
      sys.stdout.write(chunk[i+1:])
      while chunk:
        chunk = f.read(MAX_CHUNK_SIZE)
        sys.stdout.write(chunk)

def main():
  try:
    filename = sys.argv[1]
    # both of the following do the same thing, but seek method is better for large files.
    print '-----------------Simple Method-----------------'
    print simple_method(filename)
    print '-----------------Seek Method-----------------'
    seek_method(filename)
  except:
    print 'Please supply filename.'

if __name__ == '__main__':
  main()

  '''
    Notes on seek():

    fp.seek(offset, from_what)
    where fp is the file pointer you're working with; offset means how many positions you will move; 
    from_what defines your point of reference:

      0: means your reference point is the beginning of the file
      1: means your reference point is the current file position
      2: means your reference point is the end of the file
    if omitted, from_what defaults to 0.
  '''
#!/usr/bin/python

'''
  Smallest snippet problem:
    Find the smallest snippet that contains all the search key words. For example:

      input_list = ['a', 'car', 'has', 'a', 'dog']
      search_words = ['a', 'dog', 'has']

    Possible output:
      [0, 4]
      [2, 4]

    Desired output (the shortest snippet) is [2, 4]
'''

input_list = ['a', 'car', 'has', 'a', 'dog']
search_words = ['a', 'dog', 'has']

def exponential_solution():
  # this is the naive solution, that has O(n^2) running time

  solution = []
  shortest_result = [-1, -1]
  shortest_length = -1

  for i in range(len(input_list)):
    copy = search_words[:]

    if input_list[i] in copy:
      shortest_result[0] = i # save away the first hit we've got
      copy.remove(input_list[i]) # and remove it from the list words to look for, since we've already found it

      for j in range(i, len(input_list)): # now, look through the rest of the list, 
        if input_list[j] in copy: # we've located another keyword
          copy.remove(input_list[j]) # remove the keyword from the copied search terms
          shortest_result[1] = j # update the ending bound of the snippet

        if len(copy) < 1: 
          # we've found all the values we are searching for, now we see if this snippet is the shortest we've found so far
          length_of_snippet = shortest_result[1] - shortest_result[0]

          if shortest_length == -1 or length_of_snippet <= shortest_length:
            shortest_length = length_of_snippet
            solution.append(shortest_length)

  print 'Length of smallest snippet: ' + str(shortest_length)
  print 'The start and end of smallest snippet: ' + str(sorted(solution))

def linear_solution():
  # this is the clever solution, with O(n) running time
  
  indecies = {}
  for item in search_words: # make a dictionary of the search terms
    indecies[item] = -1

  for i in range(len(input_list)): # each time we find a search term, update its position in the dictionary
    if input_list[i] in indecies:
      indecies[input_list[i]] = i

  # now we have the positions of the shortest snippet, we need to pick out the max and min 
  min_index = min(indecies.values())
  max_index = max(indecies.values())

  print 'Length of smallest snippet: ' + str(max_index - min_index)
  print 'The start and end of smallest snippet: [%d, %d]' % (min_index, max_index)

def main():
  print '------------Exponential Solution------------'
  exponential_solution()
  print '\n------------Linear Solution------------'
  linear_solution()

if __name__ == '__main__':
  main()
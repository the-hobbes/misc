# please write a function that takes
# 1st argument: a string, pattern like "tele[poi]ho[nm]e"
# 	would match: telephone, teleohone, teleihone, telephome, teleohome, teleihome
# 2nd argument: a list, "dictionary" of valid words
# return all words from the list that match the pattern

# Notes:
# perhaps 100000 words, input from a touchscreen (fat-fingered a possibility)

# Plan:
# regular expression to match the pattern
# could also string searching perhaps

------------------------------------------

import re

def user_input(pattern, matching_list):
  matching_words = []
  reg = re.compile(pattern + ‘^’)
  for word in matching_list:
    if reg.match(word):
      matching_words.append(word)
  
  return matching_words

------------------------------------------

def smart_user_input(pattern, to_be_matched):
  matching_words = []
  # expand the pattern
  expansion = expand_pattern(pattern)


  # convert the matches into dictionary/hash table
  hash_table = convert(to_be_matched)

  # look through expansion and determine if in target dictionary
  for each item in expansion:
    if hash_table[item]:
      matching_words.append(item)
------------------------------------------

def find_sub_lists(pattern, permutation):
  # if the first element of the sublist is a bracket
  first_character = pattern[0]
  permutations = find_permutations(pattern, [])
 

#  call for every letter and merge at the end

def find_permutations(pattern, permutations):
  perm_list = []

  if len(pattern) <= 0:
   return permutations
 
  if len(pattern) == 1:
    return perm_list.append(pattern)

  if pattern[0] != ‘[‘:
    
    find_permutations(pattern[1:], le)
  
  
 

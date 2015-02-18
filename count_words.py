'''
  Count the number of occurences of each word in a file.
  - your ability to do these counts greatly depends on how the file is formatted, as well as its size. 
'''

txt = "Brisket ball tip shoulder chicken filet mignon, salami rump sirloin. Chuck bresaola shankle t-bone sirloin sausage chicken \
frankfurter kielbasa pancetta meatloaf. Cow landjaeger pork belly, rump pork chop brisket kevin flank prosciutto. Salami picanha ham \
spare ribs ground round meatball, filet mignon bresaola rump andouille ribeye landjaeger. Short loin venison frankfurter, pork loin \
ribeye ham beef ribs corned beef chicken andouille sausage. \n \
Brisket ball tip shoulder chicken filet mignon, salami rump sirloin. Chuck bresaola shankle t-bone sirloin sausage chicken \
frankfurter kielbasa pancetta meatloaf. Cow landjaeger pork belly, rump pork chop brisket kevin flank prosciutto. Salami picanha ham \
spare ribs ground round meatball, filet mignon bresaola rump andouille ribeye landjaeger. Short loin venison frankfurter, pork loin \
ribeye ham beef ribs corned beef chicken andouille sausage."

import re # for naive version
from collections import Counter # for smart version

def naive_version(text):
  '''Bad for big files.'''
  wc_dictionary = {}
  text_list = re.split(' | , | .', text) # split on spaces or commas or periods.

  # go through the whole file, and count occurences of each word
  for word in text_list:
    if word in wc_dictionary.keys():
      wc_dictionary[word] += 1
    else:
      wc_dictionary[word] = 0
      wc_dictionary[word] += 1

  # sort the dictionary by values, from largest to smallest, and print the top 10
  print sorted(wc_dictionary.values(), reverse=True)[:10]

def smart_version(text):
  '''
      Better for big files: doesn't require reading the entire file to memory.
      See https://docs.python.org/2/library/collections.html for deets.
  '''
  c = Counter()
  for line in text.splitlines():
    c.update(line.split())
  print c

def main():
  naive_version(txt)
  smart_version(txt)

if __name__ == '__main__':
  main()
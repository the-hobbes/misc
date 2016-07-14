'''Ceasar cipher for the scavenger hunt.'''

import string


word = list('bliss')
position = [string.lowercase.index(letter) + 1 for letter in word]
updated_positions = [(pos + 23) % 26 for pos in position]
finalized = [string.lowercase[i-1] for i in updated_positions]
print ''.join(word) + ' ==> ' + ''.join(finalized)


class LoggingDict(dict):
  '''
    Toy class to help me understand using Super(). 
  '''
    def __setitem__(self, key, value):
      '''
        After making a log entry, the method uses super() to delegate the work 
            for actually updating the dictionary with the key/value pair.
      '''
      print 'I\'ve extended a builtin! (in this case dict)'
      try:
        super().__setitem__(key, value) # works in python3
      except TypeError as te:
        print 'You are using python 2, and got an error: , %s' % te
        dict.__setitem__(self, key, value) # works in python 2x

def main():
  ld = LoggingDict()
  ld['a'] = 1 # call dict.setitem
  print ld['a']

if __name__ == '__main__':
  main()
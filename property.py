'''Demonstrate a read-only attribute.

Sets an attribute to read-only using the @property decorator. See the following
for more information: http://go/pylib/functions.html#property
'''
class Parrot(object):
  def __init__(self):
    self._voltage = 100000

  @property
  def voltage(self):
    """Get the current voltage."""
    return self._voltage

p = Parrot()
p.voltage
''' Setting the voltage should result in:
Traceback (most recent call last):
  File "property.py", line 12, in <module>
    p.voltage = 2
AttributeError: can't set attribute

'''
p.voltage = 2
p.voltage

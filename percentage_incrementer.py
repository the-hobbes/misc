"""
  Calculate an increase of a certain percentage over time.
  Takes in a starting number, a percentage, and a number of years.
  (Basically compound interest)
"""
TESTING = False

def add_percentage(value, percentage):
  ''' '''
  return (value * percentage)

def calculate_end_value(starting_value, number_of_years, percentage):
  ''' '''
  total = float(starting_value)
  for i in range(0, number_of_years):
    total += add_percentage(total, percentage)
    print ("Year: %i \t Value: %f") %(i, total)

  return total

def main():
  if TESTING:
    observed_result = calculate_end_value(1000, 5, .1)
    expected_result = 1610.51
    assert observed_result == expected_result

  ''' To run this: 
      - install python 
      - open this file in a text editor (notepad or IDLE)
      - replace the ?? values for each of these variables with
        the desired value.
      - run the script:
        https://docs.python.org/2/faq/windows.html#how-do-i-run-a-python-program-under-windows
  '''
  starting_value = ??
  number_of_years = ??
  percentage = ??

  calculate_end_value(starting_value, number_of_years, percentage)

if __name__ == '__main__':
  main()
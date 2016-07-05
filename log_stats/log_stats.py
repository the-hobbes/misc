#! /usr/bin/python
'''Create distributions of messages in logs.

Usage:
1) prepare the input file
$ awk '{ print $4"-"$1, $2 }' input > massaged_input
2) process the input file
$ cat log.txt | ./histogrammer.py
'''
import sys

def stats(input_list):
    '''Compute stats about a list.
    Args:
        input_list, the list of values we are interested in.
    Returns:
        A list of values, including min and max values of the input_list, the
        length, and 10th, 50th, and 95th percentile values of the list.
    '''
    s = sorted(input_list)
    l = len(s)
    return [min(s),
            s[int(l * 0.1)], # index into the 10th percentile of the list...
            s[int(l * 0.5)],
            s[int(l * 0.95)],
            max(s),
            l]

def display(input_dict):
    '''Display the statistics calculated from the logs input.
    Args:
        input_dict, the dict of log entries we are interested in.
    '''
    for key in sorted(input_dict.keys()):
        s = stats(input_dict[key])
        print ('%20s (min/p10/p50/p95/max): %8.1f %8.1f %8.1f %8.1f %8.1f [n = %6.0f]' % (key[0:20], s[0], s[1], s[2], s[3], s[4], s[5]))

def main():
    '''Read input from stdn and display stats about the input.'''
    lists = {}
    for line in sys.stdin:
    	tokens = line.rstrip().split(' ')
        key, numbers = tokens[0], tokens[1:]
        for n in numbers:
            lists.setdefault(key, []).append(int(n))
    display(lists)


if __name__ == '__main__':
    main()

#!/usr/bin/python
'''
  killall's basic syntax is

    killall [options] program_name(s)

  When used with no options, killall sends a signal (SIGKILL) to terminate all instances of all program names that are provided as arguments.

  My plan:
  - Take in a process name from the user.
  - Look through all of the numerical directories in /proc/, cat'ing the second field for the process name
  - Once an instance of the process has been located, return the PID (the directory number)
  - Once you've looked through all the directories and located the PID's of all the processes that share a name, you must kill them
  - Call kill() on each of the PID's you've located, printing the return value of kill to stdout.
'''

import os, signal, subprocess, sys

def read_input():
  # read in the user's input (the target process name)
  try:
    target_process = sys.argv[1]
    return target_process.lower()
  except:
    raise Exception("No process supplied")

def locate_processes(target_process):
  # return list of processes in /proc/* that match the process name
  BASE_DIR = '/proc/'
  STAT = '/stat'
  NAME_INDEX = 1
  PID_INDEX = 0
  process_list = []

  # NOTE: instead of iterating through each directory, we could iterate through
  # just the numerical ones by using a regular expression:
  # /proc/[0-9]*/ would work

  process_directories = subprocess.Popen(['ls', BASE_DIR], stdout=subprocess.PIPE)

  for directory in process_directories.stdout:
    directory = directory.strip()
    out = subprocess.Popen(['cat', BASE_DIR + directory + STAT], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for output in out.stdout:
        output = output.split(' ')
        process_name = output[NAME_INDEX].strip('(').strip(')')
        if '/' in process_name:
          process_name = process_name[0 :process_name.index('/')]
        if process_name == target_process:
          process_list.append(output[PID_INDEX])

  return process_list

def kill_processes(process_list):
  # kill each process found in process_list. return 0 if successful. 
  for process in process_list:
    try:
      os.kill(int(process), signal.SIGKILL)
    except Exception as e:
      print "An exception occurend: "
      print e
      return 1

  return 0

def main():
  '''
    This can be tested by using something like this:
      watch -n 5 ls -l
    (watch periodically runs something, in this case 'ls', every 5 seconds)
    Then, try to: 
      ./killall watch
  '''
  target_process = read_input()
  process_list = locate_processes(target_process)

  if len(process_list) <= 0:
    print "%s: No Processes Found" % target_process
    sys.exit(0)

  return_code = kill_processes(process_list)
  if return_code == 0:
    print '%s killed successfully.' % target_process
  else:
    print '%s NOT killed.' % target_process

if __name__ == '__main__':
  main()

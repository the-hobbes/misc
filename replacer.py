#!/usr/bin/python
# usage: cat production/monitoring/calendar/testdata/calendar_alert.data | ~/replacer.py > /tmp/out

import sys
import re

SEARCH_STRING = 'service="'
QUOTED = re.compile('"[^"]*"')

for line in sys.stdin:
  print line,
  if line.strip().startswith(SEARCH_STRING):
    service = QUOTED.findall(line)[0].strip("\"")
    print '  borg_user="%s", \\' % service


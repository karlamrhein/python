#!/usr/bin/python

import os

if os.environ['USER']:
   print 'Hello, '+os.environ['USER']

for a in os.environ.keys():
   print a, ' = ', os.environ[a]

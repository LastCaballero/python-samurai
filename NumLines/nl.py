#! /usr/bin/python3.8
import sys

if ( not sys.stdin.isatty() ):
	i = 1
	for line in sys.stdin:
		sys.stdout.write(str(i) + "\t"  + line)
		i += 1

for arg in sys.argv[1:]:
	f = open(arg)
	i = 1
	for line in f:
		sys.stdout.write(str(i) + "\t"  + line)
		i += 1

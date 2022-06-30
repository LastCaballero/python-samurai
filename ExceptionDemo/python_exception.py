#! /usr/bin/python3.8

import sys
from collections import deque

stack = list( range(101) )

while ( True ):
	try:
		item = stack.pop()
		print(item, "was popped from the end")
	except:
		print("Error of stack: ", sys.exc_info() )
		break


stack2 = deque( range(101) )
while ( True ):
	try:
		item_left  = stack2.popleft()
		print(item_left, "was popped from the start")
		item_right = stack2.pop()
		print(item_right, "was popped from the end")
	except:
		print("Error of stack2: ", sys.exc_info() )
		break




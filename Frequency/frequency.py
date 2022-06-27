#! /usr/bin/python3
import time

freq_seconds = []
sum_diffs = 0

def calculate():
	global sum_diffs
	for idx in range( 0 , len(freq_seconds) - 1 ):  
		sum_diffs += freq_seconds[idx+1] - freq_seconds[idx]
		return sum_diffs / len(freq_seconds)

while ( True ):
	inp = input()
	if inp == 'end' : break
	ac_time = time.time()
	freq_seconds.append( ac_time )
	if  ( len( freq_seconds ) > 1 ) :
		print(ac_time, calculate(), sep='\t')

print("\nResult: " + str(calculate()) + " Frequency")





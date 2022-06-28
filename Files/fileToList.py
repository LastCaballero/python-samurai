#! /usr/bin/python3.8

file = open('ten.txt')

list = [ line.strip() for line in file.readlines() ]

for item in list:
	print(item)

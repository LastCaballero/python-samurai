#! /usr/bin/python3.8

print( "give me a c-class network-address(f.e. 200.200.200.0/24: > ", end='')
networkaddress = input()
three_octets = networkaddress.rpartition('.')[0]
print( "how many parts do you want(2,4,8,16,32,64? > ", end='' )
parts = input()

ip_dict = {}

bin_dict = {
	2	: 	0b10000000,
	4	:	0b11000000,
	8	:	0b11100000,
	16	:	0b11110000,
	32	:	0b11111000,
	64	:	0b11111100
}

short_cut_dict = {
	2	: 	25,
	4	:	26,
	8	:	27,
	16	:	28,
	32	:	29,
	64	:	30
}

new_mask = '255.255.255.' + str(bin_dict[int(parts)])

for i in range(256):
	and_result = i & bin_dict[int(parts)]
	if ( not and_result in ip_dict ):
		ip_dict[i] = []
	ip_dict[and_result].append( i )

print('\nnew mask will be: ' + new_mask)

for key in ip_dict:
	print("\nfirst is baseaddress")
	for ip in ip_dict[key]:
		print( three_octets + '.' + str(ip) )
	print("last is broadcastaddress\n")

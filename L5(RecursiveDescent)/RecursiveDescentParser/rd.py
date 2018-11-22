def K(string):
	#print string
	if string[0]=="*":
		if string[1]=="T":
			K(string[2:])
		else:
			error()
	elif string[0]=="$":
		print "accept"
	else:
		print "not accepted"
def E(string):
	#print string
	if string[0]=="T":
		K(string[1:])
	else:
		error()
	if string[0]=="$":
		print "accepted"
def error():
	print "not accepted"
#string = "T+T+T"
string = raw_input("string  ")
print string
string = string+'$'
E(string)
grammer = {"E":["TK"],"K":["*TK",""]}
print grammer

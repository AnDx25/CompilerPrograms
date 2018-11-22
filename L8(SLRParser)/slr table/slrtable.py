import sys
import shlex

inverse_production={1: 'E->E+T', 2: 'E->T', 3: 'T->T*F', 4: 'T->F', 5: 'F->(E)', 6: 'F->id'}
hash_all= {'E': 7, '$': 6, 'F': 9, ')': 1, '(': 2, '+': 3, '*': 4, 'T': 8, 'id': 5}

table=[['State', ')', '(', '+', '*', 'id', '$', 'E', 'T', 'F'],
		['0',0,'S4',0,0,'S5',0,'S1','S2','S3'], 
	['1',0, 0,'S6',0,0,'Accept',0,0,0], 
	['2','R2', 0, 'R2', 'S7', 0, 'R2', 0, 0, 0], 
	['3','R4', 0, 'R4', 'R4', 0, 'R4', 0, 0, 0], 
	['4',0, 'S4', 0, 0,'S5', 0, 'S8','S2', 'S3'],
	['5','R6', 0, 'R6', 'R6', 0, 'R6', 0, 0, 0], 
	['6',0, 'S4', 0, 0, 'S5', 0, 0,'S9','S3'], 
	['7',0, 'S4', 0, 0,'S5', 0, 0, 0,'S10']	,
	['8','S11', 0, 'S6', 0, 0, 0, 0, 0, 0], 
	['9','R1',0,'R1','S7',0,'R1',0,0,0], 
	['10','R3',0,'R3','R3',0,'R3',0,0,0],
	['11','R5',0,'R5','R5',0,'R5',0,0,0]]
print "Parsing Table ::"
j=0
for i in table:	
	print table[j]
	j=j+1
def main():
	stack = [0]#stack of slr
	
	input_string2 =sys.argv[1]# input string to parse
	input_stack = list(shlex.shlex(input_string2))
	input_stack.append('$')
	print input_stack
	
	table2 = [["Stack", "Input Stack", "Action"]]
	i = 0
	condition = True
	counter = 1
	while condition:
		try:
			#print  "stack[] ",stack[-1],input_stack[0]
			action_string = table[int(stack[-1]) + 1][int(hash_all[input_stack[0]])]
			#print  "stack[] ",stack[-1],input_stack[0]
			action = action_string[0]
			state = action_string[1:]
			#print action_string,action,state
		except:	
			print "Invalid input\n"
			return 2	
		
		if action_string == "Accept":
			exit = 1
			condition = False
			break
						
		if action == "S":
			stack.append(input_stack[0])
			stack.append(state)
			
			del input_stack[0]
			
		elif action == "R":
			location = int(state)
			production = inverse_production[location]
				
			for i in xrange(len(production)):
				if production[i] == "-" and production[i+1] == ">":
					break
			length = 0
			j = i+2
			while j < len(production):
				if j+1 < len(production):
					if production[j] == "i" and production[j+1] == "d":
						length += 1
						j += 2
					else:
						length +=1
						j += 1	
				else:
					length +=1
					j += 1
			for k in xrange(2*length):
				stack.pop()
			char = stack[-1]
			
			nt = production[:i]
			stack.append(nt)
			to_append = table[int(char)+1][int(hash_all[nt])]
			to_append2 = to_append[1:]
			stack.append(to_append2)
		
		counter += 1

	
	if exit == 1:
		print "Input Accepted!!"
	
main()

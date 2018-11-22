def first(ter,nter,key,d):
	temp=d[key]
	f=[]
	y=0
	jay=1
	for i in range(len(temp)):
		if temp[i][y] in ter or temp[i][y]=="{" and temp[i][y] not in f:
			f.append(temp[i][0])
		if temp[i][y]=="{" and len(temp[i])==y+1:
			f.append("{")
		elif temp[i][y] in nter:
			while jay!=0 and len(temp[i])>y:
				if temp[i][y] in ter:
					f.append(temp[i][y])
					break
				for j in (first(ter,nter,temp[i][y],d)):
					if j not in f and j!="{":
						f.append(j)
					if j=="{"  and len(temp[i])==y+1:
						f.append("{")

				if "{" in (first(ter,nter,temp[i][y],d)) :
					y=y+1
				else:
					jay=0
				
			y=0

	return f
def follow(ter,nter,key,d,ss):
	fol=[]

	for k in d:
		jay=1
		if key==ss:
			fol.append('$')
			
		if k!=key:
			#print "k="+k
			#print "key"+key
			temp=d[k]
			#print temp
			for i in range(0,len(temp)):
				v=0
				for j in range(0,len(temp[i])):
					if temp[i][j]==key:
						#print temp[i]
						if len(temp[i])>j+1:
							if temp[i][j+1] in ter:
								fol.append(temp[i][j+1])
							elif temp[i][j+1] in nter:
								for z in first(ter,nter,temp[i][j+1],d):
									if z!='{':
										fol.append(z)
									else:
										v=1
										while(jay!=0):
											#print v
											if(len(temp[i])>j+v+1):
												#print temp[i][j+v+1]
												#print len(temp[i])
												#print v+j+1
												if temp[i][j+v+1] in ter:
													fol.append(temp[i][j+v+1])

												else:
													for q in first(ter,nter,temp[i][j+v+1],d):
														
														if q!='{':
															fol.append(q)
													if "{" not in first(ter,nter,temp[i][j+v+1],d):
														jay=0
														#print "a"
													else:
														v=v+1
											else:
												flag=0
												#print "in"
												for p in follow(ter,nter,k,d,ss):
													fol.append(p)

										

						else:
							for z in follow(ter,nter,k,d,ss):
								fol.append(z)
	return fol





arr=[]
ter=[]
nter=[]
ss=raw_input("Enter Start Symbol")
n=int(raw_input("Enter the no of productions you want"))
for i in range(0,n):
    arr.append(raw_input())
d=dict()
for i in range(0,len(arr)):
    d[arr[i][0]]=''
for key in d:
    t=[]
    for i in range(0,len(arr)):
        if(arr[i][0]==key):
            t.append(arr[i][3:len(arr[i])+1])
    d[key]=t
for i in range(0,n):
	if arr[i][0] not in nter:
		nter.append(arr[i][0])
for i in range(0,n):
	for j in range(0,len(arr[i])):
		if(arr[i][j] not in nter and arr[i][j]!="-" and arr[i][j]!=">" and arr[i][j] not in ter and arr[i][j]!="{" ):
			ter.append(arr[i][j])
for x in nter:
	l=first(ter,nter,x,d)
	print "first of"+x+"is"
	print set(l)
for x in nter:
	l=follow(ter,nter,x,d,ss)
	print "follow of"+x+"is"
	print set(l)

import csv
from itertools import combinations
min_cutoff=5
def get_unique(row):
	unique=[]
	for ele in row:
		if ele not in unique:
			unique.append(ele)
	return unique
dataset=[]
with open('retail_dataset.csv','rt') as f:
	data=csv.reader(f)
	for row in data:
		row=get_unique(row)
		l=[]
		for ele in row:
			if ele !='':
				l.append(ele)
		dataset.append(l)
dataset=dataset[100:150]
count={}

class node:
	def __init__(self):
		self.parent=None
		self.child=[]
		self.count=1
		self.id=None

def support(count,data): 
	for row in data:
		for ele in row:
			if ele in count:
				count[ele]+=1
			else:
				count[ele]=1
	return count

def cutoff(count,sup):
	new_count={}
	for key,val in count.items():
		if val>=sup:
			new_count[key]=val
	return new_count

count=support(count,dataset)
count=cutoff(count,min_cutoff)



l1=[]
for row in dataset:
	l=[]
	for ele in row:
		if ele in count:
			l.append([ele,count[ele]])
	l.sort(key=lambda x: x[1],reverse=True)
	l1.append(l)

'''for row in l1:
	print(row)'''

root=node()
r1=root


'''for row in l1:
	for ele in row:
		if ele not in root.child:
			root.child.append(node(ele))
		else:
			index=root.child.index()'''
def check(ele,child):
	for c in child:
		if c[0]==ele:
			return True,c[1]
	return False,None

def tree(root,row):
	for ele in row:
		flag,pointer=check(ele[0],root.child)
		if flag==True:
			root=pointer
			root.count+=1
		else:
			new=node()
			new.parent=root
			new.id=ele[0]
			root.child.append([ele[0],new])
			root=new
	root=r1

for row in l1:
	tree(root,row)

Nodes=[]

def findnodes(root):
	if root.child==[]:
		return
	for c in root.child:
		Nodes.append(c[1])
		findnodes(c[1])

findnodes(root)
#print(len(Nodes))


path={}
for n in Nodes:
	if n.parent.id!=None:
		if n.id not in path:
			lis=[]
			c=n.count
			idd=n.id
			n=n.parent
			while n.parent!=None:
				lis.append(n.id)
				n=n.parent
			lis.append(c)
			ll=[]
			ll.append(lis)
			path[idd]=ll
		else:
			lis=[]
			c=n.count
			idd=n.id
			n=n.parent
			while n.parent!=None:
				lis.append(n.id)
				n=n.parent
			lis.append(c)
			path[idd].append(lis)



def find_uni_items(row):
	l=[]
	for l1 in row:
		for ele in range(len(l1)-1):
			if l1[ele] not in l:
				l.append(l1[ele])
	return l


def find_uni_combo(row):
	l=[]
	for l1 in row:
		for ele in range(len(l1)):
			if l1[ele] not in l:
				l.append(l1[ele])
	return l

def combi_cutoff(combi,v,su):
	final=[]
	for c in combi:
		s=0
		for row in v:
			f=0
			for ele in c:
				if ele not in row:
					f=1
			if f==0:
				s=s+row[-1]
		if s>su-1:
			final.append(c)
	return final

freqitem=[]
for k,v in path.items():

	l=find_uni_items(v)

	combi=[]
	for i in range(1,len(l)+1):
		comb = combinations(l,i)
		combi.append(list(comb))

	combi=find_uni_combo(combi)

	final=combi=combi_cutoff(combi,v,min_cutoff)
	for fitem in final:
		s=str(k)
		for f in fitem:
			s=s+','+str(f)
		
		freqitem.append(s)

	#print("------------")

print("Frequent item set are")
print(freqitem)



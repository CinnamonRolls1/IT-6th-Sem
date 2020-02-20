import csv
from itertools import permutations, combinations

def get_dataset(s):
	dataset = []
	with open(s,'rt') as f:
		data = csv.reader(f)
		for row in data:
			c=0
			for i in row:
				if i != '':
					c+=1
				else:
					break
			dataset.append(row[:c])
	for row in dataset:
		for i in range(len(row)):
			#row[i] = int(row[i][:])
			row[i] = int(row[i][1:])
	for i in range(len(dataset)):
		dataset[i] = set(dataset[i])
	#dataset=dataset[100:150]
	return dataset

def generate_candidates(size,base):
	c = list(combinations(base,size))
	for i in range(len(c)):
		c[i] = set(c[i])
	return c

def find_support(subset,dataset):
	count = 0
	for t in dataset:
		if subset.issubset(t):
			count+=1
	return count

def apriori(dataset):
	maximum = 0
	for t in dataset:
		for i in t:
			if i > maximum:
				maximum = i
	num_items = maximum
	min_support = 2
	print("Minimum Support : ", min_support)
	base = [i+1 for i in range(num_items)]
	candidates = []
	itemsets = []
	size = 1
	while True:
		c = generate_candidates(size,base)
		cand = {}
		itemset = {}
		for i in c:
			cand[str(i)] = 0
		
		for i in cand:
			support = find_support(eval(i),dataset)
			cand[str(i)] = support

			if support >= min_support:
				itemset[i] = support

		candidates.append(cand)
		itemsets.append(itemset)
		size+=1
		if itemset == {}:
			break
	
	c = 1
	for i in itemsets:
		print("Frequent itemsets of size",c,":",i)
		print("")
		c+=1
	print("Association Rules: \n")

	for itemset in itemsets[1:-1]:
		for item in itemset:
			#print(type(item))
			print(list(eval(item)))
			generate_rules(list(eval(item)),dataset)
			print("")			
	#generate_rules([1,2,5],dataset)
	

def generate_rules(itemset,dataset):
	ps = powerset(itemset)
	#print(ps)
	itemset = set(tuple(itemset))
	for a in ps:
		diff = itemset.difference(set(tuple(a)))
		print(diff,' => ',set(tuple(a)),":",find_support(diff.union(set(tuple(a))),dataset)/find_support(diff,dataset))


def powerset(s):
	x = len(s)
	ps = []
	for i in range(1 << x):
		s1 = []
		for j in range(x):
			if (i & (1 << j)):
				s1.append(s[j])
		if len(s1) == 0:
			continue
		ps.append(s1)
	#print("Power Set: ",ps)
	return ps[:-1]
	



def main():

	apriori(get_dataset('test_dataset_1.csv'))
	#apriori(get_dataset('retail_dataset.csv'))


if __name__ == '__main__':
	main()

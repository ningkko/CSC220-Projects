#import numpy as np


def primePantry(items, n_items, total):
	#create a table for dynamic programming
	subsets = [[[] for i in range(total+1)]for j in range(n_items+1)]
	i=1
	
	#print(['a','a','c']+['a','c','s'])
	# loop through each elements
	for item in items:
		#print(i) 
		for j in range(total+1):
			# fill in the number which is the item number itself
			if (j==items[item]) and subsets[i][j] == []:
				subsets[i][j].append(item.split())
			# fill in the number which is the item number itself 
			elif (j==items[item]) and subsets[i][j] != []:
				subsets[i][j]+=item.split()
			for index in range(i):
				if subsets[index][j]!=[] and (items[item]+j)<=total: 
					list2 = subsets[index][j]
					for object in subsets[index][j]:
						if isinstance(object, list):
							subsets[i][items[item]+j].append(object+item.split())
						else:
							subsets[i][items[item]+j].append(object.split())
							subsets[i][items[item]+j].append(item.split())
		i+=1
	result = []
	count = 0
	# return the closest-without-going-over solution
	for j in range(total,0,-1):
		for i in range(n_items+1):
			if subsets[i][j] != []:
				for element in subsets[i][j]:
					result.append(element)
					count+=1
		if result != []:
			break
	
			
	return result, count

def main():
    l= {"a":3,"b":2,"c":5,"d":1,"e":2}
    total = 5
    print(primePantry(l, len(l), total))
     
if __name__ == '__main__':
	main()

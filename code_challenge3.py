#import numpy as np


def primePantry(items, n_items, total):
	subsets = [[[''] for i in range(total+1)]for j in range(n_items+1)]
	i=1
	for item in items:
		for j in range(total+1):
			if (j==items[item]):
				subsets[i][j] = item.split()
			for index in range(i):
				if subsets[index][j]!=[''] and (items[item]+j)<=total: 
					for string in subsets[index][j]:
						subsets[i][items[item]+j] = string.split() 
					subsets[i][items[item]+j]+=item.split()
		i+=1
	result = []
	count = 0
	for i in range(n_items+1):
		if subsets[i][total] != ['']:
			result.append(subsets[i][total])
			count+=1
	return result 

def main():
    l= {"a":3,"b":2,"c":5}
    total = 5
    print(primePantry(l, 3, total))
     
if __name__ == '__main__':
	main()
#Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
#Code-challenge 2
#Given two strings representing snippets of genes (letters ACGT), 
#identify the shortest string that could contain them both as subsequences.

def main():
	gene1 = input('Please enter a string of genes: ')
	gene2 = input('Please enter another string of genes: ')
	if(check_valid_gene(gene1)==1 and check_valid_gene(gene2)==1):
		shortest_gene, min_length = find_shortest_string(gene1,gene2)
		print("******************************************** \n string 1 – {0} string 2 – {1} \n shortest string that has both as substring \n {2} (length {3})\n********************************************".format(gene1,gene2,[gene for gene in shortest_gene],min_length))
	else:
		raise ValueError("The input string of genes is not valid")

def check_valid_gene(gene):
	'''check_valid_gene(string)::= returns TRUE if the string is composed og only A,C,G,T.
	'''
	#case insensitive
	gene = gene.upper()
	set = ['A','C','G','T']
	for c in gene:
		if c not in set: 
			return 0;
	return 1;
					
def find_shortest_string(gene1, gene2):
	'''find_shortest_string(string1,string2)::= outputs the shortest concatenated string of string1 and string2
	'''
	result = []
	#base case
	min_len = len(gene1) + len(gene2)
	result.append(gene1+gene2)

	#Case1: if the result begins with gene1
	for index1 in range(len(gene1)):
		#Compare the first digit of gene2 to every digit of gene1
		if gene2[0] == gene1[index1]:
			#and if that digit and of the following parts are the same 
			if gene1[index1:] == gene2[:(len(gene1)-index1)]:
				#concatenate gene1 and gene2 from that digit.
				combined_string = gene1 + gene2[(len(gene1)-index1):]
				#if the new string is shorter than the base case,replace it
				if len(combined_string) < min_len:
					min_len = len(combined_string)
					result[0]=combined_string
				#If BA has the same length as AB, append BA to the end of the list and return both AB and BA
				elif len(combined_string)==min_len and len(combined_string) < len(gene1+gene2) and combined_string!=result[0]:
					result.insert(1,combined_string)
				
	#Case2: if the result begins with gene2
	#Do the same thing as in Case 1
	for index2 in range(len(gene2)):
		if gene1[0] == gene2[index2]:
			if gene2[index2:] == gene1[:(len(gene2)-index2)]:
				combined_string = gene2 + gene1[(len(gene2)-index2):]
				if len(combined_string) < min_len:
					min_len = len(combined_string)
					result[0]=combined_string
				#If BA has the same length as AB, append BA to the end of the list and return both AB and BA
				elif len(combined_string)==min_len and len(combined_string) < len(gene1+gene2) and combined_string!=result[0]:
					result.insert(1,combined_string)
	#Check to see if there are multiple same length results
	for index in range(len(result)-1):
		if len(result[index+1]) > len(result[index]):
			del result[index]
	return result,min_len	
						

if __name__ == '__main__':
	main()

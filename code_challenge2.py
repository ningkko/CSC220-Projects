#Fanghui He,Yining Hua, Qiaqia Ji,Yvonne Zhu
#Feb 10, 2018
#csc220
#Code-challenge 2
#Given two strings representing snippets of genes (letters ACGT), 
#identify the shortest string that could contain them both as subsequences.
##Efficiency: Complexity: O(2n), more efficient than using recursion(O(2^n)).

def find_shortest_string(gene1, gene2):
	'''find_shortest_string(gene1,gene2)::= outputs the shortest concatenated string of gene1 and gene2
	'''
	result = ''
	#base case
	min_len = len(gene1) + len(gene2)
	result =gene1+gene2

	#Case1: if gene1 concatenates gene2
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
					result = combined_string
				
	#Case2: if gene2 concatenates gene1
	#Do the same thing as in Case 1
	for index2 in range(len(gene2)):
		if gene1[0] == gene2[index2]:
			if gene2[index2:] == gene1[:(len(gene2)-index2)]:
				combined_string = gene2 + gene1[(len(gene2)-index2):]
				if len(combined_string) < min_len:
					min_len = len(combined_string)
					result = combined_string

	return result,min_len	
						
def check(str):
	set = ['A','C','G','T']
	for c in set:
		if c not in str: 
			return 0;
	return 1;
			
def main():
	gene1 = input('Please enter a string of genes: ')
	gene2 = input('Please enter another string of genes: ')
	if(check(gene1)==1 and check(gene2)==1):
		shortest_gene, min_length = find_shortest_string(gene1,gene2)
		print("********************************************\nstring 1 – {0}     string 2 – {1}\nshortest string that has both as substring\n{2} (length {3})\n********************************************".format(gene1,gene2,shortest_gene,min_length))
	else:
		raise ValueError("The input string of genes is not valid")

if __name__ == '__main__':
	main()

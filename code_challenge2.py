#Fanghui He
#Feb 10, 2018
#csc220
#Code-challenge 2
#given two strings representing snippets of genes (letters ACGT), 
#identify the shortest string that could contain them both as subsequences.

def find_shortest_string(gene1, gene2):
	string_of_result = ''
	min_len = len(gene1) + len(gene2)
	#if gene1 concatenates gene2
	for index_of_gene1 in range(len(gene1)):
		#print(index_of_gene1)
		if gene2[0] == gene1[index_of_gene1]:
			#print(gene1[index_of_gene1])
			if gene1[index_of_gene1:] == gene2[:(len(gene1)-index_of_gene1)]:
				#print(gene1[index_of_gene1:])
				combined_string = gene1 + gene2[(len(gene1)-index_of_gene1):]
				if len(combined_string) < min_len:
					min_len = len(combined_string)
					string_of_result = combined_string
	#if gene2 concatenates gene1
	for index_of_gene2 in range(len(gene2)):
		if gene1[0] == gene2[index_of_gene2]:
			#print(gene1[index_of_gene1])
			if gene2[index_of_gene2:] == gene1[:(len(gene2)-index_of_gene2)]:
				#print(gene1[index_of_gene1:])
				combined_string = gene2 + gene1[(len(gene2)-index_of_gene2):]
				if len(combined_string) < min_len:
					min_len = len(combined_string)
					string_of_result = combined_string
	if min_len == len(gene1) + len(gene2):
		string_of_result = gene1 + gene2
	return string_of_result		
			
def main():
	gene1 = input('Please enter a string of genes: ')
	gene2 = input('Please enter another string of genes: ')
	print(find_shortest_string(gene1,gene2))
if __name__ == '__main__':
	main()
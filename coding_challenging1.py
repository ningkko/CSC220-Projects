# Fanghui He
# Feb. 1st 2018
# Written in class
# Input a directory and the interpreter will output the line numbers of the py. files in that directory

import os
import glob
def print_the_report(list_of_result):
	for inner_list in list_of_result:
		print('-'*30)
		print('File 1: '+inner_list[0])
		print('File 2: '+inner_list[1])
		print('Number of identical lines: ',inner_list[2])	
		print('-'*30)
		for list in inner_list[3]:
			print('*** ', list[0],list[1],list[2])

def main():
	path = input('The directory: ')
	#If you just want to operate in the current directory
	#list_of_filename1 = [filename for filename in os.listdir(os.getcwd()) if filename.endswith('.py')]
	#list_of_filename2 = [filename for filename in os.listdir(os.getcwd()) if filename.endswith('.py')]
	list_of_filename1 = [filename for filename in os.listdir(path) if filename.endswith('.py')]
	list_of_filename2 = [filename for filename in os.listdir(path) if filename.endswith('.py')]
	list_of_result = []
	for filename1 in list_of_filename1[0:-1]:
		count_of_file = list_of_filename1.index(filename1)+1
		for filename2 in list_of_filename2[count_of_file:]:
			list_of_identical_line = []
			line_num_f1 = 0
			count_of_identical_lines = 0
			for line1 in open(filename1): 
				if line1.strip(): #and not line1.strip().startswith('#') and not line1.strip().startswith('\"""'):
					line_num_f1+=1
					line_num_f2 = 0
					for line2 in open(filename2):
						if line2.strip(): #and not line2.strip().startswith('#') and not line2.strip().startswith('\"""'):
							line_num_f2+=1
							if line1 == line2:
								list_of_identical_line.append([line_num_f1,line_num_f2,line1])
								count_of_identical_lines+=1
			if list_of_identical_line != 0:
				list_of_result.append([filename1, filename2, count_of_identical_lines, list_of_identical_line])
			count_of_file+=1
	print_the_report(list_of_result)
	
if __name__ == '__main__':
  main()
	
		
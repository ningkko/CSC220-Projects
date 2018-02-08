#Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
#Coding_challenge 1 for csc220
#Feb 5, 2018
"""In this program we are trying to make a redundancy checker 
that reads all the files in a specified directory 
and prints a report of the lines that are identical in any pair of files
"""
import os

#Start to run the program
def main():
    list_of_report = compare_contents(input('Directory: '))
    print_the_report(list_of_report)

#Given the directory path, compare the contents of any python files in that directory
def compare_contents(path):
	#If you just want to operate in the current directory
	#list_of_filename = [filename for filename in os.listdir(os.getcwd()) if filename.endswith('.py')]
	list_of_filename = [filename for filename in os.listdir(path) if filename.endswith('.py')]
	list_of_report = []
	
	#Loop through the files in this directory and choose two files to compare
	for filename1 in list_of_filename[0:-1]:
		count_of_file = list_of_filename.index(filename1) + 1
		for filename2 in list_of_filename[count_of_file:]:
			list_of_identical_line = []
			line_num_f1 = 0
			count_of_identical_lines = 0
			
			#loop through the lines in the two files using their absolute path and compare them
			for line1 in open(path+"/"+filename1): 
				line_num_f1 += 1
				if line1.strip(): 
					line_num_f2 = 0
					for line2 in open(path+"/"+filename2):
						line_num_f2 += 1
						if line2.strip(): 
							#if the lines are the same, add the lines and line numbers to the list_of_identical_line
							if line1 == line2:
								list_of_identical_line.append([line_num_f1,line_num_f2,line1.strip()])
								count_of_identical_lines += 1
								
			#If we found identical lines, add the list_of_identical_line to list_of_report; if not, do nothing
			if count_of_identical_lines != 0:
				list_of_report.append([filename1, filename2, count_of_identical_lines, list_of_identical_line])
				
			count_of_file += 1

	return list_of_report

#Function to print out the report
def print_the_report(list_of_report):
	for inner_list in list_of_report:
		print('-'*30 +'\n'+
			'File 1: '+str(inner_list[0])+'\n'+
			'File 2: '+str(inner_list[1])+'\n'+
		        'Number of identical lines: ', str(inner_list[2])+'\n'+
		      '-'*30)
		#print all the identical lines in the two files
		for list in inner_list[3]:
			print('*** ', list[0],list[1],list[2])
#End main()
if __name__ == '__main__':
	main()

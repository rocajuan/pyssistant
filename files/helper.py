import ast
import os

#Converts the txt input file into a data data structure.
def analyze_input(path, leave_spaces=False):
	input_file = open(path, 'r')
	if leave_spaces:
		data = ast.literal_eval(input_file.read().replace("\n", "").replace("\t", ""))
	else:
		data = ast.literal_eval(input_file.read().replace(" ","").replace("\n", "").replace("\t", ""))
	input_file.close()
	return data

#Ensures that the destination directory exists, if not, it will create it.
def verify_output_dir(destination):
	#Create output directory if it does not exist
	if not os.path.exists(destination):
		os.makedirs(destination)
	return True

#Checks if the file in folder_path exists.
def verify_file_exists(filename, folder_path):
	path = "%s/%s/%s"%(os.getcwd(),folder_path, filename)
	if os.path.isfile(path):
		return path
	return ""

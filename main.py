'''IMPORT LIBRARIES'''

import os

'''DEFINE IMPORTANT VARIABLES'''

source_dir = input('Write the SOURCE directory: ')

if source_dir == False:
	raise 'ERROR: NONE directory was inserted'
if source_dir:
	try:
		if source_dir[-1] != '/':
			source_dir = source_dir + '/'
		os.listdir(source_dir)
	except Exception as e:
		raise e

print()

target_dir = input('Write the TARGET directory: ')

if target_dir == False:
	raise 'ERROR: NONE directory was inserted'
if target_dir:
	try:
		if target_dir[-1] != '/':
			target_dir = target_dir + '/'
		os.listdir(target_dir)
	except Exception as e:
		raise e

print()

'''EXCEPTIONS FILES OR/AND FOLDERS  HANDLING'''

exceptions_test = input("Do you have any file or folder that you wish \
to NO copy FROM SOURCE directory TO TARGET directory? (y/n): ")

flag = False

if exceptions_test in ['y', 'n']:
	flag = True

while flag == False:
	print()
	print('ERROR: INVALID input format, only (y/n)')
	print()
	exceptions_test = input("Do you have any file or folder that you wish \
to NO copy FROM SOURCE directory TO TARGET directory? (y/n): ")
	if exceptions_test in ['y', 'n']:
		flag = True

if exceptions_test == 'y':
	try:
		exceptions = input("INTRODUCE the EXCEPTIONS (folders and files names) separated by the character ',' without any spaces between elements: ")
		exceptions = exceptions.split(',')
	except Exception as e:
		raise e
else:
	exceptions = False

'''READ FILE NAMES'''

files = os.listdir(source_dir)

if exceptions:
	try:
		for exceptt in exceptions:
			files.remove(exceptt)
	except Exception as e:
		raise e

'''ADD SOURCE DIRECTTORY TO EACH ELEMENT OF files VARIABLE ADD " CHARACTER'''

files = ['"' + source_dir + file + '"' for file in files]

'''JOIN FILES IN A STRING'''

files = ' '.join(files)

'''BUILD THE LINUX COMMAND'''

cmd_1 = 'cp -r '
cmd_2 = files
cmd_3 = ' ' + target_dir

LINUX_CMD = cmd_1 + cmd_2 + cmd_3

'''EXECUTE LINUX COMMAND (WITH HANDLING ERRORS)'''

print()

try:
	print('TRY with: ', LINUX_CMD)
	os.system(LINUX_CMD)
except Exception as e:
	print(e)
	print()
	try:
		print('TRY with: ', 'sudo ' + LINUX_CMD)
		os.system('sudo ' + LINUX_CMD)
	except Exception as e:
		print(e)
		print()
# except e:
# 	print(e)
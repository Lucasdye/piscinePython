import sys as system

def whatis(nb):
	if nb.endswith('0') == True or nb.endswith('2') == True or nb.endswith('4') == True or nb.endswith('6') == True or nb.endswith('8') == True:
		print("I'm Even.")
	else:
		print("I'm Odd.")

def main():
	if len(system.argv) > 2:
		print("AssertionError: more than one argument is provided")
	elif system.argv[1].isdigit == False:
		print("AssertionError: argument is not an integer")
	else:
		whatis(system.argv[1])
 
if __name__ == "__main__":
	main()
import sys as system

def whatis(nb):
	if nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

def main():
  if len(system.argv) > 2:
    print("AssertionError: more than one argument is provided")
  
  try:
    x = int(system.argv[1])
    whatis(x)
  except ValueError: 
    print("AssertionError: argument is not an integer")

if __name__ == "__main__":
	main()
import sys as arg


def main():
  """
  summary: Script that translates and prints text received as an argument
  into mose code
  """
  # Parsing
  argc = len(arg.argv)
  if argc != 2:
    print("AssertionError: the arguments are bad")
    return (1)
  
  # Create Morse dictionary
  alnum_morse = {" ": "/ ",
  "A": ".- ",
  "B": "-... ",
  "C": "-.-. ",
  "D": "-.. ",
  "E": ". ",
  "F": "..-. ",
  "G": "--. ",
  "H": ".... ",
  "I": ".. ",
  "J": ".--- ",
  "K": "-.- ",
  "L": ".-.. ",
  "M": "-- ",
  "N": "-. ",
  "O": "--- ",
  "P": ".--. ",
  "Q": "--.- ",
  "R": ".-. ",
  "S": "... ",
  "T": "- ",
  "U": "..- ",
  "V": "...- ",
  "W": ".-- ",
  "X": "-..- ",
  "Y": "-.-- ",
  "Z": "--.. ",
  "1": ".---- ",
  "2": "..--- ",
  "3": "...-- ",
  "4": "....- ",
  "5": "..... ",
  "6": "-.... ",
  "7": "--... ",
  "8": "---.. ",
  "9": "----. ",
  "0": "----- "}
  
  # Upper all characters
  org_text = arg.argv[1].upper()
  morse_text = ""
  
  # Translate to morse using dictionary with list comprehension tech
  try:
    for char in org_text:
      morse_text += alnum_morse[char]
  except KeyError:
    print("AssertionError: the arguments are bad")
    return (1)
  # Print result
  print(morse_text)

if __name__ == "__main__":
  main()
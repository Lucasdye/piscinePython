import sys as system


def find_set_in_string(set_of_char: set, string: str) -> int:
    """
    Summary:
    returns the number of elements of set_of_char found in str
    """
    found_punctuation = [char for char in string if char in set_of_char]
    return (len(found_punctuation))


def analyse_string(text: str) -> tuple:
    """
    Summary:
    returns a tuple with the len of the text and a dictionary that counts
    the number of digits, upper letters, lower letter, spaces and
    punctuation marks
    """
    # Punctuation set
    punctuation_set = {"?", ":", "'", "(", ")", "-", "[",  "]",
                            ".", "_", "!", ";",  ","}

    # Storing dictionary
    count_dict = {"digits": 0, "uppers": 0, "lowers": 0,
                  "spaces": 0, "punctuations": 0}

    # Counting the different types of elements in loop
    for char in text:
        if char.isdigit():
            count_dict["digits"] += 1
        elif char.isupper():
            count_dict["uppers"] += 1
        elif char.islower():
            count_dict["lowers"] += 1
        elif char.isspace():
            count_dict["spaces"] += 1

    # Counting punctuation marks
    count_dict["punctuations"] = find_set_in_string(punctuation_set, text)

    # Returning and storing results in tuple
    res = (len(text), count_dict)
    return (res)


def waiting_for_input():
    """
    Summary:
    Blocks the program until the user enters text
    """
    str = ""
    while str == "":
        str = input("Enter text: ")
    return (str)


def main():
    """
    Summary:
    retrieves text as an argument and displays its lenght and the number
    of digits, upper letters, lower letters, spaces, digits a
    nd punctuation marks it contains
    """
    argc = len(system.argv)
    if argc <= 2:
        if argc == 1:
            str = waiting_for_input()
        else:
            str = system.argv[1]
        result = analyse_string(str)
        print("The text contains", result[0], "characters:")
        print(result[1]["uppers"], "upper letters")
        print(result[1]["lowers"], "lower letters")
        print(result[1]["punctuations"], "punctuation marks")
        print(result[1]["spaces"], "spaces")
        print(result[1]["digits"], "digits")
        return 0
    elif argc > 2:
        print("AssertionError: more than one argument is provided")
    return 1


if __name__ == main():
    main()

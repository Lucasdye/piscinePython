from ft_filter import ft_filter
import sys as arg


def main():
    """
    Summary: This script outputs the words from a string
    that are bigger than N characters long.
    The string and N are given as argumemts in the command line.
    """
    argc = len(arg.argv)

    # Parsing: at least 3 args, a string of words, and a number.
    if argc != 3:
        print("AssertionError: the arguments are bad")
        return 1
    try:
        x = int(arg.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return 1

    # Spliting words into a list.
    words = arg.argv[1].split(' ')
    

    # Checking if the words are alphabetical characters
    compare_list = ft_filter(lambda word: word.isalpha(), words)
    if len(compare_list) < len(words):
        print("AssertionError: the arguments are bad")
        return 1

    # filtering with a lambda func sent as an argument.
    new_collection = ft_filter(lambda word: len(word) > x, words)
    if (new_collection is not None):
        print(new_collection)
    return 0


if __name__ == "__main__":
    main()

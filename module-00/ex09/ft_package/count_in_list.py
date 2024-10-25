def count_in_list(lst: list, target) -> int:
    """
    Prints out and returns the number of occurences
    of target in list
    """
    count = 0
    for element in lst:
        if isinstance(element, list):
            for element in lst:
                if element == target:
                    count += 1
        elif element == target:
            count += 1
    print(count)
    return count


def main():
    """
    Calls count_in_list for printing out
    the number of occurences of target in list
    """
    count_in_list([["hello", "salut"], "bonjour", "salut", ], "salut")
    return 0


if __name__ == "__main__":
    main()

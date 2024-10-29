def count_in_list(lst: list, target) -> int:
    """
    Returns and counts the number of occurences
    of target in list by recursion
    """
    count = 0
    for element in lst:
        if isinstance(element, list):
            count = count_in_list(element, target)
        elif element == target:
            count += 1
    return count


def main():
    """
    Calls count_in_list for printing out
    the number of occurences of target in list
    """
    print(count_in_list([[["salut", "salut"], "salut"], "salut"], "salut"))
    return 0


if __name__ == "__main__":
    main()

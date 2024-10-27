def ft_filter(func, object):
    """
    summary:
    Returns a list of items for which function(item)
    is true. If function is None, return the items that are true.
    """
    try:
        if func is None:
            new_collection = [item for item in object if item]
        else:
            new_collection = [item for item in object if func(item)]
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return object
    return new_collection

def output(family: list, new_family: list):
    print("My shape is : ", len(family), ", 2", sep="")
    print("My new shape is : ", len(new_family), ", 2", sep="")

def checker(family: list, start: int, end: int):

    # 1] Checking if family is a list
    if isinstance(family, list) is False:
        return (print("family isn't a list"), 1)[1]
    # 2] Checking if start and end are ints
    if isinstance(start, int) is False or isinstance(end, int) is False:
        return (print("Incorrect start or end type"), 1)[1]
    # 3] Checking if start and end are coherent
    if start > end:
        return (print("Incorrect start or end"), 1)[1]
    # 4] Checking if all elements are in family are lists
    if len(family) != len(ft_filter(lambda lst: isinstance(lst, list), family)):
        return (print("One or several elemetns aren't strings"), 1)[1]
    # 5] Checking if all lists in family are equal to two elements
    if len(family) != len(ft_filter(lambda lst: len(lst) == 2, family)):
        return (print("List elements should be pairs", 1)[1])
    return False

def slice_me(family: list, start: int, end: int) -> list:
    if start < 0:
        start = len(family) + start
    if end < 0:
        end = len(family) + end
    if checker(family, start, end):
        return None
    new_family = family[start:end]
    output(family, new_family)
    return new_family

def main():
    new_list = slice_me()

if __name__ == "__main__":
    main()
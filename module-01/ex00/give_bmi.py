
def num_lst_checker(int_list: list[int | float]) -> bool:
    """
    Checks if the elements in both lists are floats or ints.
    """
    for el in int_list:
        if isinstance(el, int) is False and isinstance(el, float) is False:
            return True
    return False


def checker(height: list[int | float], weight: list[int | float]) -> bool:
    """
    Checks if the lists are ints or floats, and if height and weight have same
    number of elements to assure the bmi calculation.
    """
    if num_lst_checker(height):
        return True
    if num_lst_checker(weight):
        return True
    if len(height) != len(weight):
        return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a boolean for each value of the bmi list exceeding
    the limit value into a list.
    """
    # Checker
    if num_lst_checker(bmi) is True and isinstance(limit, float) is False:
        return (print("The bmi list data is corrupted."), None)[1]
    if isinstance(limit, int) is False:
        return None

    return [value >= limit for value in bmi]


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Returns a list of bmi calculated from the height and weight list paramater.
    Returns None if data of the lists is corrupted or asymetrical.
    """
    err_msg = "Either the data is corrupted or the lists aren't the same size."
    if checker(height, weight) is True:
        return (print(err_msg), None)[1]

    return [w / (h ** 2) for h, w in zip(height, weight)]


def main():
    """
    This main is intended for testing and the indepedency of the script.
    """
    return 0


if __name__ == "__main__":
    main()

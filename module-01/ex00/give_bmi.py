def int_float_checker(height: list[int | float],
                      weight: list[int | float]) -> bool:
    """
    Checks if the elements in both lists are floats or ints
    """
    if isinstance(height, list) is False:
        lst1 = [height]
    else:
        lst1 = height
    if isinstance(weight, list) is False:
        lst2 = [weight]
    else:
        lst2 = weight
    for el in lst1:
        if isinstance(el, int) is False and isinstance(el, float) is False:
            return True
    for el in lst2:
        if isinstance(el, int) is False and isinstance(el, float) is False:
            return True
    return False


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if int_float_checker(bmi, limit):
        return None
    return [value >= limit for value in bmi]


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if int_float_checker(height, weight) or len(height) != len(weight):
        return None
    return [w / (h ** 2) for h, w in zip(height, weight)]


def main():
    # bmis = give_bmi([1.80, 1.65, 1.45], [68.5, 68.5, 80])
    # print(bmis)
    # apply_limit(bmis, 22)
    return 0


if __name__ == "__main__":
    main()

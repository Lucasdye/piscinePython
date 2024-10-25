def ft_filter(func, object):
    """
    summary:
    Returns a list yielding those items of iterable for which function(item)
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


def main():
    """
    summary:
    The main function doesn't serve any purposes other than testing ft_filter
    """
    new_collection = ft_filter(None, {1, 2})
    if (new_collection is not None):
        print(new_collection)
    return 0


if __name__ == "__main__":
    main()

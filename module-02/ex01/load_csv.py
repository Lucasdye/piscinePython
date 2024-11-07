from pandas import pandas

def checker(path: str ):
    """ 
    Checks if the path is a str.
    """
    if isinstance(path, str) is False:
        return True


def open_file(path: str, option: str):
    """ 
    Tries to open path with the set option.
    """
    try:
        file = open(path, option)
    except Exception as e:
        print(type(e),__name__ + ":", e)
        return True
    return file


def getlines(file: object) -> str:
    """
    retrieves lines from a text files.
    """
    try:
        line = str(file.read())
        return line
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return None


def table_dimension(text: tuple) -> tuple:
    """
    Returns the dimensions of the csv file.
    """
    return tuple((len(text), text[0].count(",") + 1))
    

def replace_commas(text: list, rep: str) -> tuple:
    """
    Replaces the commas from strings in a list with the desired replacement value.
    """
    try:
        lines_without_commas = [el.replace(",", rep) for el in text]
    except Exception as e:
        # print(type(e).__name__ + ":", e)
        return None
    return lines_without_commas


def load(path: str) -> str:
    """
    Returns a string with dimensions and the data of csv file.
    """
    if checker(path) is True:
        print("return checker")
        return None
    
    # Extracting ans editing text
    if  (file := open_file(path, "r")) is True:
        return None
    if (lines := getlines(file)) is None:
        return None
    if (dim := table_dimension(tuple(lines.split("\n")))) is None:
        return None
    if (lines_without_commas := replace_commas(list(lines), " ")) is None:
        return None
    
    # printing format
    str_dim = f"Loading dataset of dimensions {dim[0], dim[1]}\n"
    str_csv = ""
    for el in lines_without_commas:
        str_csv += el
    res = str_dim + str_csv
    return res

def main():
    load("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
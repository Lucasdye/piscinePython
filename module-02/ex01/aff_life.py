from load_csv import load
from matplotlib import pyplot as plt


def main():
    """
    Translates load() returned string into a graph of France's life expectancy
    """
    if (load_str := load("life_expectafdfncy_years.csv")) is None:
        return 1
    
    # Trunc str to desired data
    csv_str = load_str[40:]
    x_years = csv_str[10:csv_str.find("2100") + 4]
    y_values = csv_str[csv_str.find("France") + 7:csv_str.find("\n", csv_str.find("France"))]
    
    # Convert strings into integers in lists
    x_years_int = []
    y_values_int = []
    for el in list(x_years.split(" ")):
        x_years_int.append(int(el))
    for el in list(y_values.split(" ")):
        y_values_int.append(float(el))
    
    # Create graph
    plt.plot(x_years_int, y_values_int)
    plt.ylabel('Life expextancy')
    plt.xlabel('Year')
    plt.show()


if __name__ == "__main__":
    main()
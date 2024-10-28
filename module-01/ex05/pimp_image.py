from load_image import ft_load, img
# def ft_invert(array) -> array:


def ft_red(array) -> tuple:
    color_array = list(array[1])
    red_array = [(el[0], 0, 0) for el in color_array]
    print(red_array)
# def ft_green(array) -> array:

# def ft_blue(array) -> array:

# def ft_grey(array) -> array:
    

def main():
    """
    This main serves the autonomy of the module
    """
    print(ft_load("landscape.jpg"))
    array = ft_load("landscape.jpg")
    # Create a new image with the same dimensions and RGB mode
    # new_image = img.new("RGB", (500, height))
    
    # # Flatten the 2D list of pixels into a single list if needed
    # new_image.putdata(array)


if __name__ == "__main__":
    main()
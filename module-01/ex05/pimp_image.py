from load_image import ft_load, img
# def ft_invert(array) -> array:
def ft_invert(array) -> tuple:
    color_array = list(array[1])
    invert_array = [(255 - el[0], 255 - el[1], 255 - el[2]) for el in color_array]
    return color_array


def ft_red(array) -> tuple:
    color_array = list(array[1])
    red_array = [(el[0], el[1] * 0, el[2] * 0) for el in color_array]
    return tuple(red_array)


def ft_green(array) -> tuple:
    color_array = list(array[1])
    green_array = [(el[0] - el[0], el[1], el[2] - el[2]) for el in color_array]
    return tuple(green_array)


def ft_blue(array) -> tuple:
    color_array = list(array[1])
    blue_array = [(0, 0, el[0]) for el in color_array]
    return tuple(blue_array)
    

def ft_grey(array) -> tuple:
    color_array = list(array[1])
    grey_array = [(el[1], el[1], el[1]) for el in color_array]
    return tuple(grey_array)


def main():
    """
    This main serves the autonomy of the module
    """
    print(ft_load("landscape.jpg"))
    array = ft_load("landscape.jpg")
    new_array = ft_grey(array)
    new_img = img.open("landscape.jpg")
    new_img.putdata(new_array)
    new_img.show()
    # Create a new image with the same dimensions and RGB mode
    # new_image = img.new("RGB", (500, height))
    
    # # Flatten the 2D list of pixels into a single list if needed
    # new_image.putdata(array)


if __name__ == "__main__":
    main()
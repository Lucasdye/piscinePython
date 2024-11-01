from PIL import Image as img


def checker(path: str) -> bool:
    """
    load_image modules checker
    """
    # Is the path a string ?
    if isinstance(path, str) is False:
        return True
    return False


def retrieve_img(path: str) -> img:
    """
    Retrieves image from path and returns it.
    If an error is encountered, None is returned.
    """
    try:
        im = img.open(path)
    except Exception as e:
        print(type(e).__name__ + ":",  e)
        return None
    return im


def ft_load(path: str, *arg) -> tuple:
    """
    This function loads an image from the path parameter,
    returns the pixels colors in a tuple and prints out
    the dimension of the image.
    """
    if checker(path):
        return (print("The argument isn't a string"), 1)[1]
    im = retrieve_img(path)
    if im is None:
        return 1
    msg = "The shape of image is:"
    print(f"{msg} ({im.width}, {im.height}, {len(im.mode)})")
    res = (tuple(im.getdata()))
    return res


def main():
    """
    This main serves the autonomy of the module
    """
    print(ft_load("/mnt/nfs/homes/lbouguet/Downloads/landscape.jpg"))


if __name__ == "__main__":
    main()

from load_image import ft_load, checker, retrieve_img, img


def resize_im(im: img, width: int, height: int) -> img:
    """
    Resizes the image to the corresponding parameters. Returns None
    if an exception is catched.
    """
    try:
        new_im = im.resize((width, height))
        return new_im
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return None


def center_crop(im: img, perc: float) -> img:
    """
    Center crops the image corresponding to a percentage. More the percentage
    is higher, more the full image is preserved.
    """
    if perc < 0 or perc > 1:
        return None
    
    # Center zooming maths
    coleft = (im.width / 2) - (int(perc * (im.width / 2)))
    coright = (im.width / 2) + (int(perc * (im.width / 2)))
    coupper = (im.height / 2) - (int(perc * (im.height / 2)))
    colower = (im.height / 2) + (int(perc * (im.height / 2)))
    
    # Cropping
    try:
        new_im = im.crop((coleft, coupper, coright, colower))
    except Exception as e:
        print(type(e).__name__ + ":", e)
    
    return new_im


def ft_zoom() -> bool:
    """
    Prints the informations of the original and new image,
    and diplays the zoomed version.
    """
    # Name variables
    im_name = "animal.jpeg"
    zoomed_im_name = "zoomed_animal.jpeg"
    
    # Parsing
    if checker(im_name):
        return 1
    im = retrieve_img(im_name)
    if im is None:
        return 1
    
    # Cropping
    new_im = center_crop(im , 1)
    if center_crop is None:
        return True
    
    # Resizing back to original size
    new_im = resize_im(new_im, im.width, im.height)

    # Saving new image
    new_im.save(zoomed_im_name)
    
    # Output zoomed image
    new_im.show()
    
    # Output informations
    print(ft_load(im_name))
    print(ft_load(zoomed_im_name, "New shape after slicing:"))
    
    return False


def main():
    """
    This main serves the autonomy of the module
    """
    ft_zoom()


if __name__ == "__main__":
    main()

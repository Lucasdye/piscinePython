from load_image import img, ft_load, checker, retrieve_img

def center_crop(im: img, perc: float) -> img:
    """
    Center crops the image corresponding to a percentage. if perc is 1,
    100% of the image will be preseved, if perc is 0.5, only half of the
    image will be.
    """
    if perc < 0 or perc > 1:
        return None
    
    # Center crop
    coleft = (im.width/ 2) - (int(perc * (im.width / 2)))
    coright = (im.width / 2) + (int(perc * (im.width / 2)))
    coupper = (im.height / 2) - (int(perc * (im.height / 2)))
    colower = (im.height / 2) + (int(perc * (im.height / 2)))
    
    # Cropping
    try:
        new_im = im.crop((coleft, coupper, coright, colower))
    except Exception as e:
        print(type(e).__name__ + ":", e)
    
    return new_im

def ft_rotate() -> bool:
    """
    Returns the informations of the original and new image,
    and diplays the zoomed version.
    """
    # Name variables
    im_name = "animal.jpeg"
    rot_im_name = "rot_animal.jpeg"
    
    # Parsing
    if checker(im_name):
        return 1
    im = retrieve_img(im_name)
    if im is None:
        return True
    
    # Rotating
    new_im = im.rotate(90)
    
    # Cropping
    new_im = center_crop(new_im, 0.6)
    if new_im is None:
        return True
    
   
   # Saving
    new_im.save(rot_im_name) 
    
    # Output image
    new_im.show()
    
    # Print images informations
    print(ft_load(im_name))
    print(ft_load(im_name, "New shape after Transpose:"))
    
    


def main():
    """
    This main serves the autonomy of the module
    """
    ft_rotate()
    # print(ft_load("/mnt/nfs/homes/lbouguet/Downloads/landscape.jpg"))


if __name__ == "__main__":
    main()
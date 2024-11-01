from load_image import ft_load, checker, retrieve_img
from PIL import Image as img
from PIL import ImageDraw as imgDraw
from PIL import ImageOps as imgOps

def ft_rotate() -> bool:
    """
    Returns the informations of the original and new image,
    and diplays the zoomed version.
    """
    # Name variables
    im_name = "animal.jpeg"
    zoomed_im_name = "zoomed_animal.jpeg"

    print(ft_load(im_name))
    # Parsing
    if checker(im_name):
        return 1
    im = retrieve_img(im_name)
    if im is None:
        return 1


    # Rotating
    new_im = im.rotate(90)
    new_im_rot = imgOps.flip(new_im)

    # Crop image from the middle
    coleft = (new_im_rot.width / 2) - (int(0.6 * (new_im_rot.width / 2)))
    coright = (new_im_rot.width / 2) + (int(0.25 * (new_im_rot.width / 2)))
    coupper = (new_im_rot.height / 2) - (int(0.15 * (new_im_rot.height / 2)))
    colower = (new_im_rot.height / 2) + (int(0.9 * (im.height / 2)))
   
    try:
        new_im_rot_crop = new_im_rot.crop((coleft, coupper, coright, colower))
    except Exception as e:
        print(type(e).__name__ + ":", e)
   
    # Define new nb of pixels in width and height
    width_px = new_im_rot_crop.width
    height_px = new_im_rot_crop.height

    # Creating a square canvas
    if new_im_rot_crop.height < new_im_rot_crop.width:
        len_border = new_im_rot_crop.width * 2
    else:
        len_border = new_im_rot_crop.height * 2
    canvas_width = int(len_border)
    canvas_height = int(len_border)

    canvas_im = img.new(mode = "RGB", size = (canvas_height, canvas_width), color = (200, 200, 200))

    # Create draw object for canvas_im
    y_axis = imgDraw.Draw(canvas_im)
    x_axis = imgDraw.Draw(canvas_im)

    # Define ordinate axis starting and ending coordinates
    y_start_width = (len_border // 2 ) - (new_im_rot_crop.width // 2) - 1
    y_end_width = y_start_width
    y_start_height = (len_border // 2 ) - (new_im_rot_crop.height // 2) - 1
    y_end_height = (len_border // 2) + (new_im_rot_crop.height // 2)

    # Define abscissa axis starting and ending coordinates
    x_start_width = (len_border // 2 ) - (new_im_rot_crop.width // 2)
    x_end_width = (len_border // 2 ) + (new_im_rot_crop.width // 2)
    x_start_height = (len_border // 2 ) + (new_im_rot_crop.height // 2)
    x_end_height = x_start_height

    # Draw axis
    y_axis.line([(y_start_width, y_start_height), (y_end_width, y_end_height)], width=1, fill="black")
    x_axis.line([(x_start_width, x_start_height), (x_end_width, x_end_height)], width=1, fill="black")

    # Draw graduations
    y_graduation = imgDraw.Draw(canvas_im)
    for y in range(0, height_px, 50):
        y_graduation.line([(y_start_width, y_start_height + y), (y_end_width - 10, y_start_height + y)], width=1, fill="black")

    x_graduation = imgDraw.Draw(canvas_im)
    for x in range(0, width_px, 50):
        x_graduation.line([(x_start_width + x - 1, x_start_height), (x_start_width + x - 1, x_end_height + 10)], width=1, fill="black")

    # Drawing values
    for y in range(0, new_im_rot_crop.height, 50):
        y_axis.text(((y_start_width - 18) - (len(str(y) * 5)), (y_start_height - 5) + y), str(y), fill="black")
    for x in range(0, new_im_rot_crop.width, 50):
        x_axis.text((x_start_width + x - (len(str(x)) * 3), (len_border // 2) + (new_im_rot_crop.height // 2) + 10), str(x), fill="black")

    # grey image
    new_im_rot_crop_greyed = new_im_rot_crop.convert("L")
   
    
    # Sticking cropped and greyed image on canvas
    canvas_im.paste(new_im_rot_crop_greyed, ((len_border // 2 ) - (new_im_rot_crop_greyed.width // 2), (len_border // 2 ) - (new_im_rot_crop_greyed.height // 2)))
    canvas_im.show()
    
    # # Output image
    # new_im_rotated_greyed_greyed_rotated.show()
    
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
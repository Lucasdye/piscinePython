from load_image import ft_load, checker, retrieve_img
from PIL import Image as img
from PIL import ImageDraw as imgDraw
from PIL import ImageFont as imgFont

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


def ft_zoom() -> bool:
    """
    Prints the informations of the original
    and returns and diplays a cropped, greyed and axed version
    of it, called new_image.
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

    # Crop image from the middle
    coleft = (im.width / 2) - (int(0.10 * (im.width / 2)))
    coright = (im.width / 2) + (int(0.70 * (im.width / 2)))
    coupper = (im.height / 2) - (int(0.80 * (im.height / 2)))
    colower = (im.height / 2) + (int(0.30 * (im.height / 2)))

    try:
        new_im = im.crop((coleft, coupper, coright, colower))
    except Exception as e:
        print(type(e).__name__ + ":", e)

    # Define new nb of pixels in width and height
    width_px = new_im.width
    height_px = new_im.height

    # Creating a square canvas
    if new_im.height < new_im.width:
        len_border = new_im.width * 2
    else:
        len_border = new_im.height * 2
    canvas_width = int(len_border)
    canvas_height = int(len_border)

    canvas_im = img.new(mode = "RGB", size = (canvas_height, canvas_width), color = (200, 200, 200))

    # Create draw object for canvas_im
    y_axis = imgDraw.Draw(canvas_im)
    x_axis = imgDraw.Draw(canvas_im)

    # Define ordinate axis starting and ending coordinates
    y_start_width = (len_border // 2 ) - (new_im.width // 2) - 1
    y_end_width = y_start_width
    y_start_height = (len_border // 2 ) - (new_im.height // 2) - 1
    y_end_height = (len_border // 2) + (new_im.height // 2)

    # Define abscissa axis starting and ending coordinates
    x_start_width = (len_border // 2 ) - (new_im.width // 2)
    x_end_width = (len_border // 2 ) + (new_im.width // 2)
    x_start_height = (len_border // 2 ) + (new_im.height // 2)
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
    for y in range(0, new_im.height, 50):
        y_axis.text(((y_start_width - 18) - (len(str(y) * 5)), (y_start_height - 5) + y), str(y), fill="black")
    for x in range(0, new_im.width, 50):
        x_axis.text((x_start_width + x - (len(str(x)) * 3), (len_border // 2) + (new_im.height // 2) + 10), str(x), fill="black")

    # grey image
    new_im_greyed = new_im.convert("L")
    
    # Sticking cropped and greyed image on canvas
    canvas_im.paste(new_im_greyed, ((len_border // 2 ) - (new_im.width // 2), (len_border // 2 ) - (new_im.height // 2)))
    canvas_im.show()

    print(f"New shape after slicing: ({new_im_greyed.width}, {new_im_greyed.height}, {len(new_im_greyed.mode)}) or ({new_im_greyed.width}, {new_im_greyed.height})")
    return [lst for lst in list(new_im_greyed.getdata())]


def main():
    """
    This main serves the autonomy of the module
    """
    print(ft_zoom())


if __name__ == "__main__":
    main()

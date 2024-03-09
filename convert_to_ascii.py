from PIL import Image
import os, sys
import numpy as np

def convert_to_ascii(image_filename = "fullmoon.jpg", char_size = 25):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    image = Image.open(image_filename)
    width, height = image.size

    grayscale_image = image.convert("L")
    values = np.array(grayscale_image)

    ascii_chars = []
    row = -1
    for y in range(0, height, char_size):
        ascii_chars.append([])
        row += 1
        for x in range(0, width, char_size):
            area = [i[x:x + char_size] for i in values[y:y + char_size]]
            if not area: continue
            area_brightness = sum([sum(i) for i in area])
            ascii_chars[row].append(luminance_to_ascii(area_brightness / (len(area) * len(area[0]))))

    
    with open("output.txt", 'w') as file:
        for row in ascii_chars:
            file.write("".join(map(str, row)) + "\n")
    

def luminance_to_ascii(luminance):
    if luminance <= 25:
        return "#"
    elif luminance <= 51:
        return "@"
    elif luminance <= 76:
        return "%"
    elif luminance <= 102:
        return "&"
    elif luminance <= 127:
        return "O"
    elif luminance <= 153:
        return "o"
    elif luminance <= 178:
        return "^"
    elif luminance <= 204:
        return "\""
    elif luminance <= 229:
        return "\'"
    elif luminance <= 255:
        return "."
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        convert_to_ascii(sys.argv[1])
    elif len(sys.argv) == 3:
        convert_to_ascii(sys.argv[1], sys.argv[2])
    else:
        # default execution using existing directory image and default character size
        convert_to_ascii()
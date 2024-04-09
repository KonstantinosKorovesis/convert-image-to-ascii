# convert-image-to-ascii

Convert an image to ASCII characters. For proper display outside the app, make sure you are using a monospaced font (e.g. Courier).

# How to use

Make sure the following libraries are installed: NumPy, Tkinter, Pillow

Run the convert_to_ascii.py file through the command line with two additional arguments:
- The full path of the image, or just the filename if the image is placed in the same directory as the python file
- (Optional) An integer representing how many pixels will be included in a single character of the output (e.g. for an input of 10, each character will represent a 10x10 area of pixels in the original image)

# Examples

**Original Image**

![fullmoon](https://github.com/KonstantinosKorovesis/convert-image-to-ascii/assets/147168589/b2d1e01e-e3a2-4dd2-8e11-ee4c6bb16449)

</br>

**python convert_to_ascii.py fullmoon.jpg 20**

![20](https://github.com/KonstantinosKorovesis/convert-image-to-ascii/assets/147168589/66e458dc-9284-47cf-95b7-c82b5b40daea)

</br>

**python convert_to_ascii.py fullmoon.jpg 40**

![40](https://github.com/KonstantinosKorovesis/convert-image-to-ascii/assets/147168589/7ddc20e6-99bf-4178-96c2-865cb00aa82b)

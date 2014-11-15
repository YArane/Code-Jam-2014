from PIL import Image, ImageOps

image = Image.open('C:/Users/Steve/Desktop/steve.jpg')


grey_image = ImageOps.grayscale(image)

grey_image.show()
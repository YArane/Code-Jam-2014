from PIL import Image
from matrix import Matrix
import os


def get_pixels(fname):
	image = Image.open(fname)
	size = image.size
	width = size[0]
	height = size[1]
	pixels = [[] for i in range(width)]
	for i in range(width):
		for j in range(height):
			pixels[i].append(image.getpixel((i,j)))

	return pixels


images = []
for filename in os.listdir("faces/training dataset/"):
	if filename[-3:] == "gif":
		images.append(get_pixels("faces/training dataset/" + filename))


width = 320
height = 243

avg_face_array = [[] for i in range(width)]

for i in range(width):
	for j in range(height):
		avg = 0
		for k in range(len(images)):
			avg += images[k][i][j]
		avg_face_array[i].append(avg / len(images))


avg_face = Image.open("faces/training dataset/blank.gif")
ghostface_killah = avg_face.load()

for i in range(width):
	for j in range(height):
		ghostface_killah[i, j] = avg_face_array[i][j]
avg_face.save("avg_face.gif")
avg_face.show()

errors = [[[] for i in range(width)] for j in range(height)]
for face in range(len(images)):
	for i in range(width):
		for j in range(height):
			errors[face][i].append(images[face][i][j] - avg_face_array[i][j])

from PIL import Image
#from matrix import Matrix
from numpy import matrix, linalg
import os

#return a 2d list of all pixels in an image - their colour values, particularly
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

#get the pixels of all the dang pictures
images = []
for filename in os.listdir("faces/training dataset/"):
	if filename[-3:] == "gif":
		images.append(get_pixels("faces/training dataset/" + filename))

#generate super-spookey average face
width = 320
height = 243
avg_face_array = [[] for i in range(width)]
for i in range(width):
	for j in range(height):
		avg = 0
		for k in range(len(images)):
			avg += images[k][i][j]
		avg_face_array[i].append(avg / len(images))

#dick with the pixels - dicksels if you will
avg_face = Image.open("faces/training dataset/blank.gif")
ghostface_killah = avg_face.load()
for i in range(width):
	for j in range(height):
		ghostface_killah[i, j] = avg_face_array[i][j]
avg_face.save("avg_face.gif")
#avg_face.show()

#error section - hooky r kinda thing minus trident
errors = [[[] for i in range(width)] for j in range(height)]
A = []
for face in range(len(images)):
	for i in range(width):
		for j in range(height):
			errors[face][i].append(images[face][i][j] - avg_face_array[i][j])
	#numpy format for multiplication
	numpy_error = matrix(errors[face])
	A.append(numpy_error)

#find L = At*A -- must be pickled
L = [[] for i in range(len(A))]
i = 0
for matrix_t in A:
	transpose = matrix_t.transpose()
	for m in A:
		L[i].append(transpose*m)
	i += 1
	print(i)

# ritual to summon the L 
# sorry for all the loops
L_element_array = [[0 for x in range(L[0][0].shape[1]*len(L))] for i in range(L[0][0].shape[0]*len(L))]
for I in range(len(L)):
	for i in range(L[0][0].shape[0]):
		for j in range(L[0][0].shape[1]):
			for J in range(len(L)):
				L_element_array[i+I][j+J] = int(L[I][J].item((i,j)))

L = matrix(L_element_array)

eigenvalue, v = linalg.eig(L)
eigenfaces = []
for i in range(len(images)):
	gregory = matrix([[0 for i in range(320)] for j in range(320)])
	for j in range(len(v)):
		gregory = gregory + v[i]*A[j]
	eigenfaces.append(gregory)


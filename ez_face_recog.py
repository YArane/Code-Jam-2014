from PIL import Image
import os
import math

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

def get_avg_face(face_fnames):
	list_of_face_pixels = []
	for face in face_fnames:
		face_pixels = get_pixels(face)
		list_of_face_pixels.append(face_pixels)
	width = len(list_of_face_pixels[0])
	height = len(list_of_face_pixels[0][0])
	avg_face = [[] for i in range(width)]
	for i in range(width):
		for j in range(height):
			avg = 0
			for k in range(len(list_of_face_pixels)):
				avg += list_of_face_pixels[k][i][j]
			avg_face[i].append(avg / len(list_of_face_pixels))
	return avg_face


def find_best_match(filename, list_of_avg_faces):
	input = get_pixels(filename)
	min_error = 255
	id_of_best_match = 0
	i = 0
	for face in list_of_avg_faces:
		i += 1
		error = get_error(input, face)
		if error < min_error:
			min_error = error
			id_of_best_match = i
	return id_of_best_match



def get_error(input, avg_face):
	# error = [[] for i in range(len(avg_face[0]))]
	avg_error = 0
	count = 0
	for i in range(len(avg_face)):
		for j in range(len(avg_face[0])):
			if input[i][j] > 50 and input[i][j] < 205:
				count += 1
				diff = math.fabs(avg_face[i][j] - input[i][j])
				avg_error += diff
	return avg_error / count


list_of_avg_faces = []
for i in range(1, 16):
	subject_i = []
	for filename in os.listdir("faces/training dataset/"):
		if int(filename[0:2].rstrip('_')) == int(i):
			print int(filename[0:2].rstrip('_'))
			subject_i.append("faces/training dataset/"+filename)
	list_of_avg_faces.append(get_avg_face(subject_i))


names = {
	1 :	'Hans', 
	2 :	'Ralph', 
	3 :	'Guillaume', 
	4 :	'Kenny', 
	5 :	'Al', 
	6 :	'Guiseppe', 
	7 :	'Axel', 
	8 :	'Kevin', 
	9 :	'Tuco',
	10 : 'Fabio',
	11 : 'Rhonda',
	12 : 'Jerome',
	13 : 'Calvin',
	14 : 'Winston',
	15 : 'Vlad'
}

print names[find_best_match('faces/still not using these/9_5_.gif', list_of_avg_faces)]

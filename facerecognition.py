#!/usr/bin/env python
from PIL import Image
import os
import math
import sys

#return a 2d list of all pixels in an image - their colour values, particularly
def get_pixels(fname):
	image = Image.open(fname)
	image = image.resize((256, 256), Image.ANTIALIAS)
	size = image.size
	width = size[0]
	height = size[1]
	pixels = [[] for i in range(width)]
	for i in range(width):
		for j in range(height):
			if hasattr(image.getpixel((i, j)), '__iter__'):
				new_list = []
				for el in image.getpixel((i, j)):
					new_list.append(el)
				pixels[i].append(new_list)
			else:
				pixels[i].append(image.getpixel((i,j)))
	return pixels

def get_avg_face(face_fnames):
	list_of_face_pixels = []
	for face in face_fnames:
		face_pixels = get_pixels(face)
		list_of_face_pixels.append(face_pixels)
	if hasattr(list_of_face_pixels[0][0][0], '__iter__'):
		return get_avg_face_colour(face_fnames)
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

def get_avg_face_colour(face_fnames):
	list_of_face_pixels = []
	for face in face_fnames:
		face_pixels = get_pixels(face)
		list_of_face_pixels.append(face_pixels)
	width = len(list_of_face_pixels[0])
	height = len(list_of_face_pixels[0][0])
	avg_face = [[] for i in range(width)]
	for i in range(width):
		for j in range(height):
			avg = [0, 0, 0]
			for k in range(len(list_of_face_pixels)):
				avg[0] += list_of_face_pixels[k][i][j][0]
				avg[1] += list_of_face_pixels[k][i][j][1]
				avg[2] += list_of_face_pixels[k][i][j][2]
			avg_face[i].append((avg[0]/len(list_of_face_pixels), avg[1]/len(list_of_face_pixels), avg[2]/len(list_of_face_pixels)))
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

def find_best_match_colour(filename, list_of_avg_faces):
	input = get_pixels(filename)
	min_error = 255
	id_of_best_match = 0
	i = 0
	for face in list_of_avg_faces:
		i += 1
		error = get_error_colour(input, face)
		if error < min_error:
			min_error = error
			id_of_best_match = i
	return id_of_best_match

def get_error(input, avg_face):
	avg_error = 0
	count = 0
	for i in range(len(avg_face)):
		for j in range(len(avg_face[0])):
			if input[i][j] > 50 and input[i][j] < 205:
				count += 1
				diff = math.fabs(avg_face[i][j] - input[i][j])
				avg_error += diff
	return avg_error / count

def get_error_colour(input, avg_face):
	avg_error = [0, 0, 0]
	count = 0
	for i in range(len(avg_face)):
		for j in range(len(avg_face[0])):
			count += 1
			for tup in range(len(input[i][j])):
				diff = math.fabs(avg_face[i][j][tup] - input[i][j][tup])
				avg_error[tup] += diff
	for tup in range(len(avg_error)):
		avg_error[tup] = avg_error[tup] / count
	return avg_error[0] + avg_error[1] + avg_error[2]

def count_subjects(directory):
	prev = 0
	count = 0
	for filename in sorted(os.listdir(directory)):
		if int(filename[0:2].rstrip('_')) is not prev:
			count += 1
			prev = int(filename[0:2].rstrip('_'))
	return count


def get_list_of_avg_faces(directory):
	list_of_avg_faces = []
	for i in range(1, count_subjects(directory)+1):
		subject_i = []
		for filename in os.listdir(directory):
			if int(filename[0:2].rstrip('_')) == int(i):
				subject_i.append(directory+filename)
		list_of_avg_faces.append(get_avg_face(subject_i))
	return list_of_avg_faces


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

#print names[find_best_match('faces/still not using these/9_5_.gif', list_of_avg_faces)]

def main():
	argument = str(sys.argv[1])
	image = Image.open(argument)
	if hasattr(image.getpixel((0, 0)), '__iter__'):
		print find_best_match_colour(argument, get_list_of_avg_faces('faces/training dataset/'))
	else:
		print find_best_match(argument, get_list_of_avg_faces('faces/training dataset/'))

main()

import pickle

with open("/home/sorube/Documents/Python Challenge/banner.p", 'rb') as file:
	file = pickle.load(file)
	for line in file:
		print(''.join(c * n for c, n in line))
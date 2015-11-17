import csv


def remove(dct, key):
	return {k: v for k, v in dct.iteritems() if k != key}


def get_k_mins(dct, k=5):
	mins = []
	for i in xrange(k):
		tmin = min(dct, key=dct.get)
		mins.append(tmin)
		dct = remove(dct, tmin)

	return mins


def nns(point, data):
	distances = {}
	for tpoint in data:
		distances[tpoint] = ((tpoint[0] - point[0])**2 + (tpoint[1] - point[1])**2)**0.5

	return get_k_mins(distances)


def read_data(fname='data.csv'):
	dresult = {}
	with open(fname, 'rb') as f:
		reader = csv.reader(f, delimiter=':')
		for row in reader:
			y = row[2].strip('(').strip(')').split(',')
			dresult[(int(row[0]), int(row[1]))] = (int(y[0]), int(y[1]))

	return dresult

data = read_data()
nn = nns((15.75, 6.133), data)

print nn

import csv


def generate_data(density=30):
	'''Generate a training set of data'''
	with open('data.csv', 'wb') as f:
		writer = csv.writer(f, delimiter=':')
		for x0 in xrange(density, -density, step=-1):
			for x1 in xrange(density, -density, step=-1):
				writer.writerow([x0, x1, (x0 * -1, x1 * -1)])

# generate_data()
import csv
import matplotlib.pyplot as plt
from sys import argv


# noinspection PyShadowingNames
def remove(dct, key):
    """Utility function for removing a key:value pair from a dictionary
    :param dct: The dictionary
    :param key: The key to remove
    """
    return {k: v for k, v in dct.iteritems() if k != key}


# noinspection PyShadowingNames
def get_k_mins(dct, k=5):
    """Gets some number of the minimum values in a dictionary.

       Note that the dictionary is passed by reference, so make sure that all needed operations with the dictionary
       are finished before calling this method, or create a copy.
    :param dct: The dictionary
    :param k: The number of minimum values [default: 5]
    """
    mins = []
    for i in xrange(k):
        tmin = min(dct, key=dct.get)
        mins.append(tmin)
        dct = remove(dct, tmin)

    return mins


# noinspection PyShadowingNames
def nns(point, data, k=5):
    """Performs a nearest-neighbour search on a point within a dataset
    :param point: The point in question
    :param data: The dataset
    :param k: Number of nearest neighbours
    """
    distances = {}
    for tpoint in data:
        distances[tpoint] = ((tpoint[0] - point[0]) ** 2 + (tpoint[1] - point[1]) ** 2) ** 0.5

    # distances is broken after this call, so don't use it again (shouldn't be a problem)
    return get_k_mins(distances, k=k)


def read_data(fname='data.csv'):
    """Reads a set of data from a csv file
    :param fname: The name of the file to read [default: 'data.csv']
    """
    dresult = {}
    with open(fname, 'rb') as f:
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            y = row[2].strip('(').strip(')').split(',')
            dresult[(int(row[0]), int(row[1]))] = (int(y[0]), int(y[1]))

    return dresult

if not argv:
    k = 5
else:
    k = int(argv[1])

data = read_data()
pt = (7.3893, 8.3293)
nn = nns(pt, data, k)

x0 = []
x1 = []
for k in data.keys():
    x0.append(k[0])
    x1.append(k[1])

plt.plot(x0, x1, 'b.')
plt.plot(pt[0], pt[1], 'r.')

nx0 = []
nx1 = []
for p in nn:
    nx0.append(p[0])
    nx1.append(p[1])

plt.plot(nx0, nx1, 'yH')

plt.show()

print nn

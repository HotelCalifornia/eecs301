import csv


def generate_data(density=30):
    """Generate a training set of data
    :param density: Specifies how many data points will be created ((density*2)**2) [default: 30]
    """
    with open('data.csv', 'wb') as f:
        writer = csv.writer(f, delimiter=':')
        for x0 in xrange(density, -density, -1):
            for x1 in xrange(density, -density, -1):
                writer.writerow([x0, x1, (x0 * -1, x1 * -1)])

generate_data(15)

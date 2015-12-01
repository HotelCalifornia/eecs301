import csv


def c_vec(x0, x1, pt):
    """Generate a vector at (x0, x1) that points toward pt
    :param x0: The 'x' position of the vector
    :param x1: The 'y' position of the vector
    :param pt: Where the vector will point
    """
    if x0 > pt:
        x0f = -x0
    elif x0 == pt:
        x0f = 0
    else:
        x0f = x0

    if x1 > pt:
        x1f = -x1
    elif x1 == pt:
        x1f = 0
    else:
        x1f = x1
    
    return x0f, x1f


def generate_data(density=30):
    """Generate a training set of data
    :param density: Specifies how many data points will be created ((density*2)**2) [default: 30]
    """
    with open('data.csv', 'wb') as f:
        writer = csv.writer(f, delimiter=':')
        for x0 in xrange(density):
            for x1 in xrange(density):
                writer.writerow([x0, x1, c_vec(x0, x1, density/2)])

# generate_data(15) generates a vector field with domain [0,15] and range [0,15]

import numpy
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def getDistance(a, b):
        return numpy.sqrt(numpy.abs(a.x - b.x) + numpy.abs(a.y - b.y))

    @staticmethod
    def getTotalDistance(coords):
        distance = 0
        for first, second in zip(coords[:-1], coords[1:]):
            distance += Coordinate.getDistance(first, second)
        distance += Coordinate.getDistance(coords[0], coords[-1])
        return distance

coords = []

for i in range(30):
    coords.append(Coordinate(numpy.random.uniform(), numpy.random.uniform()))

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

for first, second in zip(coords[:-1], coords[1:]):
    ax1.plot([first.x, second.x], [first.y, second.y], 'b')

ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')

for c in coords:
    ax1.plot(c.x, c.y, 'ro')

cost0 = Coordinate.getTotalDistance(coords)

temperature = 30
factor = 0.99

initTemperature = temperature

for i in range(1000):

    print(i, 'cost=', cost0)

    temperature = temperature * factor

    for j in range(500):
        r1, r2 = numpy.random.randint(0, len(coords), size=2)

        temp = coords[r1]
        coords[r1] = coords[r2]
        coords[r2] = temp

        cost1 = Coordinate.getTotalDistance(coords)

        if cost1 < cost0:
            cost0 = cost1
        else:
            roll = numpy.random.uniform()
            if roll < numpy.exp((cost0 - cost1) / temperature):
                cost0 = cost1
            else:
                temp = coords[r1]
                coords[r1] = coords[r2]
                coords[r2] = temp

for first, second in zip(coords[:-1], coords[1:]):
    ax2.plot([first.x, second.x], [first.y, second.y], 'b')

ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')

for c in coords:
    ax2.plot(c.x, c.y, 'ro')

plt.show()
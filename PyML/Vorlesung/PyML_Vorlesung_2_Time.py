import numpy
import time
print(time.clock())

def benchmark_numphy(n):
	X= numpy.ones([n,n])
	Y= numpy.ones([n,n])
	Z= numpy.zeros([n,n])
	start = time.clock()
	Z = numpy.dot(X,Y)
	end = time.clock()
	return end-start


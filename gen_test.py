import math
import numpy
import random
from cfg import *

def gen_test_data():
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	cycles_per_sample = MORSE_FREQ/SAMPLE_FREQ
	radians_per_sample = cycles_per_sample * 2 * math.pi
	WPM = random.randint(2,20)
	elements_per_second = WPM * 50.0 / 60.0
	samples_per_element = int(SAMPLE_FREQ/elements_per_second)
	
	length = samples_per_element * len(pattern)
	# Empty returns array containing random stuff, so we NEED to overwrite it
	data = numpy.empty(length, dtype=numpy.float32)
	for i in xrange(length):
		keyed = pattern[int(i/samples_per_element)]
		#keyed = 1
		data[i] = 0 if not keyed else (radians_per_sample * i)
	
	data = numpy.sin(data)
	
	
	return data
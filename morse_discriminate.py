from numpy import *
import random
import math
from gz_dsp import *
import cProfile

SAMPLE_FREQ = float(44100) #Hz
MORSE_FREQ = 440 #Hz
FFT_FREQ = 200 #ideal number of times the fft is done a second

OVERLAP_FACTOR = 1.1

def gen_test_data():
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	cycles_per_sample = MORSE_FREQ/SAMPLE_FREQ
	radians_per_sample = cycles_per_sample * 2 * math.pi
	WPM = random.randint(2,20)
	elements_per_second = WPM * 50.0 / 60.0
	samples_per_element = int(SAMPLE_FREQ/elements_per_second)
	
	length = samples_per_element * len(pattern)
	# Empty returns array containing random stuff, so we NEED to overwrite it
	data = empty(length, dtype=float32)
	for i in xrange(length):
		keyed = pattern[int(i/samples_per_element)]
		#keyed = 1
		data[i] = 0 if not keyed else (radians_per_sample * i)
	
	data = sin(data)
	
	
	return data


# TODO: Think of better name
def determine_morseness(time_domain):
	#ideal_samples_per_fft = SAMPLE_FREQ/float(FFT_FREQ)
	# make sure number of samples passed to dfft is power of 2
	#aspf = actual_samples_per_fft = int(2**round(math.log(ideal_samples_per_fft, 2)))
	aspf = 150
	
	result = []
	for i in xrange(0, len(time_domain), aspf):
		samples = time_domain[i:i+aspf*OVERLAP_FACTOR]
		if len(samples) < aspf*OVERLAP_FACTOR: #fail if you run out of data
			break
		intensity = gz_dsp(samples, MORSE_FREQ)
		
		result.append(intensity/(aspf**2/3))
		
	return result

if __name__ == "__main__":
	#gen_test_data()
	data = gen_test_data()
	print len(data)/SAMPLE_FREQ
	cProfile.run('determine_morseness(data)')




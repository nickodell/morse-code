from numpy import *
import random
import math
import matplotlib

SAMPLE_SPEED = 44100 #Hz
MORSE_FREQ = 440 #Hz
FFT_FREQ = 200 #ideal number of times the fft is done a second

def gen_test_data():
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	cycles_per_sample = MORSE_FREQ/float(SAMPLE_SPEED)
	radians_per_sample = cycles_per_sample * 2 * math.pi
	WPM = random.randint(2,20)
	elements_per_second = WPM * 50.0 / 60.0
	samples_per_element = int(SAMPLE_SPEED/elements_per_second)
	
	length = samples_per_element * len(pattern)
	# Empty returns array containing random stuff, so we NEED to overwrite it
	data = empty(length, dtype=float32)
	for i in xrange(length):
		keyed = pattern[int(i/samples_per_element)]
		#keyed = 1
		data[i] = 0 if not keyed else (radians_per_sample * i)
	
	data = sin(data)
	
	
	return data

def gz_dsp():
	

def determine_morseness(time_domain):
	#ideal_samples_per_fft = SAMPLE_SPEED/float(FFT_FREQ)
	# make sure number of samples passed to dfft is power of 2
	#aspf = actual_samples_per_fft = int(2**round(math.log(ideal_samples_per_fft, 2)))
	aspf = 200
	
	result = []
	for i in xrange(0, len(time_domain), aspf):
		samples = time_domain[i:i+aspf*2] #make the ffts overlap
		if len(samples) < aspf*2: #fail if you run out of data
			break
		freq_domain = fft.fft(samples)
		max_, max_id = 0, 0
		for j in xrange(len(freq_domain)):
			if freq_domain[j] > max_:
				max_ = freq_domain[j]
				max_id = j
		#print type(max_)
		result.append(0 if max_ < 20 else 1)
		
	return result

if __name__ == "__main__":
	#gen_test_data()
	print determine_morseness(gen_test_data())
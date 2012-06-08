from gz_dsp import *
from cfg import *


def detect_tone(signal):
	ideal_samples_per_transform = SAMPLE_FREQ/float(transform_FREQ)
	samples_per_cycle = SAMPLE_FREQ/MORSE_FREQ
	aspt = actual_samples_per_transform = int(samples_per_cycle*max(round(ideal_samples_per_transform/samples_per_cycle), 1))
	
	
	coeffs = []
	for i in xrange(0, len(signal), int(aspt/OVERLAP_FACTOR)):
		samples = signal[i:i+aspt]
		if len(samples) < aspt: #fail if you run out of data
			break
		intensity = gz_dsp(samples, MORSE_FREQ)
		
		coeffs.append(intensity/(aspt**2/4))
	
	coeffs_per_second = SAMPLE_FREQ/aspt
	return coeffs, coeffs_per_second

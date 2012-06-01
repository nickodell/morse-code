from gz_dsp import *
from cfg import *

# TODO: Think of better name
def detect_tone(signal):
	ideal_samples_per_fft = SAMPLE_FREQ/float(FFT_FREQ)
	samples_per_cycle = SAMPLE_FREQ/MORSE_FREQ
	aspf = actual_samples_per_fft = int(samples_per_cycle*round(ideal_samples_per_fft/samples_per_cycle))
	
	result = []
	for i in xrange(0, len(signal), int(aspf/OVERLAP_FACTOR)):
		samples = signal[i:i+aspf]
		if len(samples) < aspf: #fail if you run out of data
			break
		intensity = gz_dsp(samples, MORSE_FREQ)
		
		result.append(intensity/(aspf**2/4))
		
	return result
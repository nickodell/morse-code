import numpy
import math
import cfg

# implementation of goertzel function
def gz_dsp(matrix, freq):
	normalized_freq = freq/cfg.SAMPLE_FREQ
	coeff = 2 * math.cos(2 * math.pi * normalized_freq)
	s = [0, 0, 0]
	for sample in matrix:
		sample = float(sample)
		s[0] = sample + (coeff * s[1]) - s[2]
		s[1:3] = s[0:2]
	return (s[1]**2) + (s[2]**2) - (s[1] * s[2] * coeff)

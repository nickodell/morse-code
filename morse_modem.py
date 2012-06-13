import cProfile
from demodulate.cfg import *
from demodulate.detect_tone import *
from demodulate.element_resolve import *
from gen_test import *



if __name__ == "__main__":
	#gen_test_data()
	data = gen_test_data()
	#print len(data)/SAMPLE_FREQ
	#cProfile.run('detect_tone(data)')
	#print detect_tone(data)
	element_resolve(*detect_tone(data))



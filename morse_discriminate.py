import cProfile
from cfg import *
from detect_tone import *
from gen_test import *



if __name__ == "__main__":
	#gen_test_data()
	data = gen_test_data()
	#print len(data)/SAMPLE_FREQ
	#cProfile.run('detect_tone(data)')
	print ''.join(['#' if i > 0.5 else "_" for i in detect_tone(data)])



import cProfile
from cfg import *
from detect_tone import *
from gen_test import *
from element_resolve import *



if __name__ == "__main__":
	#gen_test_data()
	data = gen_test_data()
	#print len(data)/SAMPLE_FREQ
	#cProfile.run('detect_tone(data)')
	print detect_tone(data)
	print element_resolve(*detect_tone(data))


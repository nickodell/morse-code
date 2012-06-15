import cProfile
from demodulate.cfg import *
from demodulate.detect_tone import *
from demodulate.element_resolve import *
from gen_tone import *
import random



if __name__ == "__main__":	
	WPM = random.uniform(2,20)
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	#gen_test_data()
	data = gen_tone(pattern, WPM)
	#print len(data)/SAMPLE_FREQ
	#cProfile.run('detect_tone(data)')
	#print detect_tone(data)
	element_resolve(*detect_tone(data))



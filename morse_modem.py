import cProfile
from demodulate.cfg import *
from demodulate.detect_tone import *
from demodulate.element_resolve import *
from demodulate.samples import *
from gen_tone import *
import random



class Score_Holder():
	score = 0
	def rescore(self, delta):
		self.score += delta

def element_resolve(coeffs, coeffs_per_second):
	"""coeffs is Sample_Storage instance"""
	# Try everything from 0.5 WPM to 30 WPM
	step = WPM_STEP # step is multiplicative
	wpm_list = []
	f = WPM_START
	while f < WPM_END:
		wpm_list.append(f)
		f *= step
	coeffs_per_element_list = map(lambda wpm: (int(coeffs_per_second/wpm*60.0/50.0), wpm), wpm_list)
	coeffs_per_element_list = list(set(coeffs_per_element_list)) # remove duplicates
	for coeffs_per_element, wpm in coeffs_per_element_list:
		
		yield (element_resolve_at_wpm(Sample_Storage_Window(coeffs), coeffs_per_element, rescore_callback), wpm, Score_Holder())


if __name__ == "__main__":
	WPM = random.uniform(2,20)
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	#gen_test_data()
	data = gen_tone(pattern, WPM)
	stor = Sample_Storage()
	print "tone generated"
	#print len(data)/SAMPLE_FREQ
	#cProfile.run('detect_tone(data)')
	#print detect_tone(data)
	element_resolve(*detect_tone(data))



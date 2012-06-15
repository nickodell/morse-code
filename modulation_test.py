import pygame
import random
from demodulate.cfg import *
from gen_tone import *

if __name__ == "__main__":
	pygame.mixer.pre_init(frequency = int(SAMPLE_FREQ), channels = 1)
	pygame.mixer.init()
	WPM = random.uniform(2,20)
	pattern = [1,0,1,1,1,0,0,0,0,0,0,0] # morse code 'A'
	#gen_test_data()
	data = gen_tone(pattern, WPM)
	snd = pygame.sndarray.make_sound(data)
	snd.play()

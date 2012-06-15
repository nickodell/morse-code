import pygame
import random
import time
from demodulate.cfg import *
from modulate import *
from gen_tone import *

if __name__ == "__main__":
	pygame.mixer.pre_init(frequency = int(SAMPLE_FREQ), channels = 1)
	pygame.mixer.init()
	WPM = random.uniform(2,20)
	pattern = chars_to_elements.letters_to_sequence("NA NA NA NA NA NA NA BATMAN")
	#gen_test_data()
	data = gen_tone(pattern, WPM)
	snd = pygame.sndarray.make_sound(data)
	chn = snd.play()
	while chn.get_busy():
		time.sleep(1)

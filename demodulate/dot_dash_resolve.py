"""Filename is a misnomer, also looks at pauses between dots and dashes"""
import operator
from cfg import *


### Constants
DOT = 1
DASH = 2

# The pauses
INTER_ELEMENT = 3
INTER_CHARACTER = 4
INTER_WORD = 5
DEAD_AIR = 6

possible_on = {1:DOT, 3:DASH}
possible_off = {1:INTER_ELEMENT, 3:INTER_CHARACTER, 7:INTER_WORD}

def dot_dash_resolve(elements, rescore_callback):
	score = 0
	recent = []
	
	for element in elements:
		if recent[0] == element:
			# Hasn't changed state.
			recent.append(element)
		else:
			length = len(recent)
			if recent[0] == False:
				if len(recent) > max(possible_off):
					yield DEAD_AIR
				else:
					key, difference = most_similar_key(possible_off, length)
					rescore_callback(-difference)
					yield possible_off[key]
			else:
				key, difference = most_similar_key(possible_on, length)
				rescore_callback(-difference)
				yield possible_on[key]
			
			recent = []
	

def most_similar_key(dictionary, needle):
	needle = int(needle)
	key_list = sorted(map(lambda key: key, abs(needle - key), dictionary.keys()), key = operator.itemgetter(1))
	key, difference = key_list[0]
	
	return key, difference

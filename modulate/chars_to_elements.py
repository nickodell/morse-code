#Allow us to import from parent directory, even if python isn't being run with the -m option
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from common import *
mt = morse_parse.morse_table

import itertools

### Constants
DOT = 1
DASH = 2

# The pauses
INTER_ELEMENT = 3
INTER_CHARACTER = 4
INTER_WORD = 5
DEAD_AIR = 6

def dict_invert(d):
	return dict([[v,k] for k,v in d.iteritems()])

possible_on = {1:DOT, 3:DASH}
possible_off = {1:INTER_ELEMENT, 3:INTER_CHARACTER, 7:INTER_WORD}

possible_on_inv = dict_invert(possible_on)
possible_off_inv = dict_invert(possible_off)


def list_extend(l, number, item):
	"""Make sure `l` ends with at least `number` `item`s
	Does not modify l"""
	
	if not hasattr(l, '__getitem__'):
		# l is some sort of sequence funnybusiness; copy it out
		l = list(l)
	
	n = 0
	try:
		for i in xrange(number):
			if l[-(i+1)] == item: # index the list in reverse
				n += 1
				continue
			else:
				break
	except IndexError:
		# IndexError's are to be expected here.
		pass
	
	# n is now the number of trailing correct elements. Now just add number - n  items
	to_add = number - n
	if to_add <= 0:
		# return the original
		return l
	else:
		return l + [item] * to_add
	
	

def letters_to_sequence(text):
	seq = []
	text = text.upper()
	text 
	
	for c in text:
		try:
			elements = mt[c]
		except KeyError:
			pass #Silently fail if we don't know how to encode it
		for elem in mt[c]:
			if elem == ".":
				seq = list_extend(seq, possible_on_inv[DOT], True)
			elif elem == "-":
				seq = list_extend(seq, possible_on_inv[DASH], True)
			elif elem == "_":
				seq = list_extend(seq, possible_off_inv[INTER_WORD], False)
			else:
				raise Exception("Should never happen, unless something happened with the config file")
			seq = list_extend(seq, possible_off_inv[INTER_ELEMENT], False)
		seq = list_extend(seq, possible_off_inv[INTER_CHARACTER], False)
	return seq
				

def print_morse(seq):
	"""Mostly for debugging"""
	print ''.join(["#" if s else "_" for s in seq])


if __name__ == "__main__":
	print_morse(letters_to_sequence("I AM (batman)?"))

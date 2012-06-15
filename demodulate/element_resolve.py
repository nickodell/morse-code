"""Take coefficients from detect_tone and make on/off states out of them."""

import math
from cfg import *

NO_EDGE = 1 # unrelated to hank green
RISING_EDGE = 2
FALLING_EDGE = 3


def element_resolve(coeffs, coeffs_per_second):
	# Try everything from 0.5 WPM to 30 WPM
	step = WPM_STEP # step is multiplicative
	wpm = []
	f = WPM_START
	while f < WPM_END:
		wpm.append(f)
		f *= step
	coeffs_per_element_list = map(lambda wpm: int(coeffs_per_second/wpm*60.0/50.0), wpm)
	coeffs_per_element_list = list(set(coeffs_per_element_list)) # remove duplicates
	results = []
	for coeffs_per_element in coeffs_per_element_list:
		elements = element_resolve_at_wpm(coeffs, coeffs_per_element)
		if len(elements) == 0:
			continue
		score = score_element_solution(coeffs, coeffs_per_second, coeffs_per_element, elements)
		results.append((elements, score))
	elements = map(lambda x: x[1], results)
	index = elements.index(max(elements))
	result = results[index]
	print result, len(result[0])

	
def element_resolve_at_wpm(coeffs, coeffs_per_element, rescore_callback):
	coeffs_per_element = int(coeffs_per_element)
	buff = []
	accumulated_fudge = 1
	while True:
		try:
			buff = buff + coeffs.get_samples((coeffs_per_element * 2) - len(buff))
		except IndexError:
			yield "No data remaining"
		
		# We need these initial guesses to work out whether there's a transition here.
		current_element = average_over_range(coeffs[0:coeffs_per_element])
		next_element = average_over_range(coeffs[coeffs_per_element:2 * coeffs_per_element])
	
		element_transition = select_transition_type(current_element, next_element)
	
		# If we are on a falling or rising edge, we move our morse code window a little bit so it stays synced up with less-than-perfect morse code.
		if element_transition != NO_EDGE:
			# If we've not seen a transition in a long time, be more forgiving
			ajusted_fudge = int(coeffs_per_element * cap([0, 1], accumulated_fudge * MAX_FUDGE_FACTOR))
		
			start = coeffs_per_element - ajusted_fudge
			end = coeffs_per_element + ajusted_fudge
		
			i = edge_optimize(coeffs[start:end], element_transition == RISING_EDGE)
			length = cap([1, 2 * coeffs_per_element - 1], start + i)
		else:
			length = coeffs_per_element
	
		
		#print "1,", elements
		
		#print "caller,", len(coeffs_pass_on), coeffs_per_element * 4
		
		if element_transition == NO_EDGE:
			accumulated_fudge += 1
		else:
			accumulated_fudge = 1
	
		# It's unlikely that the element has changed since when we ajusted the timings, but check anyway.
		keyed = preprocess_element_state(average_over_range(coeffs[0:length]))
		rescore_callback(score_element_solution(buff, coeffs_per_second, coeffs_per_element, keyed, length))
		buff = buff[length:]
		yield keyed

def score_element_solution(buff, coeffs_per_second, coeffs_per_element, keyed, length):
	score = 0
	# Ding solution if the elements contained within are substantially different from the keyed/unkeyed state
	score -= math.sqrt(sum(map(lambda x: (keyed - x)**2, coeffs[0:length])))
	score -= abs(coeffs_per_element - length)/float(coeffs_per_element)
	return score

def select_transition_type(one, two):
	one = preprocess_element_state(one)
	two = preprocess_element_state(two)
	if one == two:
		return NO_EDGE
	elif one == True and two == False:
		return FALLING_EDGE
	elif one == False and two == True:
		return RISING_EDGE
	else:
		raise ValueError("Unknown edge type")

def average_over_range(lst):
	"""Average of all values in list"""
	return sum(lst)/float(len(lst))

def preprocess_element_state(ele):
	return bool(cap([0, 1], round(ele)))

def cap(cap_val, num):
	"""Makes sure value provided is between two extremes.
	Example usage: cap([0,10], 200) -> 10"""
	return max(min(num, cap_val[1]), cap_val[0])

def edge_optimize(coeffs, rising_edge):
	"""Can move the edge slightly so that the morse code stays synced up."""
	scores = []
	first = lambda coeff: coeff if rising_edge else 1 - coeff
	second = lambda coeff: coeff if not rising_edge else 1 - coeff
	
	for i in xrange(len(coeffs)):
		score = 0
		score -= abs(i - len(coeffs)/2.0)*EDGE_VARY_PENALTY_FACTOR
		score -= sum(map(first, coeffs[0:i]))
		score -= sum(map(second, coeffs[i:len(coeffs)]))
		scores.append(score)
	m = max(scores)
	for i, score in enumerate(scores):
		if score == m:
			return i



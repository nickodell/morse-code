MAX_FUDGE_FACTOR = 0.10 #most that the element timings can be off

EDGE_VARY_PENALTY_FACTOR = 0.50

NO_EDGE = 1 # unrelated to hank green
RISING_EDGE = 2
FALLING_EDGE = 3


def element_resolve(coeffs, coeffs_per_second):
	# Try everything from 0.5 WPM to 30 WPM
	step = 1.05 #it's multiplicative
	wpm = []
	f = 0.5
	while f < 30:
		wpm.append(f)
		f *= step
	coeffs_per_element_list = map(lambda wpm: int(coeffs_per_second/wpm*60.0/50.0), wpm)
	coeffs_per_element_list = sorted(list(set(coeffs_per_element_list))) # remove duplicates
	
	map(lambda coeffs_per_element: element_resolve_at_wpm(coeffs, coeffs_per_second, coeffs_per_element, 1), coeffs_per_element_list)

	
def element_resolve_at_wpm(coeffs, coeffs_per_second, coeffs_per_element, accumulated_fudge):
	
	current_element = sum(coeffs[0:coeffs_per_second])/coeffs_per_second
	next_element = sum(coeffs[coeffs_per_second:2*coeffs_per_second])/coeffs_per_second
	
	element_transition = select_transition_type(current_element, next_element)
	
	# If we are on a falling or rising edge, we move our morse code window a little bit so it stays synced up with less-than-perfect morse code.
	if element_transition != NO_EDGE:
		ajusted_fudge = coeffs_per_element * cap([0, 1], accumulated_fudge * MAX_FUDGE_FACTOR)
		
		start = coeffs_per_element - ajusted_fudge
		end = coeffs_per_element + ajusted_fudge
		
		i, score = edge_optimize(coeffs[start:end], element_transition == RISING_EDGE)
		length = start + i
	else:
		length = coeffs_per_element
	
	coeffs_pass_on = coeffs[length:len(coeffs)]
	if len(coeffs_pass_on) > coeffs_per_element * 2:
		elements = element_resolve_at_wpm(coeffs_pass_on, coeffs_per_second, coeffs_per_element, 1 + (accumulated_fudge if element_transition == NO_EDGE else 0) )
	return score, elements

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

def preprocess_element_state(ele):
	return bool(cap([0, 1], ele))

def cap(cap_val, num):
	return max(min(num, cap_val[1]), cap_val[0])

#Can move the edge slightly so that the morse code stays synced up.
def edge_optimize(coeffs, rising_edge):
	scores = []
	first = lambda coeff: coeff if rising_edge else 1 - coeff
	second = lambda coeff: coeff if not rising_edge else 1 - coeff
	
	for i in xrange(len(coeffs)):
		score = -abs(i - len(coeffs)/2.0)*EDGE_VARY_PENALTY_FACTOR
		score -= sum(map(first, coeffs[0:i]))
		score -= sum(map(second, coeffs[i:len(coeffs)]))
	m = max(scores)
	for i, score in enumerate(scores):
		if score == m:
			return i, score



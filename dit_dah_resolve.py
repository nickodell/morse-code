# Filename is a misnomer, also looks at pauses between dits & dahs

DOT = 1
DASH = 2

# The pauses
INTERELEMENT = 3
INTERCHARACTER = 4
INTERWORD = 5

def dit_dah_resolve(elements):
	score = 0
	number_on = 0
	number_off = 0
	
	for element in elements:
		if element:
			if number_off:

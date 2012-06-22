SAMPLE_FREQ = float(44100) #Hz
MORSE_FREQ = 440 #Hz
TRANSFORM_FREQ = 500 #ideal number of times the gz transform is done a second

OVERLAP_FACTOR = 1.1 # amount that the spectral transforms overlap

# most that the element timings can be off
# Setting this to more than 1/7 will not do what you expect
MAX_FUDGE_FACTOR = 0.10

EDGE_VARY_PENALTY_FACTOR = 0.50

WPM_START = 0.5
WPM_END = 30
WPM_STEP = 1.05 # step is multiplicative


NOT_ENOUGH_DATA = (lambda: 0) # Placeholder so that nothing is equal to this
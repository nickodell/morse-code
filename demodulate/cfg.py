### detect_tone.py
### gen_test_data.py
SAMPLE_FREQ = float(44100) #Hz
MORSE_FREQ = 440 #Hz
TRANSFORM_FREQ = 500 #ideal number of times the gz transform is done a second

OVERLAP_FACTOR = 1.1 # amount that the spectral transforms overlap

### element_resolve.py

MAX_FUDGE_FACTOR = 0.10 #most that the element timings can be off

EDGE_VARY_PENALTY_FACTOR = 0.50

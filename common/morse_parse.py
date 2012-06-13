import inspect, os
common_dir = os.path.dirname(inspect.getfile(inspect.currentframe())) # script directory

f = open(os.path.join(common_dir, "morse_table.txt"))

morse_table = f.read()
morse_table = dict([(morse[0:1], morse[2:len(morse)]) for morse in morse_table.split("\n")])

f.close()

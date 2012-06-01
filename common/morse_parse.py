f = open("morse_table.txt")

morse_table = f.read()
morse_table = dict([(morse[0:1], morse[2:len(morse)]) for morse in morse_table.split("\n")])

f.close()

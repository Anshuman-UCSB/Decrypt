import os

strings = open("strings.txt",'r').read().splitlines()
assert all(s.lower() == s for s in strings)

def classify(inp, target=None):
	inp = inp.lower()
	if target is not None:
		if target.lower() in inp:
			return 1
	for s in strings:
		if s in inp:
			return 1

	# TODO: gibbirish detector
	return 0
from string import ascii_lowercase, ascii_uppercase, ascii_letters
def caesar(string, offset):
	out = ""
	for c in string:
		if c in ascii_lowercase:
			pos = ord(c)-ord('a')
			pos += offset
			pos %= 26
			out+=chr(pos+ord('a'))
		elif c in ascii_uppercase:
			pos = ord(c)-ord('A')
			pos += offset
			pos %= 26
			out+=chr(pos+ord('A'))
		else:
			out+=c
	return out
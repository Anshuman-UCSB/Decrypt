from ciphers import *
from recognize import *
from string import ascii_letters
import random

def test_ceasar_simple():
	simple = "this is a normal string"
	assert caesar(simple, 0) == simple
	assert caesar(simple, 1) == "uijt jt b opsnbm tusjoh"
	assert caesar(caesar(simple, 428),-428) == simple
	assert caesar(caesar(simple, 20),6) == simple
def test_ceasar_random():
	ALPHABET = ascii_letters + '\t +-0123456789()*&%:"{}>?<\n\r'
	ciphertext = "".join(random.choice(ALPHABET) for _ in range(random.randint(100,500)))
	assert caesar(ciphertext, 0) == ciphertext
	assert caesar(caesar(ciphertext, 428),-428) == ciphertext
	assert caesar(caesar(ciphertext, 20),6) == ciphertext

def test_recognize():
	assert classify("flag") == 1
	assert classify("inputwithflaghere") == 1
	assert classify("INPUTWITHFLAGHERE") == 1
	assert classify("pIcOcTf{something}") == 1
	assert classify("jskldf") == 0
	assert classify("") == 0
	assert classify("FLA") == 0
	
import re, random, string, assignment1encryption, sys
from collections import Counter
from itertools import islice
from pprint import pprint

def simpleVigenerDecrypt(key, inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	ciphertext = inputFile.read()
	inputFile.close()

	plaintext = decryptVigener(key, ciphertext)

	outputFile = open(outputFileName, "w")
	outputFile.write(plaintext)
	outputFile.close()

def decryptVigener(key, plaintext):
	# convert string to a list of ASCII integer representations
	textCode = [ord(c) for c in plaintext]
	keyCode = [ord(c) for c in key]

	# subtract 97 from each integer to bring them in range of 0-25
	#textCode = [(i-97) for i in textCode if i != ord(" ")]
	textCode = [(i-97) for i in textCode]
	keyCode = [(i-97) for i in keyCode]

	# now perform the actual encrytpion
	cipherCode = [] # there should be a better way to do this
	n = 0
	for i in textCode:
		if i != (ord(" ") - 97):
			# let's try decrypting by switching addition to subtraction
			# cipherCode.append((i + keyCode[n % len(keyCode)]) % 26)
			cipherCode.append((i - keyCode[n % len(keyCode)]) % 26)
			n += 1
		else:
			# stupid but necessary to preserve spaces
			cipherCode.append(i)

	# convert result back into correct ASCII encodings
	cipherCode = [(i + 97) for i in cipherCode]

	# convert list of integers into a string
	ciphertext = "".join(chr(i) for i in cipherCode)

	return ciphertext

def importText(inputFileName):
	inputFile = open(inputFileName, "r")
	inputText = inputFile.read()
	inputFile.close()
	return inputText

# split up the ciphertext into the letters associated with each "alphabet" and compute letter frequencies
# is the supsected key length
def binAlphabets(n, text):
	binnedText = []
	for i in range(0,n):
		binnedText.append(text[i:(len(text)):n])
	
	alphabetList = []
	for text in binnedText:
		alphabet = Counter()
		for c in text:
			alphabet[c] += 1
		alphabetList.append(alphabet)
	return alphabetList

# find the shortest distances between ngrams
def shortDistNgrams(distances, text):
	# code goes here
	for ngram, values in distances.items():
		#print("Examining: {0}".format(ngram,))
		next = 0
		while next != -1:
			next = text.find(ngram, values[0] + len(ngram))
			if next != -1:
				#print("{0} found at {1} distance: {2}".format(ngram, str(next), values[1]))
				if ((next - values[0]) < values[1]) or (values[1] == 0):
					values[1] = next - values[0]
				values[0] = next

### code for identifying ngrams modified from here: http://stackoverflow.com/questions/14168601/nltk-makes-it-easy-to-compute-bigrams-of-words-what-about-letters
def split_every(n, iterable):
    i = iter(iterable)
    piece = ''.join(list(islice(i, n)))
    while piece:
        yield piece
        piece = ''.join(list(islice(i, n)))

def countnGrams(text):
    """ return ngrams for text """
    freqs = Counter()
    # range is between 3 and 6 because there are too many bigrams and an obvious 6 letter ngram
    for n in range(3,6):
    	for ngram in split_every(n, text): # adjust n here
        	freqs[ngram] += 1

    # discard any ngrams that have a frequency lower than 5 since the obvious ngram has 15 occurrences
    for ngram in list(freqs):
    	if freqs[ngram] < 5:
    		del freqs[ngram]
    return freqs

# filenames hardcoded for convenience while searching for key
#	simpleVigenerDecrypt(key, "vigenere_sp.txt", "vigenere_sp_plaintext.txt")

# def vigenerTest():
# 	simpleVigenerDecrypt("rohan", "ciphertextB.txt", "plaintextB.txt")

def ngramTest(inputFileName):
	ciphertext = importText(inputFileName)
	# because spaces are actually annoying
	ciphertext = ciphertext.replace(" ", "")
	# locate the ngrams
	freqs = countnGrams(ciphertext)

	#convert the freqs Counter into a dictionary?
	distances = {}
	for thing in list(freqs):
		distances[thing] = [0,0]

	# find the shortest distances between recurring ngrams
	shortDistNgrams(distances, ciphertext)

	# figure out which distances are most common
	commonDists = Counter()
	for ngram, values in distances.items():
		commonDists[values[1]] += 1

	# finally print out the most common distances
	pprint(commonDists.most_common(10))

def statTest(keyLen, inputFileName):
	ciphertext = importText(inputFileName)
	ciphertext = ciphertext.replace(" ", "")

	# group up the the separate shift ciphertexts
	alphabetList = binAlphabets(keyLen,ciphertext)

	# print out the letter frequencies for each alphabet
	n = 1
	for alphabet in alphabetList:
		print("alphabet " + str(n) + ":")
		pprint(alphabet.most_common(26))
		n += 1

def demoKeySearch():
	# search for the repeat distance between n-grams
	ngramTest("vigenere_sp.txt")

	# ngramTest indicated that the keylength is most likely a multiple of 5
	# start with 5, since it's the smallest
	statTest(5, "vigenere_sp.txt")

	# a quick and dirty analysis is to just assume that the most common character maps to the letter E
	# with this approach, the suspected key is "hello"
	simpleVigenerDecrypt("hello", "vigenere_sp.txt", "vigenere_sp_plaintext.txt")

	# I got lucky with the quick and dirty analysis
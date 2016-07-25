# Andrew Goettler
# Computer Security Spring 2016
# Assignment 1
# Python 3.5.1

import re, random, string

def simpleVigenerEncrypt(key, inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	plaintext = inputFile.read()
	inputFile.close()

	ciphertext = encryptVigener(key, simplePreprocess(plaintext))

	outputFile = open(outputFileName, "w")
	outputFile.write(ciphertext)
	outputFile.close()



def completeVigenerEncrypt(key, inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	plaintext = inputFile.read()
	inputFile.close()

	ciphertext = encryptVigener(key, completePreprocess(plaintext))

	outputFile = open(outputFileName, "w")
	outputFile.write(ciphertext)
	outputFile.close()



def encryptVigener(key, plaintext):
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
			cipherCode.append((i + keyCode[n % len(keyCode)]) % 26)
			n += 1
		else:
			# stupid but necessary to preserve spaces
			cipherCode.append(i)

	# convert result back into correct ASCII encodings
	cipherCode = [(i + 97) for i in cipherCode]

	# convert list of integers into a string
	ciphertext = "".join(chr(i) for i in cipherCode)

	return ciphertext



def simplePermutationEncrypt(key, inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	plaintext = inputFile.read()
	inputFile.close()

	ciphertext = encryptPermutation(key, simplePreprocess(plaintext))

	outputFile = open(outputFileName, "w")
	outputFile.write(ciphertext)
	outputFile.close()



def completePermutationEncrypt(key, inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	plaintext = inputFile.read()
	inputFile.close()

	ciphertext = encryptPermutation(key, completePreprocess(plaintext))

	outputFile = open(outputFileName, "w")
	outputFile.write(ciphertext)
	outputFile.close()



def encryptPermutation(key, plaintext):
	# strip the spaces out of the plaintext to make chunking easier, if present
	striptext = plaintext.replace(" ", "")

	# convert stripped plaintext string into a list for easy rearrangement
	striptext = list(striptext)
	plaintext = list(plaintext)

	#pad the stripped text if needed
	if (len(striptext) % len(key)) != 0 :
		for i in range( len(key) - ( len(striptext) % len(key) ) ):
			striptext.append(random.choice(string.ascii_lowercase))

	#chunk the stripped text and rearrange to create the ciphertext
	chunktext =  [striptext[i:i + len(key)] for i in range(0, len(striptext), len(key))]

	ciphertext = []

	for index, chunk in enumerate(chunktext):
		for i, c in enumerate(chunk):
			ciphertext.append( chunk[(key[i] - 1)] )

	# restore any spaces to the ciphertext
	for i, c in enumerate(plaintext):
		if c == " ":
			ciphertext.insert(i, " ")

	return "".join(c for c in ciphertext)



def simplePreprocess(s):
	s = re.sub("[\n-]", " ", s) # replace newlines and hyphens with spaces to maintain readability
	return re.sub("[^a-z ]", "", s.lower()) # switch to lowercase, remove non-alphabetic characters, leave spaces



def completePreprocess(s):
	return re.sub("[^a-z]", "", s.lower()) # switch to lowercase, remove non-alphabetic characters including whitespace

def testEncryptions():
	# without removing spaces
	simpleVigenerEncrypt("rohan", "plaintext1.txt", "simpleVigenerCiphertext.txt")
	simplePermutationEncrypt([6, 5, 4, 3, 2, 1], "plaintext1.txt", "simplePermutationCiphertext.txt")

	# with spaces removed
	completeVigenerEncrypt("heart", "plaintext2.txt", "completeVigenerCiphertext.txt")
	completePermutationEncrypt([2, 5, 3, 1, 6, 4], "plaintext2.txt", "completePermutationCiphertext.txt")

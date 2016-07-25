import re, random, string, assignment1encryption

# peforms file operations and decryption
def completePermutationDecrypt(key, inputFileName, outputFileName):
	#open, read, and close the input file
	inputFile = open(inputFileName, "r")
	ciphertext = inputFile.read()
	inputFile.close()

	# perform decryption on the input text
	plaintext = decryptPermutation(key, ciphertext)

	# open, write, and close the output file
	outputFile = open(outputFileName, "w")
	outputFile.write(plaintext)
	outputFile.close()

# generate the decryption key for the permutation cipher
def permutationDecryptKey(encryptKey):
	decryptKey = list(encryptKey)

	# "inverts" the encryption key
	for index, value in enumerate(encryptKey):
		decryptKey[value-1] = index + 1

	return decryptKey

# performs the actual decrption
def decryptPermutation(key, ciphertext):
	# call the encryption function with the decryption key
	return assignment1encryption.encryptPermutation(permutationDecryptKey(key), ciphertext)

# testing with known ciphertexts
#def permutationTest():
#	completePermutationDecrypt([2, 5, 3, 1, 6, 4], "ciphertextA.txt", "plaintextA.txt")

# filenames hardcoded for convenience during search for key
# def decrypt(key):
# 	completePermutationDecrypt(key, "permutation_nosp.txt", "permutation_nosp_plaintext.txt")

def demoPermutationDecrypt():
	# examining the ciphertext, it appears the first four letters might be the English word "when"
	# this suggests the key [4, 2, 1, 3]
	completePermutationDecrypt([4, 2, 1, 3], "permutation_nosp.txt", "permutation_nosp_plaintext.txt")
	# short keys make it easy?
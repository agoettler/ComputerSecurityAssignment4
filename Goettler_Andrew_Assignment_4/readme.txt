	For this assignment, I chose to attempt decryption of the permutation cipher
without spaces, and the Vigenere cipher with spaces.

	For the permutation cipher, I took advantage of the small key length 
required in Assignment 1. Examination of the first seven characters of the 
ciphertext "permutation_nosp.txt" revealed that the first four letters might
form the English word "when", suggesting a key of [4, 2, 1, 3]. Testing this
possible key immediately decrypted the ciphertext.

	Lucky guessing would not be as helpful with the Vigenere cipher. However,
examination of the ciphertext "vigenere_sp.txt" showed that the very first word,
of the encrypted text, "oexwsa", was a recurring character pattern, which was
encouraging.I elected to attack the ciphertext using statistical methods.
	In Python, I was able to identify a large number of n-grams. I ignored 
bigrams, focusing, on trigrams and larger n-grams. Computing the distances 
between recurring n-grams strongly suggested that the key length was a multiple 
of 5; the 10 most frequently occurring distances between n-grams all fit this 
pattern.
	I began the statistical analysis assuming a key length of 5, as the smallest
multiple seemed a reasonable place to start. In Python, I separated the
ciphertext into five separate sets, with each set likely encrypted using the
same letter of the key. I then computed word frequencies in each set. Pressed
for time, I tried assuming that the cipher character with the highest frequency
in each set mapped to the letter E. The most frequent characters in each set,
respectively, were 'l', 'i', 'p', 'p', and 's'. This suggested a key of "hello".
Testing this possible key successfully decrypted the ciphertext; to my surprise.
I did not expect statistical analysis on a single letter to crack the cipher.
	To examine the data, import "vigenereDecrypt.py" into a Python interpreter
session and execute the function "demoKeySearch()".
# Ceaser-cipher
# It is a private key encryption (symmetric encryption) method.
# It was first used by Julius Ceaser - 2000 years ago.
# It is a type of substitution cipher: we shift every single letter in the plaintext with a 
# fixed number of letters.

# First we assign numerical values to every letter in the alphabet to be able to use mathematical operations
# during encryption/decryption
# In Ceaser-cipher, the key itself will be the number of letters we use for shifting. 
# So the key will be a intiger

# Formula to solve the Ceaser-cipher using Encryption:
# E n(X) = (x+n) mod 26
# We have to consider all the characters in the plaintext
# E(x) is the encrypted letter of the original x letter
# We have to shift the given letter with n (where n is the key)
# The reason we use mod 26 in this situation is becaue the size of the english alphabet is 26.
# We want the encrypted letter to be within the range [0,SIZE_ALPHABET-1] so this is why to use mod 26

#The formula for Decryption will be the same except you'll be subtracting in the formula
# E n(X) = (x-n) mod 26
# D(x) is the decrypted letter of the original x letter

# Ceaser-Cipher is a private key cryptography method. Our key will be the number of characters we plan to shift 
# our letters. So for example, if our private key was 3, then the letters will shift 3 spaces to the right if 
# we wanted to encrypt our message into a cipher text. If we wanted to decrypt then the cypher text will shift
# 3 spaces to the left.

Alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Key = 5

def ceaser_encrypt(plain_text):
    plain_text = plain_text.upper()
    cipher_text = ''
    # Consider all the letters in the plain text
    for c in plain_text:
        index = Alphabet.find(c) # The find function returns -1 if the given substring doesn't exist in the alphabet list so the index will be -1
        index = (index+Key) % len(Alphabet)
        cipher_text += Alphabet[index]
    return cipher_text

def ceaser_decrypt(plain_text):
    plain_text = plain_text.upper()
    cipher_text = ''
    for l in plain_text:
        index = Alphabet.find(l)
        index = (index-Key) % len(Alphabet)
        cipher_text += Alphabet[index]
    return cipher_text

def crack_ceasar(cipher_text): #Brute Force Attack function
    # We try all the possible key values based on the size of the Alphabet
    cipher_text = cipher_text.upper()
    for key in range(len(Alphabet)):
        plain_text = ''

        #Use simple ceaser decryption
        for l in cipher_text:
            index = Alphabet.find(l)
            index = (index-key) % len(Alphabet)
            plain_text += Alphabet[index]
        # Print the actual decrypted message with the key
        print('With key %s, the result is: %s' % (key, plain_text))

print(crack_ceasar('YMNXENXEFERJXXFLJ'))
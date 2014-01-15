# crypto.py
# Solution to CS 1 Lab Assignment 5 by THC.
# Encrypts and decrypts files using a hybrid cryptosystem.
# Files are encrypted using block cipher with a one-time pad.
# The one-time pad is encrypted using RSA.
# The format of an encrypted file is
#    The one-time pad, encrypted by RSA, given as the ASCII representation
#        of the encrypted pad;
#    Followed by a newline character ("\n");
#    Followed by the ciphertext of the original file, encrypted using a
#        block cipher with the one-time pad.

from mod_exp import modular_exponentiation
from random import randint

BYTE_SIZE = 8                   # bits per byte
BYTE_VALUES = 2 ** BYTE_SIZE    # number of values in a byte

# Convert a string to an int, returning the int.
# The int is formed from the ASCII codes of the characters in the string.
# The leftmost character of the string has its code placed in the least
# significant byte of the int.
def str_to_int(s):
    result = 0
    multiplier = 1
    for c in s:     # process each character in s
        # Add in c, but into the next byte of the int.
        result += ord(c) * multiplier
        
        # Adjust the multiplier for the next byte.
        multiplier *= BYTE_VALUES
        
    return result

# Convert an int to a string, returning the string.
# The string is formed by considering each byte of the int as the ASCII
# code for a character.  The leftmost character of the string has its code
# in the least signficant byte of the int.  The length parameter gives the
# length of the string to form.
def int_to_str(x, length):
    result = ""
    for i in range(length):
        # Concatenate onto the result the least significant byte, converted to a char.
        result += chr(x % BYTE_VALUES)
        
        # Shift x to the right by one byte.
        x /= BYTE_VALUES
        
    return result

# Generate a random pad for a given number of bytes.  Return the pad,
# represented as a string of bytes.
def generate_pad(block_size):
    pad = ""
    for i in range(block_size):
        # Randomly generate the next byte and concatenate it onto the pad.
        pad += chr(randint(0, 255))
    return pad

# Encrypt a plaintext file into a ciphertext file, using the hybrid cryptosystem.
# Parameters are the name of the plaintext file, the name of the ciphertext file,
# the exponent and modulus used for RSA encryption of the one-time pad, and the
# number of bytes in the one-time pad.
def encrypt(plaintext_file_name, ciphertext_file_name, exp, n, block_size):
    cipher_file = open(ciphertext_file_name, "w")
    
    # Generate a random one-time pad.
    pad = generate_pad(block_size)
    
    # Convert the one-time pad to an int so that it can be encrypted with RSA.
    pad_as_int = str_to_int(pad)
    
    # Encrypt the one-time pad using RSA.
    encrypted_pad = modular_exponentiation(pad_as_int, exp, n)
    
    # Write the encrypted one-time pad to the ciphertext file, followed by a newline.
    cipher_file.write(str(encrypted_pad) + "\n")
    
    plaintext_file = open(plaintext_file_name, "rb")
    while True:
        # Read the next block of the plaintext file.
        plaintext_block = plaintext_file.read(block_size)
        if len(plaintext_block) == 0:
            break   # done if no characters left to read
        else:
            # Construct a block of ciphertext.
            ciphertext_block = ""
            
            # XOR each byte in the plaintext block with a byte from the one-time pad,
            # and concatenate it to the ciphertext block.
            for i in range(len(plaintext_block)):
                ciphertext_block += chr(ord(plaintext_block[i]) ^ ord(pad[i]))
                
            cipher_file.write(ciphertext_block)

    cipher_file.close()
    plaintext_file.close()
    
# Decrypt a ciphertext file into a decrypted plaintext file, using the hybrid cryptosystem.
# Parameters are the name of the ciphertext file, the name of the decrypted plaintext file,
# the exponent and modulus used for RSA decryption of the one-time pad, and the
# number of bytes in the one-time pad.
def decrypt(ciphertext_file_name, decrypted_file_name, exp, n, block_size):
    cipher_file = open(ciphertext_file_name, "rb")
    
    # Read the encrypted one-time pad a character at a time, until hitting the newline.
    encrypted_pad_text = ""
    while True:
        digit = cipher_file.read(1)
        if digit == "\n":
            break
        else:
            encrypted_pad_text += digit
            
    # Convert the encrypted one-time pad to an int so that it can be decrypted with RSA.
    encrypted_pad = int(encrypted_pad_text)
    
    # Decrypt the one-time pad with RSA.
    pad_as_int = modular_exponentiation(encrypted_pad, exp, n)
    
    # Convert the one-time pad to a string of bytes.
    pad = int_to_str(pad_as_int, block_size)

    decrypted_file = open(decrypted_file_name, "w")
    while True:
        # Process the next block of the ciphertext.
        ciphertext_block = cipher_file.read(block_size)
        if len(ciphertext_block) == 0:
            break       # done when no ciphertext characters remain 
        else:
            # Construct a block of decrypted plaintext.
            decrypted_block = ""
            
            # XOR each byte in the ciphertext block with a byte from the one-time pad,
            # and concatenate it to the decrypted plaintext block.
            for i in range(len(ciphertext_block)):
                decrypted_block += chr(ord(ciphertext_block[i]) ^ ord(pad[i]))
                
            decrypted_file.write(decrypted_block)
                            
    cipher_file.close()
    decrypted_file.close()

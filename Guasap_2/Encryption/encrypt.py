# import necessary libraries, numpy (as np) for numerical operations,
# and matrix and symbols from a custom module named key.
import numpy as np
from Encryption.key import symbols, matrix

#ENCRYPTION
def encrypt(msg):
  # Map each symbol in the msg to an index using a dictionary called letter_to_index.
  letter_to_index = dict(zip(symbols, range(len(symbols))))
  encrypted = ''
  message_in_numbers = []
  # Convert the msg into a list of numbers (message_in_numbers) based on the mapping.
  for letter in msg:
        message_in_numbers.append(letter_to_index[letter])
  # Pad the list with zeros to make its length a multiple of 10,
  # ensuring it can be reshaped into an Nx10 matrix.
  while len(message_in_numbers) % 10 != 0:
    message_in_numbers.append(0)
  n = int(len(message_in_numbers) / 10)
  message_div = np.array(message_in_numbers).reshape(n,10)
  # Reshape the list into an Nx10 matrix and multiplies it with the matrix provided in the key module.
  encrypted_matrix = np.dot(message_div, matrix)
  # Return the encrypted matrix.
  return encrypted_matrix
#ENCRYPTION DONE

#DECRYPTION
def decrypt(msg):
    # Map each index in the input msg (which is assumed to be an encrypted matrix)
    #  back to a symbol using index_to_letter.
    index_to_letter = dict(zip(range(len(symbols)), symbols))
    inverted_matrix = np.linalg.inv(matrix)
    # Compute the inverse of the matrix and stores it in inverted_matrix.
    multiplication_2 = np.dot(msg, inverted_matrix)
    # Multiply the input msg with the inverted_matrix to perform decryption.
    multiplication_2 = np.round(multiplication_2).astype(int)
    # Round the result to integers and flattens it into a one-dimensional array.
    message_in_numbers_2 = multiplication_2.flatten()
    # Convert the array of numbers back to characters and joins them to form the decrypted message.
    decrypted = []
    for number in message_in_numbers_2:
        decrypted.append(index_to_letter[number])
    # Returns the decrypted message.
    decrypted = ''.join(decrypted)
    return decrypted


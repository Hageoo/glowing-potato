# Matrix-Based Message Encryption and Decryption

## Introduction

This Python script provides a simple implementation of message encryption and decryption using a matrix-based technique. The code uses the NumPy library for numerical operations and expects a predefined matrix and symbols for the encryption and decryption process.

## Setup

Before using the script, ensure that you have the following prerequisites:

- Python installed on your system.
- The NumPy library installed. You can install it using `pip`:

   ```bash
   pip install numpy
   ```

- A custom module named `key` that contains the matrix (`matrix`) used for encryption and a list of symbols (`symbols`) used for character-to-index mapping. The module structure should resemble the following:

   ```python
   # key.py
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   ```

## Usage

### Encryption

To encrypt a message, use the `encrypt` function in your Python script. Here's an example:

```python
from key import matrix, symbols
from encryption_module import encrypt

message = "HELLO"
encrypted_message = encrypt(message)
print("Encrypted Message:", encrypted_message)
```

### Decryption

To decrypt an encrypted message, use the `decrypt` function. Here's an example:

```python
from key import matrix, symbols
from encryption_module import decrypt

encrypted_message = [[30, 36, 42], [66, 81, 96]]
decrypted_message = decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)
```

## Functionality

### `encrypt(msg)`

- Encrypts a given message `msg` using the predefined matrix (`matrix`) and symbols (`symbols`).
- Returns the encrypted message as a matrix.

### `decrypt(msg)`

- Decrypts an encrypted message (`msg`) provided as a matrix.
- Returns the decrypted message as a string.

## Important Notes

- This implementation assumes that the `key.py` module contains the appropriate matrix (`matrix`) and symbols (`symbols`) required for the encryption and decryption process.
- Ensure that the matrix used for encryption has an inverse matrix for decryption.
- This is a basic example and may require additional error handling and security enhancements for real-world applications.

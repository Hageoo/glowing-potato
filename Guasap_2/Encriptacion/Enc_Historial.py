from cryptography.fernet import Fernet

# Generate an encryption key
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Open the JSON file you want to encrypt
with open(r'Path to Encrypted_chat.json', 'rb') as archivo_json:
    json_data = archivo_json.read()

# Encrypt the JSON data
encrypted_data = cipher_suite.encrypt(json_data)

# Save the encrypted data in a new file
with open('historial_mensajes.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File historial_mensajes.json encrypted and saved as Encrypted_chat.json")

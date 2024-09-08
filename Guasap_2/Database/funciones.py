from Database.connection_mondongo import connect_mondongo
import datetime
import pymongo
import numpy as np
from Encryption.encrypt import decrypt, encrypt

# Connect to MongoDB using the connect_mondongo function
client = connect_mondongo()
if not client:
    print("Couldn't connect to Mondongo")

# Function to insert a user with password encryption
def insert_user(name, password):
    # Connect to MongoDB
    # Select the database and collection
    db = client["Authentication"]  # Database name
    collection = db["Sign_in"]  # Collection name
    password = password.strip()
    
    # Encrypt the password before inserting it into the database
    encrypted_password = encrypt(password)
    
    # Create the user document with the encrypted password
    user = {
        "nombre": name,
        "contraseña": encrypted_password.tolist()  # Convert to a list for MongoDB storage
    }

    # Insert the user into the collection
    result = collection.insert_one(user)

    # Return the ID of the inserted document
    return result.inserted_id

# Function to retrieve users with password decryption
def get_users():
    # Select the database and collection
    db = client["Authentication"]
    collection = db["Sign_in"]

    # Query to retrieve all documents
    cursor = collection.find()

    # Create a dictionary to store users and decrypted passwords
    credentials = {
        'nombre': {}
    }

    # Iterate through the documents and add them to the dictionary
    for user in cursor:
        name = user.get("nombre")
        encrypted_password = user.get("contraseña")
        
        # Decrypt the password before storing it
        decrypted = decrypt(np.array(encrypted_password))
        decrypted_password = decrypted.strip()
        
        credentials['nombre'][name] = decrypted_password

    return credentials

# Function to send and store encrypted messages
def send_message(name, message):
    # Select the database and collection
    db = client["Historic"]
    collection = db["Messages"]

    # Create the message document
    encrypted_msg = encrypt(message)
    message_to_list = encrypted_msg.tolist()

    message_doc = {
        "nombre": name,
        "mensaje_encriptado": message_to_list,
        "timestamp": datetime.datetime.now()
    }

    # Insert the message into the collection
    result = collection.insert_one(message_doc)

    # Return the ID of the inserted document
    return result.inserted_id

# Function to receive the last message in the desired format
def receive_last_message():
    db = client["Historic"]
    collection = db["Messages"]

    # Sort the collection by date (timestamp) in descending order and take the first document
    last_message = collection.find_one(sort=[("timestamp", pymongo.DESCENDING)])

    if last_message:
        name = last_message["nombre"]
        encrypted_message = last_message["mensaje_encriptado"]
        decrypted_message = decrypt(encrypted_message)
        
        # Format the message in the desired format
        formatted_message = f"{name}: {decrypted_message}"

        return formatted_message
    else:
        return None
# Function to receive the last 10 most recent messages in the desired format
def receive_last_10(quantity=10):
    db = client["Historic"]
    collection = db["Messages"]

    # Perform a query to retrieve the latest messages
    cursor = collection.find().sort([("timestamp", pymongo.DESCENDING)]).limit(quantity)

    # Create a list to store the messages
    messages = []

    # Iterate through the documents and add them to the list
    for message in cursor:
        name = message["nombre"]
        message_encrypted = message["mensaje_encriptado"]
        message_text = decrypt(message_encrypted)
        message_text = message_text.strip()

        # Format the message in the desired format
        formatted_message = f"{name}: {message_text}"
        messages.append(formatted_message)

    # Reverse the list to display the messages in chronological order
    messages.reverse()

    return messages

# Function to retrieve and decrypt all previous messages
def retrieve_previous_messages():
    db = client["Historic"]
    collection = db["Messages"]

    # Perform a query to retrieve messages older than the last one
    last_message = collection.find_one(
        sort=[("timestamp", pymongo.DESCENDING)]
    )

    if last_message:
        # Get the timestamp of the last message
        last_timestamp = last_message["timestamp"]

        # Perform a query to retrieve all previous messages
        cursor = collection.find(
            {"timestamp": {"$lt": last_timestamp}}
        ).sort([("timestamp", pymongo.DESCENDING)])

        # Create a list to store the messages
        messages = []

        # Iterate through the documents and add them to the list
        for message in cursor:
            name = message["nombre"]
            message_encrypted = message["mensaje_encriptado"]
            message_text = decrypt(message_encrypted)
            message_text = message_text.strip()

            # Format the message in the desired format
            formatted_message = f"{name}: {message_text}"
            messages.append(formatted_message)

        # Reverse the list to display the messages in chronological order
        messages.reverse()
        return messages
        
    else:
        return None


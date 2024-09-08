# README for Mondongo Authentication and Messaging System

## Introduction

This Python code provides a basic implementation of an authentication and messaging system using MongoDB for data storage. The system includes functions for user registration with password encryption, sending and receiving encrypted messages, and retrieving message history.

## Requirements

Before using this code, make sure you have the following requirements met:

1. **Python 3:** Ensure you have Python 3.x installed on your system.

2. **MongoDB:** You need a running MongoDB server where the data will be stored. Make sure you have MongoDB installed and running.

3. **Required Python Libraries:** You'll need the following Python libraries installed. You can install them using `pip` if you haven't already:

   - `pymongo`: For MongoDB interaction.
   - `numpy`: For numerical operations.
   - Custom modules (`Database.connection_mondongo` and `Encryption.encrypt`) used for database connection and encryption.

## Setup

1. **Database Connection:**

   - The code uses a custom module for database connection named `Database.connection_mondongo`. Ensure that this module exists and properly configures the MongoDB connection. Update the module with your MongoDB connection details.

2. **Encryption:**

   - Encryption is handled using a custom module named `Encryption.encrypt`. Ensure that this module exists and is properly configured for encryption and decryption. You can use any encryption library of your choice.

## Usage

The code provides the following functions:

1. **User Registration:**

   - Use the `insert_user` function to register a user with an encrypted password. Example:

     ```python
     insert_user("username", "password")
     ```

2. **Sending Messages:**

   - Use the `send_message` function to send an encrypted message. Example:

     ```python
     send_message("sender_name", "This is an encrypted message.")
     ```

3. **Receiving Last Message:**

   - Use the `receive_last_message` function to retrieve the last received message in the desired format. Example:

     ```python
     last_message = receive_last_message()
     if last_message:
         print(last_message)
     else:
         print("No messages found.")
     ```

4. **Receiving Last 10 Messages:**

   - Use the `receive_last_10` function to retrieve the last 10 received messages in the desired format. You can specify a different quantity. Example:

     ```python
     last_10_messages = receive_last_10(quantity=5)
     if last_10_messages:
         for message in last_10_messages:
             print(message)
     else:
         print("No messages found.")
     ```

5. **Retrieve Previous Messages:**

   - Use the `retrieve_previous_messages` function to retrieve and decrypt all previous messages older than the last message received. Example:

     ```python
     previous_messages = retrieve_previous_messages()
     if previous_messages:
         for message in previous_messages:
             print(message)
     else:
         print("No messages found.")
     ```

## Note

- Ensure that you have the necessary permissions and configurations for MongoDB access.

- This code provides basic functionality for authentication and messaging. You can extend and modify it to meet your specific requirements.

- Make sure to handle error cases and exceptions as needed in a production environment.


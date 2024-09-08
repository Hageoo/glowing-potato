# Treehouse Talks - Streamlit Chat Application

## Introduction

This Python code provides a simple chat application built using Streamlit. Users can log in, send and receive messages, and register for new accounts. The application relies on a backend provided by the `Database.funciones` module for user management and message handling.

## Requirements

Before using this code, ensure that you meet the following requirements:

### 1. Python 3

Make sure you have Python 3.x installed on your system.

### 2. Streamlit

Install Streamlit, a web application framework, using `pip`:

   ```bash
   pip install streamlit
   ```

### 3. MongoDB 

You need a running MongoDB server for data storage. Make sure you have MongoDB installed and running.

### 4. Streamlit Auto Refresh

Install the `streamlit-autorefresh` library for automatic page refresh:

   ```bash
   pip install streamlit-autorefresh
   ```

## Setup

### 1. Database Functions:

   - The code uses a custom module for database functions named `Database.funciones`. Ensure that this module exists and is properly configured for user authentication, registration, and message storage. Update the module with your MongoDB connection details.

### 2. Background Images and CSS Styles:

   - The code includes background images and CSS styles for styling the chat application. Ensure that the image URLs in the code point to valid images or replace them with your preferred images. You can also customize the CSS styles to match your desired theme.

### 3. External CSS Styles:

   - The code attempts to load additional CSS styles from an external file named `style\style.css`. Make sure this file exists and contains any additional styles you want to apply to the application.

## Usage

To run the Treehouse Talks chat application, execute the following command in your terminal:

```bash
streamlit run your_app_file.py
```

Replace `your_app_file.py` with the filename of your Python script containing the code.

The application provides the following functionality:

### User Authentication

- Users can log in with their usernames and passwords.
- If the user is not authenticated, they are prompted to log in.

### User Registration

- Users can register for new accounts with unique usernames and passwords.
- After successful registration, the user can log in.

### Chat Interface

- Authenticated users can send and receive messages in a chat interface.
- Messages are displayed in a chat-like format with user-specific styling.
- Users can reload previous messages and view the latest messages.

### Sending Messages

- Authenticated users can type and send messages using the input field.
- Sent messages are displayed with a distinctive style.

## Notes

- Ensure that you have the necessary permissions and configurations for MongoDB access.

- This code provides a basic chat application with minimal security measures. In a production environment, you should implement more robust security features.

- Customize the background images, CSS styles, and additional features to match your desired chat application's look and feel.

- The application may require further optimization for scalability and performance in a production environment.

# Project Team

# Authors

# Dev Ops Engineers:
Hageo Juda Balam Mendez
Miguel Angel Bastarrachea Carballo 

# Responsibilities: 
- Integration of Encryption/Decryption
- Documentation 
- Real time Communication 

# Machine Learning Developers:
Alfonso Alexis Canto Ancona 
Yahir Benjamin Sulu Chi

# Responsibilities: 
- Development of the Encryption and Decryption Via Matrix 


# Data Engineers:
Luis David Martinez Gutierrez
Angel Adrian Campos Borges

# Responsibilities: 
- Back-end functionalities
- Mongodb queries
- Message retrieval and storage
- Log In/Sign In feature

# Data Scientists:
Jose Manuel Solano Ochoa
Angel David Sansores Cruz

# Resposibilities: 
- CSS styling
- Dashboard design

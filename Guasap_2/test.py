import streamlit as st
import json
import time
from connection_mondongo import connect_mondongo
import funciones as fun
import streamlit_authenticator as stauth

fondo = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://th.bing.com/th/id/R.9e1c05c8531956a9b56d4a6a5f4316f2?rik=C1y19WO1bHQtsg&riu=http%3a%2f%2fmemeschistosos.net%2fwp-content%2fuploads%2f2015%2f12%2fmemes-de-hola12.jpg&ehk=01T2GplgGMaqL2SFKEPL%2fkYz2Z44hy9slzTuS1DqQSY%3d&risl=&pid=ImgRaw&r=0")
background-size: cover;
}
</style>
"""

st.markdown(fondo, unsafe_allow_html=True)

# App title
st.title("Wazaaaap 👻")

# Area to input the message
message = st.text_input("Write your message here:")

# Load the message history from a JSON file (if it exists)
message_history = []
try:
    with open("historial_mensajes.json", "r") as file:
        message_history = json.load(file)
except FileNotFoundError:
    pass

# Button to send the message (now at the bottom)
if st.button("Send"):
    # Add the user's message to the message list
    user_message = message.strip()  # Removes extra white spaces
    if user_message:  # Check if the message is not empty
        message = ""  # Clear the text input after sending the message
        
        # Simulate a response after 3 seconds
        time.sleep(3)
        response_message = "Response message!"
        
        # Add the new message and response to the history
        message_history.append({"user": "You", "message": user_message})
        message_history.append({"user": "Other User", "message": response_message})
        
        # Save the updated history to a JSON file
        with open("historial_mensajes.json", "w") as file:
            json.dump(message_history, file)

# Split the page into two columns
left_column, right_column = st.columns(2)

# Display the chat messages as text bubbles in reverse order (from bottom to top)
for message in message_history:  # Use reversed to invert the order
    if message["user"] == "You":
        # Style for your own messages (left half)
        with left_column:
            st.markdown(f'<br><div style="text-align: right; background-color: #0084ff; color: white; padding: 10px; border-radius: 10px; border: 1px solid white;">You: {message["message"]}</div>', unsafe_allow_html=True)
    else:
        # Style for messages from other users (right half)
        with right_column:
            st.markdown(f'<div style="text-align: left; background-color: white; color: black; padding: 10px; border-radius: 10px; border: 1px solid black;">Other User: {message["message"]}</div><br><br>', unsafe_allow_html=True)

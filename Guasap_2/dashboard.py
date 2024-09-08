import streamlit as st
import Database.funciones as fun 
from streamlit_autorefresh import st_autorefresh
import time

"""
This project is a brief example usage of NoSQL 
"""

# Auto refresh each 10 seconds
count = st_autorefresh(interval=10000, limit=None, key="chat_refresh_counter")

# Application title
st.title("""Treehouse Talks""")

# Set background image and additional CSS styles
st.markdown(
    """
    <style>
        .main.css-uf99v8.ea3mdgi5 {
            background-image: url("https://wallpapercave.com/wp/wp3394825.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        
        .css-k7vsyb h1::after {
            content: ""; 
            background-image: url(https://4.bp.blogspot.com/-4LbY-IQxPUg/URmLI5H6KXI/AAAAAAAAAVk/ymJ13fTpTAQ/s1600/Untitled+10.png);
            background-size: 100% auto;
            background-repeat: no-repeat;
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 200px;
            z-index: 9999; /* This makes the sword appear above other elements */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load additional CSS styles from an external file
with open("style\style.css") as f: 
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Check if the user is authenticated
session_state = st.session_state
if 'authenticated' not in session_state:
    session_state.authenticated = False

if not session_state.authenticated:
    # Show the login form
    st.subheader("Log In")
    username = st.text_input("User")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = fun.get_users()  # Get the complete dictionary of users

        if username in users['nombre'] and users['nombre'][username] == password:
            session_state.authenticated = True
            st.success("You have logged in successfully")
            if 'username' not in st.session_state:
                st.session_state['username'] = username

        else:
            st.warning("Incorrect username or password.")
            
    # Show the link to register with a different key
    if st.button("Sign In"):
        session_state.show_registration_form = True

if session_state.authenticated:

    user_ac = session_state["username"]


    st.session_state.click = True


    reload = st.button("Reload previous message")

    # Changing background image and additional CSS styles for the chat area (pie over "Treehouse Talks")
    st.markdown(
    """
    <style>
        .main.css-uf99v8.ea3mdgi5 {
            background-image: url("https://i.imgur.com/t7RNw0J.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .css-k7vsyb h1::after {
            content: ""; 
            background-image: url(https://th.bing.com/th/id/R.8cf074541e1926f40fd94edcab822b12?rik=0LHwGWJbBIsELQ&riu=http%3a%2f%2fvignette3.wikia.nocookie.net%2fadventuretimewithfinnandjake%2fimages%2fc%2fc8%2fRoyal_Tart_Slice.png%2frevision%2flatest%3fcb%3d20120711200506&ehk=Om5TVjnIdms89%2bFF%2fOx8AoPm9afhxIpYu%2bN6F8fMHEM%3d&risl=&pid=ImgRaw&r=0);
            background-size: 28% auto;
            background-repeat: no-repeat;
            position: absolute;
            bottom: 30px;
            left: 180px;
            right: 0;
            height: 125px;
        }
    </style>
        """,
        unsafe_allow_html=True)
    
    if session_state.click == True:
        messages_to_show = fun.receive_last_10()
        if reload:
            messages_to_show = fun.retrieve_previous_messages()
            session_state.click = False
            # Button to load the latest 8 messages.
            if st.button("Latest Messages"):
                    session_state.click = True

    # We no longer need to split the chat into two columns as messages will be interleaved.
    for message in messages_to_show:  # Reverse to display from bottom to top.
        if message.startswith(user_ac):
        # Style for your own messages with blue text bubbles (right-aligned).
            username, message_text = message.split(':', 1)
            st.markdown(f"<div class='own-message' style='text-align: right; font-family: Thunderman; color: black; font-size: 17px;'><strong>{username}:</strong> {message_text}</div>", unsafe_allow_html=True)
        else:
            # Style for messages from other users with green text bubbles (left-aligned).
            username, message_text = message.split(':', 1)
            st.markdown(f"<div class='received-message' style='font-family: Thunderman; color: black; font-size: 17px;'><strong>{username}:</strong> {message_text}</div>", unsafe_allow_html=True)

    # Area to enter a message.}
    clear = st.empty()
    message = clear.text_input("Type your message:", key="message_input")
    
    # Button to send the message.
    send_msg = st.button("Send")
    # If interacted with:
    if send_msg:
        # Add the user's message to the list of messages.
        user_message = message.strip()  # Remove extra whitespace.
        if user_message:  # Check if the message is not empty.
            message_id = fun.send_message(user_ac, user_message)
            # Sort of "re declaring" the text input in order to clear it
            message = clear.text_input("Type your message:", key="message_input_2")
            # Send the message to the current user and receive a response.


if session_state.get('show_registration_form'): 
    st.subheader("User Registration")
    st.markdown("<a name='registro'></a>", unsafe_allow_html=True)  # Anchor tag

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    
    if st.button("Register"):
        if new_username in fun.get_users()['nombre']: 
            st.warning("This username already exists.")
        else:
            fun.insert_user(new_username, new_password)
            st.success("User registered successfully!")
            fun.get_users()# Updating for the new user in the database

        # After successfully registering the user, hide the registration form
        session_state.show_registration_form = False

import streamlit as st
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase Admin SDK with your credentials (uncomment this when using actual credentials)
# cred = credentials.Certificate('path_to_your_firebase_credentials.json')
# firebase_admin.initialize_app(cred)

def app():
    st.title("Welcome to :violet[FitnessFusion]")
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            st.success("Login Successful")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signout = True
            st.session_state.signedout = True
        except:
            st.warning("Login Failed")
    
    def t():
        st.session_state.signedout = False
        st.session_state.signout = False
        st.session_state.username = ''

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    if not st.session_state['signedout']:
        choice = st.selectbox("Login/SignUp", ["Login", "SignUp"])

        if choice == "Login":
            email = st.text_input("Email Address")
            password = st.text_input("Password", type='password')
            st.button("Login", on_click=f)

        else:
            email = st.text_input("Email Address")
            password = st.text_input("Password", type='password')
            username = st.text_input("Enter your unique username")

            if st.button("Create My Account"):
                try:
                    # Check if the email already exists
                    user = auth.get_user_by_email(email)
                    st.warning("User with this email already exists. Please log in.")
                except auth.UserNotFoundError:
                    # If user doesn't exist, proceed to create the user
                    user = auth.create_user(email=email, password=password, uid=username)
                    st.success("Account Created Successfully")
                    st.markdown("Please login using your email and password.")
                    st.balloons()

    if st.session_state.signout:
        st.text('Name: ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.button("Sign Out", on_click=t)

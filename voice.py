import streamlit as st
import streamlit.components.v1 as components

# Initialize session state for button clicks
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = None

def display_jcare_options():
    # Create a container for buttons and text input
    col1, col2 = st.columns(2)

    # Display buttons if none have been clicked
    if st.session_state.button_clicked is None:
        with col1:
            if st.button('Proceed to buy a J Care policy and get a policy in 5 mins!?'):
                st.session_state.button_clicked = 'button1'
                # HTML and JavaScript to open a new tab
                components.html("""
                    <script>
                        window.open('https://jubileeinsurance.com/ke/product/j-care-medical-cover/');
                    </script>
                """)
        
        with col2:
            if st.button('Would you like to continue?'):
                st.session_state.button_clicked = 'button2'
                
    # Display text input box if any button was clicked
    if st.session_state.button_clicked:
        st.text_input("Let's continue!")

# Streamlit app code
st.title('Welcome to Jubilee GPT')
message = "The products that fit your description are J Care, J Care Johari, and J Care Senior"
if "J Care" in message:
    display_jcare_options()

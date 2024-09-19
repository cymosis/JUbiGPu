import streamlit as st

def display_jcare_options():
    # Link to the J Care policy
    jcare_link ="https://jubileeinsurance.com/ke/product/j-care-medical-cover/"
    st.write(f"Click [here]({jcare_link}) to view the J Care policy.")
    
    # Create a container for buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Would you like to buy a J Care policy?'):
            st.write("Redirecting to the purchase page...")
            # Implement redirection or further logic here
    
    with col2:
        if st.button('Would you like to continue?'):
            st.write("Continuing with the current options...")
            # Implement logic for continuing here

# Streamlit app code
st.title('Welcome to Jubilee GPT')

# Input field for user message
user_message = st.text_input("Enter your message:")

# Check if the user message contains "J care" and display buttons if true
if "J care" in user_message:
    display_jcare_options()

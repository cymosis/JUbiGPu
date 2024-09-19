import streamlit as st

def display_jcare_options():
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

# Display buttons directly without any input field
display_jcare_options()

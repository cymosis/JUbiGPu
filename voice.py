import streamlit as st

def display_jcare_options():
    # Create a container for buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Would you like to buy a J Care policy?'):
            st.write("https://jubileeinsurance.com/ke/product/j-care-medical-cover/")
    
    with col2:
        if st.button('Would you like to continue?'):
            st.text_input("Let's continue!")

# Streamlit app code
st.title('Welcome to Jubilee GPT')
message="The products that fit your description are J Care, J care Johari and J care senior"
if "J care" in message:
    display_jcare_options()

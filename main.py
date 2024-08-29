import streamlit as st
from urllib.parse import urlencode

# app config
st.set_page_config(
    page_title="Formula 1",
    layout="wide"
)

from views.cards_view import cards_view
from views.cards_detail_view import cards_detail_view

# Function to set the page parameter if not present
def set_default_page():
    query_params = st.query_params
    if 'page' not in query_params:
        new_params = {'page': 'main'}
        st.query_params.from_dict(new_params)

# Call the function to set default page
set_default_page()

# Get the page query parameter
params = st.query_params
page = params.get('page', ['main'])

# Load different views based on the page parameter
if page == 'main':
    cards_view()
elif page == 'details':
    cards_detail_view()
else:
    st.write("Invalid selection. Please go back to the main view.")
    st.markdown("[Go back to main view](?page=main)")
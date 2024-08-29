import streamlit as st
from streamlit_theme import st_theme # https://pypi.org/project/st-theme/

# Initialize the theme as None
theme = None

def initialize_theme(page_id):
    global theme
    if theme is None:
        theme = st_theme(adjust=True,key=int(page_id))

# theme = st_theme(adjust=True) 
# background_color = theme['backgroundColor']
# text_color = theme['fadedText60']
# border_color = theme['fadedText10'] 

def st_card(title, country, location, date, page_id):

    # Ensure the theme is initialized
    initialize_theme(page_id)
    
    background_color = 'black'
    text_color = 'white'
    border_color = 'black'

    # Check the theme before accessing its items
   #print("this is 1 from card")
    # Create a card with an anchor tag
    st.markdown(
        f"""
        <style>
        .card {{
            padding: 20px;
            margin-bottom: 10px;
            border-radius: 10px;
            background-color: {background_color};
            color: {text_color};
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            border: 1px solid {border_color};
            height: 250px;  /* Fixed height for uniform card sizes */
            overflow: hidden;  /* Prevents content overflow */
            text-align: left;
            transition: transform 0.2s ease-in-out; /* Smooth scaling */
            cursor: pointer; /* Indicate clickable */
        }}
        .card:hover {{
            transform: scale(1.03); /* Scale the card on hover */
        }}
        </style>
        <a href="?page=details&card_id={page_id}" target = "_self" style="text-decoration: none;">
            <div class="card">
                <h4>{title}</h4>
                <h5>Country: {country}</h5>
                <h6>Location: {location}</h6>
                <p>Date: {date}</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    st_card()


    
    
import streamlit as st
import fastf1

def cards_detail_view():
    params = st.query_params
    # Get the 'year' value
    year = params.get("year")
    card_id = params.get("card_id")
    
    event = fastf1.get_event(int(year), int(card_id))

    st.write(params)
    st.write(event)
    
    print("this is 1 from cards_detail_view")
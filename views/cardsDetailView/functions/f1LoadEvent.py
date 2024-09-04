import streamlit as st
import pandas as pd
import fastf1

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_event(year, card_id):
    return fastf1.get_event(int(year), int(card_id))

if __name__ == "__main__":
    load_event()
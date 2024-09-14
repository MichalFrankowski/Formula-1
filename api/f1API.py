import streamlit as st
import pandas as pd
import fastf1

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_schedule(season_year):
    schedule = fastf1.get_event_schedule(int(season_year))
    schedule['EventDate'] = pd.to_datetime(schedule['EventDate']).dt.strftime('%d %b %Y')
    return schedule

@st.cache_data
def load_session(year, card_id):
    return fastf1.get_session(int(year), int(card_id), 'Q')

@st.cache_data
def load_event(year, card_id):
    return fastf1.get_event(int(year), int(card_id), backend='fastf1') 

# Cache the session fetching process
@st.cache_data
def load_session_load(year, card_id, session_type='Q'):
    session = fastf1.get_session(int(year), int(card_id), session_type, backend='fastf1') 
    session.load()
    return session


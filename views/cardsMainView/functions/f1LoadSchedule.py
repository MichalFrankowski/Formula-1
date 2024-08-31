import streamlit as st
import pandas as pd
import fastf1

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_schedule(season_year):
    schedule = fastf1.get_event_schedule(int(season_year))
    schedule['EventDate'] = pd.to_datetime(schedule['EventDate']).dt.strftime('%d %b %Y')
    return schedule

if __name__ == "__main__":
    load_schedule()
import streamlit as st
import pandas as pd
import fastf1

# importing custom components
from components.card import st_card

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_schedule(season_year):
    schedule = fastf1.get_event_schedule(int(season_year))
    schedule['EventDate'] = pd.to_datetime(schedule['EventDate']).dt.strftime('%d %b %Y')
    return schedule

def cards_view():
    #print("this is 1 from cards_view")
    with st.form("season_form",border=False):
        # creating columns
        header = st.columns([10,4,2,2],vertical_alignment="bottom")
        # title
        header[0].header("Formula 1 | Seasons Overview")
        # year selection
        option = header[2].selectbox("Select Season Year",
                                    ("2024", "2023", "2022"))
        # submit button                    
        header[3].form_submit_button('Show Season',use_container_width=True)

    st.divider()
    st.subheader("Season " + option + " Schedule" )

    schedule = load_schedule(option)

    # Create a card for each row in the DataFrame and Display cards in a grid layout of 5x5
    rows = 5
    
    for i in range(rows):
        cols = st.columns(5,vertical_alignment="center", gap="small")  # Create 5 columns per row
        for j in range(5):
            idx = i * 5 + j
            if idx < len(schedule):
                row = schedule.iloc[idx]
                with cols[j]:
                    st_card(title=row["EventName"],country=row["Country"],location=row["Location"], date=row["EventDate"],page_id=row["RoundNumber"])

    st.divider()
    with st.expander("F1 Data"):
         st.dataframe(schedule,hide_index=True)

if __name__ == "__main__":
    cards_view()